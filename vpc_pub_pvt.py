import boto3

ec2 = boto3.resource('ec2')

# create VPC
vpc = ec2.create_vpc(CidrBlock='10.0.0.0/16')

# we can assign a name to vpc, or any resource, by using tag
vpc.create_tags(
     Tags=[
           {
           "Key": "Name", 
           "Value": "vpc_pub_pvt"
          }
       ]
  )
vpc.wait_until_available()
print(vpc.id)

# create then attach internet gateway
ig = ec2.create_internet_gateway()
vpc.attach_internet_gateway(InternetGatewayId=ig.id)

print(ig.id)

# create a route table and a public route
route_table = vpc.create_route_table()
route = route_table.create_route(
 DestinationCidrBlock='0.0.0.0/0',
 GatewayId=ig.id
)

print(route_table.id)

# create public subnet
subnet1 = ec2.create_subnet(
    CidrBlock='10.0.1.0/24',
    AvailabilityZone="{}".format('us-east-1a'),
    VpcId=vpc.id
 )

print(subnet1.id)

route_table.associate_with_subnet(SubnetId=subnet1.id)

# create private subnet 
subnet2 = ec2.create_subnet(
     CidrBlock='10.0.2.0/24',
     AvailabilityZone="{}".format('us-east-1b'), 
     VpcId=vpc.id
  )
print(subnet2.id)

