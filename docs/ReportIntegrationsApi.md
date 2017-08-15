# esp_sdk.ReportIntegrationsApi

All URIs are relative to https://api.evident.io

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](ReportIntegrationsApi.md#create) | **POST** /api/v2/reports/export/integrations.json_api | Export all alerts on reports to an integration


# **create**
> SuccessObject create(report_ids, integration_id)

Export all alerts on reports to an integration

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.ReportIntegrationsApi()
report_ids = [56] # list[int] | An array of report IDs
integration_id = 56 # int | The ID of the integration to send the alerts to

try: 
    # Export all alerts on reports to an integration
    api_response = api_instance.create(report_ids, integration_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportIntegrationsApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_ids** | [**list[int]**](int.md)| An array of report IDs | 
 **integration_id** | **int**| The ID of the integration to send the alerts to | 

### Return type

[**SuccessObject**](SuccessObject.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

