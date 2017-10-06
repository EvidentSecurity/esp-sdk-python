# ComplianceDomain

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique ID | [optional] 
**identifier** | **str** | The identifier of this domain | [optional] 
**name** | **str** | Name | [optional] 
**created_at** | [**datetime**](DateTime.md) | ISO 8601 timestamp when the resource was created | [optional] 
**updated_at** | [**datetime**](DateTime.md) | ISO 8601 timestamp when the resource was updated | [optional] 
**position** | **int** | The position of this domain within the Standard | [optional] 
**compliance_standard** | [**ComplianceStandard**](ComplianceStandard.md) | Associated Compliance Standard | [optional] 
**compliance_standard_id** | **int** | Associated Compliance Standard ID | [optional] 
**compliance_controls** | [**list[ComplianceControl]**](ComplianceControl.md) | Associated Compliance Controls | [optional] 
**compliance_control_ids** | **list[int]** | Associated Compliance Controls IDs | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


