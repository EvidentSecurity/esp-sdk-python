# esp_sdk.AttributionApi

All URIs are relative to https://api.evident.io

Method | HTTP request | Description
------------- | ------------- | -------------
[**show**](AttributionApi.md#show) | **GET** /api/v2/alerts/{alert_id}/attribution.json_api | Show the attribution for an alert


# **show**
> Attribution show(alert_id, include=include)

Show the attribution for an alert



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.AttributionApi()
alert_id = 56 # int | The ID of the alert to retrieve user attribution for
include = 'include_example' # str | Related objects that can be included in the response:  alert See Including Objects for more information. (optional)

try: 
    # Show the attribution for an alert
    api_response = api_instance.show(alert_id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributionApi->show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_id** | **int**| The ID of the alert to retrieve user attribution for | 
 **include** | **str**| Related objects that can be included in the response:  alert See Including Objects for more information. | [optional] 

### Return type

[**Attribution**](Attribution.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

