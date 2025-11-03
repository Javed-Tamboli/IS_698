provider "aws" {
  region = "us-east-1"
}

# COMMENTED OUT TO AVOID DUPLICATE
# count = 5  # Creates 5 instances
# resource "aws_instance" "web" {
#   ami           = "ami-0bdd88bd06d16ba03"
#   instance_type = "t2.micro"
#   tags = {
#     Name = "Terraform-Instance-${count.index}"
#   }
# }