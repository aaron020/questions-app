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


dynamodb = boto3.resource('dynamodb')
table_topic = dynamodb.Table('questions')
def try_this_delete():
    response = table_topic.delete_item(
        Key={'question_id': '214fc4b2-d49b-425a-8055-5ec967fba9d4', 'topic_id': '123'},
        ConditionExpression='attribute_exists(question_id)'
    )
    return response

res = try_this_delete()
print(res)