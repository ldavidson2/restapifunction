import json

def handler(event, context):
  print('received event:')
  print(event)
  
  return str(event)