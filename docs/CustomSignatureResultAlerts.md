# CustomSignatureResultAlerts

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique ID | [optional] 
**created_at** | [**datetime**](DateTime.md) | ISO 8601 timestamp when the resource was created | [optional] 
**status** | **str** | Status of the alert | [optional] 
**resource** | **str** | Resource identifier in Amazon | [optional] 
**metadata** | **object** |  | [optional] 
**tags** | **list[object]** |  | [optional] 
**updated_at** | [**datetime**](DateTime.md) | ISO 8601 timestamp when the resource was last updated | [optional] 
**external_account** | [**ExternalAccount**](ExternalAccount.md) | Associated External Account | [optional] 
**external_account_id** | **int** | Associated External Account Id | [optional] 
**region** | [**Region**](Region.md) | Associated Region | [optional] 
**region_id** | **int** | Associated Region Id | [optional] 
**custom_signature** | [**CustomSignature**](CustomSignature.md) | Associated Custom Signature | [optional] 
**custom_signature_id** | **int** | Associated Custom Signature Id | [optional] 
**errors** | **list[str]** | Array of error messages if the request failed | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


