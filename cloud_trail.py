import boto3

client = boto3.client('cloudtrail')

# create cloud trail 
response = client.create_trail(
    Name='python_trail5',
    S3BucketName='pythons20',
   
    SnsTopicName='mysns1',

    IncludeGlobalServiceEvents=True,
    IsMultiRegionTrail=True,

    EnableLogFileValidation=True    
)

# start cloud trail
response = client.start_logging(
    Name='python_trail5'
)
