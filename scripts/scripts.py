import boto3
from boto3.dynamodb.conditions import Key

# Initialize the DynamoDB resource


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
#ry_this()

dynamodb = boto3.resource('dynamodb')
table_topic = dynamodb.Table('topics')

def try_this_one():
    response = table_topic.query(
        KeyConditionExpression='topic_id = :pk',
        ExpressionAttributeValues={
            ':pk': '9e6ba43f-cd6c-4461-891b-cedfefe3b668'
        }
    )
    print(response)
    print(type(response))
    print(response['Items'])
    print(response['Items'][0])



try_this_one()