from constants import QUERY_STRING_PARAMETERS, TOPIC_ID
from common_layer.exceptions import InvalidLambdaInputException


class ValidateInput:

    @staticmethod
    def extract_input(event) -> str:
        if QUERY_STRING_PARAMETERS in event:
            query_string: dict = event.get(QUERY_STRING_PARAMETERS)
            if TOPIC_ID in query_string:
                return query_string.get(TOPIC_ID)
            else:
                raise InvalidLambdaInputException(f'Could not find {TOPIC_ID} in Input')
        else:
            raise InvalidLambdaInputException(f'Could not find {QUERY_STRING_PARAMETERS} in Input')