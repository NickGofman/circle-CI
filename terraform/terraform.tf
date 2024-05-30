terraform {
  required_version = ">= 1.6"
  backend "s3" {
    bucket  = "terraform-backend-nick"
    key     = "terraform.tfstate"
    region  = "us-east-1"
    encrypt = true
    #profile = "nick_terraform"
#    access_key = var.AWS_ACCESS_KEY_ID
#    secret_key = var.AWS_SECRET_ACCESS_KEY
  }
#  backend "local" {
#    path = "./statefile.tfstate"
#  }


  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

}

provider "aws" {
  region  = "eu-north-1"
  #profile = "nick_terraform"

 # access_key = var.AWS_ACCESS_KEY_ID
 # secret_key = var.AWS_SECRET_ACCESS_KEY

}



variable "aws_access_key" {
  description = "AWS Access Key"
  type        = string
  sensitive   = true
}

variable "aws_secret_key" {
  description = "AWS Secret Key"
  type        = string
  sensitive   = true
}
