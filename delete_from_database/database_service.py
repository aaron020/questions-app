import botocore

from common_layer.exceptions import DatabaseFailedToDeleteExeception
from common_layer.exceptions import UnAuthorizedDeleteException


class DatabaseService:

    def __init__(self, comp_id: str, topic: str, user_id: str, database_table):
        self.comp_id = comp_id
        self.topic = topic
        self.user_id = user_id
        self.database_table = database_table

    def delete_from_database(self) -> None:
        try:
            response = self.database_table.delete_item(
                Key={'comp_id': self.comp_id, 'topic': self.topic},
                ConditionExpression='user_id = :expected_user_id',
                ExpressionAttributeValues={':expected_user_id': self.user_id},
                ReturnValues='ALL_OLD'
            )
        except botocore.exceptions.ClientError as e:
            if e.response['Error']['Code'] == 'ConditionalCheckFailedException':
                raise UnAuthorizedDeleteException('User is not authorized to delete this item')
        except Exception as e:
            raise DatabaseFailedToDeleteExeception(f'Failed to delete from database: {e}')
