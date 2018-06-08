import boto3

client = boto3.client('rds')

#using all default values like vpc,subnet-group,parameter-group,option-group
#create MYSQL version 5.6.39 
response = client.create_db_instance(
    DBName='mysqldb',
    DBInstanceIdentifier='ddinfrards1',
    AllocatedStorage=25,
    DBInstanceClass='db.t2.micro',
    Engine='mysql',
    MasterUsername='venkat',
    MasterUserPassword='mypassword123',

    VpcSecurityGroupIds=[
        'sg-cafe9482',
    ],
    AvailabilityZone='us-east-1b',
    DBSubnetGroupName='default',

    DBParameterGroupName='default.mysql5.6',
    BackupRetentionPeriod=5,
    PreferredBackupWindow='04:20-04:50',
    Port=3306,

# If multiAZ enable availabilityzone not working
#    MultiAZ=True,
    EngineVersion='5.6.39',
    AutoMinorVersionUpgrade=True,
    LicenseModel='general-public-license',
    OptionGroupName='default:mysql-5-6',
    PubliclyAccessible=True,
    Tags=[
        {
            'Key': 'Name',
            'Value': 'reflex'
        }
    ]
)
