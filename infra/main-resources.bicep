param location string
param environmentName string
param resourceToken string
param resourcePrefix string

// Azure Static Web App (Free tier)
resource staticWebApp 'Microsoft.Web/staticSites@2023-12-01' = {
  name: 'az-${resourcePrefix}-${resourceToken}-swa'
  location: location
  sku: {
    name: 'Free'
    tier: 'Free'
  }
  properties: {
    stagingEnvironmentPolicy: 'Enabled'
    allowConfigFileUpdates: true
    buildProperties: {
      skipGithubActionWorkflowGeneration: true
    }
  }
  tags: {
    'azd-env-name': environmentName
    'azd-service-name': 'simple-gps'
  }
}

output WEBAPP_NAME string = staticWebApp.name
output WEBAPP_URI string = 'https://${staticWebApp.properties.defaultHostname}'
