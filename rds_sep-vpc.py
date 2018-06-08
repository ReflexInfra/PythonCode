import boto3

client = boto3.client('rds')

#create db subnet group using  particular vpc subnet ids
response = client.create_db_subnet_group(
    DBSubnetGroupDescription='My DB subne2',
    DBSubnetGroupName='mydbsub',
    SubnetIds=[
        'subnet-721dd615',
        'subnet-77589459',
    ],
)

#create db parameter group
response = client.create_db_parameter_group(
    DBParameterGroupFamily='mysql5.6',
    DBParameterGroupName='mymysqlparametergroup1',
    Description='My MySQL parameter group1'
)

#create option group
response = client.create_option_group(
    EngineName='MySQL',
    MajorEngineVersion='5.6',
    OptionGroupDescription='My MySQL 5.6 option group1',
    OptionGroupName='mymysqloptiongroup1',
)

#create MySQL DB
response = client.create_db_instance(
    DBName='mysql1',
    DBInstanceIdentifier='dd-infra-rds-pvt-vpc',
    AllocatedStorage=22,
    DBInstanceClass='db.t2.micro',
    Engine='MYSQL',
    MasterUsername='Venkat',
    MasterUserPassword='mypassword123',


    VpcSecurityGroupIds=[
        'sg-09c79241',
    ],
    AvailabilityZone='us-east-1c',
    DBSubnetGroupName='mydbsub',
    DBParameterGroupName='mymysqlparametergroup1',
    BackupRetentionPeriod=3,

    Port=3306,
# If multiAZ enable availabilityzone not working
#    MultiAZ=True,
    EngineVersion='5.6.39',
    AutoMinorVersionUpgrade=True,
    LicenseModel='general-public-license',
    OptionGroupName='mymysqloptiongroup1',

# if publiclyaccessible enable pvt vpc not working
#    PubliclyAccessible=True
    Tags=[
        {
            'Key': 'Name',
            'Value': 'reflex'
        }
    ]
)

