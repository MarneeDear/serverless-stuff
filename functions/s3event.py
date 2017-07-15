from __future__ import print_function
import json
import boto3
import datetime

print('Loading function')

s3_client = boto3.client('s3')
s3_resouce = boto3.resource('s3')

def lambda_handler(event, context):
    print("Received event: %s" % json.dumps(event, indent=2))
    print("Context: %s" % context)

    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    print (bucket)
    key = event['Records'][0]['s3']['object']['key']
    try:
        response = s3_client.get_object(Bucket=bucket, Key=key)
        print("CONTENT TYPE: " + response['ContentType'])
        # write to the target bucket
        # tuple-target
        target_message = "The MIME-type is : " + response["ContentType"] + ". At " + datetime.datetime.now
        s3_resouce.Object("tuple-target", "s3event-results.txt").put(target_message)
        return "I wrote to the file in tuple-target. " + target_message
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure it exists and your bucket is in the same region as this function.'.format(key, bucket))
        raise e
