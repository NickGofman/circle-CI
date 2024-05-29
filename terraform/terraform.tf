terraform {
  required_version = ">= 1.6"
  backend "s3" {
    bucket  = "terraform-backend-nick"
    key     = "terraform.tfstate"
    region  = "us-east-1"
    encrypt = true
    profile = "nick_terraform"

  }



  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

}

provider "aws" {
  region  = "eu-north-1"
  profile = "nick_terraform"

}

