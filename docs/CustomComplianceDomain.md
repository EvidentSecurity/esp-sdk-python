# CustomComplianceDomain

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique ID | [optional] 
**identifier** | **str** | The identifier of this custom domain | [optional] 
**name** | **str** | Name | [optional] 
**created_at** | [**datetime**](DateTime.md) | ISO 8601 timestamp when the resource was created | [optional] 
**updated_at** | [**datetime**](DateTime.md) | ISO 8601 timestamp when the resource was updated | [optional] 
**position** | **int** | The position of this custom domain within the custom standard | [optional] 
**custom_compliance_standard** | [**CustomComplianceStandard**](CustomComplianceStandard.md) | Associated Custom Compliance Standard | [optional] 
**custom_compliance_standard_id** | **int** | Associated Custom Compliance Standard ID | [optional] 
**custom_compliance_controls** | [**list[CustomComplianceControl]**](CustomComplianceControl.md) | Associated Custom Compliance Controls | [optional] 
**custom_compliance_control_ids** | **list[int]** | Associated Custom Compliance Controls IDs | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


