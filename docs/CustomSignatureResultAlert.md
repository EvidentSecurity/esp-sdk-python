# CustomSignatureResultAlert

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique ID | [optional] 
**created_at** | [**datetime**](DateTime.md) | ISO 8601 timestamp when the resource was created | [optional] 
**status** | **str** | Status of the alert. Valid values are fail, warn, error, pass, info | [optional] 
**resource** | **str** | Resource identifier in Amazon | [optional] 
**metadata** | **object** | Metadata associated with the result | [optional] 
**tags** | **list[object]** | Tags associated with the result | [optional] 
**updated_at** | [**datetime**](DateTime.md) | ISO 8601 timestamp when the resource was updated | [optional] 
**external_account** | [**ExternalAccount**](ExternalAccount.md) | Associated External Account | [optional] 
**external_account_id** | **int** | Associated External Account ID | [optional] 
**region** | [**Region**](Region.md) | Associated Region | [optional] 
**region_id** | **int** | Associated Region ID | [optional] 
**custom_signature** | [**CustomSignature**](CustomSignature.md) | Associated Custom Signature | [optional] 
**custom_signature_id** | **int** | Associated Custom Signature ID | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


