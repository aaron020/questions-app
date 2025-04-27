from common_layer.database_models import Topic
from common_layer.exceptions import InvalidLambdaInputException
from common_layer.input_helper import InputValidator


class ValidateInput:

    @staticmethod
    def extract_and_validate(event: dict):
        topic = InputValidator.extract_body_from_input(event)
        ValidateInput._validate(topic)
        return topic

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