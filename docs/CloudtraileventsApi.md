# esp_sdk.CloudTrailEventsApi

All URIs are relative to *http://localhost/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list**](CloudTrailEventsApi.md#list) | **GET** /api/v2/alerts/{alert_id}/cloud_trail_events.json_api | Get a list of Cloud Trail Events
[**show**](CloudTrailEventsApi.md#show) | **GET** /api/v2/cloud_trail_events/{id}.json_api | Show a single Cloud Trail Event


# **list**
> PaginatedCollection list(alert_id, page=page, filter=filter, include=include)

Get a list of Cloud Trail Events

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.CloudTrailEventsApi()
alert_id = 56 # int | The ID of the alert to retrieve cloud trail events for
page = {'key': 'page_example'} # dict(str, str) | Page Number (optional)
filter = {'key': 'filter_example'} # dict(str, str) | Filter Params for Searching (optional)
include = 'include_example' # str | Included Objects (optional)

try: 
    # Get a list of Cloud Trail Events
    api_response = api_instance.list(alert_id, page=page, filter=filter, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudTrailEventsApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_id** | **int**| The ID of the alert to retrieve cloud trail events for | 
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
> CloudTrailEvent show(id, include=include)

Show a single Cloud Trail Event

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.CloudTrailEventsApi()
id = 56 # int | Cloud Trail Event Id
include = 'include_example' # str | Included Objects (optional)

try: 
    # Show a single Cloud Trail Event
    api_response = api_instance.show(id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudTrailEventsApi->show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Cloud Trail Event Id | 
 **include** | **str**| Included Objects | [optional] 

### Return type

[**CloudTrailEvent**](CloudTrailEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

