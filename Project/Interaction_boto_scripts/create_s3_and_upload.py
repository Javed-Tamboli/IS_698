import boto3
s3 = boto3.client('s3')


bucket = "javed-project-123"

# Test file 
filename = "boto3-proof-by-javed.txt"
with open(filename, "w", encoding="utf-8") as f:
    f.write("This file was uploaded using Boto3 script by Javed\n")
    f.write("Assignment Part 2.C - AWS Interaction via Python Boto3\n")
    f.write("Success!")

# Upload 
s3.upload_file(filename, bucket, "boto3-upload-proof-javed.txt")
print("Boto3 file upload SUCCESSFUL!")
print(f"Bucket → {bucket}")
print(f"File  → boto3-upload-proof-javed.txt")