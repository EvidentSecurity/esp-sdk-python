# esp_sdk.AlertsApi

All URIs are relative to https://api.evident.io

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_compliance_controls**](AlertsApi.md#list_compliance_controls) | **GET** /api/v2/alerts/{alert_id}/compliance_controls.json_api | Get a list of Compliance Controls for an Alert
[**list_custom_compliance_controls**](AlertsApi.md#list_custom_compliance_controls) | **GET** /api/v2/alerts/{alert_id}/custom_compliance_controls.json_api | Get a list of Custom Compliance Controls for an Alert
[**list_for_report**](AlertsApi.md#list_for_report) | **PUT** /api/v2/reports/{report_id}/alerts.json_api | Get a list of Alerts for a Report
[**show**](AlertsApi.md#show) | **GET** /api/v2/alerts/{id}.json_api | Show a single Alert


# **list_compliance_controls**
> PaginatedCollection list_compliance_controls(alert_id, page=page, include=include)

Get a list of Compliance Controls for an Alert



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.AlertsApi()
alert_id = 56 # int | The ID of the alert the compliance controls belong to
page = '{:number=>1,+:size=>20}' # str | Page Number and Page Size.  number is the page number of the collection to return, size is the number of items to return per page (optional) (default to {:number=>1,+:size=>20})
include = 'include_example' # str | Related objects that can be included in the response:  compliance_standard, compliance_domain, signatures See Including Objects for more information. (optional)

try: 
    # Get a list of Compliance Controls for an Alert
    api_response = api_instance.list_compliance_controls(alert_id, page=page, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->list_compliance_controls: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_id** | **int**| The ID of the alert the compliance controls belong to | 
 **page** | **str**| Page Number and Page Size.  number is the page number of the collection to return, size is the number of items to return per page | [optional] [default to {:number&#x3D;&gt;1,+:size&#x3D;&gt;20}]
 **include** | **str**| Related objects that can be included in the response:  compliance_standard, compliance_domain, signatures See Including Objects for more information. | [optional] 

### Return type

[**PaginatedCollection**](PaginatedCollection.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_custom_compliance_controls**
> PaginatedCollection list_custom_compliance_controls(alert_id, page=page, include=include)

Get a list of Custom Compliance Controls for an Alert



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.AlertsApi()
alert_id = 56 # int | The ID of the alert the custom compliance controls belong to
page = '{:number=>1,+:size=>20}' # str | Page Number and Page Size.  number is the page number of the collection to return, size is the number of items to return per page (optional) (default to {:number=>1,+:size=>20})
include = 'include_example' # str | Related objects that can be included in the response:  custom_compliance_standard, custom_compliance_domain, signatures, custom_signatures See Including Objects for more information. (optional)

try: 
    # Get a list of Custom Compliance Controls for an Alert
    api_response = api_instance.list_custom_compliance_controls(alert_id, page=page, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->list_custom_compliance_controls: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_id** | **int**| The ID of the alert the custom compliance controls belong to | 
 **page** | **str**| Page Number and Page Size.  number is the page number of the collection to return, size is the number of items to return per page | [optional] [default to {:number&#x3D;&gt;1,+:size&#x3D;&gt;20}]
 **include** | **str**| Related objects that can be included in the response:  custom_compliance_standard, custom_compliance_domain, signatures, custom_signatures See Including Objects for more information. | [optional] 

### Return type

[**PaginatedCollection**](PaginatedCollection.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_for_report**
> PaginatedCollection list_for_report(report_id, filter=filter, page=page, include=include)

Get a list of Alerts for a Report



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.AlertsApi()
report_id = 56 # int | ID of the Report to Return Alerts For
filter = {'key': 'filter_example'} # dict(str, str) | Filter Params for Searching.  Equality Searchable Attribute: [id]  Limited Searchable Attributes: [signature_service_id_in, signature_risk_level_in, risk_level_in, risk_level_eq, resource_or_tag_cont, suppressed, not_suppressed, signature_name_cont, signature_identifier_cont, external_account_id_in, external_account_id_eq, external_account_team_id_in, external_account_team_id_eq, region_id_in, region_id_eq, status_in, status_eq, cloud_trail_events_present, open_as_of, signature_id_in, signature_id_eq, external_account_provider_eq]   (optional)
page = '{:number=>1,+:size=>20}' # str | Page Number and Page Size.  number is the page number of the collection to return, size is the number of items to return per page (optional) (default to {:number=>1,+:size=>20})
include = 'include_example' # str | Related objects that can be included in the response:  external_account, region, signature, custom_signature, suppression, metadata, cloud_trail_events, tags, compliance_controls, custom_compliance_controls See Including Objects for more information. (optional)

try: 
    # Get a list of Alerts for a Report
    api_response = api_instance.list_for_report(report_id, filter=filter, page=page, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->list_for_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_id** | **int**| ID of the Report to Return Alerts For | 
 **filter** | [**dict(str, str)**](str.md)| Filter Params for Searching.  Equality Searchable Attribute: [id]  Limited Searchable Attributes: [signature_service_id_in, signature_risk_level_in, risk_level_in, risk_level_eq, resource_or_tag_cont, suppressed, not_suppressed, signature_name_cont, signature_identifier_cont, external_account_id_in, external_account_id_eq, external_account_team_id_in, external_account_team_id_eq, region_id_in, region_id_eq, status_in, status_eq, cloud_trail_events_present, open_as_of, signature_id_in, signature_id_eq, external_account_provider_eq]   | [optional] 
 **page** | **str**| Page Number and Page Size.  number is the page number of the collection to return, size is the number of items to return per page | [optional] [default to {:number&#x3D;&gt;1,+:size&#x3D;&gt;20}]
 **include** | **str**| Related objects that can be included in the response:  external_account, region, signature, custom_signature, suppression, metadata, cloud_trail_events, tags, compliance_controls, custom_compliance_controls See Including Objects for more information. | [optional] 

### Return type

[**PaginatedCollection**](PaginatedCollection.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

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
id = 56 # int | Alert ID
include = 'include_example' # str | Related objects that can be included in the response:  external_account, region, signature, custom_signature, suppression, metadata, cloud_trail_events, tags, compliance_controls, custom_compliance_controls See Including Objects for more information. (optional)

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
 **id** | **int**| Alert ID | 
 **include** | **str**| Related objects that can be included in the response:  external_account, region, signature, custom_signature, suppression, metadata, cloud_trail_events, tags, compliance_controls, custom_compliance_controls See Including Objects for more information. | [optional] 

### Return type

[**Alert**](Alert.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

