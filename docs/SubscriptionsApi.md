# esp_sdk.SubscriptionsApi

All URIs are relative to https://api.evident.io

Method | HTTP request | Description
------------- | ------------- | -------------
[**show**](SubscriptionsApi.md#show) | **GET** /api/v2/subscriptions/{id}.json_api | Show a single Subscription


# **show**
> Subscription show(id, include=include)

Show a single Subscription



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.SubscriptionsApi()
id = 56 # int | Subscription ID
include = 'include_example' # str | Related objects that can be included in the response:  organization, plan See Including Objects for more information. (optional)

try: 
    # Show a single Subscription
    api_response = api_instance.show(id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Subscription ID | 
 **include** | **str**| Related objects that can be included in the response:  organization, plan See Including Objects for more information. | [optional] 

### Return type

[**Subscription**](Subscription.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

