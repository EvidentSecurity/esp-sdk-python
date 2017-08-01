# AuditLogFile

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique ID | [optional] 
**file_name** | **str** |  | [optional] 
**format** | **str** |  | [optional] 
**created_at** | [**Datetime**](Datetime.md) |  | [optional] 
**updated_at** | [**Datetime**](Datetime.md) |  | [optional] 
**organization** | [**Organization**](Organization.md) | Associated Organization | [optional] 
**organization_id** | **int** | Associated Organization Id | [optional] 
**user** | [**User**](User.md) | Associated User | [optional] 
**user_id** | **int** | Associated User Id | [optional] 
**errors** | **list[str]** | Array of error messages if the request failed | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


