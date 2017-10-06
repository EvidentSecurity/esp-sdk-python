# SubOrganization

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique ID | [optional] 
**name** | **str** | Name of the sub organization | [optional] 
**created_at** | [**datetime**](DateTime.md) | ISO 8601 timestamp when the resource was created | [optional] 
**updated_at** | [**datetime**](DateTime.md) | ISO 8601 timestamp when the resource was updated | [optional] 
**external_accounts** | [**list[ExternalAccount]**](ExternalAccount.md) | Associated External Accounts | [optional] 
**external_account_ids** | **list[int]** | Associated External Accounts IDs | [optional] 
**organization** | [**Organization**](Organization.md) | Associated Organization | [optional] 
**organization_id** | **int** | Associated Organization ID | [optional] 
**teams** | [**list[Team]**](Team.md) | Associated Teams | [optional] 
**team_ids** | **list[int]** | Associated Teams IDs | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


