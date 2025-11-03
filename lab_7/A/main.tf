terraform {
  backend "s3" {
    bucket         = "javed-lab7-bucket"
    key            = "terraform/state.tfstate"
    region         = "us-east-1"
    encrypt        = true
    dynamodb_table = "Javed-terraform-lock"
  }
}
