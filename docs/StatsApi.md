# esp_sdk.StatsApi

All URIs are relative to https://api.evident.io

Method | HTTP request | Description
------------- | ------------- | -------------
[**for_compliance_controls**](StatsApi.md#for_compliance_controls) | **GET** /api/v2/stats/{stat_id}/compliance_controls.json_api | A successful call to this API returns all the stats of all the compliance controls for a report identified by the stat_id parameter. Said report contains all statistics for this alert triggered from signatures contained in all compliance controls for the selected hour.
[**for_custom_signatures**](StatsApi.md#for_custom_signatures) | **GET** /api/v2/stats/{stat_id}/custom_signatures.json_api | A successful call to this API returns all the stats of all the custom signatures for a report identified by the stat_id parameter. Said report contains all statistics for this alert triggered from signatures contained in all custom_signatures for the selected hour.
[**for_regions**](StatsApi.md#for_regions) | **GET** /api/v2/stats/{stat_id}/regions.json_api | A successful call to this API returns all the stats of all the regions for a report identified by the stat_id parameter. Said report contains all statistics for this alert triggered from signatures contained in all regions for the selected hour.
[**for_report**](StatsApi.md#for_report) | **GET** /api/v2/reports/{report_id}/stats.json_api | A successful call to this API returns all the stats of all the alerts for a report identified by the report_id parameter. Said report contains all statistics for this alert triggered from signatures contained in all regions for the selected hour.
[**for_services**](StatsApi.md#for_services) | **GET** /api/v2/stats/{stat_id}/services.json_api | A successful call to this API returns all the stats of all the services for a report identified by the stat_id parameter. Said report contains all statistics for this alert triggered from signatures contained in all services for the selected hour.
[**for_signatures**](StatsApi.md#for_signatures) | **GET** /api/v2/stats/{stat_id}/signatures.json_api | A successful call to this API returns all the stats of all the signatures for a report identified by the stat_id parameter. Said report contains all statistics for this alert triggered from signatures contained in all signatures for the selected hour.
[**latest_for_teams**](StatsApi.md#latest_for_teams) | **GET** /api/v2/stats/latest_for_teams.json_api | A successful call to this API returns all the stats for the most recent report of each team accessible by the given API key
[**show**](StatsApi.md#show) | **GET** /api/v2/stats/{id}.json_api | Show a single Stat


# **for_compliance_controls**
> PaginatedCollection for_compliance_controls(stat_id, include=include, page=page)

A successful call to this API returns all the stats of all the compliance controls for a report identified by the stat_id parameter. Said report contains all statistics for this alert triggered from signatures contained in all compliance controls for the selected hour.

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.StatsApi()
stat_id = 56 # int | The ID of the stat to retrieve compliance control stats for
include = 'include_example' # str | Objects that can be included in the response:  compliance_control,stat  See Including Objects for more information. (optional)
page = {'key': 'page_example'} # dict(str, str) | Page Number and Page Size.  Example: page: {number: 1, size: 20} (optional)

try: 
    # A successful call to this API returns all the stats of all the compliance controls for a report identified by the stat_id parameter. Said report contains all statistics for this alert triggered from signatures contained in all compliance controls for the selected hour.
    api_response = api_instance.for_compliance_controls(stat_id, include=include, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsApi->for_compliance_controls: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stat_id** | **int**| The ID of the stat to retrieve compliance control stats for | 
 **include** | **str**| Objects that can be included in the response:  compliance_control,stat  See Including Objects for more information. | [optional] 
 **page** | [**dict(str, str)**](str.md)| Page Number and Page Size.  Example: page: {number: 1, size: 20} | [optional] 

### Return type

[**PaginatedCollection**](PaginatedCollection.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **for_custom_signatures**
> PaginatedCollection for_custom_signatures(stat_id, include=include, page=page)

A successful call to this API returns all the stats of all the custom signatures for a report identified by the stat_id parameter. Said report contains all statistics for this alert triggered from signatures contained in all custom_signatures for the selected hour.

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.StatsApi()
stat_id = 56 # int | The ID of the stat to retrieve custom signature stats for
include = 'include_example' # str | Objects that can be included in the response:  custom_signature,stat  See Including Objects for more information. (optional)
page = {'key': 'page_example'} # dict(str, str) | Page Number and Page Size.  Example: page: {number: 1, size: 20} (optional)

try: 
    # A successful call to this API returns all the stats of all the custom signatures for a report identified by the stat_id parameter. Said report contains all statistics for this alert triggered from signatures contained in all custom_signatures for the selected hour.
    api_response = api_instance.for_custom_signatures(stat_id, include=include, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsApi->for_custom_signatures: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stat_id** | **int**| The ID of the stat to retrieve custom signature stats for | 
 **include** | **str**| Objects that can be included in the response:  custom_signature,stat  See Including Objects for more information. | [optional] 
 **page** | [**dict(str, str)**](str.md)| Page Number and Page Size.  Example: page: {number: 1, size: 20} | [optional] 

### Return type

[**PaginatedCollection**](PaginatedCollection.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **for_regions**
> PaginatedCollection for_regions(stat_id, include=include, page=page)

A successful call to this API returns all the stats of all the regions for a report identified by the stat_id parameter. Said report contains all statistics for this alert triggered from signatures contained in all regions for the selected hour.

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.StatsApi()
stat_id = 56 # int | The ID of the stat to retrieve region stats for
include = 'include_example' # str | Objects that can be included in the response:  region,stat  See Including Objects for more information. (optional)
page = {'key': 'page_example'} # dict(str, str) | Page Number and Page Size.  Example: page: {number: 1, size: 20} (optional)

try: 
    # A successful call to this API returns all the stats of all the regions for a report identified by the stat_id parameter. Said report contains all statistics for this alert triggered from signatures contained in all regions for the selected hour.
    api_response = api_instance.for_regions(stat_id, include=include, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsApi->for_regions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stat_id** | **int**| The ID of the stat to retrieve region stats for | 
 **include** | **str**| Objects that can be included in the response:  region,stat  See Including Objects for more information. | [optional] 
 **page** | [**dict(str, str)**](str.md)| Page Number and Page Size.  Example: page: {number: 1, size: 20} | [optional] 

### Return type

[**PaginatedCollection**](PaginatedCollection.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **for_report**
> Stat for_report(report_id, include=include)

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
include = 'include_example' # str | Objects that can be included in the response:  report,regions,services,signatures,custom_signatures  See Including Objects for more information. (optional)

try: 
    # A successful call to this API returns all the stats of all the alerts for a report identified by the report_id parameter. Said report contains all statistics for this alert triggered from signatures contained in all regions for the selected hour.
    api_response = api_instance.for_report(report_id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsApi->for_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_id** | **int**| The ID of the report to retrieve stats for | 
 **include** | **str**| Objects that can be included in the response:  report,regions,services,signatures,custom_signatures  See Including Objects for more information. | [optional] 

### Return type

[**Stat**](Stat.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **for_services**
> PaginatedCollection for_services(stat_id, include=include, page=page)

A successful call to this API returns all the stats of all the services for a report identified by the stat_id parameter. Said report contains all statistics for this alert triggered from signatures contained in all services for the selected hour.

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.StatsApi()
stat_id = 56 # int | The ID of the stat to retrieve service stats for
include = 'include_example' # str | Objects that can be included in the response:  service,stat  See Including Objects for more information. (optional)
page = {'key': 'page_example'} # dict(str, str) | Page Number and Page Size.  Example: page: {number: 1, size: 20} (optional)

try: 
    # A successful call to this API returns all the stats of all the services for a report identified by the stat_id parameter. Said report contains all statistics for this alert triggered from signatures contained in all services for the selected hour.
    api_response = api_instance.for_services(stat_id, include=include, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsApi->for_services: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stat_id** | **int**| The ID of the stat to retrieve service stats for | 
 **include** | **str**| Objects that can be included in the response:  service,stat  See Including Objects for more information. | [optional] 
 **page** | [**dict(str, str)**](str.md)| Page Number and Page Size.  Example: page: {number: 1, size: 20} | [optional] 

### Return type

[**PaginatedCollection**](PaginatedCollection.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **for_signatures**
> PaginatedCollection for_signatures(stat_id, include=include, page=page)

A successful call to this API returns all the stats of all the signatures for a report identified by the stat_id parameter. Said report contains all statistics for this alert triggered from signatures contained in all signatures for the selected hour.

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.StatsApi()
stat_id = 56 # int | The ID of the stat to retrieve signature stats for
include = 'include_example' # str | Objects that can be included in the response:  signature,stat  See Including Objects for more information. (optional)
page = {'key': 'page_example'} # dict(str, str) | Page Number and Page Size.  Example: page: {number: 1, size: 20} (optional)

try: 
    # A successful call to this API returns all the stats of all the signatures for a report identified by the stat_id parameter. Said report contains all statistics for this alert triggered from signatures contained in all signatures for the selected hour.
    api_response = api_instance.for_signatures(stat_id, include=include, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsApi->for_signatures: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stat_id** | **int**| The ID of the stat to retrieve signature stats for | 
 **include** | **str**| Objects that can be included in the response:  signature,stat  See Including Objects for more information. | [optional] 
 **page** | [**dict(str, str)**](str.md)| Page Number and Page Size.  Example: page: {number: 1, size: 20} | [optional] 

### Return type

[**PaginatedCollection**](PaginatedCollection.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **latest_for_teams**
> PaginatedCollection latest_for_teams(include=include, page=page)

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
include = 'include_example' # str | Objects that can be included in the response:  report,regions,services,signatures,custom_signatures  See Including Objects for more information. (optional)
page = {'key': 'page_example'} # dict(str, str) | Page Number and Page Size.  Example: page: {number: 1, size: 20} (optional)

try: 
    # A successful call to this API returns all the stats for the most recent report of each team accessible by the given API key
    api_response = api_instance.latest_for_teams(include=include, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsApi->latest_for_teams: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include** | **str**| Objects that can be included in the response:  report,regions,services,signatures,custom_signatures  See Including Objects for more information. | [optional] 
 **page** | [**dict(str, str)**](str.md)| Page Number and Page Size.  Example: page: {number: 1, size: 20} | [optional] 

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
id = 56 # int | Stat Id
include = 'include_example' # str | Objects that can be included in the response:  report,regions,services,signatures,custom_signatures  See Including Objects for more information. (optional)

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
 **id** | **int**| Stat Id | 
 **include** | **str**| Objects that can be included in the response:  report,regions,services,signatures,custom_signatures  See Including Objects for more information. | [optional] 

### Return type

[**Stat**](Stat.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

