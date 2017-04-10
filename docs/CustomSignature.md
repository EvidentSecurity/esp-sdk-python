# CustomSignature

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**relationships** | **object** | Links to Associated Objects | [optional] 
**errors** | **list[str]** | Array of error messages if the request failed | [optional] 
**id** | **int** | Unique ID | [optional] 
**created_at** | [**datetime**](DateTime.md) | ISO 8601 timestamp when the resource was created | [optional] 
**description** | **str** | The description of the custom signature | [optional] 
**identifier** | **str** | The identifier of the custom signature | [optional] 
**name** | **str** | The name of the custom signature | [optional] 
**resolution** | **str** | Details for how to resolve this custom signature | [optional] 
**risk_level** | **str** | The risk-level of the problem identified by the custom signature. Valid values are Low, Medium, High | [optional] 
**updated_at** | [**datetime**](DateTime.md) | ISO 8601 timestamp when the resource was last updated | [optional] 
**organization** | [**Organization**](Organization.md) | Associated Organization | [optional] 
**organization_id** | **int** | Associated Organization Id | [optional] 
**teams** | [**list[Team]**](Team.md) | Associated Teams | [optional] 
**team_ids** | **list[int]** | Associated Team Ids | [optional] 
**definitions** | [**list[CustomSignatureDefinition]**](CustomSignatureDefinition.md) | Associated Custom Signature Definitions | [optional] 
**definition_ids** | **list[int]** | Associated Custom Signature Definition Ids | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


