#!usr/bin/env python

import boto3
client = boto3.client('ses')

response = client.send_email(
    Source='bhagwansuman2@gmail.com',
    Destination={
        'BccAddresses': [
        ],
        'CcAddresses': [
            'sent2sreenu1@gmail.com',
        ],
        'ToAddresses': [
            'uday95.v@gmail.com',
            'bgsuman@example.com',
        ],
    },
    Message={
        'Body': {
            'Html': {
                'Charset': 'UTF-8',
                'Data': 'This message body contains HTML formatting. It can, for example, contain links like this one: <a class="ulink" href="http://docs.aws.amazon.com/ses/latest/DeveloperGuide" target="_blank">Amazon SES Developer Guide</a>.',
            },
            'Text': {
                'Charset': 'UTF-8',
                'Data': 'This is the message body in text format.',
            },
        },
        'Subject': {
            'Charset': 'UTF-8',
            'Data': 'Test email',
        },
    },
)
print(response)
