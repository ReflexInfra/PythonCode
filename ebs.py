import boto3

client = boto3.client('elasticbeanstalk')
response = client.create_application(
 ApplicationName='my-ebs',
 Description='my new application',
)

print(response)

'''
response = client.create_application_version(
 ApplicationName='my-ebs',
 AutoCreateApplication=True,
 Description='my new app1',
 Process=True,
 SourceBundle={
 'S3Bucket': 'ebs20',
 'S3Key': 'phpjson.json',
 },
 VersionLabel='v1',
)
print(response)

'''

response = client.create_environment(
 ApplicationName='my-ebs',
 CNAMEPrefix='my-ebs',
 EnvironmentName='my-test-env',

 # type the 'aws elasticbeanstalk list-available-solution-stacks' cmd 
 # display the all Solutionstacknames
 SolutionStackName='64bit Amazon Linux 2018.03 v2.5.0 running Packer 1.0.3'
 #VersionLabel='v1',
 #TemplateName='my-app-v1'
)

print(response)
