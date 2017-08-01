# esp_sdk.MetadataApi

All URIs are relative to *http://localhost/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**for_alert**](MetadataApi.md#for_alert) | **GET** /api/v2/alerts/{alert_id}/metadata.json_api | Show the metadata for an alert
[**show**](MetadataApi.md#show) | **GET** /api/v2/metadata/{id}.json_api | Show a single Metadata


# **for_alert**
> Metadata for_alert(alert_id)

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

try: 
    # Show the metadata for an alert
    api_response = api_instance.for_alert(alert_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->for_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_id** | **int**| Alert Id | 

### Return type

[**Metadata**](Metadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show**
> Metadata show(id)

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
id = 56 # int | Metadata Id

try: 
    # Show a single Metadata
    api_response = api_instance.show(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Metadata Id | 

### Return type

[**Metadata**](Metadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

