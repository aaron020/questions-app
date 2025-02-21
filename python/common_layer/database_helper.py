import boto3


def connect_questions_table():
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('questions')
    return table

def connect_topics_table():
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('topics')
    return table

def connect_topic_test_table():
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('topic_test')
    return table

def connect_any_table():
    dynamodb = boto3.resource('dynamodb')
    return dynamodb