import boto3

dynamodb_resource = boto3.resource('dynamodb')
print(dynamodb_resource)