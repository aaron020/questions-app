from common_layer.api_requests_helper import get_response_headers_cors, StatusCodes, Response
from common_layer.database_helper import connect_topic_test_table
from common_layer.exceptions import InvalidLambdaInputException, DatabaseFailedToQueryExeception, \
    DatabaseFailedToPutExeception, UnAuthorizedRequestException, DatabaseNoContentException
from common_layer.input_helper import InputValidator
from database_service import DatabaseService

database_table = connect_topic_test_table()

def lambda_handler(event, context):
    headers = get_response_headers_cors(allow_methods=['GET'])
    try:
        topic_test_id: str = InputValidator.extract_value_from_params('topic_test_id', event)
        user_id: str = InputValidator.extract_user_id_from_input(event)

        topic_test : dict = DatabaseService(database_table).get_topic_test(topic_test_id)

        if topic_test.get('user_id') == user_id:
            total: int = len(topic_test.get('unanswered_questions')) + len(topic_test.get('answered_correct')) + len(topic_test.get('answered_incorrect'))
            score: float = (len(topic_test.get('answered_correct')) / total) * 100
            score = round(score, 2)
            response = {
                "total": total,
                "score": score,
                "unanswered_questions" : topic_test.get('unanswered_questions'),
                "answered_correct": topic_test.get('answered_correct'),
                "answered_incorrect": topic_test.get('answered_incorrect')
            }
            return Response(StatusCodes.STATUS_OK, headers, response).build_response()
        else:
            return Response(StatusCodes.STATUS_UNAUTHORIZED, headers, False).build_response()

    except (InvalidLambdaInputException, DatabaseFailedToQueryExeception, DatabaseFailedToPutExeception) as e:
        return Response(StatusCodes.STATUS_CLIENT_ERROR, headers, str(e)).build_response()
    except UnAuthorizedRequestException as e:
        return Response(StatusCodes.STATUS_UNAUTHORIZED, headers, str(e)).build_response()
    except DatabaseNoContentException:
        return Response(StatusCodes.STATUS_NO_CONTENT, headers, []).build_response()
    except Exception as e:
        return Response(StatusCodes.STATUS_SERVER_ERROR, headers, str(e)).build_response()


