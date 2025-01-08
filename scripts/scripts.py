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
    scan_params = {'Limit': 2}
    scan_params['ExclusiveStartKey'] = {'topic_id': '6d3dbbc0-749e-49b3-b1d9-6d0152c205e5', 'user_id': '52a57464-4081-70d9-8438-6215796a3c47'}
    response = table_topic.scan(**scan_params)
    print(response)



try_this_one()