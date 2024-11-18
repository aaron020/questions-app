from common_layer.exceptions import InvalidLambdaInputException
from constants import QUERY_STRING_PARAMETERS, TOPIC


class ValidateInput:
    def __init__(self, event: dict):
        self.event = event
        
    def extract_input(self) -> str:
        if QUERY_STRING_PARAMETERS in self.event:
            query_string: dict = self.event.get(QUERY_STRING_PARAMETERS)
            if TOPIC in query_string and query_string.get(TOPIC) != '':
                return query_string.get(TOPIC)
            else:
                raise InvalidLambdaInputException(f'Could not find {TOPIC} in Input')
        else:
            raise InvalidLambdaInputException(f'Could not find {QUERY_STRING_PARAMETERS} in Input')
