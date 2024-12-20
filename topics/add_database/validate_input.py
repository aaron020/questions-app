import json

from common_layer.database_models import Topic
from common_layer.exceptions import InvalidLambdaInputException


class ValidateInput:
    def __init__(self, event: dict):
        self.event = event

    def extract_and_validate_input(self) -> dict:
        extracted_topic: dict = self._extract_topic_from_input()
        extracted_topic['user_id'] = self._extract_user_id_from_input()
        self._validate(extracted_topic)
        return extracted_topic

    def _extract_topic_from_input(self) -> dict:
        if 'body' in self.event:
            try:
                return json.loads(self.event.get('body'))
            except Exception as e:
                raise InvalidLambdaInputException(f'unable to convert body to dict: {e}')
        else:
            raise InvalidLambdaInputException('body not present in event')

    def _extract_user_id_from_input(self) -> str:
        user_id = self.event.get('requestContext', {}).get('authorizer', {}).get('claims', {}).get('sub')
        if user_id is None:
            raise InvalidLambdaInputException("Unable to get user_id from token")
        else:
            return user_id

    @staticmethod
    def _validate(extracted_topic: dict) -> None:
        valid_keys = Topic.valid_topic_keys()

        for key in valid_keys:
            if key not in extracted_topic or extracted_topic.get(key) is None:
                raise InvalidLambdaInputException(f'topics missing the following value: {key}')

        if len(extracted_topic.get('description')) > 200:
            raise InvalidLambdaInputException(f'description cannot be more than 200 characters')

        if len(extracted_topic.get('topic_name')) > 20:
            raise InvalidLambdaInputException(f'topic name cannot be more than 20 characters')

