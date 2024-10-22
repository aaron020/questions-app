import json
import boto3
from botocore.exceptions import ClientError
from common_layer import Car
from common_layer.api_requests_helper import get_response_headers_cors, StatusCodes, Response

client = boto3.client('dynamodb')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('questions')
tableName = 'questions'


def lambda_handler(event, context):
    print(event)
    print(Car().myCar())
    body: dict = json.loads(event.get('body'))
    
    headers = get_response_headers_cors(allow_methods=['OPTIONS','POST'])
    try:
        response: dict = table.put_item(
            Item=body,
            ConditionExpression='attribute_not_exists(question_id)'
        )
        response_code: int = response.get('ResponseMetadata').get('HTTPStatusCode')
        if response_code == 200:    
            return Response(StatusCodes.STATUS_OK, headers, 'Successfully added to database').build_response()
        else:
            return Response(StatusCodes.STATUS_CLIENT_ERROR, headers, 'Issue adding to database').build_response()
    except ClientError as e:
            return Response(StatusCodes.STATUS_SERVER_ERROR, headers, f'Question Id taken: {e}').build_response()
    

    
    

        
        
