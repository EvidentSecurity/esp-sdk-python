# ComplianceStandard

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique ID | [optional] 
**created_at** | [**datetime**](DateTime.md) | Created At | [optional] 
**name** | **str** | Name | [optional] 
**description** | **str** | The description for this Compliance Standard | [optional] 
**updated_at** | [**datetime**](DateTime.md) | Updated At | [optional] 
**compliance_domains** | [**list[ComplianceDomain]**](ComplianceDomain.md) | Associated Compliance Domains | [optional] 
**compliance_domain_ids** | **list[int]** | Associated Compliance Domains Ids | [optional] 
**compliance_controls** | [**list[ComplianceControl]**](ComplianceControl.md) | Associated Compliance Controls | [optional] 
**compliance_control_ids** | **list[int]** | Associated Compliance Controls Ids | [optional] 
**errors** | **list[str]** | Array of error messages if the request failed | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


