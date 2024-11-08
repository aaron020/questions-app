from enum import Enum


class StatusCodes(Enum):
    STATUS_OK = 200
    STATUS_CLIENT_ERROR = 400
    STATUS_SERVER_ERROR = 500
    STATUS_NO_CONTENT = 204