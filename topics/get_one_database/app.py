
from common_layer.api_requests_helper import get_response_headers_cors, Response, StatusCodes
from common_layer.database_helper import connect_topics_table
from database_service import DatabaseService
from validate_input import ValidateInput
from common_layer.exceptions import DatabaseNoContentException, InvalidLambdaInputException, \
    DatabaseFailedToQueryExeception

table = database_table = connect_topics_table()


def lambda_handler(event, context):
    headers = get_response_headers_cors(allow_methods=['GET'])

    try:
        topic_id = ValidateInput.extract_input(event)
        topic = remove_user_id(DatabaseService.get_from_database(topic_id, table))
        return Response(StatusCodes.STATUS_OK, headers, topic).build_response()
    except InvalidLambdaInputException as e:
        return Response(StatusCodes.STATUS_CLIENT_ERROR, headers, str(e)).build_response()
    except DatabaseFailedToQueryExeception as e:
        return Response(StatusCodes.STATUS_SERVER_ERROR, headers, str(e)).build_response()
    except DatabaseNoContentException as e:
        return Response(StatusCodes.STATUS_NO_CONTENT, headers, str(e)).build_response()
    except Exception as e:
        return Response(StatusCodes.STATUS_SERVER_ERROR, headers, str(e)).build_response()

def remove_user_id(response : dict):
    if 'user_id' in response:
        del response['user_id']
    return response