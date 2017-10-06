# esp_sdk.ExternalAccountDisabledSignaturesApi

All URIs are relative to https://api.evident.io

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](ExternalAccountDisabledSignaturesApi.md#create) | **POST** /api/v2/external_accounts/{external_account_id}/disabled_signatures.json_api | A successful call to this API will disable a signature for an external account.
[**destroy**](ExternalAccountDisabledSignaturesApi.md#destroy) | **DELETE** /api/v2/external_accounts/{external_account_id}/disabled_signatures.json_api | A successful call to this API will remove a signature from the disabled signature list on an external account.
[**list**](ExternalAccountDisabledSignaturesApi.md#list) | **GET** /api/v2/external_accounts/{external_account_id}/disabled_signatures.json_api | A successful call to this API returns all the disabled signatures of the associated external account, identified by the external_account_id parameter.
[**update**](ExternalAccountDisabledSignaturesApi.md#update) | **PATCH** /api/v2/external_accounts/{external_account_id}/disabled_signatures.json_api | A successful call to this API will update the disabled signatures on an external account.


# **create**
> Meta create(external_account_id, signature_id)

A successful call to this API will disable a signature for an external account.

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.ExternalAccountDisabledSignaturesApi()
external_account_id = 56 # int | The ID of the external account to disable a signature on
signature_id = 56 # int | The ID of the signature to disable

try: 
    # A successful call to this API will disable a signature for an external account.
    api_response = api_instance.create(external_account_id, signature_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalAccountDisabledSignaturesApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_account_id** | **int**| The ID of the external account to disable a signature on | 
 **signature_id** | **int**| The ID of the signature to disable | 

### Return type

[**Meta**](Meta.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy**
> Meta destroy(external_account_id, signature_id)

A successful call to this API will remove a signature from the disabled signature list on an external account.

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.ExternalAccountDisabledSignaturesApi()
external_account_id = 56 # int | The ID of the external account to enable a signature on
signature_id = 56 # int | The ID of the signature to enable

try: 
    # A successful call to this API will remove a signature from the disabled signature list on an external account.
    api_response = api_instance.destroy(external_account_id, signature_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalAccountDisabledSignaturesApi->destroy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_account_id** | **int**| The ID of the external account to enable a signature on | 
 **signature_id** | **int**| The ID of the signature to enable | 

### Return type

[**Meta**](Meta.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> PaginatedCollection list(external_account_id, filter=filter, include=include, page=page)

A successful call to this API returns all the disabled signatures of the associated external account, identified by the external_account_id parameter.

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.ExternalAccountDisabledSignaturesApi()
external_account_id = 56 # int | The ID of the external account to retrieve the disabled signatures for
filter = {'key': 'filter_example'} # dict(str, str) | Filter Params for Searching.  See Searching Lists for more information. (optional)
include = 'include_example' # str | Related objects that can be included in the response.  See Including Objects for more information. (optional)
page = '{:number=>1,+:size=>20}' # str | Page Number and Page Size.  number is the page number of the collection to return, size is the number of items to return per page (optional) (default to {:number=>1,+:size=>20})

try: 
    # A successful call to this API returns all the disabled signatures of the associated external account, identified by the external_account_id parameter.
    api_response = api_instance.list(external_account_id, filter=filter, include=include, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalAccountDisabledSignaturesApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_account_id** | **int**| The ID of the external account to retrieve the disabled signatures for | 
 **filter** | [**dict(str, str)**](str.md)| Filter Params for Searching.  See Searching Lists for more information. | [optional] 
 **include** | **str**| Related objects that can be included in the response.  See Including Objects for more information. | [optional] 
 **page** | **str**| Page Number and Page Size.  number is the page number of the collection to return, size is the number of items to return per page | [optional] [default to {:number&#x3D;&gt;1,+:size&#x3D;&gt;20}]

### Return type

[**PaginatedCollection**](PaginatedCollection.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> ExternalAccount update(external_account_id, disabled_signature_ids)

A successful call to this API will update the disabled signatures on an external account.

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.ExternalAccountDisabledSignaturesApi()
external_account_id = 56 # int | The ID of the external account to update the disabled signatures of
disabled_signature_ids = [56] # list[int] | An array of all the signatures to disable on the external account.  This will enable signature IDs that were previously disabled but not included on this list

try: 
    # A successful call to this API will update the disabled signatures on an external account.
    api_response = api_instance.update(external_account_id, disabled_signature_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalAccountDisabledSignaturesApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_account_id** | **int**| The ID of the external account to update the disabled signatures of | 
 **disabled_signature_ids** | [**list[int]**](int.md)| An array of all the signatures to disable on the external account.  This will enable signature IDs that were previously disabled but not included on this list | 

### Return type

[**ExternalAccount**](ExternalAccount.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

