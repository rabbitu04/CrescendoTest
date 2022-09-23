from enum import Enum


class BotRespType(Enum, str):
    BASE = 'BaseResp'
    MY_NAME = 'MyNameResp'
    LAST_ENGAGED = 'LastEngagedResp'
    COUNT = 'CountResp'
