# ExportedReport

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique ID | [optional] 
**recipient_id** | **int** | Associated Recipient ID | [optional] 
**recipient_type** | **str** | Polymorphic recipient type. Valid values are User, ScheduledExportResult | [optional] 
**report_ids** | **list[int]** | An array of report IDs to export alerts for | [optional] 
**format** | **str** | The file format of the export. Valid values are csv, json, pdf | [optional] 
**url** | **str** | A temporary URL where the file can be accessed | [optional] 
**file_name** | **str** | The name of the file | [optional] 
**filter** | **object** | Params used to filter the alerts that will be exported | [optional] 
**created_at** | [**datetime**](DateTime.md) | ISO 8601 timestamp when the resource was created | [optional] 
**updated_at** | [**datetime**](DateTime.md) | ISO 8601 timestamp when the resource was updated | [optional] 
**recipient** | [**User**](User.md) | Associated Recipient | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


