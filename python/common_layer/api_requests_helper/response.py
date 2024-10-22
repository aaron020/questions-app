from . import StatusCodes


class Response:

    def __init__(self, status_code: StatusCodes, headers: dict, body: str):
        self.status_code = status_code
        self.headers = headers
        self.body = body

    def build_response(self) -> dict:
        return {
            'statusCode': self.status_code.value,
            'headers': self.headers,
            'body': self.body
        }

