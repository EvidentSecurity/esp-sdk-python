# esp_sdk.StatsApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**for_report**](StatsApi.md#for_report) | **GET** /v2/reports/{report_id}/stats.json | A successful call to this API returns all the stats of all the alerts for a report identified by the report_id parameter. Said report contains all statistics for this alert triggered from signatures contained in all regions for the selected hour.
[**latest_for_teams**](StatsApi.md#latest_for_teams) | **GET** /v2/stats/latest_for_teams.json | A successful call to this API returns all the stats for the most recent report of each team accessible by the given API key


# **for_report**
> Stat for_report(report_id)

A successful call to this API returns all the stats of all the alerts for a report identified by the report_id parameter. Said report contains all statistics for this alert triggered from signatures contained in all regions for the selected hour.

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.StatsApi()
report_id = 56 # int | The ID of the report to retrieve stats for

try: 
    # A successful call to this API returns all the stats of all the alerts for a report identified by the report_id parameter. Said report contains all statistics for this alert triggered from signatures contained in all regions for the selected hour.
    api_response = api_instance.for_report(report_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsApi->for_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_id** | **int**| The ID of the report to retrieve stats for | 

### Return type

[**Stat**](Stat.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **latest_for_teams**
> list[Stat] latest_for_teams()

A successful call to this API returns all the stats for the most recent report of each team accessible by the given API key

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.StatsApi()

try: 
    # A successful call to this API returns all the stats for the most recent report of each team accessible by the given API key
    api_response = api_instance.latest_for_teams()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsApi->latest_for_teams: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Stat]**](Stat.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

