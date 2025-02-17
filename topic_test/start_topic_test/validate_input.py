from common_layer.exceptions import InvalidLambdaInputException
from constants import QUERY_STRING_PARAMETERS, TOPIC_ID


class ValidateInput:
    def __init__(self, event: dict):
        self.event = event
        
    def extract_input(self) -> str:
        if QUERY_STRING_PARAMETERS in self.event:
            query_string: dict = self.event.get(QUERY_STRING_PARAMETERS)
            if TOPIC_ID in query_string and query_string.get(TOPIC_ID) != '':
                return query_string.get(TOPIC_ID)
            else:
                raise InvalidLambdaInputException(f'Could not find {TOPIC_ID} in Input')
        else:
            raise InvalidLambdaInputException(f'Could not find {QUERY_STRING_PARAMETERS} in Input')
