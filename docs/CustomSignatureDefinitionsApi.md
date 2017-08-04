# esp_sdk.CustomSignatureDefinitionsApi

All URIs are relative to *http://localhost/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate**](CustomSignatureDefinitionsApi.md#activate) | **PATCH** /api/v2/custom_signature_definitions/{custom_signature_definition_id}/activate.json_api | A successful call to this API activates and returns a specific custom signature definition identified by the id parameter. The definition must have a status of editable to be activated.
[**archive**](CustomSignatureDefinitionsApi.md#archive) | **PATCH** /api/v2/custom_signature_definitions/{custom_signature_definition_id}/archive.json_api | A successful call to this API archives and returns a specific custom signature definition identified by the id parameter. The definition must have a status of active to be archived.
[**create**](CustomSignatureDefinitionsApi.md#create) | **POST** /api/v2/custom_signature_definitions.json_api | Create a(n) Custom Signature/Definition
[**destroy**](CustomSignatureDefinitionsApi.md#destroy) | **DELETE** /api/v2/custom_signature_definitions/{id}.json_api | Remove a(n) CustomSignature::Definition
[**list**](CustomSignatureDefinitionsApi.md#list) | **PUT** /api/v2/custom_signature_definitions.json_api | Get a list of Custom Signature/Definitions
[**show**](CustomSignatureDefinitionsApi.md#show) | **GET** /api/v2/custom_signature_definitions/{id}.json_api | Show a single Custom Signature/Definition
[**update**](CustomSignatureDefinitionsApi.md#update) | **PATCH** /api/v2/custom_signature_definitions/{id}.json_api | Update a(n) Custom Signature/Definition


# **activate**
> CustomSignatureDefinition activate(custom_signature_definition_id)

A successful call to this API activates and returns a specific custom signature definition identified by the id parameter. The definition must have a status of editable to be activated.

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.CustomSignatureDefinitionsApi()
custom_signature_definition_id = 56 # int | Custom Signature Definition Id

try: 
    # A successful call to this API activates and returns a specific custom signature definition identified by the id parameter. The definition must have a status of editable to be activated.
    api_response = api_instance.activate(custom_signature_definition_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSignatureDefinitionsApi->activate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_signature_definition_id** | **int**| Custom Signature Definition Id | 

### Return type

[**CustomSignatureDefinition**](CustomSignatureDefinition.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
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
custom_signature_definition_id = 56 # int | Custom Signature Definition Id

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
 **custom_signature_definition_id** | **int**| Custom Signature Definition Id | 

### Return type

[**CustomSignatureDefinition**](CustomSignatureDefinition.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create**
> CustomSignatureDefinition create(custom_signature_id)

Create a(n) Custom Signature/Definition

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.CustomSignatureDefinitionsApi()
custom_signature_id = 56 # int | ID of the custom signature this definition should belong to.

try: 
    # Create a(n) Custom Signature/Definition
    api_response = api_instance.create(custom_signature_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSignatureDefinitionsApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_signature_id** | **int**| ID of the custom signature this definition should belong to. | 

### Return type

[**CustomSignatureDefinition**](CustomSignatureDefinition.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy**
> CustomSignatureDefinition destroy(id)

Remove a(n) CustomSignature::Definition

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.CustomSignatureDefinitionsApi()
id = 56 # int | CustomSignature::Definition Id

try: 
    # Remove a(n) CustomSignature::Definition
    api_response = api_instance.destroy(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSignatureDefinitionsApi->destroy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| CustomSignature::Definition Id | 

### Return type

[**CustomSignatureDefinition**](CustomSignatureDefinition.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> PaginatedCollection list(filter=filter, include=include, page=page)

Get a list of Custom Signature/Definitions

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.CustomSignatureDefinitionsApi()
filter = {'key': 'filter_example'} # dict(str, str) | Filter Params for Searching.  Equality Searchable Attributes: [id, language, status, version_number]    Searchable Association: [custom_signature] See the filter parameter of the association's list action to see what attributes are searchable on each association. See Searching on Relationships for more information. See Searching Lists for more information. Example: filter: {name_eq: 'Bob'} (optional)
include = 'include_example' # str | Objects that can be included in the response:  custom_signature,results  See Including Objects for more information. (optional)
page = {'key': 'page_example'} # dict(str, str) | Page Number and Page Size.  Example: page: {number: 1, size: 20} (optional)

try: 
    # Get a list of Custom Signature/Definitions
    api_response = api_instance.list(filter=filter, include=include, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSignatureDefinitionsApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | [**dict(str, str)**](str.md)| Filter Params for Searching.  Equality Searchable Attributes: [id, language, status, version_number]    Searchable Association: [custom_signature] See the filter parameter of the association&#39;s list action to see what attributes are searchable on each association. See Searching on Relationships for more information. See Searching Lists for more information. Example: filter: {name_eq: &#39;Bob&#39;} | [optional] 
 **include** | **str**| Objects that can be included in the response:  custom_signature,results  See Including Objects for more information. | [optional] 
 **page** | [**dict(str, str)**](str.md)| Page Number and Page Size.  Example: page: {number: 1, size: 20} | [optional] 

### Return type

[**PaginatedCollection**](PaginatedCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show**
> CustomSignatureDefinition show(id, include=include)

Show a single Custom Signature/Definition

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.CustomSignatureDefinitionsApi()
id = 56 # int | Custom Signature/Definition Id
include = 'include_example' # str | Objects that can be included in the response:  custom_signature,results  See Including Objects for more information. (optional)

try: 
    # Show a single Custom Signature/Definition
    api_response = api_instance.show(id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSignatureDefinitionsApi->show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Custom Signature/Definition Id | 
 **include** | **str**| Objects that can be included in the response:  custom_signature,results  See Including Objects for more information. | [optional] 

### Return type

[**CustomSignatureDefinition**](CustomSignatureDefinition.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> CustomSignatureDefinition update(id, code, language)

Update a(n) Custom Signature/Definition

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.CustomSignatureDefinitionsApi()
id = 56 # int | Custom Signature/Definition Id
code = 'code_example' # str | The code for the definition
language = 'language_example' # str | The language of the code

try: 
    # Update a(n) Custom Signature/Definition
    api_response = api_instance.update(id, code, language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSignatureDefinitionsApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Custom Signature/Definition Id | 
 **code** | **str**| The code for the definition | 
 **language** | **str**| The language of the code | 

### Return type

[**CustomSignatureDefinition**](CustomSignatureDefinition.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

