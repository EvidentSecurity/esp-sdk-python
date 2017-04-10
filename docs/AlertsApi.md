# esp_sdk.AlertsApi

All URIs are relative to *http://localhost/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list**](AlertsApi.md#list) | **PUT** /api/v2/reports/{report_id}/alerts.json_api | Get a list of Alerts
[**show**](AlertsApi.md#show) | **GET** /api/v2/alerts/{id}.json_api | Show a single Alert


# **list**
> PaginatedCollection list(report_id, page=page, filter=filter, include=include, region_id=region_id, status=status, first_seen=first_seen, suppressed=suppressed, team_id=team_id, external_account_id=external_account_id, service_id=service_id, signature_severity=signature_severity, signature_name=signature_name, resource=resource, signature_identifier=signature_identifier)

Get a list of Alerts

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.AlertsApi()
report_id = 56 # int | Id of the Report to Return Alerts For
page = {'key': 'page_example'} # dict(str, str) | Page Number (optional)
filter = {'key': 'filter_example'} # dict(str, str) | Filter Params for Searching (optional)
include = 'include_example' # str | Included Objects (optional)
region_id = 56 # int | Return only alerts for this region. (optional)
status = 'status_example' # str | Return only alerts for the give status(es). Valid values are fail, warn, error, pass, info (optional)
first_seen = 56 # int | Return only alerts that have started within a number of hours of the report. For example, first_seen of 3 will return alerts that started showing up within the last 3 hours of the report. (optional)
suppressed = true # bool | Return only suppressed alerts (optional)
team_id = 56 # int | Return only alerts for the given team. (optional)
external_account_id = 56 # int | Return only alerts for the given external id. (optional)
service_id = 56 # int | Return only alerts on signatures with the given service. (optional)
signature_severity = 'signature_severity_example' # str | Return only alerts for signatures with the given risk_level. Valid values are Low, Medium, High (optional)
signature_name = 'signature_name_example' # str | Return only alerts for signatures with the given name. (optional)
resource = 'resource_example' # str | Return only alerts for the given resource or tag. (optional)
signature_identifier = 'signature_identifier_example' # str | Return only alerts for signatures with the given identifier. (optional)

try: 
    # Get a list of Alerts
    api_response = api_instance.list(report_id, page=page, filter=filter, include=include, region_id=region_id, status=status, first_seen=first_seen, suppressed=suppressed, team_id=team_id, external_account_id=external_account_id, service_id=service_id, signature_severity=signature_severity, signature_name=signature_name, resource=resource, signature_identifier=signature_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_id** | **int**| Id of the Report to Return Alerts For | 
 **page** | [**dict(str, str)**](str.md)| Page Number | [optional] 
 **filter** | [**dict(str, str)**](str.md)| Filter Params for Searching | [optional] 
 **include** | **str**| Included Objects | [optional] 
 **region_id** | **int**| Return only alerts for this region. | [optional] 
 **status** | **str**| Return only alerts for the give status(es). Valid values are fail, warn, error, pass, info | [optional] 
 **first_seen** | **int**| Return only alerts that have started within a number of hours of the report. For example, first_seen of 3 will return alerts that started showing up within the last 3 hours of the report. | [optional] 
 **suppressed** | **bool**| Return only suppressed alerts | [optional] 
 **team_id** | **int**| Return only alerts for the given team. | [optional] 
 **external_account_id** | **int**| Return only alerts for the given external id. | [optional] 
 **service_id** | **int**| Return only alerts on signatures with the given service. | [optional] 
 **signature_severity** | **str**| Return only alerts for signatures with the given risk_level. Valid values are Low, Medium, High | [optional] 
 **signature_name** | **str**| Return only alerts for signatures with the given name. | [optional] 
 **resource** | **str**| Return only alerts for the given resource or tag. | [optional] 
 **signature_identifier** | **str**| Return only alerts for signatures with the given identifier. | [optional] 

### Return type

[**PaginatedCollection**](PaginatedCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show**
> Alert show(id, include=include)

Show a single Alert

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.AlertsApi()
id = 56 # int | Alert Id
include = 'include_example' # str | Included Objects (optional)

try: 
    # Show a single Alert
    api_response = api_instance.show(id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Alert Id | 
 **include** | **str**| Included Objects | [optional] 

### Return type

[**Alert**](Alert.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

