import http
import os
from datetime import datetime

from flask import abort, request
from flask import current_app as app
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, events

from src.constant import BotRespType
from src.line_bot import api_bp


class BotRespFactory:
    class BaseResp:
        def __init__(self, user_id, msg: str):
            self.user_id = user_id
            self.msg = msg
            self.update_user_record()

        def update_user_record(self):
            record = app.user_records.get(self.user_id, None)
            if record is None:
                record = {'count': 1}
                app.user_records[self.user_id] = record
            else:
                record['count'] += 1
            self.count = record['count']
            self.last_engaged = record.get('last_engaged', None)
            record['last_engaged'] = datetime.now()

        def resp(self):
            return self.msg

    class MyNameResp(BaseResp):
        def resp(self):
            return self.user_id

    class LastEngagedResp(BaseResp):
        def resp(self):
            return self.last_engaged

    class CountResp(BaseResp):
        def resp(self):
            return self.count

    def __init__(self, user_id, msg: str):
        resp_cls_key = msg.upper()
        resp_cls_key = resp_cls_key.replace(' ', '_')

        resp_cls = self.__class__.__dict__.get(
            getattr(BotRespType, resp_cls_key, BotRespType.BASE)
        )

        self.instance = resp_cls(
            user_id,
            msg
        )

    def get_instance(self):
        return self.instance

line_bot_api = LineBotApi(os.getenv('CHANNEL_ACCESS_TOKEN'))
handler = WebhookHandler(os.getenv('CHANNEL_SECRET'))


@api_bp.route('/line-bot-webhook', methods=['POST'])
def line_webhook():
    # check request header
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(http.HTTPStatus.BAD_REQUEST, 'Invalid signature.')

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event: events.MessageEvent):
    msg = event.message.text
    user_id = event.source.user_id
    bot_resp: BotRespFactory.BaseResp = BotRespFactory(
        user_id,
        msg
    ).get_instance()

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=bot_resp.resp())
    )

    return
