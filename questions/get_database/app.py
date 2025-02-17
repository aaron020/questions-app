import json
import boto3
from decimal import Decimal

from common_layer.api_requests_helper import get_response_headers_cors, Response, StatusCodes
from common_layer.database_helper import connect_questions_table
from common_layer.database_helper import connect_topics_table
from common_layer.exceptions import InvalidLambdaInputException, DatabaseNoContentException, DatabaseFailedToQueryExeception
from database_service import DatabaseService
from validate_input import ValidateInput
from common_layer.database_helpers import TopicOwner
from common_layer.input_helper import InputValidator


table = connect_questions_table()
table_topics = connect_topics_table()

def lambda_handler(event, context):
    headers = get_response_headers_cors(allow_methods=['GET'])
    try:
        topic: str = ValidateInput(event).extract_input()
        user_id: str = InputValidator.extract_user_id_from_input(event)
        required_user_ids: list = TopicOwner.find_topic_owners(table_topics, topic)
        if user_id in required_user_ids:
            questions: list = DatabaseService(topic, table).get_from_database()
            return Response(StatusCodes.STATUS_OK, headers, remove_user_id(questions)).build_response()
        else:
            return Response(StatusCodes.STATUS_UNAUTHORIZED, headers, False).build_response()
    except InvalidLambdaInputException as e:
        return Response(StatusCodes.STATUS_CLIENT_ERROR, headers, str(e)).build_response()
    except DatabaseFailedToQueryExeception as e:
        return Response(StatusCodes.STATUS_SERVER_ERROR, headers, str(e)).build_response()
    except DatabaseNoContentException as e:
        return Response(StatusCodes.STATUS_NO_CONTENT, headers, []).build_response()
    except Exception as e:
        return Response(StatusCodes.STATUS_SERVER_ERROR, headers, str(e)).build_response()

def remove_user_id(response : list):
    for d in response:
        if 'user_id' in d:
            del d['user_id']
    return response
