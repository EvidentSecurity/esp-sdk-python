# esp_sdk.ContactRequestsApi

All URIs are relative to https://api.evident.io

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](ContactRequestsApi.md#create) | **POST** /api/v2/contact_requests.json_api | Create a(n) Contact Request


# **create**
> ContactRequest create(description, request_type, title, include=include)

Create a(n) Contact Request



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.ContactRequestsApi()
description = 'description_example' # str | Body of your message
request_type = 'request_type_example' # str | Type of contact request. Valid values are support, feature
title = 'title_example' # str | Subject of your message
include = 'include_example' # str | Related objects that can be included in the response:  user See Including Objects for more information. (optional)

try: 
    # Create a(n) Contact Request
    api_response = api_instance.create(description, request_type, title, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactRequestsApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **description** | **str**| Body of your message | 
 **request_type** | **str**| Type of contact request. Valid values are support, feature | 
 **title** | **str**| Subject of your message | 
 **include** | **str**| Related objects that can be included in the response:  user See Including Objects for more information. | [optional] 

### Return type

[**ContactRequest**](ContactRequest.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

