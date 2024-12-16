from boto3.dynamodb.conditions import Key

from common_layer.exceptions import DatabaseFailedToQueryExeception, DatabaseNoContentException


class DatabaseService:
    def __init__(self, topic_id: str, database_table):
        self.topic_id = topic_id
        self.database_table = database_table

    def get_from_database(self) -> list:
        try:
            response = self.database_table.query(
                IndexName='TopicIndex',
                KeyConditionExpression=Key('topic_id').eq(self.topic_id),
                ReturnConsumedCapacity='TOTAL'
            )
            items: list = response.get('Items', [])
        except Exception as e:
            raise DatabaseFailedToQueryExeception(f'Unable to query database: {e}')

        if len(items) == 0:
            raise DatabaseNoContentException(f'Found no items for topics {self.topic_id}')

        return items