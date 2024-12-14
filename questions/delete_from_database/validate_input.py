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

    def extract_user_id_from_input(self) -> str:
        user_id = self.event.get('requestContext', {}).get('authorizer', {}).get('claims', {}).get('sub')
        if user_id is None:
            raise InvalidLambdaInputException("Unable to get user_id from token")
        else:
            return user_id
