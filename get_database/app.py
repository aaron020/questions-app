import json
import boto3
from decimal import Decimal

from common_layer.api_requests_helper import get_response_headers_cors, Response, StatusCodes
from common_layer.exceptions import InvalidLambdaInputException, DatabaseNoContentException, DatabaseFailedToQueryExeception
from database_service import DatabaseService
from validate_input import ValidateInput

client = boto3.client('dynamodb')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('topic_questions')
tableName = 'questions'


def lambda_handler(event, context):
    headers = get_response_headers_cors(allow_methods=['GET'])
    try:
        topic: str = ValidateInput(event).extract_input()
        questions: list = DatabaseService(topic, table).get_from_database()
        return Response(StatusCodes.STATUS_OK, headers, questions).build_response()
    except InvalidLambdaInputException as e:
        return Response(StatusCodes.STATUS_CLIENT_ERROR, headers, str(e)).build_response()
    except DatabaseFailedToQueryExeception as e:
        return Response(StatusCodes.STATUS_SERVER_ERROR, headers, str(e)).build_response()
    except DatabaseNoContentException as e:
        return Response(StatusCodes.STATUS_NO_CONTENT, headers, str(e)).build_response()
    except Exception as e:
        return Response(StatusCodes.STATUS_SERVER_ERROR, headers, str(e)).build_response()


