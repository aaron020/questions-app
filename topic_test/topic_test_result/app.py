from common_layer.api_requests_helper import get_response_headers_cors, StatusCodes, Response
from common_layer.database_helper import connect_any_table
from common_layer.exceptions import InvalidLambdaInputException, DatabaseFailedToQueryExeception, \
    DatabaseFailedToPutExeception, UnAuthorizedRequestException, DatabaseNoContentException
from common_layer.input_helper import InputValidator

database_connection = connect_any_table()

def lambda_handler(event, context):
    headers = get_response_headers_cors(allow_methods=['POST'])
    try:
        topic_test_id: str = InputValidator.extract_value_from_params('topic_test_id', event)
        user_id: str = InputValidator.extract_user_id_from_input(event)

        return Response(StatusCodes.STATUS_OK, headers, response).build_response()
    except (InvalidLambdaInputException, DatabaseFailedToQueryExeception, DatabaseFailedToPutExeception) as e:
        return Response(StatusCodes.STATUS_CLIENT_ERROR, headers, str(e)).build_response()
    except UnAuthorizedRequestException as e:
        return Response(StatusCodes.STATUS_UNAUTHORIZED, headers, str(e)).build_response()
    except DatabaseNoContentException:
        return Response(StatusCodes.STATUS_NO_CONTENT, headers, []).build_response()
    except Exception as e:
        return Response(StatusCodes.STATUS_SERVER_ERROR, headers, str(e)).build_response()

def remove_user_id(response : dict):
    if 'user_id' in response:
        del response['user_id']
    return response
