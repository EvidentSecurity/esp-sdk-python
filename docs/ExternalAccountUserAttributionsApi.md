# esp_sdk.ExternalAccountUserAttributionsApi

All URIs are relative to *http://localhost/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**update**](ExternalAccountUserAttributionsApi.md#update) | **PATCH** /api/v2/external_accounts/{external_account_id}/user_attribution.json_api | A successful call to this API will update the user attributions on an external account.


# **update**
> ExternalAccount update(external_account_id, cloudtrail_name)

A successful call to this API will update the user attributions on an external account.

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.ExternalAccountUserAttributionsApi()
external_account_id = 56 # int | The ID of the external account to update the user attributions of.
cloudtrail_name = 'cloudtrail_name_example' # str | An array of all the signatures to disable on the external account.

try: 
    # A successful call to this API will update the user attributions on an external account.
    api_response = api_instance.update(external_account_id, cloudtrail_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalAccountUserAttributionsApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_account_id** | **int**| The ID of the external account to update the user attributions of. | 
 **cloudtrail_name** | **str**| An array of all the signatures to disable on the external account. | 

### Return type

[**ExternalAccount**](ExternalAccount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

