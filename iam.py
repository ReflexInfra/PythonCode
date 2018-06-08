import boto3

client = boto3.client('iam')

#create user
response = client.create_user(
    UserName='Venkat',
)

print(response)

#create group
response = client.create_group(
    GroupName='dd_infra',
)

# give permissions to group
response = client.attach_group_policy(
    GroupName='dd_infra',
    PolicyArn='arn:aws:iam::aws:policy/AdministratorAccess'
)
response = client.attach_group_policy(
    GroupName='dd_infra',
    PolicyArn='arn:aws:iam::aws:policy/AlexaForBusinessFullAccess'

#    PolicyArn='arn:aws:iam::aws:policy/AlexaForBusinessDeviceSetup',
)
#add user to group
response = client.add_user_to_group(
    GroupName='dd_infra',
    UserName='Venkat'
)
print(response)
