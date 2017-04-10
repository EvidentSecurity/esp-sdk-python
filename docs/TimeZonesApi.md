# esp_sdk.TimeZonesApi

All URIs are relative to *http://localhost/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list**](TimeZonesApi.md#list) | **GET** /api/v2/time_zones.json_api | A successful call to this API returns a list of time zones.


# **list**
> list[TimeZone] list()

A successful call to this API returns a list of time zones.

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.TimeZonesApi()

try: 
    # A successful call to this API returns a list of time zones.
    api_response = api_instance.list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeZonesApi->list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[TimeZone]**](TimeZone.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

