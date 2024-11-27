from typing import Tuple, Optional, Any

from common_layer.exceptions import InvalidLambdaInputException
from constants import QUERY_STRING_PARAMETERS, COMP_ID, TOPIC, AUTHORIZATION
from constants import HEADERS


class ValidateInput:
    def __init__(self, event: dict):
        self.event = event

    def extract_query_string_parameters(self) -> tuple:
        if QUERY_STRING_PARAMETERS in self.event:

            query_string: dict = self.event.get(QUERY_STRING_PARAMETERS)
            if (COMP_ID in query_string and query_string.get(COMP_ID) != '' and
                (TOPIC in query_string and query_string.get(TOPIC) != '')):
                return query_string.get(COMP_ID), query_string.get(TOPIC)
            else:
                raise InvalidLambdaInputException(f'Could not find {COMP_ID} or {TOPIC} in Input')
        else:
            raise InvalidLambdaInputException(f'Could not find {QUERY_STRING_PARAMETERS} in Input')

    def extract_headers(self) -> str:
        if HEADERS in self.event:
            headers: dict = self.event.get(HEADERS)

            if AUTHORIZATION in headers and headers.get(AUTHORIZATION):
                return headers.get(AUTHORIZATION)
            else:
                raise InvalidLambdaInputException(f'Could not find {AUTHORIZATION} in Input')
        else:
            raise InvalidLambdaInputException(f'Could not find {AUTHORIZATION} in Input')
