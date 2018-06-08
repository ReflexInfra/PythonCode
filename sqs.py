#!usr/bin/env python
import boto3

#Creating a SQS
client = boto3.client('sqs')
response = client.create_queue(
    QueueName='flipkart',
)

# Create a new message
response = client.send_message(
    MessageBody='The order does not have a redrive policy',
    QueueUrl='https://sqs.us-east-1.amazonaws.com/717341664422/flipkart',
)

# Create SQS client
sqs = boto3.client('sqs')

# Send message to SQS queue
response = sqs.send_message(
    QueueUrl='https://sqs.us-east-1.amazonaws.com/717341664422/flipkart',
    DelaySeconds=10,
    MessageAttributes={
        'Title': {
            'DataType': 'String',
            'StringValue': 'Redmi Note5 Mobile '
        },
        'Author': {
            'DataType': 'String',
            'StringValue': 'Suman'
        },
        'WeeksOn': {
            'DataType': 'Number',
            'StringValue': '6'
        }
    },
    MessageBody=(
        'Information about current order: It will be delivered by Mon.'
    )
)

print(response['MessageId'])
