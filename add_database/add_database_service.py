import json

from add_database.validate_input import ValidateInput
from common_layer.exceptions import InvalidLambdaInputException


class AddDatabaseService:

    def __init__(self, event: dict):
        self.input_question = ValidateInput(event).extract_and_validate_input()

    def add_question_to_database(self):




