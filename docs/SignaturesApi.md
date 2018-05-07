# esp_sdk.SignaturesApi

All URIs are relative to https://api.evident.io

Method | HTTP request | Description
------------- | ------------- | -------------
[**list**](SignaturesApi.md#list) | **PUT** /api/v2/signatures.json_api | Get a list of Signatures
[**list_disabled_external_accounts**](SignaturesApi.md#list_disabled_external_accounts) | **GET** /api/v2/signatures/{signature_id}/disabled_external_accounts.json_api | Get a list of disabled External Accounts for a signature
[**list_with_custom_risk_level_for_external_account**](SignaturesApi.md#list_with_custom_risk_level_for_external_account) | **PUT** /api/v2/external_accounts/{external_account_id}/signature_custom_risk_levels.json_api | Get A list of Signatures with default and custom risk levels for an External Account
[**remove_custom_risk_level_for_external_account**](SignaturesApi.md#remove_custom_risk_level_for_external_account) | **DELETE** /api/v2/external_accounts/{external_account_id}/signature_custom_risk_levels/{signature_id}.json_api | Remove a custom risk level to a Signature for an External Account
[**set_custom_risk_level_for_external_account**](SignaturesApi.md#set_custom_risk_level_for_external_account) | **POST** /api/v2/external_accounts/{external_account_id}/signature_custom_risk_levels.json_api | Add a custom risk level to a Signature for an External Account
[**show**](SignaturesApi.md#show) | **GET** /api/v2/signatures/{id}.json_api | Show a single Signature
[**update_custom_risk_level_for_external_account**](SignaturesApi.md#update_custom_risk_level_for_external_account) | **PATCH** /api/v2/external_accounts/{external_account_id}/signature_custom_risk_levels/{signature_id}.json_api | Update a Signature&#39;s custom risk level for an External Account


# **list**
> PaginatedCollection list(include=include, filter=filter, page=page)

Get a list of Signatures



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.SignaturesApi()
include = 'include_example' # str | Related objects that can be included in the response:  service, suppressions See Including Objects for more information. (optional)
filter = {'key': 'filter_example'} # dict(str, str) | Filter Params for Searching.  Equality Searchable Attributes: [id, risk_level, service_id, disabled, supports_user_attribution, name, identifier, description, resolution] Matching Searchable Attributes: [name, identifier, description, resolution] Limited Searchable Attribute: [service_provider_eq] Sortable Attributes: [name, identifier, updated_at, created_at, id] Searchable Associations: [signature_copy, disabled_external_accounts, integrations, suppressions] See Searching Lists for more information. See the filter parameter of the association's list action to see what attributes are searchable on each association. See Conditions on Relationships in Searching Lists for more information. (optional)
page = '{:number=>1,+:size=>20}' # str | Page Number and Page Size.  Number is the page number of the collection to return, size is the number of items to return per page. (optional) (default to {:number=>1,+:size=>20})

try: 
    # Get a list of Signatures
    api_response = api_instance.list(include=include, filter=filter, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SignaturesApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include** | **str**| Related objects that can be included in the response:  service, suppressions See Including Objects for more information. | [optional] 
 **filter** | [**dict(str, str)**](str.md)| Filter Params for Searching.  Equality Searchable Attributes: [id, risk_level, service_id, disabled, supports_user_attribution, name, identifier, description, resolution] Matching Searchable Attributes: [name, identifier, description, resolution] Limited Searchable Attribute: [service_provider_eq] Sortable Attributes: [name, identifier, updated_at, created_at, id] Searchable Associations: [signature_copy, disabled_external_accounts, integrations, suppressions] See Searching Lists for more information. See the filter parameter of the association&#39;s list action to see what attributes are searchable on each association. See Conditions on Relationships in Searching Lists for more information. | [optional] 
 **page** | **str**| Page Number and Page Size.  Number is the page number of the collection to return, size is the number of items to return per page. | [optional] [default to {:number&#x3D;&gt;1,+:size&#x3D;&gt;20}]

### Return type

[**PaginatedCollection**](PaginatedCollection.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_disabled_external_accounts**
> PaginatedCollection list_disabled_external_accounts(signature_id, include=include, filter=filter, page=page)

Get a list of disabled External Accounts for a signature



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.SignaturesApi()
signature_id = 56 # int | The ID of the signature to get the list of disabled external accounts for
include = 'include_example' # str | Related objects that can be included in the response:  organization, sub_organization, team, scan_intervals, disabled_signatures, suppressions, azure_group, credentials See Including Objects for more information. (optional)
filter = {'key': 'filter_example'} # dict(str, str) | Filter Params for Searching.  Equality Searchable Attributes: [id, nickname, name] Matching Searchable Attributes: [nickname, name] Limited Searchable Attributes: [account_eq, arn_eq, provider_eq, subscription_id_eq] Sortable Attributes: [name, updated_at, created_at, id] Searchable Associations: [organization, sub_organization, team, compliance_standards, azure_group, disabled_signatures, suppressions] See Searching Lists for more information. See the filter parameter of the association's list action to see what attributes are searchable on each association. See Conditions on Relationships in Searching Lists for more information. (optional)
page = '{:number=>1,+:size=>20}' # str | Page Number and Page Size.  Number is the page number of the collection to return, size is the number of items to return per page. (optional) (default to {:number=>1,+:size=>20})

try: 
    # Get a list of disabled External Accounts for a signature
    api_response = api_instance.list_disabled_external_accounts(signature_id, include=include, filter=filter, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SignaturesApi->list_disabled_external_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **signature_id** | **int**| The ID of the signature to get the list of disabled external accounts for | 
 **include** | **str**| Related objects that can be included in the response:  organization, sub_organization, team, scan_intervals, disabled_signatures, suppressions, azure_group, credentials See Including Objects for more information. | [optional] 
 **filter** | [**dict(str, str)**](str.md)| Filter Params for Searching.  Equality Searchable Attributes: [id, nickname, name] Matching Searchable Attributes: [nickname, name] Limited Searchable Attributes: [account_eq, arn_eq, provider_eq, subscription_id_eq] Sortable Attributes: [name, updated_at, created_at, id] Searchable Associations: [organization, sub_organization, team, compliance_standards, azure_group, disabled_signatures, suppressions] See Searching Lists for more information. See the filter parameter of the association&#39;s list action to see what attributes are searchable on each association. See Conditions on Relationships in Searching Lists for more information. | [optional] 
 **page** | **str**| Page Number and Page Size.  Number is the page number of the collection to return, size is the number of items to return per page. | [optional] [default to {:number&#x3D;&gt;1,+:size&#x3D;&gt;20}]

### Return type

[**PaginatedCollection**](PaginatedCollection.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_with_custom_risk_level_for_external_account**
> PaginatedCollection list_with_custom_risk_level_for_external_account(external_account_id, include=include, filter=filter, page=page)

Get A list of Signatures with default and custom risk levels for an External Account

Return only signatures that have a custom risk level set by searching with `filter:{custom_risk_level_present: 1}`

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.SignaturesApi()
external_account_id = 56 # int | The ID of the external account to retrieve
include = 'include_example' # str | Related objects that can be included in the response:  service, suppressions See Including Objects for more information. (optional)
filter = {'key': 'filter_example'} # dict(str, str) | Filter Params for Searching.  Equality Searchable Attributes: [id, risk_level, service_id, disabled, supports_user_attribution, name, identifier, description, resolution] Matching Searchable Attributes: [name, identifier, description, resolution] Limited Searchable Attributes: [custom_risk_level_present, service_provider_eq] Sortable Attributes: [name, identifier, updated_at, created_at, id] Searchable Associations: [signature_copy, disabled_external_accounts, integrations, suppressions] See Searching Lists for more information. See the filter parameter of the association's list action to see what attributes are searchable on each association. See Conditions on Relationships in Searching Lists for more information. (optional)
page = '{:number=>1,+:size=>20}' # str | Page Number and Page Size.  Number is the page number of the collection to return, size is the number of items to return per page. (optional) (default to {:number=>1,+:size=>20})

try: 
    # Get A list of Signatures with default and custom risk levels for an External Account
    api_response = api_instance.list_with_custom_risk_level_for_external_account(external_account_id, include=include, filter=filter, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SignaturesApi->list_with_custom_risk_level_for_external_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_account_id** | **int**| The ID of the external account to retrieve | 
 **include** | **str**| Related objects that can be included in the response:  service, suppressions See Including Objects for more information. | [optional] 
 **filter** | [**dict(str, str)**](str.md)| Filter Params for Searching.  Equality Searchable Attributes: [id, risk_level, service_id, disabled, supports_user_attribution, name, identifier, description, resolution] Matching Searchable Attributes: [name, identifier, description, resolution] Limited Searchable Attributes: [custom_risk_level_present, service_provider_eq] Sortable Attributes: [name, identifier, updated_at, created_at, id] Searchable Associations: [signature_copy, disabled_external_accounts, integrations, suppressions] See Searching Lists for more information. See the filter parameter of the association&#39;s list action to see what attributes are searchable on each association. See Conditions on Relationships in Searching Lists for more information. | [optional] 
 **page** | **str**| Page Number and Page Size.  Number is the page number of the collection to return, size is the number of items to return per page. | [optional] [default to {:number&#x3D;&gt;1,+:size&#x3D;&gt;20}]

### Return type

[**PaginatedCollection**](PaginatedCollection.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_custom_risk_level_for_external_account**
> Meta remove_custom_risk_level_for_external_account(external_account_id, signature_id)

Remove a custom risk level to a Signature for an External Account



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.SignaturesApi()
external_account_id = 56 # int | The ID of the external account this signature custom risk level is for
signature_id = 56 # int | The signature ID this signature custom risk level is for

try: 
    # Remove a custom risk level to a Signature for an External Account
    api_response = api_instance.remove_custom_risk_level_for_external_account(external_account_id, signature_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SignaturesApi->remove_custom_risk_level_for_external_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_account_id** | **int**| The ID of the external account this signature custom risk level is for | 
 **signature_id** | **int**| The signature ID this signature custom risk level is for | 

### Return type

[**Meta**](Meta.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_custom_risk_level_for_external_account**
> Signature set_custom_risk_level_for_external_account(external_account_id, risk_level, signature_id, include=include)

Add a custom risk level to a Signature for an External Account



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.SignaturesApi()
external_account_id = 56 # int | The ID of the external account this signature custom risk level is for
risk_level = 'risk_level_example' # str | The custom risk-level of the problem identified by the signature for this external_account. Valid values are low, medium, high
signature_id = 56 # int | The signature ID this signature custom risk level is for
include = 'include_example' # str | Related objects that can be included in the response:  service, suppressions See Including Objects for more information. (optional)

try: 
    # Add a custom risk level to a Signature for an External Account
    api_response = api_instance.set_custom_risk_level_for_external_account(external_account_id, risk_level, signature_id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SignaturesApi->set_custom_risk_level_for_external_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_account_id** | **int**| The ID of the external account this signature custom risk level is for | 
 **risk_level** | **str**| The custom risk-level of the problem identified by the signature for this external_account. Valid values are low, medium, high | 
 **signature_id** | **int**| The signature ID this signature custom risk level is for | 
 **include** | **str**| Related objects that can be included in the response:  service, suppressions See Including Objects for more information. | [optional] 

### Return type

[**Signature**](Signature.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show**
> Signature show(id, include=include)

Show a single Signature



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.SignaturesApi()
id = 56 # int | Signature ID
include = 'include_example' # str | Related objects that can be included in the response:  service, suppressions See Including Objects for more information. (optional)

try: 
    # Show a single Signature
    api_response = api_instance.show(id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SignaturesApi->show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Signature ID | 
 **include** | **str**| Related objects that can be included in the response:  service, suppressions See Including Objects for more information. | [optional] 

### Return type

[**Signature**](Signature.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_custom_risk_level_for_external_account**
> Signature update_custom_risk_level_for_external_account(external_account_id, signature_id, include=include, risk_level=risk_level)

Update a Signature's custom risk level for an External Account



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.SignaturesApi()
external_account_id = 56 # int | The ID of the external account this signature custom risk level is for
signature_id = 56 # int | The signature ID this signature custom risk level is for
include = 'include_example' # str | Related objects that can be included in the response:  service, suppressions See Including Objects for more information. (optional)
risk_level = 'risk_level_example' # str | The custom risk-level of the problem identified by the signature for this external_account. Valid values are low, medium, high (optional)

try: 
    # Update a Signature's custom risk level for an External Account
    api_response = api_instance.update_custom_risk_level_for_external_account(external_account_id, signature_id, include=include, risk_level=risk_level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SignaturesApi->update_custom_risk_level_for_external_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_account_id** | **int**| The ID of the external account this signature custom risk level is for | 
 **signature_id** | **int**| The signature ID this signature custom risk level is for | 
 **include** | **str**| Related objects that can be included in the response:  service, suppressions See Including Objects for more information. | [optional] 
 **risk_level** | **str**| The custom risk-level of the problem identified by the signature for this external_account. Valid values are low, medium, high | [optional] 

### Return type

[**Signature**](Signature.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

