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
**user_email** | **str** | The email of the user attempting the action | [optional] 
**platform** | **str** | The platform the user attempted the action from | [optional] 
**created_at** | [**datetime**](DateTime.md) | ISO 8601 timestamp when the resource was created | [optional] 
**updated_at** | [**datetime**](DateTime.md) | ISO 8601 timestamp when the resource was updated | [optional] 
**organization** | [**Organization**](Organization.md) | Associated Organization | [optional] 
**organization_id** | **int** | Associated Organization ID | [optional] 
**user** | [**User**](User.md) | Associated User | [optional] 
**user_id** | **int** | Associated User ID | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


