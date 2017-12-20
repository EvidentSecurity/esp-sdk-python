# ExternalAccount

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique ID | [optional] 
**created_at** | [**datetime**](DateTime.md) | ISO 8601 timestamp when the resource was created | [optional] 
**name** | **str** | Name | [optional] 
**updated_at** | [**datetime**](DateTime.md) | ISO 8601 timestamp when the resource was updated | [optional] 
**provider** | **str** | The cloud provider this account is for | [optional] 
**team** | [**Team**](Team.md) | Associated Team | [optional] 
**team_id** | **int** | Associated Team ID | [optional] 
**scan_intervals** | [**list[ScanInterval]**](ScanInterval.md) | Associated Scan Intervals | [optional] 
**scan_interval_ids** | **list[int]** | Associated Scan Intervals IDs | [optional] 
**disabled_signatures** | [**list[Signature]**](Signature.md) | Associated Disabled Signatures | [optional] 
**disabled_signature_ids** | **list[int]** | Associated Disabled Signatures IDs | [optional] 
**azure_group** | [**AzureGroup**](AzureGroup.md) | Associated Azure Group | [optional] 
**azure_group_id** | **int** | Associated Azure Group ID | [optional] 
**credentials** | [**ExternalAccountAmazonIAM**](ExternalAccountAmazonIAM.md) | Associated Credentials | [optional] 
**credentials_id** | **int** | Associated Credentials ID | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


