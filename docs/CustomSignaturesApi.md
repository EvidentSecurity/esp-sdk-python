# esp_sdk.CustomSignaturesApi

All URIs are relative to https://api.evident.io

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](CustomSignaturesApi.md#create) | **POST** /api/v2/custom_signatures.json_api | Create a(n) Custom Signature
[**delete**](CustomSignaturesApi.md#delete) | **DELETE** /api/v2/custom_signatures/{id}.json_api | Delete a(n) Custom Signature
[**list**](CustomSignaturesApi.md#list) | **PUT** /api/v2/custom_signatures.json_api | Get a list of Custom Signatures
[**show**](CustomSignaturesApi.md#show) | **GET** /api/v2/custom_signatures/{id}.json_api | Show a single Custom Signature
[**update**](CustomSignaturesApi.md#update) | **PATCH** /api/v2/custom_signatures/{id}.json_api | Update a(n) Custom Signature


# **create**
> CustomSignature create(external_account_ids, identifier, name, provider, risk_level, include=include, description=description, include_new_accounts=include_new_accounts, resolution=resolution, service_id=service_id)

Create a(n) Custom Signature



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.CustomSignaturesApi()
external_account_ids = [56] # list[int] | The external account IDs this custom signature should run for. If no accounts are selected the custom signature will not be run.
identifier = 'identifier_example' # str | The identifier to use for the custom signature. Common format is AWS:- such as AWS:IAM-001
name = 'name_example' # str | The name of the custom signature
provider = 'provider_example' # str | The cloud provider this account is for
risk_level = 'risk_level_example' # str | The risk-level of the problem identified by the custom signature. Valid values are low, medium, high
include = 'include_example' # str | Related objects that can be included in the response:  organization, teams, external_accounts, definitions, suppressions, service See Including Objects for more information. (optional)
description = 'description_example' # str | The description of the custom signature that is displayed on alerts (optional)
include_new_accounts = true # bool | When enabled, automatically adds new accounts to this signature. This field can only be set by an organization level user. (optional)
resolution = 'resolution_example' # str | Details for how to resolve this custom signature that is displayed on alerts (optional)
service_id = 56 # int | The service this custom signature is for. If no service is selected it will default to Custom. (optional)

try: 
    # Create a(n) Custom Signature
    api_response = api_instance.create(external_account_ids, identifier, name, provider, risk_level, include=include, description=description, include_new_accounts=include_new_accounts, resolution=resolution, service_id=service_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSignaturesApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_account_ids** | [**list[int]**](int.md)| The external account IDs this custom signature should run for. If no accounts are selected the custom signature will not be run. | 
 **identifier** | **str**| The identifier to use for the custom signature. Common format is AWS:- such as AWS:IAM-001 | 
 **name** | **str**| The name of the custom signature | 
 **provider** | **str**| The cloud provider this account is for | 
 **risk_level** | **str**| The risk-level of the problem identified by the custom signature. Valid values are low, medium, high | 
 **include** | **str**| Related objects that can be included in the response:  organization, teams, external_accounts, definitions, suppressions, service See Including Objects for more information. | [optional] 
 **description** | **str**| The description of the custom signature that is displayed on alerts | [optional] 
 **include_new_accounts** | **bool**| When enabled, automatically adds new accounts to this signature. This field can only be set by an organization level user. | [optional] 
 **resolution** | **str**| Details for how to resolve this custom signature that is displayed on alerts | [optional] 
 **service_id** | **int**| The service this custom signature is for. If no service is selected it will default to Custom. | [optional] 

### Return type

[**CustomSignature**](CustomSignature.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> Meta delete(id)

Delete a(n) Custom Signature



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.CustomSignaturesApi()
id = 56 # int | Custom Signature ID

try: 
    # Delete a(n) Custom Signature
    api_response = api_instance.delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSignaturesApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Custom Signature ID | 

### Return type

[**Meta**](Meta.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> PaginatedCollection list(include=include, filter=filter, page=page)

Get a list of Custom Signatures



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.CustomSignaturesApi()
include = 'include_example' # str | Related objects that can be included in the response:  organization, teams, external_accounts, definitions, suppressions, service See Including Objects for more information. (optional)
filter = {'key': 'filter_example'} # dict(str, str) | Filter Params for Searching.  Equality Searchable Attributes: [id, risk_level, service_id, name, identifier] Matching Searchable Attributes: [name, identifier] Limited Searchable Attribute: [provider_eq] Sortable Attributes: [name, provider, updated_at, created_at, id] Searchable Associations: [organization, teams, definitions, integrations, suppressions] See Searching Lists for more information. See the filter parameter of the association's list action to see what attributes are searchable on each association. See Conditions on Relationships in Searching Lists for more information. (optional)
page = '{:number=>1,+:size=>20}' # str | Page Number and Page Size.  Number is the page number of the collection to return, size is the number of items to return per page. (optional) (default to {:number=>1,+:size=>20})

try: 
    # Get a list of Custom Signatures
    api_response = api_instance.list(include=include, filter=filter, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSignaturesApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include** | **str**| Related objects that can be included in the response:  organization, teams, external_accounts, definitions, suppressions, service See Including Objects for more information. | [optional] 
 **filter** | [**dict(str, str)**](str.md)| Filter Params for Searching.  Equality Searchable Attributes: [id, risk_level, service_id, name, identifier] Matching Searchable Attributes: [name, identifier] Limited Searchable Attribute: [provider_eq] Sortable Attributes: [name, provider, updated_at, created_at, id] Searchable Associations: [organization, teams, definitions, integrations, suppressions] See Searching Lists for more information. See the filter parameter of the association&#39;s list action to see what attributes are searchable on each association. See Conditions on Relationships in Searching Lists for more information. | [optional] 
 **page** | **str**| Page Number and Page Size.  Number is the page number of the collection to return, size is the number of items to return per page. | [optional] [default to {:number&#x3D;&gt;1,+:size&#x3D;&gt;20}]

### Return type

[**PaginatedCollection**](PaginatedCollection.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show**
> CustomSignature show(id, include=include)

Show a single Custom Signature



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.CustomSignaturesApi()
id = 56 # int | Custom Signature ID
include = 'include_example' # str | Related objects that can be included in the response:  organization, teams, external_accounts, definitions, suppressions, service See Including Objects for more information. (optional)

try: 
    # Show a single Custom Signature
    api_response = api_instance.show(id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSignaturesApi->show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Custom Signature ID | 
 **include** | **str**| Related objects that can be included in the response:  organization, teams, external_accounts, definitions, suppressions, service See Including Objects for more information. | [optional] 

### Return type

[**CustomSignature**](CustomSignature.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> CustomSignature update(id, include=include, description=description, external_account_ids=external_account_ids, identifier=identifier, include_new_accounts=include_new_accounts, name=name, resolution=resolution, risk_level=risk_level, service_id=service_id)

Update a(n) Custom Signature



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.CustomSignaturesApi()
id = 56 # int | Custom Signature ID
include = 'include_example' # str | Related objects that can be included in the response:  organization, teams, external_accounts, definitions, suppressions, service See Including Objects for more information. (optional)
description = 'description_example' # str | The description of the custom signature that is displayed on alerts (optional)
external_account_ids = [56] # list[int] | The external account IDs this custom signature should run for. If no accounts are selected the custom signature will not be run. (optional)
identifier = 'identifier_example' # str | The identifier to use for the custom signature. Common format is AWS:- such as AWS:IAM-001 (optional)
include_new_accounts = true # bool | When enabled, automatically adds new accounts to this signature. This field can only be set by an organization level user. (optional)
name = 'name_example' # str | The name of the custom signature (optional)
resolution = 'resolution_example' # str | Details for how to resolve this custom signature that is displayed on alerts (optional)
risk_level = 'risk_level_example' # str | The risk-level of the problem identified by the custom signature. Valid values are low, medium, high (optional)
service_id = 56 # int | The service this custom signature is for. If no service is selected it will default to Custom. (optional)

try: 
    # Update a(n) Custom Signature
    api_response = api_instance.update(id, include=include, description=description, external_account_ids=external_account_ids, identifier=identifier, include_new_accounts=include_new_accounts, name=name, resolution=resolution, risk_level=risk_level, service_id=service_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSignaturesApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Custom Signature ID | 
 **include** | **str**| Related objects that can be included in the response:  organization, teams, external_accounts, definitions, suppressions, service See Including Objects for more information. | [optional] 
 **description** | **str**| The description of the custom signature that is displayed on alerts | [optional] 
 **external_account_ids** | [**list[int]**](int.md)| The external account IDs this custom signature should run for. If no accounts are selected the custom signature will not be run. | [optional] 
 **identifier** | **str**| The identifier to use for the custom signature. Common format is AWS:- such as AWS:IAM-001 | [optional] 
 **include_new_accounts** | **bool**| When enabled, automatically adds new accounts to this signature. This field can only be set by an organization level user. | [optional] 
 **name** | **str**| The name of the custom signature | [optional] 
 **resolution** | **str**| Details for how to resolve this custom signature that is displayed on alerts | [optional] 
 **risk_level** | **str**| The risk-level of the problem identified by the custom signature. Valid values are low, medium, high | [optional] 
 **service_id** | **int**| The service this custom signature is for. If no service is selected it will default to Custom. | [optional] 

### Return type

[**CustomSignature**](CustomSignature.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

