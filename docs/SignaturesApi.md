# esp_sdk.SignaturesApi

All URIs are relative to *http://localhost/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list**](SignaturesApi.md#list) | **PUT** /api/v2/signatures.json_api | Get a list of Signatures
[**run**](SignaturesApi.md#run) | **POST** /api/v2/signatures/{id}/run.json_api | A successful call to this API returns a list of alerts for the specific signature identified by the id parameter. The body of the request must contain a json api compliant hash of attributes with type signatures
[**show**](SignaturesApi.md#show) | **GET** /api/v2/signatures/{id}.json_api | Show a single Signature


# **list**
> PaginatedCollection list(page=page, filter=filter, include=include)

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
page = {'key': 'page_example'} # dict(str, str) | Page Number (optional)
filter = {'key': 'filter_example'} # dict(str, str) | Filter Params for Searching (optional)
include = 'include_example' # str | Included Objects (optional)

try: 
    # Get a list of Signatures
    api_response = api_instance.list(page=page, filter=filter, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SignaturesApi->list: %s\n" % e)
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

# **run**
> list[Alert] run(id, external_account_id, region=region)

A successful call to this API returns a list of alerts for the specific signature identified by the id parameter. The body of the request must contain a json api compliant hash of attributes with type signatures

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.SignaturesApi()
id = 56 # int | The ID of the signature to run
external_account_id = 56 # int | The ID of the external account to run this signature against
region = esp_sdk.Object() # Object | A single region name to run this signature against (optional)

try: 
    # A successful call to this API returns a list of alerts for the specific signature identified by the id parameter. The body of the request must contain a json api compliant hash of attributes with type signatures
    api_response = api_instance.run(id, external_account_id, region=region)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SignaturesApi->run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the signature to run | 
 **external_account_id** | **int**| The ID of the external account to run this signature against | 
 **region** | [**Object**](.md)| A single region name to run this signature against | [optional] 

### Return type

[**list[Alert]**](Alert.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

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
id = 56 # int | Signature Id
include = 'include_example' # str | Included Objects (optional)

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
 **id** | **int**| Signature Id | 
 **include** | **str**| Included Objects | [optional] 

### Return type

[**Signature**](Signature.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

