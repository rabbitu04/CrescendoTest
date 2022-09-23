from enum import Enum


class BotRespType(str, Enum):
    BASE = 'BaseResp'
    MY_NAME = 'MyNameResp'
    LAST_ENGAGED = 'LastEngagedResp'
    COUNT = 'CountResp'
