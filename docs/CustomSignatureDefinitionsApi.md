# esp_sdk.CustomSignatureDefinitionsApi

All URIs are relative to *http://localhost/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](CustomSignatureDefinitionsApi.md#create) | **POST** /api/v2/custom_signature_definitions.json_api | Create a(n) Definition
[**destroy**](CustomSignatureDefinitionsApi.md#destroy) | **DELETE** /api/v2/custom_signature_definitions/{id}.json_api | Remove a(n) Definition
[**list**](CustomSignatureDefinitionsApi.md#list) | **PUT** /api/v2/custom_signature_definitions.json_api | Get a list of Definitions
[**show**](CustomSignatureDefinitionsApi.md#show) | **GET** /api/v2/custom_signature_definitions/{id}.json_api | Show a single Definition
[**update**](CustomSignatureDefinitionsApi.md#update) | **PATCH** /api/v2/custom_signature_definitions/{id}.json_api | Update a(n) Definition


# **create**
> Definition create(custom_signature_id)

Create a(n) Definition

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
    # Create a(n) Definition
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

[**Definition**](Definition.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy**
> object destroy(id)

Remove a(n) Definition

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.CustomSignatureDefinitionsApi()
id = 56 # int | Definition Id

try: 
    # Remove a(n) Definition
    api_response = api_instance.destroy(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSignatureDefinitionsApi->destroy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Definition Id | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> PaginatedCollection list(page=page, filter=filter, include=include)

Get a list of Definitions

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.CustomSignatureDefinitionsApi()
page = {'key': 'page_example'} # dict(str, str) | Page Number (optional)
filter = {'key': 'filter_example'} # dict(str, str) | Filter Params for Searching (optional)
include = 'include_example' # str | Included Objects (optional)

try: 
    # Get a list of Definitions
    api_response = api_instance.list(page=page, filter=filter, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSignatureDefinitionsApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | [**dict(str, str)**](str.md)| Page Number | [optional] 
 **filter** | [**dict(str, str)**](str.md)| Filter Params for Searching | [optional] 
 **include** | **str**| Included Objects | [optional] 

### Return type

[**PaginatedCollection**](PaginatedCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show**
> Definition show(id, include=include)

Show a single Definition

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.CustomSignatureDefinitionsApi()
id = 56 # int | Definition Id
include = 'include_example' # str | Included Objects (optional)

try: 
    # Show a single Definition
    api_response = api_instance.show(id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSignatureDefinitionsApi->show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Definition Id | 
 **include** | **str**| Included Objects | [optional] 

### Return type

[**Definition**](Definition.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> Definition update(id, code, language)

Update a(n) Definition

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.CustomSignatureDefinitionsApi()
id = 56 # int | Definition Id
code = 'code_example' # str | The code for the definition
language = 'language_example' # str | The language of the code

try: 
    # Update a(n) Definition
    api_response = api_instance.update(id, code, language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSignatureDefinitionsApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Definition Id | 
 **code** | **str**| The code for the definition | 
 **language** | **str**| The language of the code | 

### Return type

[**Definition**](Definition.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

