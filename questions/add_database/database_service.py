import uuid
import random

from botocore.exceptions import ClientError

from common_layer.database_models import Question
from common_layer.exceptions import DatabaseFailedToPutExeception


class DatabaseService:

    def __init__(self, input_question: dict, database_table):
        self.database_question: dict = self.convert_to_database_question(input_question)
        self.database_table = database_table

    def add_to_database(self):
        try:
            response: dict = self.database_table.put_item(
                Item=self.database_question,
                ConditionExpression='attribute_not_exists(question_id)'
            )
            response_code: int = response.get('ResponseMetadata').get('HTTPStatusCode')
            if response_code != 200:
                raise DatabaseFailedToPutExeception(f'Unable to add to database, response code: {response_code}')
        except ClientError as e:
            raise DatabaseFailedToPutExeception(f'Unable to add to database, {e}')


    @staticmethod
    def convert_to_database_question(input_question: dict) -> dict:
        question_id: str =  str(uuid.uuid4())

        random_num: int = random.randint(1, 1000)

        answers = []
        for answer in input_question.get('answers'):
            answers.append({
                "answer": answer.get('answer'),
                "correct": answer.get('correct'),
                "answer_id": str(uuid.uuid4())
            })
        return Question(question_id,input_question.get('topic_id'), input_question.get('questions'),answers,
                                          input_question.get('explanation'), input_question.get('difficulty'),
                                          random_num, input_question.get('user_id')).prepare_for_database()

