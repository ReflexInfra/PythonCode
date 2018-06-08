#!usr/bin/env python
import boto3

client = boto3.client('ses')

#verify_domain_dkim
response = client.verify_domain_dkim(
    Domain='awslearning.com'
)

#verify_domain_identity
response = client.verify_domain_identity(
    Domain='awslearning.com'
)

#verify_email_address
response = client.verify_email_address(
    EmailAddress='bgsuman@gmail.com',
)

#verify_email_identity
response = client.verify_email_identity(
    EmailAddress='bgsuman@gmail.com',
)

print(response)
