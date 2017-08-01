# AuditLog

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique ID | [optional] 
**item_type** | **str** | Item that was changed | [optional] 
**item_id** | **int** | ID of the item that was changed | [optional] 
**action** | **str** | Action attempted on the item | [optional] 
**successful** | **bool** | Shows if the action was successful | [optional] 
**access_denied** | **bool** | Shows if access was denied | [optional] 
**user_ip** | **str** | The IP of the user attempting the action | [optional] 
**platform** | **str** | The platform the user attempted the action from | [optional] 
**created_at** | [**Datetime**](Datetime.md) | A timestamp of when this record was created | [optional] 
**updated_at** | [**Datetime**](Datetime.md) | A timestamp of the last time this record was changed | [optional] 
**organization** | [**Organization**](Organization.md) | Associated Organization | [optional] 
**organization_id** | **int** | Associated Organization Id | [optional] 
**user** | [**User**](User.md) | Associated User | [optional] 
**user_id** | **int** | Associated User Id | [optional] 
**errors** | **list[str]** | Array of error messages if the request failed | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


