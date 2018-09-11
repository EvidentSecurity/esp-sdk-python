# ScheduledExportResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique ID | [optional] 
**uuid** | **str** | The uuid to access the result | [optional] 
**expires_at** | [**datetime**](DateTime.md) | ISO 8601 timestamp when the result will expire | [optional] 
**url** | **str** | A temporary URL where the file can be accessed | [optional] 
**created_at** | [**datetime**](DateTime.md) | ISO 8601 timestamp when the resource was created | [optional] 
**updated_at** | [**datetime**](DateTime.md) | ISO 8601 timestamp when the resource was updated | [optional] 
**scheduled_export** | [**ScheduledExport**](ScheduledExport.md) | Associated Scheduled Export | [optional] 
**scheduled_export_id** | **int** | Associated Scheduled Export ID | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


