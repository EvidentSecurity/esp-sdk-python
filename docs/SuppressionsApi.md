# esp_sdk.SuppressionsApi

All URIs are relative to *http://localhost/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deactivate**](SuppressionsApi.md#deactivate) | **PATCH** /api/v2/suppressions/{id}/deactivate.json_api | A successful call to this API will deactivate a suppression identified by the id parameter.
[**list**](SuppressionsApi.md#list) | **PUT** /api/v2/suppressions.json_api | Get a list of Suppressions
[**show**](SuppressionsApi.md#show) | **GET** /api/v2/suppressions/{id}.json_api | Show a single Suppression


# **deactivate**
> Suppression deactivate(id)

A successful call to this API will deactivate a suppression identified by the id parameter.

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.SuppressionsApi()
id = 56 # int | Suppression Id

try: 
    # A successful call to this API will deactivate a suppression identified by the id parameter.
    api_response = api_instance.deactivate(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SuppressionsApi->deactivate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Suppression Id | 

### Return type

[**Suppression**](Suppression.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> PaginatedCollection list(page=page, filter=filter, include=include)

Get a list of Suppressions

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.SuppressionsApi()
page = {'key': 'page_example'} # dict(str, str) | Page Number (optional)
filter = {'key': 'filter_example'} # dict(str, str) | Filter Params for Searching (optional)
include = 'include_example' # str | Included Objects (optional)

try: 
    # Get a list of Suppressions
    api_response = api_instance.list(page=page, filter=filter, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SuppressionsApi->list: %s\n" % e)
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
> Suppression show(id, include=include)

Show a single Suppression

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.SuppressionsApi()
id = 56 # int | Suppression Id
include = 'include_example' # str | Included Objects (optional)

try: 
    # Show a single Suppression
    api_response = api_instance.show(id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SuppressionsApi->show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Suppression Id | 
 **include** | **str**| Included Objects | [optional] 

### Return type

[**Suppression**](Suppression.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

