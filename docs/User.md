# User

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique ID | [optional] 
**created_at** | [**datetime**](DateTime.md) | ISO 8601 timestamp when the resource was created | [optional] 
**email** | **str** | The email of the user | [optional] 
**time_zone** | **str** | The time-zone of the user | [optional] 
**first_name** | **str** | The first name of the user | [optional] 
**last_name** | **str** | The last name of the user | [optional] 
**phone** | **str** | The phone number associated with the user | [optional] 
**mfa_enabled** | **bool** | Specifies whether Multi Factor Authentication is enabled or not | [optional] 
**disable_daily_emails** | **bool** | This option toggles the daily emails option | [optional] 
**locked** | **bool** | Specifies whether the user account is locked from accessing ESP | [optional] 
**locked_at** | [**datetime**](DateTime.md) | The time the user account was locked | [optional] 
**updated_at** | [**datetime**](DateTime.md) | ISO 8601 timestamp when the resource was updated | [optional] 
**organization** | [**Organization**](Organization.md) | Associated Organization | [optional] 
**organization_id** | **int** | Associated Organization Id | [optional] 
**sub_organizations** | [**list[SubOrganization]**](SubOrganization.md) | Associated Sub Organizations | [optional] 
**sub_organization_ids** | **list[int]** | Associated Sub Organizations Ids | [optional] 
**teams** | [**list[Team]**](Team.md) | Associated Teams | [optional] 
**team_ids** | **list[int]** | Associated Teams Ids | [optional] 
**role** | [**Role**](Role.md) | Associated Role | [optional] 
**role_id** | **int** | Associated Role Id | [optional] 
**errors** | **list[str]** | Array of error messages if the request failed | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


