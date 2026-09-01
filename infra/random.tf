#random strings for resource names for them to be unique 
resource "random_string" "suffix" {
  length  = 6
  special = false
  upper   = false

}
