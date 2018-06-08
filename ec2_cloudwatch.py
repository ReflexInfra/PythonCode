#!/usr/bin/env python 

import boto3
# create instance with cloud watch
ec2 = boto3.resource('ec2')
instance = ec2.create_instances(
 ImageId='ami-a4dc46db',
 MinCount=1,
MaxCount=1,
KeyName='007',
SecurityGroupIds=["sg-6bde051c"],
#SubnetIds=["subnet-f09fcadf"],
InstanceType='t2.micro')
print instance[0].id


client = boto3.client('cloudwatch')

response = client.put_metric_alarm(
    AlarmName='ec2-cpu',
    AlarmDescription='cpu is stop whne 30% less',
    ActionsEnabled=True,
    Dimensions=[
        {
          'Name': 'InstanceId',
          'Value': instance[0].id
        },
    ],
#    InstanceId=instance[0].id,
    AlarmActions=[
		'arn:aws:sns:us-east-1:649030859017:cpu-utz'
#		'arn:aws:swf:us-east-1:{649030859017}:action/actions/AWS_EC2.InstanceId.Stop/1.0' 

 #  			'arn:aws:automate:us-east-1:ec2:stop'
 ],
    MetricName='CPUUtilization',
    Namespace='AWS/EC2',
    Statistic='Average',
    Period= 60,
   # Unit='Percent',
    Threshold=30,
    EvaluationPeriods=1,
    DatapointsToAlarm=1,
   # Threshold=30,
    ComparisonOperator='LessThanThreshold',
   # TreatMissingData='breaching'
    
)
