# Signature

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**relationships** | **object** | Links to Associated Objects | [optional] 
**errors** | **list[str]** | Array of error messages if the request failed | [optional] 
**id** | **int** | Unique Id | 
**created_at** | [**datetime**](DateTime.md) | ISO 8601 timestamp when the resource was created | [optional] 
**description** | **str** | The description of the signature | [optional] 
**identifier** | **str** | The identifier of the signature | [optional] 
**name** | **str** | The name of the signature | [optional] 
**resolution** | **str** | Details for how to resolve this signature | [optional] 
**risk_level** | **str** | The risk-level of the problem identified by the signature. Valid values are Low, Medium, High | [optional] 
**updated_at** | [**datetime**](DateTime.md) | ISO 8601 timestamp when the resource was last updated | [optional] 
**service** | [**Service**](Service.md) | Associated Service | [optional] 
**service_id** | **int** | Associated Service Id | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


