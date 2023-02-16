import json
import boto3

dynamodb = boto3.resource('dynamodb', region_name="us-east-2",
         aws_access_key_id="AKIAX3FHVXYSKFFYPGE7",
         aws_secret_access_key= "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")
table = dynamodb.Table('RestApiDB-staging')

def handler(event, context):
    response = table.get_item(
        Key={
            'PK': 'COMP#0',
            'SK': 'COMP#0'
        }
    )

    data = str(response['Item']['companyName'])
  print('received event:')
  print(event)
  
  return data