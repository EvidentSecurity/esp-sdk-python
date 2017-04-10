# esp_sdk.RegionStatsApi

All URIs are relative to *http://localhost/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list**](RegionStatsApi.md#list) | **GET** /api/v2/stats/{stat_id}/regions.json_api | A successful call to this API returns all the stats of all the regions for a report identified by the stat_id parameter. Said report contains all statistics for this alert triggered from signatures contained in all regions for the selected hour.


# **list**
> PaginatedCollection list(stat_id)

A successful call to this API returns all the stats of all the regions for a report identified by the stat_id parameter. Said report contains all statistics for this alert triggered from signatures contained in all regions for the selected hour.

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.RegionStatsApi()
stat_id = 56 # int | The ID of the stat to retrieve region stats for

try: 
    # A successful call to this API returns all the stats of all the regions for a report identified by the stat_id parameter. Said report contains all statistics for this alert triggered from signatures contained in all regions for the selected hour.
    api_response = api_instance.list(stat_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegionStatsApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stat_id** | **int**| The ID of the stat to retrieve region stats for | 

### Return type

[**PaginatedCollection**](PaginatedCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

