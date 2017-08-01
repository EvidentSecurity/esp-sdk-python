# esp_sdk.RegionSuppressionsApi

All URIs are relative to *http://localhost/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_region_suppression**](RegionSuppressionsApi.md#create_region_suppression) | **POST** /api/v2/suppressions/regions.json_api | A successful call to this API creates a new region suppression for the supplied regions . The body of the request must contain a json api compliant hash of attributes with type suppression/regions.


# **create_region_suppression**
> create_region_suppression(regions, external_account_ids, reason, resource)

A successful call to this API creates a new region suppression for the supplied regions . The body of the request must contain a json api compliant hash of attributes with type suppression/regions.

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.RegionSuppressionsApi()
regions = ['regions_example'] # list[str] | An array of region names to suppress
external_account_ids = [56] # list[int] | An Array of the external accounts identified by external_account_id to suppress the signature or custom signature on
reason = 'reason_example' # str | The reason for creating the suppression
resource = 'resource_example' # str | The resource string this suppression will suppress alerts for

try: 
    # A successful call to this API creates a new region suppression for the supplied regions . The body of the request must contain a json api compliant hash of attributes with type suppression/regions.
    api_instance.create_region_suppression(regions, external_account_ids, reason, resource)
except ApiException as e:
    print("Exception when calling RegionSuppressionsApi->create_region_suppression: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **regions** | [**list[str]**](str.md)| An array of region names to suppress | 
 **external_account_ids** | [**list[int]**](int.md)| An Array of the external accounts identified by external_account_id to suppress the signature or custom signature on | 
 **reason** | **str**| The reason for creating the suppression | 
 **resource** | **str**| The resource string this suppression will suppress alerts for | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

