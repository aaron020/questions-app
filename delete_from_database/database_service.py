from common_layer.exceptions.custom_exceptions import DatabaseFailedToDeleteExeception


class DatabaseService:

    def __init__(self, comp_id: str, topic: str, database_table):
        self.comp_id = comp_id
        self.topic = topic
        self.database_table = database_table

    def delete_from_database(self) -> None:
        try:
            response = self.database_table.delete_item(
                Key={'comp_id' : self.comp_id, 'topic': self.topic},
                ReturnValues='ALL_OLD'
            )
        except Exception as e:
            raise DatabaseFailedToDeleteExeception(f'Failed to delete from database {e}')
