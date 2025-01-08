from common_layer.exceptions import InvalidLambdaInputException
from constants import QUERY_STRING_PARAMETERS
from constants import LIMIT


class ValidateInput:

    @staticmethod
    def extract_input(event):
        if QUERY_STRING_PARAMETERS in event:
            query_string: dict = event.get(QUERY_STRING_PARAMETERS)
            if LIMIT in query_string:
                return int(query_string.get(LIMIT))
            else:
                raise InvalidLambdaInputException(f'Could not find {LIMIT} in Input')
        else:
            raise InvalidLambdaInputException(f'Could not find {QUERY_STRING_PARAMETERS} in Input')

