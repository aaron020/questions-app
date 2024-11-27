import json

from common_layer.exceptions import InvalidLambdaInputException


class ValidateInput:
    def __init__(self, event: dict):
        self.event = event

    def extract_and_validate_input(self) -> dict:
        extracted_question: dict = self._extract_question_from_input()
        extracted_question['user_id'] = self._extract_user_id_from_input()
        self._validate(extracted_question)
        return extracted_question

    def _extract_question_from_input(self) -> dict:
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
    def _validate(extracted_question: dict) -> None:
        valid_keys = ['question', 'answers', 'topic', 'explanation', 'difficulty', 'user_id']

        for key in valid_keys:
            if key not in extracted_question or extracted_question.get(key) is None:
                raise InvalidLambdaInputException(f'question missing the following value: {key}')

        if 0 > extracted_question.get('difficulty') > 3:
            raise InvalidLambdaInputException(f'question difficulty must be between 1 and 3')

        if len(extracted_question.get('answers')) > 5:
            raise InvalidLambdaInputException(f'answers cannot be more than 5')

