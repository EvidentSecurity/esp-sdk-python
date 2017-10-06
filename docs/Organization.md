# Organization

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique ID | [optional] 
**created_at** | [**datetime**](DateTime.md) | ISO 8601 timestamp when the resource was created | [optional] 
**name** | **str** | Name of the organization | [optional] 
**require_mfa** | **bool** | Whether or not users for this organization are required to enable Multi Factor Authentication | [optional] 
**updated_at** | [**datetime**](DateTime.md) | ISO 8601 timestamp when the resource was updated | [optional] 
**subscription** | [**Subscription**](Subscription.md) | Associated Subscription | [optional] 
**subscription_id** | **int** | Associated Subscription ID | [optional] 
**custom_signatures** | [**list[CustomSignature]**](CustomSignature.md) | Associated Custom Signatures | [optional] 
**custom_signature_ids** | **list[int]** | Associated Custom Signatures IDs | [optional] 
**external_accounts** | [**list[ExternalAccount]**](ExternalAccount.md) | Associated External Accounts | [optional] 
**external_account_ids** | **list[int]** | Associated External Accounts IDs | [optional] 
**sub_organizations** | [**list[SubOrganization]**](SubOrganization.md) | Associated Sub Organizations | [optional] 
**sub_organization_ids** | **list[int]** | Associated Sub Organizations IDs | [optional] 
**teams** | [**list[Team]**](Team.md) | Associated Teams | [optional] 
**team_ids** | **list[int]** | Associated Teams IDs | [optional] 
**users** | [**list[User]**](User.md) | Associated Users | [optional] 
**user_ids** | **list[int]** | Associated Users IDs | [optional] 
**compliance_standards** | [**list[ComplianceStandard]**](ComplianceStandard.md) | Associated Compliance Standards | [optional] 
**compliance_standard_ids** | **list[int]** | Associated Compliance Standards IDs | [optional] 
**integrations** | [**list[Integration]**](Integration.md) | Associated Integrations | [optional] 
**integration_ids** | **list[int]** | Associated Integrations IDs | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


