# esp_sdk.AuditLogFileExportApi

All URIs are relative to https://api.evident.io

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](AuditLogFileExportApi.md#create) | **POST** /api/v2/audit_logs/export/files.json_api | Export an Audit Log File
[**show**](AuditLogFileExportApi.md#show) | **GET** /api/v2/audit_logs/export/files/{id}.json_api | Show a single AuditLogFile


# **create**
> AuditLogFile create()

Export an Audit Log File

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.AuditLogFileExportApi()

try: 
    # Export an Audit Log File
    api_response = api_instance.create()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuditLogFileExportApi->create: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AuditLogFile**](AuditLogFile.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show**
> AuditLogFile show(id, include=include)

Show a single AuditLogFile

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.AuditLogFileExportApi()
id = 56 # int | AuditLogFile ID
include = 'include_example' # str | Related objects that can be included in the response.  See Including Objects for more information. (optional)

try: 
    # Show a single AuditLogFile
    api_response = api_instance.show(id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuditLogFileExportApi->show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| AuditLogFile ID | 
 **include** | **str**| Related objects that can be included in the response.  See Including Objects for more information. | [optional] 

### Return type

[**AuditLogFile**](AuditLogFile.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

