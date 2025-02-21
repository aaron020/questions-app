
from common_layer.api_requests_helper import get_response_headers_cors, Response, StatusCodes
from common_layer.database_helper import connect_topics_table
from common_layer.exceptions import DatabaseFailedToScan, DatabaseNoContentException, InvalidLambdaInputException
from common_layer.input_helper import InputValidator
from database_service import DatabaseService
from validate_input import ValidateInput

table = database_table = connect_topics_table()

def lambda_handler(event, context):
    headers = get_response_headers_cors(allow_methods=['GET'])

    try:
        topic_id: str = InputValidator.extract_value_from_params('topic_id', event)
        user_id: str = InputValidator.extract_value_from_params('user_id', event)
        last_evaluated_key = {"topic_id": topic_id, "user_id": user_id}
    except InvalidLambdaInputException:
        last_evaluated_key = None

    try:
        limit = ValidateInput.extract_input(event)
        topics = remove_user_id(DatabaseService.scan_database(table, last_evaluated_key, limit))
        return Response(StatusCodes.STATUS_OK, headers, topics).build_response()
    except InvalidLambdaInputException as e:
        return Response(StatusCodes.STATUS_CLIENT_ERROR, headers, str(e)).build_response()
    except DatabaseFailedToScan as e:
        return Response(StatusCodes.STATUS_SERVER_ERROR, headers, str(e)).build_response()
    except DatabaseNoContentException as e:
        return Response(StatusCodes.STATUS_NO_CONTENT, headers, str(e)).build_response()
    except Exception as e:
        return Response(StatusCodes.STATUS_SERVER_ERROR, headers, str(e)).build_response()


def remove_user_id(response : dict):
    for d in response['topics']:
        if 'user_id' in d:
            del d['user_id']
    return response

event = {
  "queryStringParameters": {
    "limit": "5"
  },
  "body": "{\"topic_id\": \"839cd8b6-7462-4f03-aac7-16301be13d6b\",\"user_id\": \"b2d564a4-1051-701f-040f-5ad112e6224f\"}"
}

lambda_handler(event, None)