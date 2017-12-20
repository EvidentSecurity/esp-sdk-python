# esp_sdk.MetadataApi

All URIs are relative to https://api.evident.io

Method | HTTP request | Description
------------- | ------------- | -------------
[**for_alert**](MetadataApi.md#for_alert) | **GET** /api/v2/alerts/{alert_id}/metadata.json_api | Show the metadata for an alert
[**show**](MetadataApi.md#show) | **GET** /api/v2/metadata/{id}.json_api | Show a single Metadata


# **for_alert**
> Metadata for_alert(alert_id, include=include)

Show the metadata for an alert



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.MetadataApi()
alert_id = 56 # int | Alert Id
include = 'include_example' # str | Related objects that can be included in the response:   See Including Objects for more information. (optional)

try: 
    # Show the metadata for an alert
    api_response = api_instance.for_alert(alert_id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->for_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_id** | **int**| Alert Id | 
 **include** | **str**| Related objects that can be included in the response:   See Including Objects for more information. | [optional] 

### Return type

[**Metadata**](Metadata.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show**
> Metadata show(id, include=include)

Show a single Metadata



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.MetadataApi()
id = 56 # int | Metadata ID
include = 'include_example' # str | Related objects that can be included in the response:   See Including Objects for more information. (optional)

try: 
    # Show a single Metadata
    api_response = api_instance.show(id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Metadata ID | 
 **include** | **str**| Related objects that can be included in the response:   See Including Objects for more information. | [optional] 

### Return type

[**Metadata**](Metadata.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

