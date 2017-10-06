# esp_sdk.ContactRequestsApi

All URIs are relative to https://api.evident.io

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](ContactRequestsApi.md#create) | **POST** /api/v2/contact_requests.json_api | Create a(n) ContactRequest


# **create**
> ContactRequest create(title, description, request_type)

Create a(n) ContactRequest

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.ContactRequestsApi()
title = 'title_example' # str | Subject of your message
description = 'description_example' # str | Body of your message
request_type = 'request_type_example' # str | Type of contact request. Valid values are support, feature

try: 
    # Create a(n) ContactRequest
    api_response = api_instance.create(title, description, request_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactRequestsApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **title** | **str**| Subject of your message | 
 **description** | **str**| Body of your message | 
 **request_type** | **str**| Type of contact request. Valid values are support, feature | 

### Return type

[**ContactRequest**](ContactRequest.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

