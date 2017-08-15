# esp_sdk.RegionsApi

All URIs are relative to https://api.evident.io

Method | HTTP request | Description
------------- | ------------- | -------------
[**list**](RegionsApi.md#list) | **PUT** /api/v2/regions.json_api | Get a list of Regions
[**show**](RegionsApi.md#show) | **GET** /api/v2/regions/{id}.json_api | Show a single Region


# **list**
> PaginatedCollection list(filter=filter, page=page)

Get a list of Regions

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.RegionsApi()
filter = {'key': 'filter_example'} # dict(str, str) | Filter Params for Searching.  Equality Searchable Attributes: [id, code] Matching Searchable Attribute: [code] Limited Searchable Attribute: [provider_eq]  Searchable Association: [suppressions] See the filter parameter of the association's list action to see what attributes are searchable on each association. See Searching on Relationships for more information. See Searching Lists for more information. Example: filter: {name_eq: 'Bob'} (optional)
page = {'key': 'page_example'} # dict(str, str) | Page Number and Page Size.  Example: page: {number: 1, size: 20} (optional)

try: 
    # Get a list of Regions
    api_response = api_instance.list(filter=filter, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegionsApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | [**dict(str, str)**](str.md)| Filter Params for Searching.  Equality Searchable Attributes: [id, code] Matching Searchable Attribute: [code] Limited Searchable Attribute: [provider_eq]  Searchable Association: [suppressions] See the filter parameter of the association&#39;s list action to see what attributes are searchable on each association. See Searching on Relationships for more information. See Searching Lists for more information. Example: filter: {name_eq: &#39;Bob&#39;} | [optional] 
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
> Region show(id)

Show a single Region

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.RegionsApi()
id = 56 # int | Region Id

try: 
    # Show a single Region
    api_response = api_instance.show(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegionsApi->show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Region Id | 

### Return type

[**Region**](Region.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

