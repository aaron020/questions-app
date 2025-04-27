from common_layer.api_requests_helper import get_response_headers_cors
from common_layer.database_helper import connect_questions_table
from common_layer.database_helpers import TopicOwner
from common_layer.input_helper import InputValidator
from topics.update_topic.validate_input import ValidateInput

table = connect_questions_table()

def lambda_handler(event, context):
    headers = get_response_headers_cors(allow_methods=['PATCH'])
    try:
        input_topic: dict = ValidateInput.extract_and_validate(event)
        topic_owner_id = input_topic.get('user_id')
        user_id = InputValidator.extract_user_id_from_input(event)
        if user_id == topic_owner_id:
            DatabaseService(input_question, table).update_database()
        else:
            return Response(StatusCodes.STATUS_UNAUTHORIZED, headers, False).build_response()
        return Response(StatusCodes.STATUS_OK, headers, 'Question updated').build_response()
    except InvalidLambdaInputException as e:
        return Response(StatusCodes.STATUS_CLIENT_ERROR, headers, str(e)).build_response()

    except DatabaseFailedToPutExeception as e:
        return Response(StatusCodes.STATUS_SERVER_ERROR, headers, str(e)).build_response()

    except Exception as e:
        return Response(StatusCodes.STATUS_SERVER_ERROR, headers, str(e)).build_response()