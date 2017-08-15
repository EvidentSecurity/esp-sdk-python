# esp_sdk.CloudTrailEventsApi

All URIs are relative to https://api.evident.io


Method | HTTP request | Description
------------- | ------------- | -------------
[**list**](CloudTrailEventsApi.md#list) | **GET** /api/v2/alerts/{alert_id}/cloud_trail_events.json_api | Get a list of Cloud Trail Events
[**show**](CloudTrailEventsApi.md#show) | **GET** /api/v2/cloud_trail_events/{id}.json_api | Show a single Cloud Trail Event


# **list**
> PaginatedCollection list(alert_id, page=page)

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
page = {'key': 'page_example'} # dict(str, str) | Page Number and Page Size.  Example: page: {number: 1, size: 20} (optional)

try: 
    # Get a list of Cloud Trail Events
    api_response = api_instance.list(alert_id, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudTrailEventsApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_id** | **int**| The ID of the alert to retrieve cloud trail events for | 
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
> CloudTrailEvent show(id)

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

try: 
    # Show a single Cloud Trail Event
    api_response = api_instance.show(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudTrailEventsApi->show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Cloud Trail Event Id | 

### Return type

[**CloudTrailEvent**](CloudTrailEvent.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json

 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

