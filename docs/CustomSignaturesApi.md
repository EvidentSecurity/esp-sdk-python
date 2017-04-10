# esp_sdk.CustomSignaturesApi

All URIs are relative to *http://localhost/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](CustomSignaturesApi.md#create) | **POST** /api/v2/custom_signatures.json_api | Create a(n) Custom Signature
[**destroy**](CustomSignaturesApi.md#destroy) | **DELETE** /api/v2/custom_signatures/{id}.json_api | Remove a(n) Custom Signature
[**list**](CustomSignaturesApi.md#list) | **PUT** /api/v2/custom_signatures.json_api | Get a list of Custom Signatures
[**show**](CustomSignaturesApi.md#show) | **GET** /api/v2/custom_signatures/{id}.json_api | Show a single Custom Signature
[**update**](CustomSignaturesApi.md#update) | **PATCH** /api/v2/custom_signatures/{id}.json_api | Update a(n) Custom Signature


# **create**
> CustomSignature create(name)

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
name = 'name_example' # str | Name

try: 
    # Create a(n) Custom Signature
    api_response = api_instance.create(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSignaturesApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name | 

### Return type

[**CustomSignature**](CustomSignature.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy**
> object destroy(id)

Remove a(n) Custom Signature

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.CustomSignaturesApi()
id = 56 # int | Custom Signature Id

try: 
    # Remove a(n) Custom Signature
    api_response = api_instance.destroy(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSignaturesApi->destroy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Custom Signature Id | 

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
page = {'key': 'page_example'} # dict(str, str) | Page Number (optional)
filter = {'key': 'filter_example'} # dict(str, str) | Filter Params for Searching (optional)
include = 'include_example' # str | Included Objects (optional)

try: 
    # Get a list of Custom Signatures
    api_response = api_instance.list(page=page, filter=filter, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSignaturesApi->list: %s\n" % e)
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
id = 56 # int | Custom Signature Id
include = 'include_example' # str | Included Objects (optional)

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
 **id** | **int**| Custom Signature Id | 
 **include** | **str**| Included Objects | [optional] 

### Return type

[**CustomSignature**](CustomSignature.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> CustomSignature update(id, name)

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
id = 56 # int | Custom Signature Id
name = 'name_example' # str | Name

try: 
    # Update a(n) Custom Signature
    api_response = api_instance.update(id, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSignaturesApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Custom Signature Id | 
 **name** | **str**| Name | 

### Return type

[**CustomSignature**](CustomSignature.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

