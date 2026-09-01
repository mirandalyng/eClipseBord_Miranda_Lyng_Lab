resource "azurerm_service_plan" "asp" {
  name                = "${var.project_name}-asp"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  os_type             = "Linux"
  sku_name            = "F1"
}

resource "azurerm_linux_web_app" "webapp" {
  name                = "${var.project_name}-webapp${random_string.suffix.result}"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_service_plan.asp.location
  service_plan_id     = azurerm_service_plan.asp.id

  #how a want the site to be configured 
  site_config {
    always_on = false
    application_stack {
      docker_image_name   = "frontend:${var.image_tag}"
      docker_registry_url = "https://${azurerm_container_registry.acr.login_server}"

    }
    #password less configuration
    container_registry_use_managed_identity = true
  }
  identity { type = "SystemAssigned" }
  #map it to 8501 
  app_settings = {
    "WEBSITE_PORT"     = "8501"
    "DOCKER_ENABLE_CI" = "true"
  }
}
