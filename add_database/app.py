import boto3

from database_service import DatabaseService
from validate_input import ValidateInput
from common_layer.api_requests_helper import get_response_headers_cors, StatusCodes, Response
from common_layer.exceptions import InvalidLambdaInputException, DatabaseFailedToAddExeception

client = boto3.client('dynamodb')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('topic_questions')
tableName = 'topic_questions'


def lambda_handler(event, context):
    headers = get_response_headers_cors(allow_methods=['OPTIONS','POST'])
    try:
        input_question: dict = ValidateInput(event).extract_and_validate_input()
        DatabaseService(input_question, table).add_to_database()

        return Response(StatusCodes.STATUS_OK, headers, 'Question added to database').build_response()
    except InvalidLambdaInputException as e:
        return Response(StatusCodes.STATUS_CLIENT_ERROR, headers, str(e)).build_response()

    except DatabaseFailedToAddExeception as e:
        return Response(StatusCodes.STATUS_SERVER_ERROR, headers, str(e)).build_response()

    except Exception as e:
        return Response(StatusCodes.STATUS_SERVER_ERROR, headers, str(e)).build_response()

    

    
    

        
        
