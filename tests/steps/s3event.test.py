import sys
import os
sys.path.insert(0, r"C:\Users\Marnee\Dropbox\github\serverless-stuff")
from functions.s3event import lambda_handler
from hamcrest import assert_that, equal_to
from behave import given, when, then
import json

@given(u'we have a bucket named "{bucket}"')
def step_impl(context, bucket):
   context.source_bucket = bucket

@when(u'anyone uploads an image file "{image}" to "{source}"')
def step_impl(context, image, source):
    # pretend the event occurred
    # S3 will send the function an event object
    cwd = os.getcwd()
    path = os.path.join(cwd, "tests\data\happyfaceevent.json")
    with open(path, "r") as eventdata:
       context.event = json.load(eventdata)
    lambda_handler(context.event, "")  

@then(u'the file "<output>" is written to "{target}"')
def step_impl(context, output, target):
    raise NotImplementedError("")

@then(u'the contents are "<mimetype>"')
def step_impl(context, mimetype):
    raise NotImplementedError(u'STEP: Then the contents are "{mimetype}"')