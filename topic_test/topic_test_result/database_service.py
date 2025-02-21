from common_layer.exceptions import DatabaseFailedToQueryExeception, DatabaseNoContentException


class DatabaseService:
    def __init__(self, database_table):
        self.database_table = database_table

    def get_topic_test(self, topic_test_id: str) -> dict:
        try:
            response = self.database_table.query(
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



