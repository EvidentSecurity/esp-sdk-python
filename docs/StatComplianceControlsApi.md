# esp_sdk.StatComplianceControlsApi

All URIs are relative to https://api.evident.io

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_for_stat**](StatComplianceControlsApi.md#list_for_stat) | **GET** /api/v2/stats/{stat_id}/compliance_controls.json_api | Statistics for compliance controls
[**show**](StatComplianceControlsApi.md#show) | **GET** /api/v2/stats/compliance_controls/{id}.json_api | Show a single Stat Compliance Control


# **list_for_stat**
> PaginatedCollection list_for_stat(stat_id, include=include, filter=filter, page=page)

Statistics for compliance controls

A successful call to this API returns all the statistics of all the compliance controls for a report identified by the stat_id parameter. Said report contains all statistics for this alert triggered from signatures contained in all compliance controls for the selected hour.

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.StatComplianceControlsApi()
stat_id = 56 # int | The ID of the stat to retrieve compliance control statistics for
include = 'include_example' # str | Related objects that can be included in the response:  compliance_control, stat See Including Objects for more information. (optional)
filter = {'key': 'filter_example'} # dict(str, str) | Filter Params for Searching.  Equality Searchable Attributes: [stat_id, type_id]     (optional)
page = '{:number=>1,+:size=>20}' # str | Page Number and Page Size.  Number is the page number of the collection to return, size is the number of items to return per page. (optional) (default to {:number=>1,+:size=>20})

try: 
    # Statistics for compliance controls
    api_response = api_instance.list_for_stat(stat_id, include=include, filter=filter, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatComplianceControlsApi->list_for_stat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stat_id** | **int**| The ID of the stat to retrieve compliance control statistics for | 
 **include** | **str**| Related objects that can be included in the response:  compliance_control, stat See Including Objects for more information. | [optional] 
 **filter** | [**dict(str, str)**](str.md)| Filter Params for Searching.  Equality Searchable Attributes: [stat_id, type_id]     | [optional] 
 **page** | **str**| Page Number and Page Size.  Number is the page number of the collection to return, size is the number of items to return per page. | [optional] [default to {:number&#x3D;&gt;1,+:size&#x3D;&gt;20}]

### Return type

[**PaginatedCollection**](PaginatedCollection.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show**
> StatComplianceControl show(id, include=include)

Show a single Stat Compliance Control



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.StatComplianceControlsApi()
id = 56 # int | Stat Compliance Control ID
include = 'include_example' # str | Related objects that can be included in the response:  compliance_control, stat See Including Objects for more information. (optional)

try: 
    # Show a single Stat Compliance Control
    api_response = api_instance.show(id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatComplianceControlsApi->show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Stat Compliance Control ID | 
 **include** | **str**| Related objects that can be included in the response:  compliance_control, stat See Including Objects for more information. | [optional] 

### Return type

[**StatComplianceControl**](StatComplianceControl.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

