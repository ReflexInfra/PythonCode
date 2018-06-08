import boto3

client = boto3.client('autoscaling')

response = client.create_launch_configuration(
#    IamInstanceProfile='my-iam-role',
    ImageId='ami-a4dc46db',
    InstanceType='t2.micro',
    LaunchConfigurationName='my-config',
    SecurityGroups=[
        'sg-d2faf99b',
    ],
)

print(response)

response = client.create_auto_scaling_group(
    AutoScalingGroupName='my-auto-scaling-group',
    LaunchConfigurationName='my-config',
    MaxSize=3,
    MinSize=2,
    VPCZoneIdentifier='subnet-1e5a2831',
)

print(response)

'''
response = client.attach_load_balancers(
    AutoScalingGroupName='my-auto-scaling-group',
    LoadBalancerNames=[
        'Elb',
    ],
)
print(response)
'''
# configure our scalling policy
response = client.put_scaling_policy(
    AdjustmentType='PercentChangeInCapacity',
    AutoScalingGroupName='my-auto-scaling-group',
    PolicyName='Scaleout',
    ScalingAdjustment=20,
)

print(response)

response = client.put_scaling_policy(
    AdjustmentType='ChangeInCapacity',
    AutoScalingGroupName='my-auto-scaling-group',
    PolicyName='ScaleIn',
    ScalingAdjustment=-1,
)

print(response)

