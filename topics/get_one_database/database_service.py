from common_layer.exceptions import DatabaseFailedToQueryExeception, DatabaseNoContentException

class DatabaseService:

    @staticmethod
    def get_from_database(topic_id: str, database_table):
        try:
            response = database_table.query(
                KeyConditionExpression='topic_id = :pk',
                ExpressionAttributeValues={
                    ':pk': topic_id
                }
            )
        except Exception as e:
            raise DatabaseFailedToQueryExeception(f'Unable to query database: {e}')

        if len(response['Items']) == 0:
            raise DatabaseNoContentException(f'Found no items for topic_id {topic_id}')

        return response['Items'][0]