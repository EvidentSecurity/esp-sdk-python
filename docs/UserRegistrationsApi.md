# esp_sdk.UserRegistrationsApi

All URIs are relative to *http://localhost/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](UserRegistrationsApi.md#create) | **POST** /api/v2/users/registrations.json_api | A successful call to this API creates a new user


# **create**
> User create(email, first_name, last_name, phone, password, password_confirmation, captcha, organization_attributes)

A successful call to this API creates a new user

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.UserRegistrationsApi()
email = 'email_example' # str | The Email of the new user
first_name = 'first_name_example' # str | The new user's first name
last_name = 'last_name_example' # str | The new user's last name
phone = 'phone_example' # str | The new user's phone number
password = 'password_example' # str | The password for the new user
password_confirmation = 'password_confirmation_example' # str | The password confirmation for the new user
captcha = 'captcha_example' # str | The submitted captcha information for the form
organization_attributes = {'key': 'organization_attributes_example'} # dict(str, str) | The attributes of the Organization the new user is joining

try: 
    # A successful call to this API creates a new user
    api_response = api_instance.create(email, first_name, last_name, phone, password, password_confirmation, captcha, organization_attributes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserRegistrationsApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| The Email of the new user | 
 **first_name** | **str**| The new user&#39;s first name | 
 **last_name** | **str**| The new user&#39;s last name | 
 **phone** | **str**| The new user&#39;s phone number | 
 **password** | **str**| The password for the new user | 
 **password_confirmation** | **str**| The password confirmation for the new user | 
 **captcha** | **str**| The submitted captcha information for the form | 
 **organization_attributes** | [**dict(str, str)**](str.md)| The attributes of the Organization the new user is joining | 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

