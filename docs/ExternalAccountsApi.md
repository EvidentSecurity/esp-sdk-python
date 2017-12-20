# esp_sdk.ExternalAccountsApi

All URIs are relative to https://api.evident.io

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_compliance_standard**](ExternalAccountsApi.md#add_compliance_standard) | **POST** /api/v2/external_accounts/{external_account_id}/compliance_standards.json_api | Add a compliance standard to an external account
[**add_custom_compliance_standard**](ExternalAccountsApi.md#add_custom_compliance_standard) | **POST** /api/v2/external_accounts/{external_account_id}/custom_compliance_standards.json_api | Add a custom compliance standard to an external account
[**add_disabled_signature**](ExternalAccountsApi.md#add_disabled_signature) | **POST** /api/v2/external_accounts/{external_account_id}/disabled_signatures.json_api | Disable a signature for an external account
[**delete**](ExternalAccountsApi.md#delete) | **DELETE** /api/v2/external_accounts/{id}.json_api | Delete a(n) External Account
[**list**](ExternalAccountsApi.md#list) | **PUT** /api/v2/external_accounts.json_api | Get a list of External Accounts
[**list_compliance_standards**](ExternalAccountsApi.md#list_compliance_standards) | **GET** /api/v2/external_accounts/{external_account_id}/compliance_standards.json_api | Get a list of compliance standards for an external account
[**list_custom_compliance_standards**](ExternalAccountsApi.md#list_custom_compliance_standards) | **GET** /api/v2/external_accounts/{external_account_id}/custom_compliance_standards.json_api | Get a list of custom compliance standards for an external account
[**list_disabled_signatures**](ExternalAccountsApi.md#list_disabled_signatures) | **PUT** /api/v2/external_accounts/{external_account_id}/disabled_signatures.json_api | Get a list all the disabled signatures for an external account
[**remove_compliance_standard**](ExternalAccountsApi.md#remove_compliance_standard) | **DELETE** /api/v2/external_accounts/{external_account_id}/compliance_standards/{compliance_standard_id}.json_api | Remove a compliance standard from an external account
[**remove_custom_compliance_standard**](ExternalAccountsApi.md#remove_custom_compliance_standard) | **DELETE** /api/v2/external_accounts/{external_account_id}/custom_compliance_standards/{custom_compliance_standard_id}.json_api | Remove a custom compliance standard from an external account
[**remove_disabled_signature**](ExternalAccountsApi.md#remove_disabled_signature) | **DELETE** /api/v2/external_accounts/{external_account_id}/disabled_signatures/{signature_id}.json_api | Re-enable a signature for an external account
[**show**](ExternalAccountsApi.md#show) | **GET** /api/v2/external_accounts/{id}.json_api | Show a single External Account


# **add_compliance_standard**
> ComplianceStandard add_compliance_standard(external_account_id, compliance_standard_id, include=include)

Add a compliance standard to an external account



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.ExternalAccountsApi()
external_account_id = 56 # int | The ID of the external account this compliance standard belongs to
compliance_standard_id = 56 # int | The ID of the compliance standard that belongs to this external account
include = 'include_example' # str | Related objects that can be included in the response:  compliance_domains, compliance_controls See Including Objects for more information. (optional)

try: 
    # Add a compliance standard to an external account
    api_response = api_instance.add_compliance_standard(external_account_id, compliance_standard_id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalAccountsApi->add_compliance_standard: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_account_id** | **int**| The ID of the external account this compliance standard belongs to | 
 **compliance_standard_id** | **int**| The ID of the compliance standard that belongs to this external account | 
 **include** | **str**| Related objects that can be included in the response:  compliance_domains, compliance_controls See Including Objects for more information. | [optional] 

### Return type

[**ComplianceStandard**](ComplianceStandard.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_custom_compliance_standard**
> Meta add_custom_compliance_standard(external_account_id, custom_compliance_standard_id)

Add a custom compliance standard to an external account



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.ExternalAccountsApi()
external_account_id = 56 # int | The ID of the external account this custom compliance standard belongs to
custom_compliance_standard_id = 56 # int | The ID of the custom compliance standard that belongs to this external account

try: 
    # Add a custom compliance standard to an external account
    api_response = api_instance.add_custom_compliance_standard(external_account_id, custom_compliance_standard_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalAccountsApi->add_custom_compliance_standard: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_account_id** | **int**| The ID of the external account this custom compliance standard belongs to | 
 **custom_compliance_standard_id** | **int**| The ID of the custom compliance standard that belongs to this external account | 

### Return type

[**Meta**](Meta.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_disabled_signature**
> Signature add_disabled_signature(external_account_id, signature_id, include=include)

Disable a signature for an external account



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.ExternalAccountsApi()
external_account_id = 56 # int | The ID of the external account to disable a signature on
signature_id = 56 # int | The ID of the signature to disable
include = 'include_example' # str | Related objects that can be included in the response:  service See Including Objects for more information. (optional)

try: 
    # Disable a signature for an external account
    api_response = api_instance.add_disabled_signature(external_account_id, signature_id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalAccountsApi->add_disabled_signature: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_account_id** | **int**| The ID of the external account to disable a signature on | 
 **signature_id** | **int**| The ID of the signature to disable | 
 **include** | **str**| Related objects that can be included in the response:  service See Including Objects for more information. | [optional] 

### Return type

[**Signature**](Signature.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> Meta delete(id)

Delete a(n) External Account



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.ExternalAccountsApi()
id = 56 # int |  ID

try: 
    # Delete a(n) External Account
    api_response = api_instance.delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalAccountsApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  ID | 

### Return type

[**Meta**](Meta.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> PaginatedCollection list(filter=filter, page=page, include=include)

Get a list of External Accounts



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.ExternalAccountsApi()
filter = {'key': 'filter_example'} # dict(str, str) | Filter Params for Searching.  Equality Searchable Attributes: [id, nickname, name] Matching Searchable Attributes: [nickname, name] Limited Searchable Attributes: [account_eq, arn_eq, provider_eq, subscription_id_eq] Sortable Attributes: [name, updated_at, created_at, id] Searchable Associations: [organization, sub_organization, team, compliance_standards, azure_group, disabled_signatures] See Searching Lists for more information. See the filter parameter of the association's list action to see what attributes are searchable on each association. See Conditions on Relationships in Searching Lists for more information. (optional)
page = '{:number=>1,+:size=>20}' # str | Page Number and Page Size.  number is the page number of the collection to return, size is the number of items to return per page (optional) (default to {:number=>1,+:size=>20})
include = 'include_example' # str | Related objects that can be included in the response:  organization, sub_organization, team, scan_intervals, disabled_signatures, azure_group, credentials See Including Objects for more information. (optional)

try: 
    # Get a list of External Accounts
    api_response = api_instance.list(filter=filter, page=page, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalAccountsApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | [**dict(str, str)**](str.md)| Filter Params for Searching.  Equality Searchable Attributes: [id, nickname, name] Matching Searchable Attributes: [nickname, name] Limited Searchable Attributes: [account_eq, arn_eq, provider_eq, subscription_id_eq] Sortable Attributes: [name, updated_at, created_at, id] Searchable Associations: [organization, sub_organization, team, compliance_standards, azure_group, disabled_signatures] See Searching Lists for more information. See the filter parameter of the association&#39;s list action to see what attributes are searchable on each association. See Conditions on Relationships in Searching Lists for more information. | [optional] 
 **page** | **str**| Page Number and Page Size.  number is the page number of the collection to return, size is the number of items to return per page | [optional] [default to {:number&#x3D;&gt;1,+:size&#x3D;&gt;20}]
 **include** | **str**| Related objects that can be included in the response:  organization, sub_organization, team, scan_intervals, disabled_signatures, azure_group, credentials See Including Objects for more information. | [optional] 

### Return type

[**PaginatedCollection**](PaginatedCollection.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_compliance_standards**
> PaginatedCollection list_compliance_standards(external_account_id, page=page, include=include)

Get a list of compliance standards for an external account



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.ExternalAccountsApi()
external_account_id = 56 # int | The ID of the external account this compliance standard belongs to
page = '{:number=>1,+:size=>20}' # str | Page Number and Page Size.  number is the page number of the collection to return, size is the number of items to return per page (optional) (default to {:number=>1,+:size=>20})
include = 'include_example' # str | Related objects that can be included in the response:  compliance_domains, compliance_controls See Including Objects for more information. (optional)

try: 
    # Get a list of compliance standards for an external account
    api_response = api_instance.list_compliance_standards(external_account_id, page=page, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalAccountsApi->list_compliance_standards: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_account_id** | **int**| The ID of the external account this compliance standard belongs to | 
 **page** | **str**| Page Number and Page Size.  number is the page number of the collection to return, size is the number of items to return per page | [optional] [default to {:number&#x3D;&gt;1,+:size&#x3D;&gt;20}]
 **include** | **str**| Related objects that can be included in the response:  compliance_domains, compliance_controls See Including Objects for more information. | [optional] 

### Return type

[**PaginatedCollection**](PaginatedCollection.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_custom_compliance_standards**
> PaginatedCollection list_custom_compliance_standards(external_account_id, page=page, include=include)

Get a list of custom compliance standards for an external account



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.ExternalAccountsApi()
external_account_id = 56 # int | The ID of the external account this custom compliance standard belongs to
page = '{:number=>1,+:size=>20}' # str | Page Number and Page Size.  number is the page number of the collection to return, size is the number of items to return per page (optional) (default to {:number=>1,+:size=>20})
include = 'include_example' # str | Related objects that can be included in the response:  custom_compliance_domains, custom_compliance_controls See Including Objects for more information. (optional)

try: 
    # Get a list of custom compliance standards for an external account
    api_response = api_instance.list_custom_compliance_standards(external_account_id, page=page, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalAccountsApi->list_custom_compliance_standards: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_account_id** | **int**| The ID of the external account this custom compliance standard belongs to | 
 **page** | **str**| Page Number and Page Size.  number is the page number of the collection to return, size is the number of items to return per page | [optional] [default to {:number&#x3D;&gt;1,+:size&#x3D;&gt;20}]
 **include** | **str**| Related objects that can be included in the response:  custom_compliance_domains, custom_compliance_controls See Including Objects for more information. | [optional] 

### Return type

[**PaginatedCollection**](PaginatedCollection.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_disabled_signatures**
> PaginatedCollection list_disabled_signatures(external_account_id, filter=filter, page=page, include=include)

Get a list all the disabled signatures for an external account



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.ExternalAccountsApi()
external_account_id = 56 # int | The ID of the external account to retrieve the disabled signatures for
filter = {'key': 'filter_example'} # dict(str, str) | Filter Params for Searching.  Equality Searchable Attributes: [id, risk_level, service_id, disabled, supports_user_attribution, name, identifier, description, resolution] Matching Searchable Attributes: [name, identifier, description, resolution] Limited Searchable Attribute: [service_provider_eq] Sortable Attributes: [name, identifier, updated_at, created_at, id] Searchable Associations: [signature_copy, disabled_external_accounts, integrations] See Searching Lists for more information. See the filter parameter of the association's list action to see what attributes are searchable on each association. See Conditions on Relationships in Searching Lists for more information. (optional)
page = '{:number=>1,+:size=>20}' # str | Page Number and Page Size.  number is the page number of the collection to return, size is the number of items to return per page (optional) (default to {:number=>1,+:size=>20})
include = 'include_example' # str | Related objects that can be included in the response:  service See Including Objects for more information. (optional)

try: 
    # Get a list all the disabled signatures for an external account
    api_response = api_instance.list_disabled_signatures(external_account_id, filter=filter, page=page, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalAccountsApi->list_disabled_signatures: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_account_id** | **int**| The ID of the external account to retrieve the disabled signatures for | 
 **filter** | [**dict(str, str)**](str.md)| Filter Params for Searching.  Equality Searchable Attributes: [id, risk_level, service_id, disabled, supports_user_attribution, name, identifier, description, resolution] Matching Searchable Attributes: [name, identifier, description, resolution] Limited Searchable Attribute: [service_provider_eq] Sortable Attributes: [name, identifier, updated_at, created_at, id] Searchable Associations: [signature_copy, disabled_external_accounts, integrations] See Searching Lists for more information. See the filter parameter of the association&#39;s list action to see what attributes are searchable on each association. See Conditions on Relationships in Searching Lists for more information. | [optional] 
 **page** | **str**| Page Number and Page Size.  number is the page number of the collection to return, size is the number of items to return per page | [optional] [default to {:number&#x3D;&gt;1,+:size&#x3D;&gt;20}]
 **include** | **str**| Related objects that can be included in the response:  service See Including Objects for more information. | [optional] 

### Return type

[**PaginatedCollection**](PaginatedCollection.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_compliance_standard**
> Meta remove_compliance_standard(external_account_id, compliance_standard_id)

Remove a compliance standard from an external account



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.ExternalAccountsApi()
external_account_id = 56 # int | The ID of the external account this compliance standard belongs to
compliance_standard_id = 56 # int | The ID of the compliance standard that belongs to this external account

try: 
    # Remove a compliance standard from an external account
    api_response = api_instance.remove_compliance_standard(external_account_id, compliance_standard_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalAccountsApi->remove_compliance_standard: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_account_id** | **int**| The ID of the external account this compliance standard belongs to | 
 **compliance_standard_id** | **int**| The ID of the compliance standard that belongs to this external account | 

### Return type

[**Meta**](Meta.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_custom_compliance_standard**
> Meta remove_custom_compliance_standard(external_account_id, custom_compliance_standard_id)

Remove a custom compliance standard from an external account



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.ExternalAccountsApi()
external_account_id = 56 # int | The ID of the external account this custom compliance standard belongs to
custom_compliance_standard_id = 56 # int | The ID of the custom compliance standard that belongs to this external account

try: 
    # Remove a custom compliance standard from an external account
    api_response = api_instance.remove_custom_compliance_standard(external_account_id, custom_compliance_standard_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalAccountsApi->remove_custom_compliance_standard: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_account_id** | **int**| The ID of the external account this custom compliance standard belongs to | 
 **custom_compliance_standard_id** | **int**| The ID of the custom compliance standard that belongs to this external account | 

### Return type

[**Meta**](Meta.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_disabled_signature**
> Meta remove_disabled_signature(external_account_id, signature_id)

Re-enable a signature for an external account



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.ExternalAccountsApi()
external_account_id = 56 # int | The ID of the external account to enable a signature on
signature_id = 56 # int | The ID of the signature to enable

try: 
    # Re-enable a signature for an external account
    api_response = api_instance.remove_disabled_signature(external_account_id, signature_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalAccountsApi->remove_disabled_signature: %s\n" % e)
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

# **show**
> ExternalAccount show(id, include=include)

Show a single External Account



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.ExternalAccountsApi()
id = 56 # int | External Account ID
include = 'include_example' # str | Related objects that can be included in the response:  organization, sub_organization, team, scan_intervals, disabled_signatures, azure_group, credentials See Including Objects for more information. (optional)

try: 
    # Show a single External Account
    api_response = api_instance.show(id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalAccountsApi->show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| External Account ID | 
 **include** | **str**| Related objects that can be included in the response:  organization, sub_organization, team, scan_intervals, disabled_signatures, azure_group, credentials See Including Objects for more information. | [optional] 

### Return type

[**ExternalAccount**](ExternalAccount.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

