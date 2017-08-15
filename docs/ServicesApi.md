# esp_sdk.ServicesApi

All URIs are relative to https://api.evident.io

Method | HTTP request | Description
------------- | ------------- | -------------
[**list**](ServicesApi.md#list) | **PUT** /api/v2/services.json_api | Get a list of Services
[**show**](ServicesApi.md#show) | **GET** /api/v2/services/{id}.json_api | Show a single Service


# **list**
> PaginatedCollection list(filter=filter, page=page)

Get a list of Services

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.ServicesApi()
filter = {'key': 'filter_example'} # dict(str, str) | Filter Params for Searching.  Equality Searchable Attributes: [id, name, policy_name] Matching Searchable Attributes: [name, policy_name] Limited Searchable Attribute: [provider_eq]   Example: filter: {name_eq: 'Bob'} (optional)
page = {'key': 'page_example'} # dict(str, str) | Page Number and Page Size.  Example: page: {number: 1, size: 20} (optional)

try: 
    # Get a list of Services
    api_response = api_instance.list(filter=filter, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServicesApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | [**dict(str, str)**](str.md)| Filter Params for Searching.  Equality Searchable Attributes: [id, name, policy_name] Matching Searchable Attributes: [name, policy_name] Limited Searchable Attribute: [provider_eq]   Example: filter: {name_eq: &#39;Bob&#39;} | [optional] 
 **page** | [**dict(str, str)**](str.md)| Page Number and Page Size.  Example: page: {number: 1, size: 20} | [optional] 

### Return type

[**PaginatedCollection**](PaginatedCollection.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show**
> Service show(id)

Show a single Service

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.ServicesApi()
id = 56 # int | Service Id

try: 
    # Show a single Service
    api_response = api_instance.show(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServicesApi->show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Service Id | 

### Return type

[**Service**](Service.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

