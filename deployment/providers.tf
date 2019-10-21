provider "google" {
  credentials = "${file("~/gcloud-service-key.json")}"
  project = "yugiohbot"
  region  = "us-east1"
}

provider "google-beta" {
  credentials = "${file("~/gcloud-service-key.json")}"
  project = "yugiohbot"
  region  = "us-east1"
}

terraform {}
