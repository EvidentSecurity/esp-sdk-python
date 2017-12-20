# esp_sdk.TagsApi

All URIs are relative to https://api.evident.io

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_for_alert**](TagsApi.md#list_for_alert) | **GET** /api/v2/alerts/{alert_id}/tags.json_api | Get a list of Tags
[**show**](TagsApi.md#show) | **GET** /api/v2/tags/{id}.json_api | Show a single Tag


# **list_for_alert**
> PaginatedCollection list_for_alert(alert_id, page=page, include=include)

Get a list of Tags



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.TagsApi()
alert_id = 56 # int | The ID of the alert to list tags for
page = '{:number=>1,+:size=>20}' # str | Page Number and Page Size.  number is the page number of the collection to return, size is the number of items to return per page (optional) (default to {:number=>1,+:size=>20})
include = 'include_example' # str | Related objects that can be included in the response:   See Including Objects for more information. (optional)

try: 
    # Get a list of Tags
    api_response = api_instance.list_for_alert(alert_id, page=page, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->list_for_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_id** | **int**| The ID of the alert to list tags for | 
 **page** | **str**| Page Number and Page Size.  number is the page number of the collection to return, size is the number of items to return per page | [optional] [default to {:number&#x3D;&gt;1,+:size&#x3D;&gt;20}]
 **include** | **str**| Related objects that can be included in the response:   See Including Objects for more information. | [optional] 

### Return type

[**PaginatedCollection**](PaginatedCollection.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show**
> Tag show(id, include=include)

Show a single Tag



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.TagsApi()
id = 56 # int | Tag ID
include = 'include_example' # str | Related objects that can be included in the response:   See Including Objects for more information. (optional)

try: 
    # Show a single Tag
    api_response = api_instance.show(id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Tag ID | 
 **include** | **str**| Related objects that can be included in the response:   See Including Objects for more information. | [optional] 

### Return type

[**Tag**](Tag.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

