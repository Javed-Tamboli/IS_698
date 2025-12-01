import boto3

ec2 = boto3.client('ec2')
response = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

print("Running EC2 Instances (via Boto3):")
print("-" * 50)
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        instance_id = instance['InstanceId']
        instance_type = instance['InstanceType']
        az = instance['Placement']['AvailabilityZone']
        name = "No Name"
        for tag in instance.get('Tags', []):
            if tag['Key'] == 'Name':
                name = tag['Value']
        print(f"{instance_id} | {instance_type} | {az} | {name}")