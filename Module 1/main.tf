terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
      version = "7.16.0"
    }
  }
}

provider "google" {
  project     = "single-arcadia-448620-u5"
  region      = "europe-southwest1"
}