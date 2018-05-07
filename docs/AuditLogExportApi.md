# esp_sdk.AuditLogExportApi

All URIs are relative to https://api.evident.io

Method | HTTP request | Description
------------- | ------------- | -------------
[**request_file**](AuditLogExportApi.md#request_file) | **POST** /api/v2/audit_logs/export/files.json_api | Export an Audit Log File
[**show_file_details**](AuditLogExportApi.md#show_file_details) | **GET** /api/v2/audit_logs/export/files/{id}.json_api | Show a single Audit Log File


# **request_file**
> AuditLogFile request_file(include=include)

Export an Audit Log File

An email will be sent to the user (having organization level access) requesting creation once the file is ready for download. The file will have all audit logs for the organization in CSV format.  The URL and filename in the response will be blank on create but will be present in the response on the show endpoint once the export has been generated.

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.AuditLogExportApi()
include = 'include_example' # str | Related objects that can be included in the response:  organization, user See Including Objects for more information. (optional)

try: 
    # Export an Audit Log File
    api_response = api_instance.request_file(include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuditLogExportApi->request_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include** | **str**| Related objects that can be included in the response:  organization, user See Including Objects for more information. | [optional] 

### Return type

[**AuditLogFile**](AuditLogFile.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_file_details**
> AuditLogFile show_file_details(id, include=include)

Show a single Audit Log File

The URL returned will expire and will no longer work after the expiration.

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.AuditLogExportApi()
id = 56 # int | Audit Log File ID
include = 'include_example' # str | Related objects that can be included in the response:  organization, user See Including Objects for more information. (optional)

try: 
    # Show a single Audit Log File
    api_response = api_instance.show_file_details(id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuditLogExportApi->show_file_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Audit Log File ID | 
 **include** | **str**| Related objects that can be included in the response:  organization, user See Including Objects for more information. | [optional] 

### Return type

[**AuditLogFile**](AuditLogFile.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

