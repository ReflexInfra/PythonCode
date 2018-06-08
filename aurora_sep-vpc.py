import boto3

client = boto3.client('rds')

# create db cluster parameter group
 
response = client.create_db_cluster_parameter_group(
    DBClusterParameterGroupName='clusterparametergroup',
    DBParameterGroupFamily='aurora5.6',
    Description='My DB cluster parameter group',
)

# create db option group
response = client.create_option_group(
    EngineName='aurora',
    MajorEngineVersion='5.6',
    OptionGroupDescription='aurora 5.6 option group',
    OptionGroupName='auroraoptiongroup',
)


# create subnet group using subnet ids
response = client.create_db_subnet_group(
    DBSubnetGroupDescription='My vpc db sunbnet group',
    DBSubnetGroupName='mydbsubnetgroup',
    SubnetIds=[
        'subnet-721dd615',
        'subnet-77589459',
    ],
)

#create cluster
response = client.create_db_cluster(
    AvailabilityZones=[
        'us-east-1c',
    ],
    BackupRetentionPeriod=3,
    DBClusterIdentifier='mydbcluster1',
    DBClusterParameterGroupName='clusterparametergroup',
    VpcSecurityGroupIds=[
        'sg-09c79241',
    ],
    DBSubnetGroupName='mydbsubnetgroup',

    DatabaseName='myauroradb1',
    Engine='aurora',
    EngineVersion='5.6.10a',
    MasterUserPassword='password123',
    MasterUsername='venkat',
#    OptionGroupName='default:aurora-5-6',
    Port=3306,
    StorageEncrypted=True,
)

#create aurora db
response = client.create_db_instance(
    DBInstanceIdentifier='dd-aurora-separate-vpc',

    DBInstanceClass='db.t2.small',
    Engine='aurora',
    AvailabilityZone='us-east-1c',
    DBSubnetGroupName='mydbsubnetgroup',

   OptionGroupName='auroraoptiongroup',
# This is not default vpc so we don't enable PubliclyAccessible
#    PubliclyAccessible=True,
    Tags=[
        {
            'Key': 'Name',
            'Value': 'dd_infra_aurora_separate-vpc'
        }
    ],
    DBClusterIdentifier='mydbcluster1'
   )

