# esp_sdk.CustomSignatureResultsApi

All URIs are relative to *http://localhost/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](CustomSignatureResultsApi.md#create) | **POST** /api/v2/custom_signature_results.json_api | Create a(n) Result
[**list**](CustomSignatureResultsApi.md#list) | **PUT** /api/v2/custom_signature_results.json_api | Get a list of Results
[**show**](CustomSignatureResultsApi.md#show) | **GET** /api/v2/custom_signature_results/{id}.json_api | Show a single Result


# **create**
> Result create(code, custom_signature_definition_id, external_account_id, language, region_id, region=region)

Create a(n) Result

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.CustomSignatureResultsApi()
code = 'code_example' # str | The code to run
custom_signature_definition_id = 56 # int | ID of the custom signature definition this result should belong to.
external_account_id = 56 # int | ID of the external account the code should run for.
language = 'language_example' # str | The language of the code
region_id = 56 # int | ID of the region the code should run for.
region = 'region_example' # str | Code of the region the result code should run for. Ex: us-east-1. This can be sent instead of region_id (optional)

try: 
    # Create a(n) Result
    api_response = api_instance.create(code, custom_signature_definition_id, external_account_id, language, region_id, region=region)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSignatureResultsApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The code to run | 
 **custom_signature_definition_id** | **int**| ID of the custom signature definition this result should belong to. | 
 **external_account_id** | **int**| ID of the external account the code should run for. | 
 **language** | **str**| The language of the code | 
 **region_id** | **int**| ID of the region the code should run for. | 
 **region** | **str**| Code of the region the result code should run for. Ex: us-east-1. This can be sent instead of region_id | [optional] 

### Return type

[**Result**](Result.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> PaginatedCollection list(page=page, filter=filter, include=include)

Get a list of Results

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.CustomSignatureResultsApi()
page = {'key': 'page_example'} # dict(str, str) | Page Number (optional)
filter = {'key': 'filter_example'} # dict(str, str) | Filter Params for Searching (optional)
include = 'include_example' # str | Included Objects (optional)

try: 
    # Get a list of Results
    api_response = api_instance.list(page=page, filter=filter, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSignatureResultsApi->list: %s\n" % e)
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
> Result show(id, include=include)

Show a single Result

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.CustomSignatureResultsApi()
id = 56 # int | Result Id
include = 'include_example' # str | Included Objects (optional)

try: 
    # Show a single Result
    api_response = api_instance.show(id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSignatureResultsApi->show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Result Id | 
 **include** | **str**| Included Objects | [optional] 

### Return type

[**Result**](Result.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

