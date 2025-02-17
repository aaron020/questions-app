from check_topic_owner_service import CheckTopicOwnerService
from common_layer.database_helper import connect_topics_table
from common_layer.api_requests_helper import get_response_headers_cors, Response, StatusCodes
from common_layer.exceptions import DatabaseNoContentException, InvalidLambdaInputException, \
    DatabaseFailedToQueryExeception

table = database_table = connect_topics_table()

def lambda_handler(event, context):
    headers = get_response_headers_cors(allow_methods=['GET'])
    try:
        if CheckTopicOwnerService().check_topic_owner(event, table):
            return Response(StatusCodes.STATUS_OK, headers, True).build_response()
        else:
            return Response(StatusCodes.STATUS_UNAUTHORIZED, headers, False).build_response()
    except InvalidLambdaInputException as e:
        return Response(StatusCodes.STATUS_CLIENT_ERROR, headers, str(e)).build_response()
    except DatabaseFailedToQueryExeception as e:
        return Response(StatusCodes.STATUS_SERVER_ERROR, headers, str(e)).build_response()
    except DatabaseNoContentException as e:
        return Response(StatusCodes.STATUS_NO_CONTENT, headers, str(e)).build_response()
    except Exception as e:
        return Response(StatusCodes.STATUS_SERVER_ERROR, headers, str(e)).build_response()