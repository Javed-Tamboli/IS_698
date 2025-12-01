# AWS Cloud Project – Javed  
**IS_698 – Cloud Computing | Full Infrastructure + Automation Project**

## Overview  
This project demonstrates a complete production-grade AWS architecture using **Infrastructure as Code (IaC)** and **Python automation.

### Architecture Summary
- **VPC** with public & private subnets across 2 AZs (Terraform)
- **Application Load Balancer** + **Auto Scaling Group** (2–4 EC2 instances)
- **Nginx web server** serving custom HTML page with instance ID
- **Multi-AZ **MySQL RDS** in private subnets
- **S3 bucket** with **Lambda function** that logs every upload to CloudWatch
- Full interaction using **AWS CLI + Python Boto3**
