import boto3

client = boto3.client('rds')

# create subnet group using subnet ids
response = client.create_db_subnet_group(
    DBSubnetGroupDescription='My vpc db sunbnet group',
    DBSubnetGroupName='mydbsubnetgroup',
    SubnetIds=[
        'subnet-721dd615',
        'subnet-77589459',
    ],
)

