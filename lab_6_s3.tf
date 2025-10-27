#provider "aws" {
 # region = "us-east-1"
#}

#resource "aws_s3_bucket" "my_bucket" {
 # bucket = "javed-lab6-s3"  # bucket name, must be globally unique
#}

#resource "aws_s3_bucket_versioning" "versioning_example" {
 # bucket = aws_s3_bucket.my_bucket.id  # correct reference
  #versioning_configuration {
   # status = "Enabled"
  #}
#}
