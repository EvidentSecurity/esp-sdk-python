# esp_sdk.CustomSignatureDefinitionsApi

All URIs are relative to https://api.evident.io

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate**](CustomSignatureDefinitionsApi.md#activate) | **PATCH** /api/v2/custom_signature_definitions/{custom_signature_definition_id}/activate.json_api | Activate a Custom Signature Definition
[**archive**](CustomSignatureDefinitionsApi.md#archive) | **PATCH** /api/v2/custom_signature_definitions/{custom_signature_definition_id}/archive.json_api | Archive a Custom Signature Definition
[**create**](CustomSignatureDefinitionsApi.md#create) | **POST** /api/v2/custom_signature_definitions.json_api | Create a(n) Custom Signature Definition
[**delete**](CustomSignatureDefinitionsApi.md#delete) | **DELETE** /api/v2/custom_signature_definitions/{id}.json_api | Delete a(n) Custom Signature Definition
[**list**](CustomSignatureDefinitionsApi.md#list) | **PUT** /api/v2/custom_signature_definitions.json_api | Get a list of Custom Signature Definitions
[**show**](CustomSignatureDefinitionsApi.md#show) | **GET** /api/v2/custom_signature_definitions/{id}.json_api | Show a single Custom Signature Definition
[**update**](CustomSignatureDefinitionsApi.md#update) | **PATCH** /api/v2/custom_signature_definitions/{id}.json_api | Update a(n) Custom Signature Definition


# **activate**
> CustomSignatureDefinition activate(custom_signature_definition_id, include=include)

Activate a Custom Signature Definition

A successful call to this API marks the definition for activation.  The definition will go into the 'validating' state and will be tested before activating. The definition must have a status of editable to be activated.

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.CustomSignatureDefinitionsApi()
custom_signature_definition_id = 56 # int | ID of Custom Signature Definition
include = 'include_example' # str | Related objects that can be included in the response:  custom_signature, results See Including Objects for more information. (optional)

try: 
    # Activate a Custom Signature Definition
    api_response = api_instance.activate(custom_signature_definition_id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSignatureDefinitionsApi->activate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_signature_definition_id** | **int**| ID of Custom Signature Definition | 
 **include** | **str**| Related objects that can be included in the response:  custom_signature, results See Including Objects for more information. | [optional] 

### Return type

[**CustomSignatureDefinition**](CustomSignatureDefinition.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **archive**
> CustomSignatureDefinition archive(custom_signature_definition_id, include=include)

Archive a Custom Signature Definition

A successful call to this API archives and returns a specific custom signature definition identified by the id parameter. The definition must have a status of active to be archived.

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.CustomSignatureDefinitionsApi()
custom_signature_definition_id = 56 # int | ID of Custom Signature Definition
include = 'include_example' # str | Related objects that can be included in the response:  custom_signature, results See Including Objects for more information. (optional)

try: 
    # Archive a Custom Signature Definition
    api_response = api_instance.archive(custom_signature_definition_id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSignatureDefinitionsApi->archive: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_signature_definition_id** | **int**| ID of Custom Signature Definition | 
 **include** | **str**| Related objects that can be included in the response:  custom_signature, results See Including Objects for more information. | [optional] 

### Return type

[**CustomSignatureDefinition**](CustomSignatureDefinition.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create**
> CustomSignatureDefinition create(custom_signature_id, include=include)

Create a(n) Custom Signature Definition



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.CustomSignatureDefinitionsApi()
custom_signature_id = 56 # int | ID of the custom signature this definition belongs to
include = 'include_example' # str | Related objects that can be included in the response:  custom_signature, results See Including Objects for more information. (optional)

try: 
    # Create a(n) Custom Signature Definition
    api_response = api_instance.create(custom_signature_id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSignatureDefinitionsApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_signature_id** | **int**| ID of the custom signature this definition belongs to | 
 **include** | **str**| Related objects that can be included in the response:  custom_signature, results See Including Objects for more information. | [optional] 

### Return type

[**CustomSignatureDefinition**](CustomSignatureDefinition.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> Meta delete(id)

Delete a(n) Custom Signature Definition



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.CustomSignatureDefinitionsApi()
id = 56 # int |  ID

try: 
    # Delete a(n) Custom Signature Definition
    api_response = api_instance.delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSignatureDefinitionsApi->delete: %s\n" % e)
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

Get a list of Custom Signature Definitions



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.CustomSignatureDefinitionsApi()
filter = {'key': 'filter_example'} # dict(str, str) | Filter Params for Searching.  Equality Searchable Attributes: [id, language, status, version_number]    Searchable Association: [custom_signature] See Searching Lists for more information. See the filter parameter of the association's list action to see what attributes are searchable on each association. See Conditions on Relationships in Searching Lists for more information. (optional)
page = '{:number=>1,+:size=>20}' # str | Page Number and Page Size.  number is the page number of the collection to return, size is the number of items to return per page (optional) (default to {:number=>1,+:size=>20})
include = 'include_example' # str | Related objects that can be included in the response:  custom_signature, results See Including Objects for more information. (optional)

try: 
    # Get a list of Custom Signature Definitions
    api_response = api_instance.list(filter=filter, page=page, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSignatureDefinitionsApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | [**dict(str, str)**](str.md)| Filter Params for Searching.  Equality Searchable Attributes: [id, language, status, version_number]    Searchable Association: [custom_signature] See Searching Lists for more information. See the filter parameter of the association&#39;s list action to see what attributes are searchable on each association. See Conditions on Relationships in Searching Lists for more information. | [optional] 
 **page** | **str**| Page Number and Page Size.  number is the page number of the collection to return, size is the number of items to return per page | [optional] [default to {:number&#x3D;&gt;1,+:size&#x3D;&gt;20}]
 **include** | **str**| Related objects that can be included in the response:  custom_signature, results See Including Objects for more information. | [optional] 

### Return type

[**PaginatedCollection**](PaginatedCollection.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show**
> CustomSignatureDefinition show(id, include=include)

Show a single Custom Signature Definition



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.CustomSignatureDefinitionsApi()
id = 56 # int | Custom Signature Definition ID
include = 'include_example' # str | Related objects that can be included in the response:  custom_signature, results See Including Objects for more information. (optional)

try: 
    # Show a single Custom Signature Definition
    api_response = api_instance.show(id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSignatureDefinitionsApi->show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Custom Signature Definition ID | 
 **include** | **str**| Related objects that can be included in the response:  custom_signature, results See Including Objects for more information. | [optional] 

### Return type

[**CustomSignatureDefinition**](CustomSignatureDefinition.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> CustomSignatureDefinition update(id, code=code, language=language, include=include)

Update a(n) Custom Signature Definition



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.CustomSignatureDefinitionsApi()
id = 56 # int | Custom Signature Definition ID
code = 'code_example' # str | The code for this definition (optional)
language = 'language_example' # str | The language of the definition. Valid values are ruby, javascript (optional)
include = 'include_example' # str | Related objects that can be included in the response:  custom_signature, results See Including Objects for more information. (optional)

try: 
    # Update a(n) Custom Signature Definition
    api_response = api_instance.update(id, code=code, language=language, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSignatureDefinitionsApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Custom Signature Definition ID | 
 **code** | **str**| The code for this definition | [optional] 
 **language** | **str**| The language of the definition. Valid values are ruby, javascript | [optional] 
 **include** | **str**| Related objects that can be included in the response:  custom_signature, results See Including Objects for more information. | [optional] 

### Return type

[**CustomSignatureDefinition**](CustomSignatureDefinition.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

