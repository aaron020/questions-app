from botocore.exceptions import ClientError

from common_layer.exceptions import DatabaseFailedToQueryExeception, DatabaseNoContentException, \
    DatabaseFailedToPutExeception


class DatabaseService:
    def __init__(self, database_connection):
        self.database_connection = database_connection

    def get_topic_test(self, topic_test_id: str):
        try:
            database_table = self.database_connection.Table('topic_test')
            response = database_table.query(
                KeyConditionExpression='topic_test_id = :pk',
                ExpressionAttributeValues={
                    ':pk': topic_test_id
                }
            )
        except Exception as e:
            raise DatabaseFailedToQueryExeception(f'Unable to query database: {e}')

        if len(response['Items']) == 0:
            raise DatabaseNoContentException(f'Found no items for topic_test_id {topic_test_id}')

        return response['Items'][0]

    def get_question(self, question_id: str):
        try:
            database_table = self.database_connection.Table('questions')
            response = database_table.query(
                KeyConditionExpression='question_id = :pk',
                ExpressionAttributeValues={
                    ':pk': question_id
                }
            )
        except Exception as e:
            raise DatabaseFailedToQueryExeception(f'Unable to query database: {e}')

        if len(response['Items']) == 0:
            raise DatabaseNoContentException(f'Found no items for question_id {question_id}')

        return response['Items'][0]

    def update_topic_test(self, topic_test: dict):
        try:
            database_table = self.database_connection.Table('topic_test')
            response: dict = database_table.put_item(
                Item=topic_test
            )
            response_code: int = response.get('ResponseMetadata').get('HTTPStatusCode')
            if response_code != 200:
                raise DatabaseFailedToPutExeception(f'Unable to update database, response code: {response_code}')
        except ClientError as e:
            raise DatabaseFailedToPutExeception(f'Unable to update database, {e}')

