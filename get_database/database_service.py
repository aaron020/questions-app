from boto3.dynamodb.conditions import Key

from common_layer.exceptions.custom_exceptions import DatabaseFailedToQueryExeception, DatabaseNoContentException


class DatabaseService:
    def __init__(self, topic: str, database_table):
        self.topic = topic
        self.database_table = database_table

    def get_from_database(self) -> list:
        try:
            response = self.database_table.query(
                IndexName='TopicIndex',
                KeyConditionExpression=Key('topic').eq(self.topic),
                ReturnConsumedCapacity='TOTAL'
            )
            items: list = response.get('Items', [])
        except Exception as e:
            raise DatabaseFailedToQueryExeception(f'Unable to query database: {e}')

        if len(items) == 0:
            raise DatabaseNoContentException(f'Found no items for topics {self.topic}')

        return items