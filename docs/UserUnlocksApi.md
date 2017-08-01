# esp_sdk.UserUnlocksApi

All URIs are relative to *http://localhost/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](UserUnlocksApi.md#create) | **POST** /api/v2/users/unlocks.json_api | This endpoint sends unlock instructions to the email provided
[**show**](UserUnlocksApi.md#show) | **GET** /api/v2/users/unlocks.json_api | A successful call to this API will unlock the account with the generated unlock token


# **create**
> create(email)

This endpoint sends unlock instructions to the email provided

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.UserUnlocksApi()
email = 'email_example' # str | The email to send unlock instructions to

try: 
    # This endpoint sends unlock instructions to the email provided
    api_instance.create(email)
except ApiException as e:
    print("Exception when calling UserUnlocksApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| The email to send unlock instructions to | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show**
> User show(unlock_token)

A successful call to this API will unlock the account with the generated unlock token

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.UserUnlocksApi()
unlock_token = 'unlock_token_example' # str | The generated unlock token

try: 
    # A successful call to this API will unlock the account with the generated unlock token
    api_response = api_instance.show(unlock_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserUnlocksApi->show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unlock_token** | **str**| The generated unlock token | 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

