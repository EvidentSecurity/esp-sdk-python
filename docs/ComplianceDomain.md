# ComplianceDomain

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique ID | [optional] 
**created_at** | [**datetime**](DateTime.md) | Created At | [optional] 
**name** | **str** | Name | [optional] 
**identifier** | **str** | The identifier of this domain | [optional] 
**updated_at** | [**datetime**](DateTime.md) | Updated At | [optional] 
**position** | **int** | The position of this domain within the Standard | [optional] 
**compliance_standard** | [**ComplianceStandard**](ComplianceStandard.md) | Associated Compliance Standard | [optional] 
**compliance_standard_id** | **int** | Associated Compliance Standard Id | [optional] 
**compliance_controls** | [**list[ComplianceControl]**](ComplianceControl.md) | Associated Compliance Controls | [optional] 
**compliance_control_ids** | **list[int]** | Associated Compliance Controls Ids | [optional] 
**errors** | **list[str]** | Array of error messages if the request failed | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


