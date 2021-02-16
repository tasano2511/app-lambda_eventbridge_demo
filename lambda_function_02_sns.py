import logging
import boto3
import json

# Initialize logger and set log level
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Initialize SNS client for Ireland region
session = boto3.Session(
    region_name="us-east-1"
)
sns_client = session.client('sns')


def lambda_handler(event, context):

    # Send message
    print(event)
    #console.log('EVENT: Lambda scheduler with CloudWatch Events');
    #console.log('EVENT DETAILS:', JSON.stringify(event));
    
    response = sns_client.publish(
        #PhoneNumber=event["phone_number"],
        PhoneNumber='18043811279',
        Message='Hi there! This is a test message sent with Amazon SNS via EventBridge rule cron(0,5 13 ? * SAT,SUN,MON *),
        MessageAttributes={
            'AWS.SNS.SMS.SenderID': {
                'DataType': 'String',
                'StringValue': 'SENDERID'
            },
            'AWS.SNS.SMS.SMSType': {
                'DataType': 'String',
                'StringValue': 'Promotional'
            }
        }
    )

    logger.info(r
