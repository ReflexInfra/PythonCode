import boto3

client = boto3.client('ec2')

response = client.create_volume(
    AvailabilityZone='us-east-1a',
    Size=10,
    Encrypted=True,

#The snapshot from which to create the volume

    #SnapshotId='snap-0839247b24bc26a38', 

# "gp2" for General Purpose SSD, "io1" for Provisioned IOPS SSD,
# "st1" for Throughput Optimized HDD, "sc1" for Cold HDD, 
# "standard" for Magnetic volumes.
  
  VolumeType='gp2',

)

print (response)

# Attaches an EBS volume to a running or stopped instance
'''
response = client.attach_volume(

# Device names like /dev/sdf, /dev/sdp, /dev/sdh, xvdh 
    Device='xvdh',
    InstanceId='i-0b06eecb99afad61c',
    VolumeId='vol-041a5a06f825d16d7'
    
)
print (response)
'''
#Creates a snapshot of an EBS volume
'''
response = client.create_snapshot(
    Description='This is my root volume snapshot.',
    VolumeId='vol-041a5a06f825d16d7',
)
'''
