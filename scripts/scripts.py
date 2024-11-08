import boto3
from boto3.dynamodb.conditions import Key

# Initialize the DynamoDB resource
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('topic_questions')

def try_this():
    # Replace 'desired_topic_value' with the actual value of the topic you want to query
    response = table.query(
        IndexName='TopicIndex',  # GSI name
        KeyConditionExpression=Key('topic').eq('aws'),
        ReturnConsumedCapacity='TOTAL'
    )
    print(response)
    # Get the items and the consumed capacity
    items = response.get('Items', [])
    consumed_capacity = response.get('ConsumedCapacity')

    print("Number of items:", len(items))
    print("Consumed capacity (RCUs):", consumed_capacity)
    print(type(items))
    print(type(items[0]))

# Call the function to perform the query
try_this()
