

### Sample Exact Input:
```json
{
  "body": "{\"questions\": \"What is the default and max retention period for messages in a queue?\",\"answers\": [{\"4 days default, 10 days max\": false}, {\"4 days default, 10 days max\": true}],\"topic_id\": \"aws\",\"explanation\":\"Im not really sure\",\"difficulty\":2}",
  "requestContext": {
    "authorizer": {
      "claims": {
        "sub": "user_id"
      }
    }
  }
}
```


### Sample API Body Input:
```json
{
    "question": "What is the default and max retention period for messages in a queue?",
    "answers": [{"4 days default, 10 days max": false}, {"4 days default, 10 days max": true}],
    "topic": "aws",
    "explanation":"Im not really sure",
    "difficulty":2
}
