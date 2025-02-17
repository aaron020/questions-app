from common_layer.database_helpers import TopicOwner
from common_layer.exceptions import InvalidLambdaInputException, DatabaseFailedToQueryExeception, \
    DatabaseNoContentException
from common_layer.input_helper import InputValidator
from constants import QUERY_STRING_PARAMETERS, TOPIC_ID


class CheckTopicOwnerService:

    def check_topic_owner(self, event, database_service) -> bool:
        given_user_id: str = InputValidator.extract_user_id_from_input(event)
        topic_id: str = self._extract_input(event)
        required_user_id: list = TopicOwner.find_topic_owners(database_service, topic_id)

        if given_user_id in required_user_id:
            return True
        else:
            return False

    @staticmethod
    def _extract_input(event: str) -> str:
        if QUERY_STRING_PARAMETERS in event:
            query_string: dict = event.get(QUERY_STRING_PARAMETERS)
            if TOPIC_ID in query_string:
                return query_string.get(TOPIC_ID)
            else:
                raise InvalidLambdaInputException(f'Could not find {TOPIC_ID} in Input')
        else:
            raise InvalidLambdaInputException(f'Could not find {QUERY_STRING_PARAMETERS} in Input')

    @staticmethod
    def _pull_user_id_from_database(database_table, topic_id):
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

        return response['Items'][0]['user_id']

