# CustomSignature

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique ID | [optional] 
**created_at** | [**datetime**](DateTime.md) | ISO 8601 timestamp when the resource was created | [optional] 
**description** | **str** | The description of the custom signature that is displayed on alerts | [optional] 
**identifier** | **str** | The identifier to use for the custom signature. Common format is AWS:- such as AWS:IAM-001 | [optional] 
**include_new_accounts** | **bool** | When enabled, automatically adds new accounts to this signature. This field can only be set by an organization level user. | [optional] 
**name** | **str** | The name of the custom signature | [optional] 
**resolution** | **str** | Details for how to resolve this custom signature that is displayed on alerts | [optional] 
**risk_level** | **str** | The risk-level of the problem identified by the custom signature. Valid values are low, medium, high | [optional] 
**updated_at** | [**datetime**](DateTime.md) | ISO 8601 timestamp when the resource was updated | [optional] 
**organization** | [**Organization**](Organization.md) | Associated Organization | [optional] 
**organization_id** | **int** | Associated Organization ID | [optional] 
**external_accounts** | [**list[ExternalAccount]**](ExternalAccount.md) | Associated External Accounts | [optional] 
**external_account_ids** | **list[int]** | Associated External Accounts IDs | [optional] 
**definitions** | [**list[CustomSignatureDefinition]**](CustomSignatureDefinition.md) | Associated Definitions | [optional] 
**definition_ids** | **list[int]** | Associated Definitions IDs | [optional] 
**suppressions** | [**list[Suppression]**](Suppression.md) | Associated Suppressions | [optional] 
**suppression_ids** | **list[int]** | Associated Suppressions IDs | [optional] 
**service** | [**Service**](Service.md) | Associated Service | [optional] 
**service_id** | **int** | Associated Service ID | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


