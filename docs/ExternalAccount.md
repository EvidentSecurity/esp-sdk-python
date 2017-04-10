# ExternalAccount

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**relationships** | **object** | Links to Associated Objects | [optional] 
**errors** | **list[str]** | Array of error messages if the request failed | [optional] 
**id** | **int** | Unique Id | [optional] 
**account** | **str** | The name of the account created | [optional] 
**arn** | **str** | Amazon Resource Name for the IAM role | [optional] 
**created_at** | [**datetime**](DateTime.md) | Created At | [optional] 
**external_id** | **str** | External Identifier set on the role | [optional] 
**name** | **str** | Name | [optional] 
**updated_at** | [**datetime**](DateTime.md) | Updated At | [optional] 
**cloudtrail_name** | **str** | Cloudtrail Name | [optional] 
**organization** | [**Organization**](Organization.md) | Associated Organization | [optional] 
**organization_id** | **int** | Associated Organization Id | [optional] 
**sub_organization** | [**SubOrganization**](SubOrganization.md) | Associated Sub Organization | [optional] 
**sub_organization_id** | **int** | Associated Sub Organization Id | [optional] 
**team** | [**Team**](Team.md) | Associated Team | [optional] 
**team_id** | **int** | Associated Team Id | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


