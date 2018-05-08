# ApiKey

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique ID | [optional] 
**access_id** | **str** | Access ID | [optional] 
**name** | **str** | The name of the API Key | [optional] 
**last_used_at** | [**datetime**](DateTime.md) | ISO 8601 timestamp when the key was last used | [optional] 
**created_at** | [**datetime**](DateTime.md) | ISO 8601 timestamp when the resource was created | [optional] 
**updated_at** | [**datetime**](DateTime.md) | ISO 8601 timestamp when the resource was updated | [optional] 
**secret_key** | **str** | Secret Key - This will only be returned once when the key is first created. | [optional] 
**user** | [**User**](User.md) | Associated User | [optional] 
**user_id** | **int** | Associated User ID | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


