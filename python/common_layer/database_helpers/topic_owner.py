from common_layer.exceptions import DatabaseFailedToQueryExeception, DatabaseNoContentException


class TopicOwner:

    @staticmethod
    def find_topic_owners(database_table, topic_id) -> list:
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

        return [response['Items'][0]['user_id']]