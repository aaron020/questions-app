from common_layer.api_requests_helper import get_response_headers_cors, StatusCodes, Response
from common_layer.database_helper import connect_topics_table
from common_layer.exceptions import InvalidLambdaInputException, DatabaseFailedToPutExeception
from database_service import DatabaseService
from validate_input import ValidateInput

table = database_table = connect_topics_table()

def lambda_handler(event, context):
    headers = get_response_headers_cors(allow_methods=['POST'])

    try:
        input_topic: dict = ValidateInput(event).extract_and_validate_input()
        new_topic = DatabaseService(input_topic, table).add_to_database()
        return Response(StatusCodes.STATUS_OK, headers, new_topic.get('topic_id')).build_response()
    except InvalidLambdaInputException as e:
        return Response(StatusCodes.STATUS_CLIENT_ERROR, headers, str(e)).build_response()
    except DatabaseFailedToPutExeception as e:
        return Response(StatusCodes.STATUS_SERVER_ERROR, headers, str(e)).build_response()
    except Exception as e:
        return Response(StatusCodes.STATUS_SERVER_ERROR, headers, str(e)).build_response()
