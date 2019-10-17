#!/bin/bash

printf "\nBegin Deployment of AWS Lambda.\n"

function finish {
    rv=$?
    printf "\nDeployment completed with code ${rv}\n"
}

trap finish EXIT

current_directory=$(dirname $0)
pushd ${current_directory}

set -e

echo "Uploading package file to S3"
aws s3 cp ../package.zip s3://021651181835-lambda-packages/yugiohbot-card-generator-package.zip

echo "Initialising Terraform."
terraform init \
    -backend=true \
    -backend-config="access_key=${AWS_ACCESS_KEY_ID}" \
    -backend-config="secret_key=${AWS_SECRET_ACCESS_KEY}"

echo "Planning Terraform."
terraform plan \
    -out=output.tfplan

echo "Applying Terraform."
terraform apply \
    -auto-approve \
    "output.tfplan"
