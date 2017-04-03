# esp_sdk.DashboardApi

All URIs are relative to *http://localhost/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**recent**](DashboardApi.md#recent) | **GET** /api/v2/dashboard/recent.json_api | 


# **recent**
> PaginatedCollection recent(page=page)



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.DashboardApi()
page = {'key': 'page_example'} # dict(str, str) | Page Number (optional)

try: 
    api_response = api_instance.recent(page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardApi->recent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | [**dict(str, str)**](str.md)| Page Number | [optional] 

### Return type

[**PaginatedCollection**](PaginatedCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

