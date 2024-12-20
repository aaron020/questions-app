import botocore

from common_layer.exceptions import DatabaseFailedToDeleteExeception
from common_layer.exceptions import UnAuthorizedDeleteException


class DatabaseService:

    def __init__(self, question_id: str, topic_id: str, user_id: str, database_table):
        self.question_id = question_id
        self.topic_id = topic_id
        self.user_id = user_id
        self.database_table = database_table

    def delete_from_database(self) -> None:
        try:
            response = self.database_table.delete_item(
                Key={'comp_id': self.question_id, 'topic': self.topic_id},
                ConditionExpression='user_id = :expected_user_id',
                ExpressionAttributeValues={':expected_user_id': self.user_id},
                ReturnValues='ALL_OLD'
            )
        except botocore.exceptions.ClientError as e:
            if e.response['Error']['Code'] == 'ConditionalCheckFailedException':
                raise UnAuthorizedDeleteException('User is not authorized to delete this item')
        except Exception as e:
            raise DatabaseFailedToDeleteExeception(f'Failed to delete from database: {e}')
