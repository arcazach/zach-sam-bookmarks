import boto3
import os
import json

def handler(message, context):
  print(message)

  bookmarkId = message['pathParameters']['id']

  print('Deleting bookmark %s from table %s' % (bookmarkId, os.environ['TABLE_NAME']))
  client = boto3.client('dynamodb')
  response = client.delete_item(TableName = os.environ['TABLE_NAME'], Key = {'id': {'S': bookmarkId}})
  print('Done')

  return {
    'statusCode': 204,
    'headers': {},
    'body': ''
  }