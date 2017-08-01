# esp_sdk.ReportCompliancesApi

All URIs are relative to *http://localhost/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](ReportCompliancesApi.md#create) | **POST** /api/v2/reports/export/compliance.json_api | This endpoint is used to create a Compliance Report.


# **create**
> file create()

This endpoint is used to create a Compliance Report.

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.ReportCompliancesApi()

try: 
    # This endpoint is used to create a Compliance Report.
    api_response = api_instance.create()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportCompliancesApi->create: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

