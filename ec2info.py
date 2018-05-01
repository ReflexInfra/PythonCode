import boto3

def instance_info():
    instance_information = {}
    ip_dict = {}
    client = boto3.client('ec2')
    addresses_dict = client.describe_addresses().get('Addresses')

    for address in addresses_dict:
        if address.get('InstanceId'):
            instance_information[address['InstanceId']] = [address.get('PublicIp')]

    dex_dict = client.describe_tags().get('Tags')
    for dex in dex_dict:
        if instance_information.get(dex['ResourceId']):
            instance_information[dex['ResourceId']].append(dex.get('Value'))

    for instance in instance_information:

        if len(instance_information[instance]) == 2:
            ip_dict[instance_information[instance][0]] = instance_information[instance][1]
        else:
            ip_dict[instance_information[instance][0]] = ''
    return instance_information, ip_dict
