from common_layer.api_requests_helper import StatusCodes, Response, get_response_headers_cors
from common_layer.database_helper import connect_database
from common_layer.exceptions import InvalidLambdaInputException, UnAuthorizedDeleteException, DatabaseFailedToDeleteExeception
from database_service import DatabaseService
from validate_input import ValidateInput

database_table = connect_database()

def lambda_handler(event, context):
    headers = get_response_headers_cors(allow_methods=['DELETE'])

    try:
        validate_input = ValidateInput(event)
        comp_id, topic = validate_input.extract_query_string_parameters()
        user_id: str = validate_input.extract_user_id_from_input()
        DatabaseService(comp_id, topic, user_id, database_table).delete_from_database()
        return Response(StatusCodes.STATUS_OK, headers, f'Question with comp_id {comp_id} deleted').build_response()

    except InvalidLambdaInputException as e:
        return Response(StatusCodes.STATUS_CLIENT_ERROR, headers, str(e)).build_response()
    except DatabaseFailedToDeleteExeception as e:
        return Response(StatusCodes.STATUS_SERVER_ERROR, headers, str(e)).build_response()
    except UnAuthorizedDeleteException as e:
        return Response(StatusCodes.STATUS_UNAUTHORIZED, headers, str(e)).build_response()
    except Exception as e:
        return Response(StatusCodes.STATUS_SERVER_ERROR, headers, str(e)).build_response()