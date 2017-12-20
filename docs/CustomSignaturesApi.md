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
> CustomSignature create(identifier, name, risk_level, external_account_ids, description=description, resolution=resolution, include=include)

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
identifier = 'identifier_example' # str | The identifier to use for the custom signature. Common format is AWS:- such as AWS:IAM-001
name = 'name_example' # str | The name of the custom signature
risk_level = 'risk_level_example' # str | The risk-level of the problem identified by the custom signature. Valid values are low, medium, high
external_account_ids = [56] # list[int] | The external account IDs this custom signature should run for. If no accounts are selected the custom signature will not be run.
description = 'description_example' # str | The description of the custom signature that is displayed on alerts (optional)
resolution = 'resolution_example' # str | Details for how to resolve this custom signature that is displayed on alerts (optional)
include = 'include_example' # str | Related objects that can be included in the response:  organization, teams, external_accounts, definitions See Including Objects for more information. (optional)

try: 
    # Create a(n) Custom Signature
    api_response = api_instance.create(identifier, name, risk_level, external_account_ids, description=description, resolution=resolution, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSignaturesApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| The identifier to use for the custom signature. Common format is AWS:- such as AWS:IAM-001 | 
 **name** | **str**| The name of the custom signature | 
 **risk_level** | **str**| The risk-level of the problem identified by the custom signature. Valid values are low, medium, high | 
 **external_account_ids** | [**list[int]**](int.md)| The external account IDs this custom signature should run for. If no accounts are selected the custom signature will not be run. | 
 **description** | **str**| The description of the custom signature that is displayed on alerts | [optional] 
 **resolution** | **str**| Details for how to resolve this custom signature that is displayed on alerts | [optional] 
 **include** | **str**| Related objects that can be included in the response:  organization, teams, external_accounts, definitions See Including Objects for more information. | [optional] 

### Return type

[**CustomSignature**](CustomSignature.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

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
id = 56 # int |  ID

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
filter = {'key': 'filter_example'} # dict(str, str) | Filter Params for Searching.  Equality Searchable Attributes: [id, risk_level, service_id, name, identifier] Matching Searchable Attributes: [name, identifier]  Sortable Attributes: [name, updated_at, created_at, id] Searchable Associations: [organization, teams, definitions, integrations] See Searching Lists for more information. See the filter parameter of the association's list action to see what attributes are searchable on each association. See Conditions on Relationships in Searching Lists for more information. (optional)
page = '{:number=>1,+:size=>20}' # str | Page Number and Page Size.  number is the page number of the collection to return, size is the number of items to return per page (optional) (default to {:number=>1,+:size=>20})
include = 'include_example' # str | Related objects that can be included in the response:  organization, teams, external_accounts, definitions See Including Objects for more information. (optional)

try: 
    # Get a list of Custom Signatures
    api_response = api_instance.list(filter=filter, page=page, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSignaturesApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | [**dict(str, str)**](str.md)| Filter Params for Searching.  Equality Searchable Attributes: [id, risk_level, service_id, name, identifier] Matching Searchable Attributes: [name, identifier]  Sortable Attributes: [name, updated_at, created_at, id] Searchable Associations: [organization, teams, definitions, integrations] See Searching Lists for more information. See the filter parameter of the association&#39;s list action to see what attributes are searchable on each association. See Conditions on Relationships in Searching Lists for more information. | [optional] 
 **page** | **str**| Page Number and Page Size.  number is the page number of the collection to return, size is the number of items to return per page | [optional] [default to {:number&#x3D;&gt;1,+:size&#x3D;&gt;20}]
 **include** | **str**| Related objects that can be included in the response:  organization, teams, external_accounts, definitions See Including Objects for more information. | [optional] 

### Return type

[**PaginatedCollection**](PaginatedCollection.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

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
include = 'include_example' # str | Related objects that can be included in the response:  organization, teams, external_accounts, definitions See Including Objects for more information. (optional)

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
 **include** | **str**| Related objects that can be included in the response:  organization, teams, external_accounts, definitions See Including Objects for more information. | [optional] 

### Return type

[**CustomSignature**](CustomSignature.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> CustomSignature update(id, description=description, identifier=identifier, name=name, resolution=resolution, risk_level=risk_level, external_account_ids=external_account_ids, include=include)

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
description = 'description_example' # str | The description of the custom signature that is displayed on alerts (optional)
identifier = 'identifier_example' # str | The identifier to use for the custom signature. Common format is AWS:- such as AWS:IAM-001 (optional)
name = 'name_example' # str | The name of the custom signature (optional)
resolution = 'resolution_example' # str | Details for how to resolve this custom signature that is displayed on alerts (optional)
risk_level = 'risk_level_example' # str | The risk-level of the problem identified by the custom signature. Valid values are low, medium, high (optional)
external_account_ids = [56] # list[int] | The external account IDs this custom signature should run for. If no accounts are selected the custom signature will not be run. (optional)
include = 'include_example' # str | Related objects that can be included in the response:  organization, teams, external_accounts, definitions See Including Objects for more information. (optional)

try: 
    # Update a(n) Custom Signature
    api_response = api_instance.update(id, description=description, identifier=identifier, name=name, resolution=resolution, risk_level=risk_level, external_account_ids=external_account_ids, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSignaturesApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Custom Signature ID | 
 **description** | **str**| The description of the custom signature that is displayed on alerts | [optional] 
 **identifier** | **str**| The identifier to use for the custom signature. Common format is AWS:- such as AWS:IAM-001 | [optional] 
 **name** | **str**| The name of the custom signature | [optional] 
 **resolution** | **str**| Details for how to resolve this custom signature that is displayed on alerts | [optional] 
 **risk_level** | **str**| The risk-level of the problem identified by the custom signature. Valid values are low, medium, high | [optional] 
 **external_account_ids** | [**list[int]**](int.md)| The external account IDs this custom signature should run for. If no accounts are selected the custom signature will not be run. | [optional] 
 **include** | **str**| Related objects that can be included in the response:  organization, teams, external_accounts, definitions See Including Objects for more information. | [optional] 

### Return type

[**CustomSignature**](CustomSignature.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

