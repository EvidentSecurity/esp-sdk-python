# CustomSignatureResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique ID | [optional] 
**created_at** | [**datetime**](DateTime.md) | ISO 8601 timestamp when the resource was created | [optional] 
**code** | **str** | The code used for this result | [optional] 
**language** | **str** | The language of the code. Valid values are ruby, javascript | [optional] 
**status** | **str** | Status of the result. Valid values are running, failed, complete | [optional] 
**updated_at** | [**datetime**](DateTime.md) | ISO 8601 timestamp when the resource was updated | [optional] 
**error_messages** | **list[str]** | Error messages that occurred while running the code | [optional] 
**external_account** | [**ExternalAccount**](ExternalAccount.md) | Associated External Account | [optional] 
**external_account_id** | **int** | Associated External Account ID | [optional] 
**region** | [**Region**](Region.md) | Associated Region | [optional] 
**region_id** | **int** | Associated Region ID | [optional] 
**definition** | [**CustomSignatureDefinition**](CustomSignatureDefinition.md) | Associated Definition | [optional] 
**definition_id** | **int** | Associated Definition ID | [optional] 
**alerts** | [**list[Alert]**](Alert.md) | Associated Alerts | [optional] 
**alert_ids** | **list[int]** | Associated Alerts IDs | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


