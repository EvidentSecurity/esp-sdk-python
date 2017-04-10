# Service

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**relationships** | **object** | Links to Associated Objects | [optional] 
**errors** | **list[str]** | Array of error messages if the request failed | [optional] 
**id** | **int** | Unique ID | [optional] 
**code** | **str** | The code associated with this service | [optional] 
**created_at** | [**datetime**](DateTime.md) | ISO 8601 timestamp when the resource was created | [optional] 
**default_interval** | **int** | Default interval used for scans if a scan interval was not created | [optional] 
**minimum_interval** | **int** | Minimum interval allowed for scans on this service | [optional] 
**name** | **str** | The name of the service | [optional] 
**policy_name** | **str** | The policy name of the service. This matches the namespace set by Amazon here | [optional] 
**updated_at** | [**datetime**](DateTime.md) | ISO 8601 timestamp when the resource was last updated | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


