# Definition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**relationships** | **object** | Links to Associated Objects | [optional] 
**errors** | **list[str]** | Array of error messages if the request failed | [optional] 
**id** | **int** | Unique ID | [optional] 
**code** | **str** | The code for this definition | [optional] 
**created_at** | [**datetime**](DateTime.md) | ISO 8601 timestamp when the resource was created | [optional] 
**language** | **str** | The language of the definition | [optional] 
**version_number** | **int** | Version of definition | [optional] 
**status** | **str** | Status of the definition | [optional] 
**updated_at** | [**datetime**](DateTime.md) | ISO 8601 timestamp when the resource was last updated | [optional] 
**custom_signature** | [**CustomSignature**](CustomSignature.md) | Associated Custom Signature  | [optional] 
**custom_signature_id** | **int** | Associated Custom Signature Id | [optional] 
**results** | [**list[CustomSignatureResult]**](CustomSignatureResult.md) | Associated Custom Signatures | [optional] 
**result_ids** | **list[int]** | Associated Custom Signature Ids | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


