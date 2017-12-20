# Signature

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique ID | [optional] 
**created_at** | [**datetime**](DateTime.md) | ISO 8601 timestamp when the resource was created | [optional] 
**description** | **str** | The description of the signature | [optional] 
**identifier** | **str** | The identifier of the signature | [optional] 
**name** | **str** | The name of the signature | [optional] 
**resolution** | **str** | Details for how to resolve this signature | [optional] 
**risk_level** | **str** | The risk-level of the problem identified by the signature. Valid values are low, medium, high | [optional] 
**updated_at** | [**datetime**](DateTime.md) | ISO 8601 timestamp when the resource was updated | [optional] 
**custom_risk_level** | **str** | The custom risk-level of the problem identified by the signature for this external_account. Valid values are low, medium, high | [optional] 
**service** | [**Service**](Service.md) | Associated Service | [optional] 
**service_id** | **int** | Associated Service ID | [optional] 
**disabled_external_accounts** | [**ExternalAccount**](ExternalAccount.md) | Associated Disabled External Accounts | [optional] 
**disabled_external_accounts_id** | **int** | Associated Disabled External Accounts ID | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


