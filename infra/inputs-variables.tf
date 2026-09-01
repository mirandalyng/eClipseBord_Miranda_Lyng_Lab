variable "resource-group-name" {
  default = "rg-fullstack-python"
  type    = string

}

variable "location" {
  type    = string
  default = "norwayeast"

}

variable "project_name" {
  default = "lab-azure"
}

variable "acr_name" {
  default = "labml"

}

variable "image_tag" {
  default = "latest"
}
