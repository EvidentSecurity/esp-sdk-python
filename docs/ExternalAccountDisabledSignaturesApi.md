# esp_sdk.ExternalAccountDisabledSignaturesApi

All URIs are relative to *http://localhost/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](ExternalAccountDisabledSignaturesApi.md#create) | **POST** /api/v2/external_accounts/{external_account_id}/disabled_signatures.json_api | A successful call to this API will disable a signature for an external account.
[**destroy**](ExternalAccountDisabledSignaturesApi.md#destroy) | **DELETE** /api/v2/external_accounts/{external_account_id}/disabled_signatures.json_api | A successful call to this API will remove a signature from the disabled signature list on an external account.
[**list**](ExternalAccountDisabledSignaturesApi.md#list) | **GET** /api/v2/external_accounts/{external_account_id}/disabled_signatures.json_api | A successful call to this API returns all the disabled signatures of the associated external account, identified by the external_account_id parameter.
[**update**](ExternalAccountDisabledSignaturesApi.md#update) | **PATCH** /api/v2/external_accounts/{external_account_id}/disabled_signatures.json_api | A successful call to this API will update the disabled signatures on an external account.


# **create**
> SuccessObject create(external_account_id, signature_id)

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
external_account_id = 56 # int | The ID of the external account to disable a signature on.
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
 **external_account_id** | **int**| The ID of the external account to disable a signature on. | 
 **signature_id** | **int**| The ID of the signature to disable | 

### Return type

[**SuccessObject**](SuccessObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy**
> SuccessObject destroy(external_account_id, signature_id)

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
external_account_id = 56 # int | The ID of the external account to enable the signature on.
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
 **external_account_id** | **int**| The ID of the external account to enable the signature on. | 
 **signature_id** | **int**| The ID of the signature to enable | 

### Return type

[**SuccessObject**](SuccessObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
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
external_account_id = 56 # int | The ID of the external account to retrieve the disabled signatures for.
filter = {'key': 'filter_example'} # dict(str, str) | Filter Params for Searching.  Equality Searchable Attributes: [id, risk_level, service_id, disabled, supports_user_attribution, name, identifier, description, resolution] Matching Searchable Attributes: [name, identifier, description, resolution]  Sortable Attributes: [name, identifier, updated_at, created_at, id] Searchable Associations: [signature_copy, disabled_external_accounts, integrations] See the filter parameter of the association's list action to see what attributes are searchable on each association. See Searching on Relationships for more information. See Searching Lists for more information. Example: filter: {name_eq: 'Bob'} (optional)
include = 'include_example' # str | Objects that can be included in the response:  service,disabled_external_accounts  See Including Objects for more information. (optional)
page = {'key': 'page_example'} # dict(str, str) | Page Number and Page Size.  Example: page: {number: 1, size: 20} (optional)

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
 **external_account_id** | **int**| The ID of the external account to retrieve the disabled signatures for. | 
 **filter** | [**dict(str, str)**](str.md)| Filter Params for Searching.  Equality Searchable Attributes: [id, risk_level, service_id, disabled, supports_user_attribution, name, identifier, description, resolution] Matching Searchable Attributes: [name, identifier, description, resolution]  Sortable Attributes: [name, identifier, updated_at, created_at, id] Searchable Associations: [signature_copy, disabled_external_accounts, integrations] See the filter parameter of the association&#39;s list action to see what attributes are searchable on each association. See Searching on Relationships for more information. See Searching Lists for more information. Example: filter: {name_eq: &#39;Bob&#39;} | [optional] 
 **include** | **str**| Objects that can be included in the response:  service,disabled_external_accounts  See Including Objects for more information. | [optional] 
 **page** | [**dict(str, str)**](str.md)| Page Number and Page Size.  Example: page: {number: 1, size: 20} | [optional] 

### Return type

[**PaginatedCollection**](PaginatedCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
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
external_account_id = 56 # int | The ID of the external account to update the disabled signatures of.
disabled_signature_ids = [56] # list[int] | An array of all the signatures to disable on the external account.

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
 **external_account_id** | **int**| The ID of the external account to update the disabled signatures of. | 
 **disabled_signature_ids** | [**list[int]**](int.md)| An array of all the signatures to disable on the external account. | 

### Return type

[**ExternalAccount**](ExternalAccount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

