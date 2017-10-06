# esp_sdk.OrganizationsApi

All URIs are relative to https://api.evident.io

Method | HTTP request | Description
------------- | ------------- | -------------
[**list**](OrganizationsApi.md#list) | **PUT** /api/v2/organizations.json_api | Get a list of Organizations
[**show**](OrganizationsApi.md#show) | **GET** /api/v2/organizations/{id}.json_api | Show a single Organization
[**update**](OrganizationsApi.md#update) | **PATCH** /api/v2/organizations/{id}.json_api | Update a(n) Organization


# **list**
> PaginatedCollection list(filter=filter, include=include, page=page)

Get a list of Organizations

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.OrganizationsApi()
filter = {'key': 'filter_example'} # dict(str, str) | Filter Params for Searching.  See Searching Lists for more information. (optional)
include = 'include_example' # str | Related objects that can be included in the response.  See Including Objects for more information. (optional)
page = '{:number=>1,+:size=>20}' # str | Page Number and Page Size.  number is the page number of the collection to return, size is the number of items to return per page (optional) (default to {:number=>1,+:size=>20})

try: 
    # Get a list of Organizations
    api_response = api_instance.list(filter=filter, include=include, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | [**dict(str, str)**](str.md)| Filter Params for Searching.  See Searching Lists for more information. | [optional] 
 **include** | **str**| Related objects that can be included in the response.  See Including Objects for more information. | [optional] 
 **page** | **str**| Page Number and Page Size.  number is the page number of the collection to return, size is the number of items to return per page | [optional] [default to {:number&#x3D;&gt;1,+:size&#x3D;&gt;20}]

### Return type

[**PaginatedCollection**](PaginatedCollection.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show**
> Organization show(id, include=include)

Show a single Organization

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.OrganizationsApi()
id = 56 # int | Organization ID
include = 'include_example' # str | Related objects that can be included in the response.  See Including Objects for more information. (optional)

try: 
    # Show a single Organization
    api_response = api_instance.show(id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Organization ID | 
 **include** | **str**| Related objects that can be included in the response.  See Including Objects for more information. | [optional] 

### Return type

[**Organization**](Organization.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> Organization update(id, name)

Update a(n) Organization

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.OrganizationsApi()
id = 56 # int | Organization ID
name = 'name_example' # str | Name of the organization

try: 
    # Update a(n) Organization
    api_response = api_instance.update(id, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Organization ID | 
 **name** | **str**| Name of the organization | 

### Return type

[**Organization**](Organization.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

