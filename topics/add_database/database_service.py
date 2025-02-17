import uuid
import random
from unicodedata import category

from botocore.exceptions import ClientError

from common_layer.database_models import Question, Topic
from common_layer.exceptions import DatabaseFailedToPutExeception


class DatabaseService:

    def __init__(self, input_question: dict, database_table):
        self.database_topic: dict = self.convert_to_database_topic(input_question)
        self.database_table = database_table

    def add_to_database(self) -> dict:
        try:
            response: dict = self.database_table.put_item(
                Item=self.database_topic,
                ConditionExpression='attribute_not_exists(comp_id)'
            )
            response_code: int = response.get('ResponseMetadata').get('HTTPStatusCode')
            if response_code != 200:
                raise DatabaseFailedToPutExeception(f'Unable to add to database, response code: {response_code}')
            return self.database_topic
        except ClientError as e:
            raise DatabaseFailedToPutExeception(f'Unable to add to database, {e}')


    @staticmethod
    def convert_to_database_topic(input_topic: dict) -> dict:
        topic_id: str =  str(uuid.uuid4())
        return Topic(topic_id=topic_id,
                     user_id=input_topic.get('user_id'),
                     topic_name=input_topic.get('topic_name'),
                     description=input_topic.get('description'),
                     category=input_topic.get('category')).prepare_for_database()
