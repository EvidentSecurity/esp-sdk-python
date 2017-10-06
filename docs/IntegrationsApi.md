# esp_sdk.IntegrationsApi

All URIs are relative to https://api.evident.io

Method | HTTP request | Description
------------- | ------------- | -------------
[**show**](IntegrationsApi.md#show) | **GET** /api/v2/integrations/{id}.json_api | Show a single Integration


# **show**
> Integration show(id, include=include)

Show a single Integration

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.IntegrationsApi()
id = 56 # int | Integration ID
include = 'include_example' # str | Related objects that can be included in the response.  See Including Objects for more information. (optional)

try: 
    # Show a single Integration
    api_response = api_instance.show(id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Integration ID | 
 **include** | **str**| Related objects that can be included in the response.  See Including Objects for more information. | [optional] 

### Return type

[**Integration**](Integration.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

