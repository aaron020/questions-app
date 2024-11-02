

### Sample Exact Input:
```json
{
  "body": "{\"question\": \"What is the default and max retention period for messages in a queue?\",\"answers\": [{\"4 days default, 10 days max\": false}, {\"4 days default, 10 days max\": true}],\"topic\": \"aws\",\"explanation\":\"Im not really sure\",\"difficulty\":2}"
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
