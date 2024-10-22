import json
import boto3
from botocore.exceptions import ClientError
from common_layer import Car

client = boto3.client('dynamodb')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('questions')
tableName = 'questions'


def lambda_handler(event, context):
    print(event)
    print(Car().myCar())
    body: dict = json.loads(event.get('body'))
    
    headers = {
        'Access-Control-Allow-Origin': '*',  
        'Access-Control-Allow-Methods': 'OPTIONS,POST',  
        'Access-Control-Allow-Headers': 'Content-Type,Authorization,X-Amz-Date,X-Api-Key,X-Amz-Security-Token',  
        'Content-Type': 'application/json'
    }
    try:
        response: dict = table.put_item(
            Item=body,
            ConditionExpression='attribute_not_exists(question_id)'
        )
        response_code: int = response.get('ResponseMetadata').get('HTTPStatusCode')
        if response_code == 200:    
            return {
                'statusCode': 200,
                'headers':headers,
                'body': 'Succesfully added to database'
            }
        else:
            return {
                'statusCode': response_code,
                'headers':headers,
                'body': 'Problem adding to database'
            }
    except ClientError as e:
            return {
                'statusCode': 400,
                'headers':headers,
                'body': 'The question_id specified already exists'
            } 
    

    
    

        
        
