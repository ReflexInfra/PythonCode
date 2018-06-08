#!usr/bin/env python
import boto3

#Creating a topic for SNS
client = boto3.client('sns')
response = client.create_topic(
    Name='Maven_Project'
)

#Creating SNS using Email protocol
subscription_client = boto3.client('sns')
subscription_client.subscribe(
                TopicArn="arn:aws:sns:us-east-1:717341664422:Maven_Project",
                Protocol="email",
                Endpoint="bgsuman@gmail.com"
            )

#Creating SNS using HTTP protocol
subscription_client = boto3.client('sns')
subscription_client.subscribe(
                TopicArn="arn:aws:sns:us-east-1:717341664422:Maven_Project",
                Protocol="HTTP",
                Endpoint="http://www.theuselessweb.com/"
            )

#Creating SNS using HTTPS protocol
subscription_client = boto3.client('sns')
subscription_client.subscribe(
                TopicArn="arn:aws:sns:us-east-1:717341664422:Maven_Project",
                Protocol="HTTPS",
                Endpoint="https://softonic.com/"
            )

#Creating SNS using SMS protocol
subscription_client = boto3.client('sns')
subscription_client.subscribe(
                TopicArn="arn:aws:sns:us-east-1:717341664422:Maven_Project",
                Protocol="SMS",
                Endpoint="8884665517"
            )
print(response)

