#!/usr/bin/env python
import boto3 
ec2 = boto3.resource('ec2') 
instance = ec2.create_instances(
 ImageId='ami-43a15f3e',
 MinCount=1, 
MaxCount=1, 
KeyName='key', 
SecurityGroupIds=["sg-0ba6bd42"],
SubnetId="subnet-f09fcadf",
InstanceType='t1.micro') 
print instance[0].id
