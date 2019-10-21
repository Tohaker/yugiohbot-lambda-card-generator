locals { 
    cloud_run_service_name  = "YuGiOhBot__Card_Generator"
}

variable "location" {
  description = "The GCP region to deploy in."
  default = "us-east1"
}

variable "image" {
  description = "Name of the docker image to deploy"
  default = "gcr.io/yugiohbot/card-generator"
}