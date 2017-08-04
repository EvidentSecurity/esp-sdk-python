# Suppression

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique ID | [optional] 
**created_at** | [**datetime**](DateTime.md) | ISO 8601 timestamp when the resource was created | [optional] 
**reason** | **str** | The reason for the suppresion | [optional] 
**resource** | **str** | The resource string this suppression will suppress alerts for | [optional] 
**status** | **str** | The status of this suppresion | [optional] 
**suppression_type** | **str** | Type of suppression. Possible values are unique_identifiers, regions, and signatures | [optional] 
**updated_at** | [**datetime**](DateTime.md) | ISO 8601 timestamp when the suppression was last updated | [optional] 
**organization** | [**Organization**](Organization.md) | Associated Organization | [optional] 
**organization_id** | **int** | Associated Organization Id | [optional] 
**created_by** | [**User**](User.md) | Associated Created By | [optional] 
**created_by_id** | **int** | Associated Created By Id | [optional] 
**regions** | [**list[Region]**](Region.md) | Associated Regions | [optional] 
**region_ids** | **list[int]** | Associated Regions Ids | [optional] 
**external_accounts** | [**list[ExternalAccount]**](ExternalAccount.md) | Associated External Accounts | [optional] 
**external_account_ids** | **list[int]** | Associated External Accounts Ids | [optional] 
**signatures** | [**list[Signature]**](Signature.md) | Associated Signatures | [optional] 
**signature_ids** | **list[int]** | Associated Signatures Ids | [optional] 
**custom_signatures** | [**list[CustomSignature]**](CustomSignature.md) | Associated Custom Signatures | [optional] 
**custom_signature_ids** | **list[int]** | Associated Custom Signatures Ids | [optional] 
**errors** | **list[str]** | Array of error messages if the request failed | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


