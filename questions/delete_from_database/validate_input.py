from typing import Tuple, Optional, Any

from common_layer.exceptions import InvalidLambdaInputException
from constants import QUERY_STRING_PARAMETERS, QUESTION_ID, TOPIC_ID, AUTHORIZATION
from constants import HEADERS


class ValidateInput:
    def __init__(self, event: dict):
        self.event = event

    def extract_query_string_parameters(self) -> tuple:
        if QUERY_STRING_PARAMETERS in self.event:

            query_string: dict = self.event.get(QUERY_STRING_PARAMETERS)
            if (QUESTION_ID in query_string and query_string.get(QUESTION_ID) != '' and
                (TOPIC_ID in query_string and query_string.get(TOPIC_ID) != '')):
                return query_string.get(QUESTION_ID), query_string.get(TOPIC_ID)
            else:
                raise InvalidLambdaInputException(f'Could not find {QUESTION_ID} or {TOPIC_ID} in Input')
        else:
            raise InvalidLambdaInputException(f'Could not find {QUERY_STRING_PARAMETERS} in Input')

    def extract_user_id_from_input(self) -> str:
        user_id = self.event.get('requestContext', {}).get('authorizer', {}).get('claims', {}).get('sub')
        if user_id is None:
            raise InvalidLambdaInputException("Unable to get user_id from token")
        else:
            return user_id
