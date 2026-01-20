targetScope = 'subscription'

@minLength(1)
@maxLength(64)
@description('Name of the environment that can be used as part of naming resource convention')
param environmentName string

@minLength(1)
@description('Primary location for all resources')
param location string

@description('Name of the resource group')
param resourceGroupName string

var resourceToken = uniqueString(subscription().id, location, environmentName)
var resourcePrefix = 'madebygps'

// Resource Group
resource resourceGroup 'Microsoft.Resources/resourceGroups@2024-03-01' = {
  name: resourceGroupName
  location: location
  tags: {
    'azd-env-name': environmentName
  }
}

// Main resources module
module resources 'main-resources.bicep'= {
  name: 'resources'
  scope: resourceGroup
  params: {
    location: location
    environmentName: environmentName
    resourceToken: resourceToken
    resourcePrefix: resourcePrefix
  }
}

output RESOURCE_GROUP_ID string = resourceGroup.id
output WEBAPP_NAME string = resources.outputs.WEBAPP_NAME
output WEBAPP_URI string = resources.outputs.WEBAPP_URI
