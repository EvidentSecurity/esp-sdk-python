# esp_sdk.CustomSignatureDefinitionsApi

All URIs are relative to https://api.evident.io

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate**](CustomSignatureDefinitionsApi.md#activate) | **PATCH** /api/v2/custom_signature_definitions/{custom_signature_definition_id}/activate.json_api | A successful call to this API marks the definition for activation.  The definition will go into the &#39;validating&#39; state and will be tested before activating. The definition must have a status of editable to be activated.
[**archive**](CustomSignatureDefinitionsApi.md#archive) | **PATCH** /api/v2/custom_signature_definitions/{custom_signature_definition_id}/archive.json_api | A successful call to this API archives and returns a specific custom signature definition identified by the id parameter. The definition must have a status of active to be archived.
[**create**](CustomSignatureDefinitionsApi.md#create) | **POST** /api/v2/custom_signature_definitions.json_api | Create a(n) CustomSignatureDefinition
[**destroy**](CustomSignatureDefinitionsApi.md#destroy) | **DELETE** /api/v2/custom_signature_definitions/{id}.json_api | Remove a(n) CustomSignatureDefinition
[**list**](CustomSignatureDefinitionsApi.md#list) | **PUT** /api/v2/custom_signature_definitions.json_api | Get a list of CustomSignatureDefinitions
[**show**](CustomSignatureDefinitionsApi.md#show) | **GET** /api/v2/custom_signature_definitions/{id}.json_api | Show a single CustomSignatureDefinition
[**update**](CustomSignatureDefinitionsApi.md#update) | **PATCH** /api/v2/custom_signature_definitions/{id}.json_api | Update a(n) CustomSignatureDefinition


# **activate**
> CustomSignatureDefinition activate(custom_signature_definition_id)

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

try: 
    # A successful call to this API marks the definition for activation.  The definition will go into the 'validating' state and will be tested before activating. The definition must have a status of editable to be activated.
    api_response = api_instance.activate(custom_signature_definition_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSignatureDefinitionsApi->activate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_signature_definition_id** | **int**| ID of Custom Signature Definition | 

### Return type

[**CustomSignatureDefinition**](CustomSignatureDefinition.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **archive**
> CustomSignatureDefinition archive(custom_signature_definition_id)

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

try: 
    # A successful call to this API archives and returns a specific custom signature definition identified by the id parameter. The definition must have a status of active to be archived.
    api_response = api_instance.archive(custom_signature_definition_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSignatureDefinitionsApi->archive: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_signature_definition_id** | **int**| ID of Custom Signature Definition | 

### Return type

[**CustomSignatureDefinition**](CustomSignatureDefinition.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create**
> CustomSignatureDefinition create(custom_signature_id)

Create a(n) CustomSignatureDefinition

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

try: 
    # Create a(n) CustomSignatureDefinition
    api_response = api_instance.create(custom_signature_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSignatureDefinitionsApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_signature_id** | **int**| ID of the custom signature this definition belongs to | 

### Return type

[**CustomSignatureDefinition**](CustomSignatureDefinition.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy**
> Meta destroy(id)

Remove a(n) CustomSignatureDefinition

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.CustomSignatureDefinitionsApi()
id = 56 # int | CustomSignatureDefinition ID

try: 
    # Remove a(n) CustomSignatureDefinition
    api_response = api_instance.destroy(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSignatureDefinitionsApi->destroy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| CustomSignatureDefinition ID | 

### Return type

[**Meta**](Meta.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> PaginatedCollection list(filter=filter, include=include, page=page)

Get a list of CustomSignatureDefinitions

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.CustomSignatureDefinitionsApi()
filter = {'key': 'filter_example'} # dict(str, str) | Filter Params for Searching.  See Searching Lists for more information. (optional)
include = 'include_example' # str | Related objects that can be included in the response.  See Including Objects for more information. (optional)
page = '{:number=>1,+:size=>20}' # str | Page Number and Page Size.  number is the page number of the collection to return, size is the number of items to return per page (optional) (default to {:number=>1,+:size=>20})

try: 
    # Get a list of CustomSignatureDefinitions
    api_response = api_instance.list(filter=filter, include=include, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSignatureDefinitionsApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **show**
> CustomSignatureDefinition show(id, include=include)

Show a single CustomSignatureDefinition

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.CustomSignatureDefinitionsApi()
id = 56 # int | CustomSignatureDefinition ID
include = 'include_example' # str | Related objects that can be included in the response.  See Including Objects for more information. (optional)

try: 
    # Show a single CustomSignatureDefinition
    api_response = api_instance.show(id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSignatureDefinitionsApi->show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| CustomSignatureDefinition ID | 
 **include** | **str**| Related objects that can be included in the response.  See Including Objects for more information. | [optional] 

### Return type

[**CustomSignatureDefinition**](CustomSignatureDefinition.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> CustomSignatureDefinition update(id, code, language)

Update a(n) CustomSignatureDefinition

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.CustomSignatureDefinitionsApi()
id = 56 # int | CustomSignatureDefinition ID
code = 'code_example' # str | The code for this definition
language = 'language_example' # str | The language of the definition. Valid values are ruby, javascript

try: 
    # Update a(n) CustomSignatureDefinition
    api_response = api_instance.update(id, code, language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSignatureDefinitionsApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| CustomSignatureDefinition ID | 
 **code** | **str**| The code for this definition | 
 **language** | **str**| The language of the definition. Valid values are ruby, javascript | 

### Return type

[**CustomSignatureDefinition**](CustomSignatureDefinition.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

