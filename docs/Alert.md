# Alert

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique ID | [optional] 
**created_at** | [**datetime**](DateTime.md) | ISO 8601 timestamp when the resource was created | [optional] 
**status** | **str** | Status of the alert. Valid values are fail, warn, error, pass, info | [optional] 
**risk_level** | **str** | The risk-level of the problem identified by the signature or custom signature. Valid values are low, medium, high | [optional] 
**resource** | **str** | Resource identifier in Amazon | [optional] 
**ended_reason** | **str** | The reason this alert ended. Valid values are from_api, new_alert, from_scan, not_present_after_scan, signature_deleted, custom_signature_deleted, suppression_created, suppression_deactivated, custom_risk_level_created, custom_risk_level_deleted | [optional] 
**replaced_by_id** | **int** | The ID of the alert that replaced this alert | [optional] 
**replaced_by_status** | **str** | The status of the alert that replaced this alert | [optional] 
**updated_at** | [**datetime**](DateTime.md) | ISO 8601 timestamp when the resource was updated | [optional] 
**started_at** | [**datetime**](DateTime.md) | ISO 8601 timestamp when the alert started being active | [optional] 
**ended_at** | [**datetime**](DateTime.md) | ISO 8601 timestamp when the alert stopped being active | [optional] 
**external_account** | [**ExternalAccount**](ExternalAccount.md) | Associated External Account | [optional] 
**external_account_id** | **int** | Associated External Account ID | [optional] 
**region** | [**Region**](Region.md) | Associated Region | [optional] 
**region_id** | **int** | Associated Region ID | [optional] 
**signature** | [**Signature**](Signature.md) | Associated Signature | [optional] 
**signature_id** | **int** | Associated Signature ID | [optional] 
**custom_signature** | [**CustomSignature**](CustomSignature.md) | Associated Custom Signature | [optional] 
**custom_signature_id** | **int** | Associated Custom Signature ID | [optional] 
**suppression** | [**Suppression**](Suppression.md) | Associated Suppression | [optional] 
**suppression_id** | **int** | Associated Suppression ID | [optional] 
**metadata** | [**Metadata**](Metadata.md) | Associated Metadata | [optional] 
**attribution** | [**Attribution**](Attribution.md) | Associated Attribution | [optional] 
**tags** | [**list[Tag]**](Tag.md) | Associated Tags | [optional] 
**compliance_controls** | [**list[ComplianceControl]**](ComplianceControl.md) | Associated Compliance Controls | [optional] 
**custom_compliance_controls** | [**list[CustomComplianceControl]**](CustomComplianceControl.md) | Associated Custom Compliance Controls | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


