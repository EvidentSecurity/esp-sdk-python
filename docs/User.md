# User

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique ID | [optional] 
**created_at** | [**datetime**](DateTime.md) | ISO 8601 timestamp when the resource was created | [optional] 
**email** | **str** | The email of the user | [optional] 
**time_zone** | **str** | The time zone of the user. See Time Zones for a list of valid time zones | [optional] 
**updated_at** | [**datetime**](DateTime.md) | ISO 8601 timestamp when the resource was updated | [optional] 
**first_name** | **str** | The first name of the user | [optional] 
**last_name** | **str** | The last name of the user | [optional] 
**phone** | **str** | The phone number of the user | [optional] 
**mfa_enabled** | **bool** | Specifies whether Multi Factor Authentication is enabled or not | [optional] 
**disable_daily_emails** | **bool** | Specifies whether the daily emails should be turned off or not | [optional] 
**locked** | **bool** | Specifies whether the user account is locked from accessing ESP | [optional] 
**locked_at** | [**datetime**](DateTime.md) | The time the user account was locked | [optional] 
**access_level** | **str** | The level of access this user has. Team access has access to items belonging only to that team. Sub Organization access has access to items belonging only to all teams under that sub organization. Organization access has access to all sub organizations and teams under that organization. Valid values are organization_level, sub_organization_level, team_level | [optional] 
**organization** | [**Organization**](Organization.md) | Associated Organization | [optional] 
**organization_id** | **int** | Associated Organization ID | [optional] 
**sub_organizations** | [**list[SubOrganization]**](SubOrganization.md) | Associated Sub Organizations | [optional] 
**sub_organization_ids** | **list[int]** | Associated Sub Organizations IDs | [optional] 
**teams** | [**list[Team]**](Team.md) | Associated Teams | [optional] 
**team_ids** | **list[int]** | Associated Teams IDs | [optional] 
**role** | [**Role**](Role.md) | Associated Role | [optional] 
**role_id** | **int** | Associated Role ID | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


