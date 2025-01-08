from common_layer.exceptions import DatabaseFailedToScan, DatabaseNoContentException


class DatabaseService:

    @staticmethod
    def scan_database(database_table, last_evaluated_key, limit):
        scan_params = {'Limit': limit}
        try:
            if last_evaluated_key is not None:
                scan_params['ExclusiveStartKey'] = last_evaluated_key

            response = database_table.scan(**scan_params)

            items = response.get('Items', [])
            new_last_evaluated_key = response.get('LastEvaluatedKey')
        except Exception as e:
            raise DatabaseFailedToScan(f'Unable to query database: {e}')

        if not items:
            raise DatabaseNoContentException('Found no items from database')

        return {'topics':items, 'last_evaluated_key':new_last_evaluated_key}

