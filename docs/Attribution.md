# Attribution

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique ID | [optional] 
**event_id** | **int** | GUID to uniquely identify each event | [optional] 
**event_name** | **str** | The requested action, which is one of the actions listed in the API Reference for the service | [optional] 
**event_time** | [**datetime**](DateTime.md) | ISO 8601 timestamp when the event occurred | [optional] 
**raw_event** | **object** | The event as it is sent in | [optional] 
**user** | **str** | The user associated with the event | [optional] 
**ip_address** | **str** | The apparent IP address that the request was made from for the given event | [optional] 
**scope_name** | **str** | The agent through which the request was made, such as the AWS Management Console or an AWS SDK | [optional] 
**alert** | [**Alert**](Alert.md) | Associated Alert | [optional] 
**alert_id** | **int** | Associated Alert ID | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


