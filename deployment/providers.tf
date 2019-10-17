provider "aws" {
  profile = "terraform-deployer"
  region  = "eu-west-2"
}

terraform {
  backend "s3" {
    bucket  = "021651181835-terraform-state"
    key     = "lambda_card_generator.tfstate"
    region  = "eu-west-2"
  }
}

data "aws_caller_identity" "current" {}
