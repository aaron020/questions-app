import botocore

from common_layer.exceptions import DatabaseFailedToDeleteExeception
from common_layer.exceptions import UnAuthorizedDeleteException


class DatabaseService:

    def __init__(self, question_id: str, topic_id: str, database_table):
        self.question_id = question_id
        self.topic_id = topic_id
        self.database_table = database_table

    def delete_from_database(self) -> None:
        try:
            self.database_table.delete_item(
                Key={'question_id': self.question_id, 'topic_id': self.topic_id},
            )
        except Exception as e:
            raise DatabaseFailedToDeleteExeception(f'Failed to delete from database: {e}')
