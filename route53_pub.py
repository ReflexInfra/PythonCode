import boto3

client = boto3.client('route53')

response = client.create_hosted_zone(
    Name='krishnapvk.cf',
#    VPC={
#      'VPCRegion': 'us-east-1',
#      'VPCId': 'vpc-2b965a50'
#    },

# The value that you specified for CallerReference (unique string) when you created the hosted zone
    CallerReference='krishna1513',
    HostedZoneConfig={
        'Comment': 'hi this is python route123 ',
        'PrivateZone': False
    },
  
)

