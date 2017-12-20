# Integration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique ID | [optional] 
**created_at** | [**datetime**](DateTime.md) | ISO 8601 timestamp when the resource was created | [optional] 
**updated_at** | [**datetime**](DateTime.md) | ISO 8601 timestamp when the resource was updated | [optional] 
**state** | **str** | The state the integration is in. Valid values are setup, active, error, disabled | [optional] 
**statuses** | **list[str]** | Only send alerts that have the status in this list. Valid values are fail, warn, error, pass, info | [optional] 
**name** | **str** | Name of the integration | [optional] 
**all_high_risk** | **bool** | Send all high risk alerts | [optional] 
**all_medium_risk** | **bool** | Send all medium risk alerts | [optional] 
**all_low_risk** | **bool** | Send all low risk alerts | [optional] 
**send_updates** | **bool** | This feature enables the integration to send alerts when they are updated. When disabled, alerts will only be sent when they are initially created. When enabled, alerts will additionally be sent when a change is made such as the alert ending. An alert may end for multiple reasons. | [optional] 
**error_messages** | **list[str]** | Array of error messages | [optional] 
**last_throttled_at** | [**datetime**](DateTime.md) | The time at which this integration was last throttled. | [optional] 
**send_when_suppressed** | **bool** | Send notifications for suppressed alerts | [optional] 
**organization** | [**Organization**](Organization.md) | Associated Organization | [optional] 
**organization_id** | **int** | Associated Organization ID | [optional] 
**creator** | [**User**](User.md) | Associated Creator | [optional] 
**creator_id** | **int** | Associated Creator ID | [optional] 
**service** | [**Service**](Service.md) | Associated Service | [optional] 
**service_id** | **int** | Associated Service ID | [optional] 
**external_accounts** | [**list[ExternalAccount]**](ExternalAccount.md) | Associated External Accounts | [optional] 
**external_account_ids** | **list[int]** | Associated External Accounts IDs | [optional] 
**signatures** | [**list[Signature]**](Signature.md) | Associated Signatures | [optional] 
**signature_ids** | **list[int]** | Associated Signatures IDs | [optional] 
**custom_signatures** | [**list[CustomSignature]**](CustomSignature.md) | Associated Custom Signatures | [optional] 
**custom_signature_ids** | **list[int]** | Associated Custom Signatures IDs | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


