import json

from common_layer.exceptions import InvalidLambdaInputException


class ValidateInput:
    def __init__(self, event: dict):
        self.event = event

    def extract_and_validate_input(self):
        body: dict = self._extract_body_from_input()
        self._validate(body)
        return body

    def _extract_body_from_input(self):
        if 'body' in self.event:
            try:
                return json.loads(self.event.get('body'))
            except Exception as e:
                raise InvalidLambdaInputException(f'unable to convert body to dict: {e}')
        else:
            raise InvalidLambdaInputException('body not present in event')

    @staticmethod
    def _validate(body: dict) -> None:
        valid_keys = ['topic_test_id', 'question_id', 'answer_id']

        for key in valid_keys:
            if key not in body or body.get(key) is None:
                raise InvalidLambdaInputException(f'body missing the following value: {key}')
