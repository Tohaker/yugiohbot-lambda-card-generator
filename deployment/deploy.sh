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

echo "Building docker image"
docker build -t gcr.io/yugiohbot/card-generator ../

echo "Authorising gcloud"
echo $GCLOUD_SERVICE_KEY | base64 --decode -i > ${HOME}/gcloud-service-key.json
gcloud auth activate-service-account --key-file ${HOME}/gcloud-service-key.json
gcloud --quiet config set project yugiohbot
gcloud --quiet config set compute/zone us-east1

echo "Pushing docker image"
gcloud docker push gcr.io/yugiohbot/card-generator

echo "Initialising Terraform."
terraform init

echo "Planning Terraform."
terraform plan \
    -out=output.tfplan

echo "Applying Terraform."
terraform apply \
    -auto-approve \
    "output.tfplan"
