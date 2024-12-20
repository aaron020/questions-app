import boto3

from common_layer.database_helper import connect_questions_table
from database_service import DatabaseService
from validate_input import ValidateInput
from common_layer.api_requests_helper import get_response_headers_cors, StatusCodes, Response
from common_layer.exceptions import InvalidLambdaInputException, DatabaseFailedToPutExeception

table = database_table = connect_questions_table()

def lambda_handler(event, context):
    headers = get_response_headers_cors(allow_methods=['POST'])
    try:
        input_question: dict = ValidateInput(event).extract_and_validate_input()
        DatabaseService(input_question, table).add_to_database()

        return Response(StatusCodes.STATUS_OK, headers, 'Question added to database').build_response()
    except InvalidLambdaInputException as e:
        return Response(StatusCodes.STATUS_CLIENT_ERROR, headers, str(e)).build_response()

    except DatabaseFailedToPutExeception as e:
        return Response(StatusCodes.STATUS_SERVER_ERROR, headers, str(e)).build_response()

    except Exception as e:
        return Response(StatusCodes.STATUS_SERVER_ERROR, headers, str(e)).build_response()

    

    
    

        
        
