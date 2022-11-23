import json
import boto3
import base64

"""
This function is called when the Lambda function is invoked.
and it will upload the file to S3 bucket
according to the api gateway event with following format:
{
    "file": "base64 encoded file",
    "filename": "filename.extension"
}
"""


def lambda_handler(event, context):
    bucket_name = 'softitlan-storage'
    region = 'us-east-2'
    try:
        # get the file from the event
        file = event['file']
        filename = event['filename']
        # decode the file
        file = base64.b64decode(file)
        # upload the file to s3 bucket
        s3 = boto3.client('s3')
        s3.put_object(Body=file, Bucket=bucket_name, Key="images/" + filename)

        url = f'https://{bucket_name}.s3.{region}.amazonaws.com/images/{filename}'

        return {
            'successes': True,
            'statusCode': 200,
            'message': 'File uploaded successfully',
            'data': {
                'url': url
            }
        }
    except Exception as e:
        return {
            'successes': False,
            'statusCode': 500,
            'message': 'Error to upload file!',
            'data': {
                'error': str(e)
            }
        }
