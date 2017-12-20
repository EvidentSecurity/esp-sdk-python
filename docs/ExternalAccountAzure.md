# ExternalAccountAzure

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique ID | [optional] 
**subscription_id** | **str** | Azure subscription ID | [optional] 
**client_id** | **str** | Azure client ID | [optional] 
**tenant_id** | **str** | Azure tenant ID | [optional] 
**created_at** | [**datetime**](DateTime.md) | ISO 8601 timestamp when the resource was created | [optional] 
**updated_at** | [**datetime**](DateTime.md) | ISO 8601 timestamp when the resource was updated | [optional] 
**last_message_received_at** | [**datetime**](DateTime.md) | ISO 8601 timestamp when the last event was received from Azure. This is updated hourly. | [optional] 
**app_key** | **str** | Azure app key | [optional] 
**channel_url** | **str** | The URL for the azure account channel.  It is only returned when first created or when reset. | [optional] 
**channel_active** | **bool** | Returns true if the channel is active | [optional] 
**external_account** | [**ExternalAccount**](ExternalAccount.md) | Associated External Account | [optional] 
**external_account_id** | **int** | Associated External Account ID | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


