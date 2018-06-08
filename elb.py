#!usr/bin/env python
import boto3

#Creating the Load balancer:
client = boto3.client('elb')
response = client.create_load_balancer(
                        LoadBalancerName='my-elb',
                        Listeners=[
                        {
                        'Protocol': 'HTTP',
                        'LoadBalancerPort': 80,
                        'InstanceProtocol': 'HTTP',
                        'InstancePort': 80,
                        },
                ],
        Subnets=[
                'subnet-1477ff1b',
                ],
        SecurityGroups=[
                'sg-b69c23fe',
                ],
        Tags=[
                {
                'Key': 'test',
                'Value': 'aws_learning'
                },
         ]
)

print(response)
