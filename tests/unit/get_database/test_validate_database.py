import pytest

from common_layer.exceptions import InvalidLambdaInputException
from get_database.validate_input import ValidateInput


class TestValidateInput:

    def test_extract_topic_from_input(self):
        event: dict = {
            'queryStringParameters': {
                'topic': 'python'
            }
        }

        topic: str = ValidateInput(event)._extract_topic_from_input()

        assert topic == 'python'

    def test_extract_topic_from_input_no_query_string_param(self):
        event: dict = {
            'queryString': {
                'topic': 'python'
            }
        }
        with pytest.raises(InvalidLambdaInputException) as context:
            ValidateInput(event)._extract_topic_from_input()

        assert 'Could not find queryStringParameters in Input' in str(context)

    def test_extract_topic_from_input_no_topic(self):
        event: dict = {
            'queryStringParameters': {
                'topics': 'python'
            }
        }
        with pytest.raises(InvalidLambdaInputException) as context:
            ValidateInput(event)._extract_topic_from_input()

        assert 'Could not find topic in Input' in str(context)

    def test_extract_topic_from_input_no_topic_empty(self):
        event: dict = {
            'queryStringParameters': {
                'topic': ''
            }
        }
        with pytest.raises(InvalidLambdaInputException) as context:
            ValidateInput(event)._extract_topic_from_input()

        assert 'Could not find topic in Input' in str(context)


