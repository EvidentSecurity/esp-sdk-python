# esp_sdk.StatServicesApi

All URIs are relative to https://api.evident.io

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_for_stat**](StatServicesApi.md#list_for_stat) | **GET** /api/v2/stats/{stat_id}/services.json_api | Get a list of stats for services
[**show**](StatServicesApi.md#show) | **GET** /api/v2/stats/services/{id}.json_api | Show a single Stat Service


# **list_for_stat**
> PaginatedCollection list_for_stat(stat_id, page=page, include=include)

Get a list of stats for services

A successful call to this API returns all the stats of all the services for a report identified by the stat_id parameter. Said report contains all statistics for this alert triggered from services contained in all services for the selected hour.

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.StatServicesApi()
stat_id = 56 # int | The ID of the stat to retrieve service stats for
page = '{:number=>1,+:size=>20}' # str | Page Number and Page Size.  number is the page number of the collection to return, size is the number of items to return per page (optional) (default to {:number=>1,+:size=>20})
include = 'include_example' # str | Related objects that can be included in the response:  service, stat See Including Objects for more information. (optional)

try: 
    # Get a list of stats for services
    api_response = api_instance.list_for_stat(stat_id, page=page, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatServicesApi->list_for_stat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stat_id** | **int**| The ID of the stat to retrieve service stats for | 
 **page** | **str**| Page Number and Page Size.  number is the page number of the collection to return, size is the number of items to return per page | [optional] [default to {:number&#x3D;&gt;1,+:size&#x3D;&gt;20}]
 **include** | **str**| Related objects that can be included in the response:  service, stat See Including Objects for more information. | [optional] 

### Return type

[**PaginatedCollection**](PaginatedCollection.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show**
> StatService show(id, include=include)

Show a single Stat Service



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.StatServicesApi()
id = 56 # int | Stat Service ID
include = 'include_example' # str | Related objects that can be included in the response:  service, stat See Including Objects for more information. (optional)

try: 
    # Show a single Stat Service
    api_response = api_instance.show(id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatServicesApi->show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Stat Service ID | 
 **include** | **str**| Related objects that can be included in the response:  service, stat See Including Objects for more information. | [optional] 

### Return type

[**StatService**](StatService.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

