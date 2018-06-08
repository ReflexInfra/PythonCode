import boto3

client = boto3.client('rds')

# create db option group
response = client.create_option_group(
    EngineName='aurora',
    MajorEngineVersion='5.6',
    OptionGroupDescription='aurora 5.6 option group',
    OptionGroupName='auroraoptiongroup',
)

