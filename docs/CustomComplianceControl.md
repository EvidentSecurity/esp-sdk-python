# CustomComplianceControl

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique ID | [optional] 
**name** | **str** | Name | [optional] 
**identifier** | **str** | The identifier of this custom control | [optional] 
**description** | **str** | The description for this custom control | [optional] 
**created_at** | [**datetime**](DateTime.md) | ISO 8601 timestamp when the resource was created | [optional] 
**updated_at** | [**datetime**](DateTime.md) | ISO 8601 timestamp when the resource was updated | [optional] 
**position** | **int** | The position of this custom control within the custom domain | [optional] 
**custom_compliance_standard** | [**CustomComplianceStandard**](CustomComplianceStandard.md) | Associated Custom Compliance Standard | [optional] 
**custom_compliance_standard_id** | **int** | Associated Custom Compliance Standard ID | [optional] 
**custom_compliance_domain** | [**CustomComplianceDomain**](CustomComplianceDomain.md) | Associated Custom Compliance Domain | [optional] 
**custom_compliance_domain_id** | **int** | Associated Custom Compliance Domain ID | [optional] 
**signatures** | [**list[Signature]**](Signature.md) | Associated Signatures | [optional] 
**signature_ids** | **list[int]** | Associated Signatures IDs | [optional] 
**custom_signatures** | [**list[CustomSignature]**](CustomSignature.md) | Associated Custom Signatures | [optional] 
**custom_signature_ids** | **list[int]** | Associated Custom Signatures IDs | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


