# esp_sdk.ReportExportApi

All URIs are relative to https://api.evident.io

Method | HTTP request | Description
------------- | ------------- | -------------
[**request_file**](ReportExportApi.md#request_file) | **POST** /api/v2/reports/export/files.json_api | Export all alerts for a set of reports to a file
[**send_to_integration**](ReportExportApi.md#send_to_integration) | **POST** /api/v2/reports/export/integrations.json_api | Export all alerts on reports to an integration
[**show_file_details**](ReportExportApi.md#show_file_details) | **GET** /api/v2/reports/export/files/{id}.json_api | Show a single Exported Report


# **request_file**
> ExportedReport request_file(report_ids, requested_format, filter=filter)

Export all alerts for a set of reports to a file

<p>An email will be sent to the calling user once the file is ready for download.</p> <p>The URL and filename attributes will be blank on create. When exporting is complete these attributes will be filled in and can be viewed using the show action.</p>

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.ReportExportApi()
report_ids = [56] # list[int] | An array of report IDs to export alerts for
requested_format = 'requested_format_example' # str | The file format of the export. Valid values are csv, json, pdf
filter = {'key': 'filter_example'} # dict(str, str) | Params used to filter the alerts that will be exported (optional)

try: 
    # Export all alerts for a set of reports to a file
    api_response = api_instance.request_file(report_ids, requested_format, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportExportApi->request_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_ids** | [**list[int]**](int.md)| An array of report IDs to export alerts for | 
 **requested_format** | **str**| The file format of the export. Valid values are csv, json, pdf | 
 **filter** | [**dict(str, str)**](str.md)| Params used to filter the alerts that will be exported | [optional] 

### Return type

[**ExportedReport**](ExportedReport.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_to_integration**
> Meta send_to_integration(integration_id, report_ids, filter=filter)

Export all alerts on reports to an integration



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.ReportExportApi()
integration_id = 56 # int | The ID of the integration to send the alerts to
report_ids = [56] # list[int] | An array of report IDs
filter = {'key': 'filter_example'} # dict(str, str) | Params used to filter the alerts that will be exported (optional)

try: 
    # Export all alerts on reports to an integration
    api_response = api_instance.send_to_integration(integration_id, report_ids, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportExportApi->send_to_integration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_id** | **int**| The ID of the integration to send the alerts to | 
 **report_ids** | [**list[int]**](int.md)| An array of report IDs | 
 **filter** | [**dict(str, str)**](str.md)| Params used to filter the alerts that will be exported | [optional] 

### Return type

[**Meta**](Meta.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_file_details**
> ExportedReport show_file_details(id)

Show a single Exported Report

The URL provided is temporary and will expire shortly after the request. To download the exported file you will need to follow the URL provided.

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.ReportExportApi()
id = 56 # int | Exported Report ID

try: 
    # Show a single Exported Report
    api_response = api_instance.show_file_details(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportExportApi->show_file_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Exported Report ID | 

### Return type

[**ExportedReport**](ExportedReport.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

