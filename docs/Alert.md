# Alert

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**relationships** | **object** | Links to Associated Objects | [optional] 
**errors** | **list[str]** | Array of error messages if the request failed | [optional] 
**id** | **int** | Unique Id | 
**created_at** | [**datetime**](DateTime.md) | ISO 8601 timestamp when the resource was created | [optional] 
**ended_at** | [**datetime**](DateTime.md) | ISO 8601 timestamp when the alert stopped being active | [optional] 
**resource** | **str** | Resource identifier in Amazon | [optional] 
**stated_at** | [**datetime**](DateTime.md) | ISO 8601 timestamp when the alert started being active | [optional] 
**status** | **str** | Status of the alert | [optional] 
**risk_level** | **str** | Risk Level of the alert | [optional] 
**updated_at** | [**datetime**](DateTime.md) | ISO 8601 timestamp when the resource was last updated | [optional] 
**custom_signature** | [**CustomSignature**](CustomSignature.md) | Either a signature or custom signature but not both will be present | [optional] 
**custom_signature_id** | **int** | Either a signature or custom signature but not both will be present | [optional] 
**external_account** | [**ExternalAccount**](ExternalAccount.md) | Associated External Account | [optional] 
**external_account_id** | **int** | Associated External Account Id | [optional] 
**region** | [**Region**](Region.md) | Associated Region | [optional] 
**region_id** | **int** | Associated Region Id | [optional] 
**signature** | [**Signature**](Signature.md) | Either a signature or custom signature but not both will be present | [optional] 
**signature_id** | **int** | Either a signature or custom signature but not both will be present | [optional] 
**supression** | [**Suppression**](Suppression.md) | If present the alert was suppressed | [optional] 
**supression_id** | **int** | If present the alert was suppressed | [optional] 
**metadata** | [**Metadata**](Metadata.md) | Associated Metadata | [optional] 
**metadata_id** | **int** | Associated Metadata Id | [optional] 
**cloud_trail_events** | [**list[CloudTrailEvent]**](CloudTrailEvent.md) | Associated Cloud Trail Events | [optional] 
**cloud_trail_event_ids** | **list[int]** | Associated Cloud Trail Event Ids | [optional] 
**tags** | [**list[Tag]**](Tag.md) | Associated Tags | [optional] 
**tag_ids** | **list[int]** | Associated Tag Ids | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


