import boto3
import os
import json

def handler(message, context):
  print(message)

  if 'body' not in message:
    return {}

  bookmark = json.loads(message['body'])
  bookmarkId = message['pathParameters']['id']

  params = {
    'id': {'S': bookmarkId},
    'url': {'S': bookmark['url']},
    'name': {'S': bookmark['name']},
    'description': {'S': bookmark['description']}
  }

  print('Updating bookmark %s from table %s' % (bookmarkId, os.environ['TABLE_NAME']))
  client = boto3.client('dynamodb')
  response = client.put_item(TableName = os.environ['TABLE_NAME'], Item=params)
  print('Done')

  return {
    'statusCode': 204,
    'headers': {},
    'body': ''
  }