# Organization

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**relationships** | **object** | Links to Associated Objects | [optional] 
**errors** | **list[str]** | Array of error messages if the request failed | [optional] 
**id** | **int** | Unique Id | 
**name** | **str** | Name | [optional] 
**created_at** | [**datetime**](DateTime.md) | ISO 8601 timestamp when the resource was created | [optional] 
**updated_at** | [**datetime**](DateTime.md) | ISO 8601 timestamp when the resource was last updated | [optional] 
**custom_signatures** | [**list[CustomSignature]**](CustomSignature.md) | Associated Custom Signatures | [optional] 
**custom_signature_ids** | **list[int]** | Associated Custom Signature Ids | [optional] 
**external_accounts** | [**list[ExternalAccount]**](ExternalAccount.md) | Associated External Accounts | [optional] 
**external_account_ids** | **list[int]** | Associated External Account Ids | [optional] 
**sub_organizations** | [**list[SubOrganization]**](SubOrganization.md) | Associated Sub Organizations | [optional] 
**sub_organization_ids** | **list[int]** | Associated Sub Organization Ids | [optional] 
**teams** | [**list[Team]**](Team.md) | Associated Teams | [optional] 
**team_ids** | **list[int]** | Associated Team Ids | [optional] 
**users** | [**list[User]**](User.md) | Associated Users | [optional] 
**user_ids** | **list[int]** | Associated User Ids | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


