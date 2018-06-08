import boto3

client = boto3.client('rds')

#Creating cluster
response = client.create_db_cluster(
    AvailabilityZones=[
        'us-east-1c',
    ],
    BackupRetentionPeriod=1,
    DBClusterIdentifier='mydbcluster',
    DBClusterParameterGroupName='clusterparametergroup',
    VpcSecurityGroupIds=[
        'sg-c13d1eb6',
    ],
    DBSubnetGroupName='default',

    DatabaseName='myauroradb',
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
    DBInstanceIdentifier='dd-infra-aurora-rds',
     
    DBInstanceClass='db.t2.small',
    Engine='aurora',
    AvailabilityZone='us-east-1b',
    DBSubnetGroupName='default',

   OptionGroupName='default:aurora-5-6',
    PubliclyAccessible=True,
    Tags=[
        {
            'Key': 'Name',
            'Value': 'auroraDB_default_vpc'
        }
    ],
    DBClusterIdentifier='mydbcluster'
   )

