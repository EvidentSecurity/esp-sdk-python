# esp_sdk.StatCustomSignaturesApi

All URIs are relative to https://api.evident.io

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_for_stat**](StatCustomSignaturesApi.md#list_for_stat) | **GET** /api/v2/stats/{stat_id}/custom_signatures.json_api | Stats for custom signatures
[**show**](StatCustomSignaturesApi.md#show) | **GET** /api/v2/stats/custom_signatures/{id}.json_api | Show a single Stat Custom Signature


# **list_for_stat**
> PaginatedCollection list_for_stat(stat_id, page=page, include=include)

Stats for custom signatures

A successful call to this API returns all the stats of all the custom signatures for a report identified by the stat_id parameter. Said report contains all statistics for this alert triggered from signatures contained in all custom_signatures for the selected hour.

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.StatCustomSignaturesApi()
stat_id = 56 # int | The ID of the stat to retrieve custom signature stats for
page = '{:number=>1,+:size=>20}' # str | Page Number and Page Size.  number is the page number of the collection to return, size is the number of items to return per page (optional) (default to {:number=>1,+:size=>20})
include = 'include_example' # str | Related objects that can be included in the response:  custom_signature, stat See Including Objects for more information. (optional)

try: 
    # Stats for custom signatures
    api_response = api_instance.list_for_stat(stat_id, page=page, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatCustomSignaturesApi->list_for_stat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stat_id** | **int**| The ID of the stat to retrieve custom signature stats for | 
 **page** | **str**| Page Number and Page Size.  number is the page number of the collection to return, size is the number of items to return per page | [optional] [default to {:number&#x3D;&gt;1,+:size&#x3D;&gt;20}]
 **include** | **str**| Related objects that can be included in the response:  custom_signature, stat See Including Objects for more information. | [optional] 

### Return type

[**PaginatedCollection**](PaginatedCollection.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show**
> StatCustomSignature show(id, include=include)

Show a single Stat Custom Signature



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.StatCustomSignaturesApi()
id = 56 # int | Stat Custom Signature ID
include = 'include_example' # str | Related objects that can be included in the response:  custom_signature, stat See Including Objects for more information. (optional)

try: 
    # Show a single Stat Custom Signature
    api_response = api_instance.show(id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatCustomSignaturesApi->show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Stat Custom Signature ID | 
 **include** | **str**| Related objects that can be included in the response:  custom_signature, stat See Including Objects for more information. | [optional] 

### Return type

[**StatCustomSignature**](StatCustomSignature.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

