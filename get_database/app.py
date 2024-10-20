import json
import boto3
from decimal import Decimal

client = boto3.client('dynamodb')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('questions')
tableName = 'questions'

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return super(DecimalEncoder, self).default(obj)
        

def lambda_handler(event, context):
    print(f'lambda recieved: {event}')
        # Define the CORS headers
    headers = {
        'Access-Control-Allow-Origin': '*',  
        'Access-Control-Allow-Methods': 'OPTIONS,GET',  
        'Access-Control-Allow-Headers': 'Content-Type,Authorization,X-Amz-Date,X-Api-Key,X-Amz-Security-Token',  
        'Content-Type': 'application/json'
    }
    
    body: dict = event.get('queryStringParameters')
    question_id = body.get('question_id') 
        
    found_item = table.get_item(Key={'question_id': question_id})['Item']
    
    return {
        'statusCode': 200,
        'headers': headers,
        'body': json.dumps(found_item, cls=DecimalEncoder)
    }