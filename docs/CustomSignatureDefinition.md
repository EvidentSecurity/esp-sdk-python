# CustomSignatureDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique ID | [optional] 
**code** | **str** | The code for this definition | [optional] 
**updated_at** | [**datetime**](DateTime.md) | ISO 8601 timestamp when the resource was updated | [optional] 
**created_at** | [**datetime**](DateTime.md) | ISO 8601 timestamp when the resource was created | [optional] 
**version_number** | **int** | Version of definition | [optional] 
**language** | **str** | The language of the definition. Valid values are ruby, javascript | [optional] 
**status** | **str** | Status of the definition. Valid values are editable, validating, active, archived, disabled | [optional] 
**custom_signature** | [**CustomSignature**](CustomSignature.md) | Associated Custom Signature | [optional] 
**custom_signature_id** | **int** | Associated Custom Signature ID | [optional] 
**results** | [**list[CustomSignatureResult]**](CustomSignatureResult.md) | Associated Results | [optional] 
**result_ids** | **list[int]** | Associated Results IDs | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


