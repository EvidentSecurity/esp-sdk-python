# Report

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**relationships** | **object** | Links to Associated Objects | [optional] 
**errors** | **list[str]** | Array of error messages if the request failed | [optional] 
**id** | **int** | Unique ID | [optional] 
**created_at** | [**datetime**](DateTime.md) | ISO 8601 timestamp when the alert was created | [optional] 
**status** | **str** | Status of the report | [optional] 
**updated_at** | [**datetime**](DateTime.md) | ISO 8601 timestamp when the alert was last updated | [optional] 
**alerts** | [**list[Alert]**](Alert.md) | Associated Alerts | [optional] 
**alert_ids** | **list[int]** | Associated Alert Ids | [optional] 
**organization** | [**Organization**](Organization.md) | Associated Organization | [optional] 
**organization_id** | **int** | Associated Organization Id | [optional] 
**sub_organization** | [**SubOrganization**](SubOrganization.md) | Associated Sub Organization | [optional] 
**sub_organization_id** | **int** | Associated Sub Organization Id | [optional] 
**team** | [**Team**](Team.md) | Associated Team | [optional] 
**team_id** | **int** | Associated Team Id | [optional] 
**external_account** | [**ExternalAccount**](ExternalAccount.md) | Associated External Account | [optional] 
**external_account_id** | **int** | Associated External Account Id | [optional] 
**stat** | [**Stat**](Stat.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


