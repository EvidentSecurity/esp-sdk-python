# esp_sdk.UserPasswordsApi

All URIs are relative to *http://localhost/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](UserPasswordsApi.md#create) | **POST** /api/v2/users/passwords.json_api | A successful call to this API will send password reset instructions to the email provided
[**update**](UserPasswordsApi.md#update) | **PATCH** /api/v2/users/passwords.json_api | A successful call to this API changes a user&#39;s password


# **create**
> create(email)

A successful call to this API will send password reset instructions to the email provided

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.UserPasswordsApi()
email = 'email_example' # str | The email to send password reset instructions to

try: 
    # A successful call to this API will send password reset instructions to the email provided
    api_instance.create(email)
except ApiException as e:
    print("Exception when calling UserPasswordsApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| The email to send password reset instructions to | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> User update(password, password_confirmation, reset_password_token)

A successful call to this API changes a user's password

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.UserPasswordsApi()
password = 'password_example' # str | The new password for the user
password_confirmation = 'password_confirmation_example' # str | The new password confirmation for the user
reset_password_token = 'reset_password_token_example' # str | The token generated with the Password Reset request

try: 
    # A successful call to this API changes a user's password
    api_response = api_instance.update(password, password_confirmation, reset_password_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserPasswordsApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **password** | **str**| The new password for the user | 
 **password_confirmation** | **str**| The new password confirmation for the user | 
 **reset_password_token** | **str**| The token generated with the Password Reset request | 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

