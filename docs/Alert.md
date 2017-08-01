# Alert

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique ID | [optional] 
**created_at** | [**datetime**](DateTime.md) | ISO 8601 timestamp when the resource was created | [optional] 
**description** | **str** | The description of the user | [optional] 
**identifier** | **str** | The identifier of the signature | [optional] 
**name** | **str** | The name of the signature | [optional] 
**resolution** | **str** | Details for how to resolve this signature | [optional] 
**updated_at** | [**datetime**](DateTime.md) | ISO 8601 timestamp when the resource was last updated | [optional] 
**risk_level** | **str** | The risk-level of the problem identified by the signature. Valid values are Low, Medium, High | [optional] 
**external_account** | [**ExternalAccount**](ExternalAccount.md) | Associated External Account | [optional] 
**external_account_id** | **int** | Associated External Account Id | [optional] 
**region** | [**Region**](Region.md) | Associated Region | [optional] 
**region_id** | **int** | Associated Region Id | [optional] 
**signature** | [**Signature**](Signature.md) | Associated Signature | [optional] 
**signature_id** | **int** | Associated Signature Id | [optional] 
**custom_signature** | [**CustomSignature**](CustomSignature.md) | Associated Custom Signature | [optional] 
**custom_signature_id** | **int** | Associated Custom Signature Id | [optional] 
**suppression** | [**Suppression**](Suppression.md) | Associated Suppression | [optional] 
**suppression_id** | **int** | Associated Suppression Id | [optional] 
**metadata** | [**Metadata**](Metadata.md) | Associated Metadata | [optional] 
**metadata_id** | **int** | Associated Metadata Id | [optional] 
**cloud_trail_events** | [**list[CloudTrailEvent]**](CloudTrailEvent.md) | Associated Cloud Trail Events | [optional] 
**cloud_trail_event_ids** | **list[int]** | Associated Cloud Trail Events Ids | [optional] 
**tags** | [**list[Tag]**](Tag.md) | Associated Tags | [optional] 
**tag_ids** | **list[int]** | Associated Tags Ids | [optional] 
**compliance_controls** | [**list[ComplianceControl]**](ComplianceControl.md) | Associated Compliance Controls | [optional] 
**compliance_control_ids** | **list[int]** | Associated Compliance Controls Ids | [optional] 
**errors** | **list[str]** | Array of error messages if the request failed | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


