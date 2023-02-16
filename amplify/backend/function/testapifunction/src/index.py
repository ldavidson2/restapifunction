import json
import boto3

dynamodb = boto3.resource('dynamodb', region_name="us-east-2",
         aws_access_key_id="AKIAX3FHVXYSKFFYPGE7",
         aws_secret_access_key= "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")
table = dynamodb.Table('resttest-staging')

def handler(event, context):
    response = table.query(
    KeyConditionExpression=Key('PK').eq('COMP#0')
    )

    data = str(response['Items'])
    print('received event:')
    print(event)
  
    return data