#!usr/bin/env python
import boto3

#Creating s3 bucket
s3 = boto3.client('s3')
s3.create_bucket(Bucket='my-db-bucket')

#Uploading the file inside the bucket
s3.upload_file('/home/ubuntu/hello.txt', 'my-db-bucket', 'hello.txt')
s3.upload_file('/home/ubuntu/lambda.py', 'my-db-bucket', 's3.py')

#add the bucket policy
s3_conn = boto3.resource('s3')
bucket_policy = s3_conn.BucketPolicy('my-db-bucket')

# Call to S3 to retrieve the policy for the given bucket
# ACL's to grant basic read/write permissions to other AWS accounts
result = s3.get_bucket_acl(Bucket='my-db-bucket')

print(result)
