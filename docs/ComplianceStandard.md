# ComplianceStandard

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique ID | [optional] 
**name** | **str** | Name | [optional] 
**created_at** | [**datetime**](DateTime.md) | ISO 8601 timestamp when the resource was created | [optional] 
**description** | **str** | The description for this Compliance Standard | [optional] 
**updated_at** | [**datetime**](DateTime.md) | ISO 8601 timestamp when the resource was updated | [optional] 
**max_accounts** | **int** | The max number of external accounts allowed for the organization.  This is only returned by the organizations/:organization_id/compliance_standards endpoint. | [optional] 
**compliance_domains** | [**list[ComplianceDomain]**](ComplianceDomain.md) | Associated Compliance Domains | [optional] 
**compliance_domain_ids** | **list[int]** | Associated Compliance Domains IDs | [optional] 
**compliance_controls** | [**list[ComplianceControl]**](ComplianceControl.md) | Associated Compliance Controls | [optional] 
**compliance_control_ids** | **list[int]** | Associated Compliance Controls IDs | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


