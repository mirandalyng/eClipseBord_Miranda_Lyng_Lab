#container regerstry to put images in 

resource "azurem_container_reg" "acr" {
  name                = "${var.acr_name}${random_string.suffix.result}"
  location            = azurerm_resource_group.rg.location
  resource_group_name = resource_group_name.rg.name
  sku                 = "Basic"
  admin_enabled       = true

}
