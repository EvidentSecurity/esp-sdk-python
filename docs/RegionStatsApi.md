# esp_sdk.RegionStatsApi

All URIs are relative to *http://localhost/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_stats_stat_id_regions_json_api_get**](RegionStatsApi.md#api_v2_stats_stat_id_regions_json_api_get) | **GET** /api/v2/stats/{stat_id}/regions.json_api | 


# **api_v2_stats_stat_id_regions_json_api_get**
> api_v2_stats_stat_id_regions_json_api_get(stat_id)



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
    api_instance.api_v2_stats_stat_id_regions_json_api_get(stat_id)
except ApiException as e:
    print("Exception when calling RegionStatsApi->api_v2_stats_stat_id_regions_json_api_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stat_id** | **int**| The ID of the stat to retrieve region stats for | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

