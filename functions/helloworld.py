from __future__ import print_function
import boto3

s3_client = boto3.client("s3")

def lambda_handler(event, context):
    print ("The sleeper has awakened.")
    return "The sleeper has awakened. Will he take the golden path?"