# esp_sdk.SignatureSuppressionsApi

All URIs are relative to *http://localhost/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_signature_suppression**](SignatureSuppressionsApi.md#create_signature_suppression) | **POST** /api/v2/suppressions/signatures.json_api | A successful call to this API creates a new signature suppression for the supplied signature_ids or custom_signature_ids. The body of the request must contain a json API compliant hash of attributes with type suppression/signatures.


# **create_signature_suppression**
> create_signature_suppression(regions, external_account_ids, reason, resource, signature_ids=signature_ids, custom_signature_ids=custom_signature_ids)

A successful call to this API creates a new signature suppression for the supplied signature_ids or custom_signature_ids. The body of the request must contain a json API compliant hash of attributes with type suppression/signatures.

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.SignatureSuppressionsApi()
regions = ['regions_example'] # list[str] | An array of region names to suppress
external_account_ids = [56] # list[int] | An Array of the external accounts identified by external_account_id to suppress the signature or custom signature on
reason = 'reason_example' # str | The reason for creating the suppression
resource = 'resource_example' # str | The resource string this suppression will suppress alerts for
signature_ids = [56] # list[int] | An array of signatures identified by signature_id to suppress. Required if custom_signature_ids is blank (optional)
custom_signature_ids = [56] # list[int] | An array of custom signatures identified by custom_signature_id to suppress. Required if signature_ids is blank (optional)

try: 
    # A successful call to this API creates a new signature suppression for the supplied signature_ids or custom_signature_ids. The body of the request must contain a json API compliant hash of attributes with type suppression/signatures.
    api_instance.create_signature_suppression(regions, external_account_ids, reason, resource, signature_ids=signature_ids, custom_signature_ids=custom_signature_ids)
except ApiException as e:
    print("Exception when calling SignatureSuppressionsApi->create_signature_suppression: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **regions** | [**list[str]**](str.md)| An array of region names to suppress | 
 **external_account_ids** | [**list[int]**](int.md)| An Array of the external accounts identified by external_account_id to suppress the signature or custom signature on | 
 **reason** | **str**| The reason for creating the suppression | 
 **resource** | **str**| The resource string this suppression will suppress alerts for | 
 **signature_ids** | [**list[int]**](int.md)| An array of signatures identified by signature_id to suppress. Required if custom_signature_ids is blank | [optional] 
 **custom_signature_ids** | [**list[int]**](int.md)| An array of custom signatures identified by custom_signature_id to suppress. Required if signature_ids is blank | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

