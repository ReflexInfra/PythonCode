import boto3

client = boto3.client('rds')

response = client.create_db_parameter_group(
    DBParameterGroupFamily='mysql5.6',
    DBParameterGroupName='mymysqlparametergroup1',
    Description='My MySQL parameter group1'
)

