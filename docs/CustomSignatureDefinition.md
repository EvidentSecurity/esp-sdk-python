# CustomSignatureDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique ID | [optional] 
**code** | **str** | The code used for this result | [optional] 
**created_at** | [**datetime**](DateTime.md) | ISO 8601 timestamp when the resource was created | [optional] 
**error_messages** | **list[str]** | Error messages that occurred while running the code | [optional] 
**language** | **str** | The language of the code | [optional] 
**status** | **str** | Status of the result | [optional] 
**updated_at** | [**datetime**](DateTime.md) | ISO 8601 timestamp when the resource was last updated | [optional] 
**definition** | [**CustomSignatureDefinition**](CustomSignatureDefinition.md) | Associated Custom Signature Definition | [optional] 
**definition_id** | **int** | Associated Custom Signature Definition Id | [optional] 
**region** | [**Region**](Region.md) | Associated Region | [optional] 
**region_id** | **int** | Associated Region Id | [optional] 
**external_account** | [**ExternalAccount**](ExternalAccount.md) | Associated External Account | [optional] 
**external_account_id** | **int** | Associated External Account Id | [optional] 
**alerts** | [**list[Alert]**](Alert.md) | Associated Alerts | [optional] 
**alert_ids** | **list[int]** | Associated Alert Ids | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


