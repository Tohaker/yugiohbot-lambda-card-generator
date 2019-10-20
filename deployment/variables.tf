locals { 
    lambda_title_text_name  = "YuGiOhBot__Card_Generator"
}

variable "region" {
  description = "The AWS region to deploy in."
  default = "eu-west-2"
}

variable "s3_package" {
  description = "The name of the package to deploy in S3."
  default = "yugiohbot-card-generator-package.zip"
}

variable "local_package" {
  description = "The location of the package to deploy."
  default = "../package.zip"
}

variable "bucket" {
  description = "The S3 bucket where the package is stored."
  default = "021651181835-lambda-packages"
}

variable "handler" {
  description = "Name of the lambda function and handler entrypoint."
  default = "lambda_function.lambda_handler"
}

variable "runtime" {
  description = "The runtime language to be used."
  default = "python3.7"
}

variable "chromedriver" {
  description = "The location of the bundled chromedriver."
  default = "/var/task/bin/chromedriver"
}

variable "headless-chromium" {
  description = "The location of the bundled chromium installation"
  default = "/var/task/bin/headless-chromium"
}