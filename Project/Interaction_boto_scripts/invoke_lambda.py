import boto3
import json

client = boto3.client('lambda')

response = client.invoke(
    FunctionName='student-s3-upload-logger',
    InvocationType='RequestResponse',  
    Payload=json.dumps({"test": "manual invoke via Boto3"})
)

result = response['Payload'].read().decode()
print("Lambda invoked successfully via Boto3!")
print("Response:", result)