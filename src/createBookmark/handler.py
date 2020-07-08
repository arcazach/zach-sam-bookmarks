import boto3
import os
import json

def handler(message, context):
  print(message)

  if 'body' not in message:
    return {}

  bookmark = json.loads(message['body'])
  params = {
    'id': {'S': bookmark['id']},
    'url': {'S': bookmark['url']},
    'name': {'S': bookmark['name']},
    'description': {'S': bookmark['description']}
  }

  print('Adding bookmark to table %s' % os.environ['TABLE_NAME'])
  client = boto3.client('dynamodb')
  response = client.put_item(TableName = os.environ['TABLE_NAME'], Item = params)
  print('bookmark added to inventory, done')

  return {
    'statusCode': 204,
    'headers': {},
    'body': ''
  }