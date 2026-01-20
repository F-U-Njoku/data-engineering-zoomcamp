
variable "project_id" {
    description = "Cloud project ID (GCP project)"
    type        = string

    validation {
        condition     = length(var.project_id) > 0
        error_message = "project_id must not be empty."
    }
}

variable "region" {
    description = "Primary region for resources"
    type        = string
    default     = "europe-southwest1"
}

variable "location" {
    description = "Project Location (specific region or multi-region)"
    type        = string
    default     = "EU"
}

variable "storage_bucket_name" {
    description = "Name for a GCS storage bucket"
    type        = string
    default     = null
}

variable "bigquery_dataset_name" {
    description = "Name for the BigQuery dataset"
    type        = string
    default     = null
}


