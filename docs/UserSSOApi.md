# esp_sdk.UserSSOApi

All URIs are relative to *http://localhost/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](UserSSOApi.md#create) | **POST** /api/v2/users/sso.json_api | This endpoint is used to create a ESP JWT based on a Ping SSO token
[**error**](UserSSOApi.md#error) | **PATCH** /api/v2/users/sso/error.json_api | Displays a SAML error
[**show**](UserSSOApi.md#show) | **GET** /api/v2/users/sso.json_api | A successful call to this API redirects to the sso_url of the organization associated with a user.


# **create**
> UserJWT create(ping_token)

This endpoint is used to create a ESP JWT based on a Ping SSO token

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.UserSSOApi()
ping_token = 'ping_token_example' # str | The Ping SSO token to identify the user

try: 
    # This endpoint is used to create a ESP JWT based on a Ping SSO token
    api_response = api_instance.create(ping_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserSSOApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ping_token** | **str**| The Ping SSO token to identify the user | 

### Return type

[**UserJWT**](UserJWT.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **error**
> error()

Displays a SAML error

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.UserSSOApi()

try: 
    # Displays a SAML error
    api_instance.error()
except ApiException as e:
    print("Exception when calling UserSSOApi->error: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show**
> show(email)

A successful call to this API redirects to the sso_url of the organization associated with a user.

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.UserSSOApi()
email = 'email_example' # str | The email of the User associated with the Organization to show the sso_url for

try: 
    # A successful call to this API redirects to the sso_url of the organization associated with a user.
    api_instance.show(email)
except ApiException as e:
    print("Exception when calling UserSSOApi->show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| The email of the User associated with the Organization to show the sso_url for | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

