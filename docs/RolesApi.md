# esp_sdk.RolesApi

All URIs are relative to *http://localhost/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list**](RolesApi.md#list) | **GET** /api/v2/roles.json_api | Get a list of Roles
[**show**](RolesApi.md#show) | **GET** /api/v2/roles/{id}.json_api | Show a single Role


# **list**
> PaginatedCollection list(page=page, filter=filter, include=include)

Get a list of Roles

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.RolesApi()
page = {'key': 'page_example'} # dict(str, str) | Page Number (optional)
filter = {'key': 'filter_example'} # dict(str, str) | Filter Params for Searching (optional)
include = 'include_example' # str | Included Objects (optional)

try: 
    # Get a list of Roles
    api_response = api_instance.list(page=page, filter=filter, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | [**dict(str, str)**](str.md)| Page Number | [optional] 
 **filter** | [**dict(str, str)**](str.md)| Filter Params for Searching | [optional] 
 **include** | **str**| Included Objects | [optional] 

### Return type

[**PaginatedCollection**](PaginatedCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show**
> Role show(id, include=include)

Show a single Role

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.RolesApi()
id = 56 # int | Role Id
include = 'include_example' # str | Included Objects (optional)

try: 
    # Show a single Role
    api_response = api_instance.show(id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Role Id | 
 **include** | **str**| Included Objects | [optional] 

### Return type

[**Role**](Role.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

