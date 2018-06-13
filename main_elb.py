#r/bin/env python
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
                'subnet-eb569e8c',
                ],
        SecurityGroups=[
                'sg-2e1f4266',
                ],
        Tags=[
                {
                'Key': 'test',
                'Value': 'aws_learning'
                },
         ]
)
response = client.configure_health_check(
 LoadBalancerName='my-elb',
                        HealthCheck={
                        'Target': 'HTTP:80/index.html',
                        'Interval': 20,
                        'Timeout': 3,
                        'UnhealthyThreshold': 2,
                        'HealthyThreshold': 2
                },
)


print(response)

response = client.register_instances_with_load_balancer(
    LoadBalancerName='my-elb',
    Instances=[
        {
            'InstanceId': 'i-06d25adf98626b42f'
        },
    ]
)
