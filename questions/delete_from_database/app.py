from common_layer.api_requests_helper import StatusCodes, Response, get_response_headers_cors
from common_layer.database_helper import connect_questions_table, connect_topics_table
from common_layer.database_helpers import TopicOwner
from common_layer.exceptions import InvalidLambdaInputException, UnAuthorizedDeleteException, DatabaseFailedToDeleteExeception
from database_service import DatabaseService
from validate_input import ValidateInput

database_table = connect_questions_table()
table_topics = connect_topics_table()

def lambda_handler(event, context):
    headers = get_response_headers_cors(allow_methods=['DELETE'])

    try:
        validate_input = ValidateInput(event)
        question_id, topic_id = validate_input.extract_query_string_parameters()
        user_id: str = validate_input.extract_user_id_from_input()
        required_user_ids: list = TopicOwner.find_topic_owners(table_topics, topic_id)
        if user_id in required_user_ids:
            DatabaseService(question_id, topic_id, database_table).delete_from_database()
            return Response(StatusCodes.STATUS_OK, headers, f'Question with question_id {question_id} deleted').build_response()
        else:
            return Response(StatusCodes.STATUS_UNAUTHORIZED, headers, False).build_response()
    except InvalidLambdaInputException as e:
        return Response(StatusCodes.STATUS_CLIENT_ERROR, headers, str(e)).build_response()
    except DatabaseFailedToDeleteExeception as e:
        return Response(StatusCodes.STATUS_SERVER_ERROR, headers, str(e)).build_response()
    except UnAuthorizedDeleteException as e:
        return Response(StatusCodes.STATUS_UNAUTHORIZED, headers, str(e)).build_response()
    except Exception as e:
        return Response(StatusCodes.STATUS_SERVER_ERROR, headers, str(e)).build_response()

event = {
    "queryStringParameters": {
        "question_id": "dd4edb09-ab85-4667-a083-9fa02454699d",
        "topic_id": "5b4f8728-bdea-4b3c-8956-f5dea3198b21"
    },
    "requestContext": {
        "authorizer": {
            "claims": {
                "sub": "d23544c4-e0f1-7004-0a36-8bdb02d33bee"
            }
        }
    }
}

print(lambda_handler(event, None))