# ComplianceControl

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique ID | [optional] 
**created_at** | [**datetime**](DateTime.md) | ISO 8601 timestamp when the resource was created | [optional] 
**name** | **str** | Name | [optional] 
**identifier** | **str** | The identifier of this control | [optional] 
**description** | **str** | The description for this control | [optional] 
**updated_at** | [**datetime**](DateTime.md) | ISO 8601 timestamp when the resource was updated | [optional] 
**position** | **int** | The position of this control within the Domain | [optional] 
**compliance_standard** | [**ComplianceStandard**](ComplianceStandard.md) | Associated Compliance Standard | [optional] 
**compliance_standard_id** | **int** | Associated Compliance Standard ID | [optional] 
**compliance_domain** | [**ComplianceDomain**](ComplianceDomain.md) | Associated Compliance Domain | [optional] 
**compliance_domain_id** | **int** | Associated Compliance Domain ID | [optional] 
**signatures** | [**list[Signature]**](Signature.md) | Associated Signatures | [optional] 
**signature_ids** | **list[int]** | Associated Signatures IDs | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


