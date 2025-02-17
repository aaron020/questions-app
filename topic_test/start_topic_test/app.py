import json
import boto3
from decimal import Decimal

from common_layer.api_requests_helper import get_response_headers_cors, Response, StatusCodes
from common_layer.database_helper import connect_any_table
from common_layer.exceptions import InvalidLambdaInputException, DatabaseNoContentException, \
    DatabaseFailedToQueryExeception, DatabaseFailedToPutExeception
from database_service import DatabaseService
from start_topic_test_service import StartTopicTest
from validate_input import ValidateInput
from common_layer.input_helper import InputValidator


database_connection = connect_any_table()

def lambda_handler(event, context):
    headers = get_response_headers_cors(allow_methods=['POST'])
    try:
        topic_id: str = ValidateInput(event).extract_input()
        user_id: str = InputValidator.extract_user_id_from_input(event)
        database_service: DatabaseService = DatabaseService(database_connection)
        topic_test_id, questions = StartTopicTest(database_service).start_topic_test(topic_id, user_id)

        response = {
            'topic_test_id': topic_test_id,
            'data':  remove_correct_boolean(questions)
        }

        return Response(StatusCodes.STATUS_OK, headers, response).build_response()
    except InvalidLambdaInputException as e:
        return Response(StatusCodes.STATUS_CLIENT_ERROR, headers, str(e)).build_response()
    except (DatabaseFailedToQueryExeception, DatabaseFailedToPutExeception) as e:
        return Response(StatusCodes.STATUS_SERVER_ERROR, headers, str(e)).build_response()
    except DatabaseNoContentException as e:
        return Response(StatusCodes.STATUS_NO_CONTENT, headers, []).build_response()
    except Exception as e:
        return Response(StatusCodes.STATUS_SERVER_ERROR, headers, str(e)).build_response()


def remove_correct_boolean(questions) -> list:
    for question in questions:
        if 'user_id' in question:
            del question['user_id']
        if 'explanation' in question:
            del question['explanation']
        for answer in question.get('answers'):
            if 'correct' in answer:
                del answer['correct']
    return questions