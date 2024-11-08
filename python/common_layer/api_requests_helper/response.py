import json
from decimal import Decimal
from typing import Any

from . import StatusCodes

def decimal_serializer(obj):
    if isinstance(obj, Decimal):
        return float(obj)  # Or use str(obj) if you prefer strings for Decimal
    raise TypeError(f"Object of type {type(obj).__name__} is not JSON serializable")

class Response:

    def __init__(self, status_code: StatusCodes, headers: dict, body: Any):
        self.status_code = status_code
        self.headers = headers
        self.body = body

    def build_response(self) -> dict:

        if isinstance(self.body, str):
            body = json.dumps(self.body)
        elif isinstance(self.body, list) or isinstance(self.body, dict):
            body = json.dumps(self.body, default=decimal_serializer)
        else:
            body = self.body

        return {
            'statusCode': self.status_code.value,
            'headers': self.headers,
            'body': body
        }

