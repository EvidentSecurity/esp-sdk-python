# esp_sdk.AuditLogFileExportApi

All URIs are relative to *http://localhost/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](AuditLogFileExportApi.md#create) | **POST** /api/v2/audit_logs/export/files.json_api | Export an Audit Log File
[**show**](AuditLogFileExportApi.md#show) | **GET** /api/v2/audit_logs/export/files/{id}.json_api | Show a single Audit Log File


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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show**
> AuditLogFile show(id, include=include)

Show a single Audit Log File

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.AuditLogFileExportApi()
id = 56 # int | Audit Log File Id
include = 'include_example' # str | Objects that can be included in the response:  organization,user  See Including Objects for more information. (optional)

try: 
    # Show a single Audit Log File
    api_response = api_instance.show(id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuditLogFileExportApi->show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Audit Log File Id | 
 **include** | **str**| Objects that can be included in the response:  organization,user  See Including Objects for more information. | [optional] 

### Return type

[**AuditLogFile**](AuditLogFile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

