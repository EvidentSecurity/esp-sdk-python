# esp_sdk.UserTokensApi

All URIs are relative to *http://localhost/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](UserTokensApi.md#create) | **POST** /api/v2/users/tokens.json_api | This endpoint creates a token for a user
[**update**](UserTokensApi.md#update) | **PATCH** /api/v2/users/tokens.json_api | A successful call to this API updates and accepts a User Invitation


# **create**
> UserJWT create(user)

This endpoint creates a token for a user

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.UserTokensApi()
user = esp_sdk.Object() # Object | The user object to create a token for

try: 
    # This endpoint creates a token for a user
    api_response = api_instance.create(user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserTokensApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | [**Object**](.md)| The user object to create a token for | 

### Return type

[**UserJWT**](UserJWT.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> User update(authorization)

A successful call to this API updates and accepts a User Invitation

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.UserTokensApi()
authorization = 'authorization_example' # str | The token of the user to authenticate

try: 
    # A successful call to this API updates and accepts a User Invitation
    api_response = api_instance.update(authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserTokensApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| The token of the user to authenticate | 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

