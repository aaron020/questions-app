import json

from common_layer.exceptions import InvalidLambdaInputException

QUERY_STRING_PARAMETERS: str = 'queryStringParameters'

class InputValidator:

    @staticmethod
    def extract_user_id_from_input(event: dict) -> str:
        user_id = event.get('requestContext', {}).get('authorizer', {}).get('claims', {}).get('sub')
        if user_id is None:
            raise InvalidLambdaInputException("Unable to get user_id from token")
        else:
            return user_id

    @staticmethod
    def extract_value_from_params(param_key : str, event: dict) -> str:
        if QUERY_STRING_PARAMETERS in event:
            query_string: dict = event.get(QUERY_STRING_PARAMETERS)
            if param_key in query_string:
                return query_string.get(param_key)
            else:
                raise InvalidLambdaInputException(f'Could not find {param_key} in Input')
        else:
            raise InvalidLambdaInputException(f'Could not find {QUERY_STRING_PARAMETERS} in Input')

    @staticmethod
    def extract_body_from_input(event: dict) -> dict:
        if 'body' in event:
            try:
                return json.loads(event.get('body'))
            except Exception as e:
                raise InvalidLambdaInputException(f'unable to convert body to dict: {e}')
        else:
            raise InvalidLambdaInputException('body not present in event')