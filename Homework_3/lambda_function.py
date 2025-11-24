# lambda_function.py
import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        size = record['s3']['object'].get('size', 'Unknown')
        
        logger.info(f"NEW FILE DETECTED → Bucket: {bucket} | File: {key} | Size: {size} bytes")
    
    return {
        'statusCode': 200,
        'body': json.dumps('Lambda triggered successfully!')
    }