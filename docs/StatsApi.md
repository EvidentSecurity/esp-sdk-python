# esp_sdk.StatsApi

All URIs are relative to https://api.evident.io

Method | HTTP request | Description
------------- | ------------- | -------------
[**for_report**](StatsApi.md#for_report) | **GET** /api/v2/reports/{report_id}/stats.json_api | Stats for a report
[**latest_for_teams**](StatsApi.md#latest_for_teams) | **PUT** /api/v2/stats/latest_for_teams.json_api | Stats for teams
[**show**](StatsApi.md#show) | **GET** /api/v2/stats/{id}.json_api | Show a single Stat


# **for_report**
> Stat for_report(report_id, include=include)

Stats for a report

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
include = 'include_example' # str | Related objects that can be included in the response:  report, regions, services, signatures, custom_signatures, custom_compliance_controls, compliance_controls See Including Objects for more information. (optional)

try: 
    # Stats for a report
    api_response = api_instance.for_report(report_id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsApi->for_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_id** | **int**| The ID of the report to retrieve stats for | 
 **include** | **str**| Related objects that can be included in the response:  report, regions, services, signatures, custom_signatures, custom_compliance_controls, compliance_controls See Including Objects for more information. | [optional] 

### Return type

[**Stat**](Stat.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **latest_for_teams**
> PaginatedCollection latest_for_teams(filter=filter, page=page, include=include)

Stats for teams

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
filter = {'key': 'filter_example'} # dict(str, str) | Filter Params for Searching.      Searchable Association: [report] See Searching Lists for more information. See the filter parameter of the association's list action to see what attributes are searchable on each association. See Conditions on Relationships in Searching Lists for more information. (optional)
page = '{:number=>1,+:size=>20}' # str | Page Number and Page Size.  number is the page number of the collection to return, size is the number of items to return per page (optional) (default to {:number=>1,+:size=>20})
include = 'include_example' # str | Related objects that can be included in the response:  report, regions, services, signatures, custom_signatures, custom_compliance_controls, compliance_controls See Including Objects for more information. (optional)

try: 
    # Stats for teams
    api_response = api_instance.latest_for_teams(filter=filter, page=page, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsApi->latest_for_teams: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | [**dict(str, str)**](str.md)| Filter Params for Searching.      Searchable Association: [report] See Searching Lists for more information. See the filter parameter of the association&#39;s list action to see what attributes are searchable on each association. See Conditions on Relationships in Searching Lists for more information. | [optional] 
 **page** | **str**| Page Number and Page Size.  number is the page number of the collection to return, size is the number of items to return per page | [optional] [default to {:number&#x3D;&gt;1,+:size&#x3D;&gt;20}]
 **include** | **str**| Related objects that can be included in the response:  report, regions, services, signatures, custom_signatures, custom_compliance_controls, compliance_controls See Including Objects for more information. | [optional] 

### Return type

[**PaginatedCollection**](PaginatedCollection.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show**
> Stat show(id, include=include)

Show a single Stat



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.StatsApi()
id = 56 # int | Stat ID
include = 'include_example' # str | Related objects that can be included in the response:  report, regions, services, signatures, custom_signatures, custom_compliance_controls, compliance_controls See Including Objects for more information. (optional)

try: 
    # Show a single Stat
    api_response = api_instance.show(id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsApi->show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Stat ID | 
 **include** | **str**| Related objects that can be included in the response:  report, regions, services, signatures, custom_signatures, custom_compliance_controls, compliance_controls See Including Objects for more information. | [optional] 

### Return type

[**Stat**](Stat.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

