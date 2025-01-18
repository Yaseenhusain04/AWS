import json
import boto3
import os
from botocore.exceptions import ClientError

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    # Get the bucket name from environment variables
    bucket_name = os.environ['S3_BUCKET_NAME']
    
    # Extract the file content and filename from the event
    file_content = event.get('file_content')
    file_name = event.get('file_name')
    
    # Check if the file content and name are provided
    if not file_content or not file_name:
        return {
            'statusCode': 400,
            'body': json.dumps('Error: Please provide both file_content and file_name.')
        }
    
    try:
        # Upload the file to S3
        s3_client.put_object(Bucket=bucket_name, Key=file_name, Body=file_content)
        
        return {
            'statusCode': 200,
            'body': json.dumps(f'Successfully uploaded {file_name} to {bucket_name}.')
        }
    except ClientError as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error uploading file: {str(e)}')
        }