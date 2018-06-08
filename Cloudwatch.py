import boto3

client = boto3.client('cloudwatch')
# create alarm for one instance
response = client.put_metric_alarm(
    AlarmName='ec2-cpu',
#    AlarmDescription='cpu is stop whne 30% less',
    ActionsEnabled=True,
#    InstanceId=instance[0].id,
    InsufficientDataActions=[
                'arn:aws:swf:us-east-1:{649030859017}:action/actions/AWS_EC2.[InstanceId=instance.id].Stop/1.0(instance.id)'

 #                      'arn:aws:automate:us-east-1:ec2:stop'
 ],

   AlarmDescription='cpu is stop whne 30% less',
   Dimensions=[
        {
          'Name': 'InstanceId',
          'Value': 'i-08201b9c25208b8bd'
        },
    ],
    MetricName='CPUUtilization',
    Namespace='AWS/EC2',
    Statistic='Average',

    Period= 60,
    Unit='Seconds',
    EvaluationPeriods=1,
    DatapointsToAlarm=1,
    Threshold=30,
    ComparisonOperator='LessThanThreshold',
    TreatMissingData='breaching',

)
