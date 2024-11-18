import boto3


def connect_database():
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('topic_questions')
    return table