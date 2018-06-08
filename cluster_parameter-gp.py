import boto3

client = boto3.client('rds')

# create db cluster parameter group

response = client.create_db_cluster_parameter_group(
    DBClusterParameterGroupName='clusterparametergroup',
    DBParameterGroupFamily='aurora5.6',
    Description='My DB cluster parameter group',
)


