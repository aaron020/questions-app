from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError

from common_layer.database_models import TopicTest
from common_layer.exceptions import DatabaseFailedToQueryExeception, DatabaseNoContentException, \
    DatabaseFailedToPutExeception


class DatabaseService:
    def __init__(self, database_connection):
        self.database_connection = database_connection

    def get_questions_database(self, topic_id: str) -> list:
        try:
            database_table = self.database_connection.Table('questions')
            response = database_table.query(
                IndexName='TopicIndex',
                KeyConditionExpression=Key('topic_id').eq(topic_id),
                ReturnConsumedCapacity='TOTAL'
            )
            items: list = response.get('Items', [])
        except Exception as e:
            raise DatabaseFailedToQueryExeception(f'Unable to query database: {e}')

        if len(items) == 0:
            raise DatabaseNoContentException(f'Found no items for topics {topic_id}')

        return items

    def add_topic_test_database(self, topic_test: TopicTest):
        database_table = self.database_connection.Table('topic_test')
        try:
            response: dict = database_table.put_item(
                Item=topic_test.prepare_for_database(),
                ConditionExpression='attribute_not_exists(topic_test_id)'
            )
            response_code: int = response.get('ResponseMetadata').get('HTTPStatusCode')
            if response_code != 200:
                raise DatabaseFailedToPutExeception(f'Unable to add to database, response code: {response_code}')
        except ClientError as e:
            raise DatabaseFailedToPutExeception(f'Unable to add to database, {e}')
