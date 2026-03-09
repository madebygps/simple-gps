param location string
param environmentName string
param resourceToken string
param resourcePrefix string

// App Service Plan (Free tier)
resource appServicePlan 'Microsoft.Web/serverfarms@2023-12-01' = {
  name: 'az-${resourcePrefix}-${resourceToken}-plan'
  location: location
  sku: {
    name: 'F1'
    tier: 'Free'
  }
  kind: 'linux'
  properties: {
    reserved: true
  }
  tags: {
    'azd-env-name': environmentName
  }
}

// App Service
resource webApp 'Microsoft.Web/sites@2023-12-01' = {
  name: 'az-${resourcePrefix}-${resourceToken}-app'
  location: location
  properties: {
    serverFarmId: appServicePlan.id
    siteConfig: {
      linuxFxVersion: 'PYTHON|3.12'
      appCommandLine: 'python -m http.server 8000 --directory /home/site/wwwroot'
      ftpsState: 'Disabled'
      minTlsVersion: '1.2'
    }
    httpsOnly: true
  }
  tags: {
    'azd-env-name': environmentName
    'azd-service-name': 'simple-gps'
  }
}

output WEBAPP_NAME string = webApp.name
output WEBAPP_URI string = 'https://${webApp.properties.defaultHostname}'
