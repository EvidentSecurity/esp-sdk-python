# CustomComplianceStandard

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique ID | [optional] 
**organization_id** | **int** | The ID of the organization this custom compliance standard belongs to | [optional] 
**name** | **str** | Name | [optional] 
**created_at** | [**datetime**](DateTime.md) | ISO 8601 timestamp when the resource was created | [optional] 
**description** | **str** | The description for this Compliance Standard | [optional] 
**updated_at** | [**datetime**](DateTime.md) | ISO 8601 timestamp when the resource was updated | [optional] 
**max_accounts** | **int** | The maximum number of external accounts that can be added to the custom compliance standard | [optional] 
**max_domains** | **int** | The maximum number of custom compliance domains that can be added to the custom compliance standard | [optional] 
**max_controls** | **int** | The maximum number of custom compliance controls that can be added to the custom compliance standard | [optional] 
**custom_compliance_domains** | [**list[CustomComplianceDomain]**](CustomComplianceDomain.md) | Associated Custom Compliance Domains | [optional] 
**custom_compliance_domain_ids** | **list[int]** | Associated Custom Compliance Domains IDs | [optional] 
**custom_compliance_controls** | [**list[CustomComplianceControl]**](CustomComplianceControl.md) | Associated Custom Compliance Controls | [optional] 
**custom_compliance_control_ids** | **list[int]** | Associated Custom Compliance Controls IDs | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


