from __future__ import print_function
import json
# from urllib.parse import unquote_plus
import boto3

print('Loading function')

s3_client = boto3.client('s3')
s3_resouce = boto3.resource('s3')

def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    print("Context: ")
    print(context)

    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    print (bucket)
    # key = unquote_plus(event['Records'][0]['s3']['object']['key']
        # .encode('utf8'))
    key = event['Records'][0]['s3']['object']['key']
    try:
        response = s3_client.get_object(Bucket=bucket, Key=key)
        print("CONTENT TYPE: " + response['ContentType'])
        # write to the target bucket
        # tuple-target
        s3_resouce.Object("tuple-target", "s3event-results.txt").put(Body=response["ContentType"])
        return response['ContentType']
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure it exists and your bucket is in the same region as this function.'.format(key, bucket))
        raise e
