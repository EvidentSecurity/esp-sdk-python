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
**disabled_signatures** | [**list[Signature]**](Signature.md) | Associated Disabled Signatures | [optional] 
**suppressions** | [**list[Suppression]**](Suppression.md) | Associated Suppressions | [optional] 
**suppression_ids** | **list[int]** | Associated Suppressions IDs | [optional] 
**azure_group** | [**AzureGroup**](AzureGroup.md) | Associated Azure Group | [optional] 
**credentials** | [**ExternalAccountAmazonIam**](ExternalAccountAmazonIam.md) | Associated Credentials | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


