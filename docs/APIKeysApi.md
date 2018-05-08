# esp_sdk.APIKeysApi

All URIs are relative to https://api.evident.io

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](APIKeysApi.md#create) | **POST** /api/v2/api_keys.json_api | Create a(n) API Key
[**delete**](APIKeysApi.md#delete) | **DELETE** /api/v2/api_keys/{id}.json_api | Delete a(n) API Key
[**list**](APIKeysApi.md#list) | **GET** /api/v2/api_keys.json_api | Get a list of API Keys
[**show**](APIKeysApi.md#show) | **GET** /api/v2/api_keys/{id}.json_api | Show a single API Key
[**update**](APIKeysApi.md#update) | **PATCH** /api/v2/api_keys/{id}.json_api | Update a(n) API Key


# **create**
> ApiKey create(include=include, name=name)

Create a(n) API Key

The secret key will only be returned once when the key is first created

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.APIKeysApi()
include = 'include_example' # str | Related objects that can be included in the response:  user See Including Objects for more information. (optional)
name = 'name_example' # str | The name of the API Key (optional)

try: 
    # Create a(n) API Key
    api_response = api_instance.create(include=include, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIKeysApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include** | **str**| Related objects that can be included in the response:  user See Including Objects for more information. | [optional] 
 **name** | **str**| The name of the API Key | [optional] 

### Return type

[**ApiKey**](ApiKey.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> Meta delete(id)

Delete a(n) API Key



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.APIKeysApi()
id = 56 # int | API Key ID

try: 
    # Delete a(n) API Key
    api_response = api_instance.delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIKeysApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| API Key ID | 

### Return type

[**Meta**](Meta.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> PaginatedCollection list(include=include, page=page)

Get a list of API Keys



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.APIKeysApi()
include = 'include_example' # str | Related objects that can be included in the response:  user See Including Objects for more information. (optional)
page = '{:number=>1,+:size=>20}' # str | Page Number and Page Size.  Number is the page number of the collection to return, size is the number of items to return per page. (optional) (default to {:number=>1,+:size=>20})

try: 
    # Get a list of API Keys
    api_response = api_instance.list(include=include, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIKeysApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include** | **str**| Related objects that can be included in the response:  user See Including Objects for more information. | [optional] 
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
> ApiKey show(id, include=include)

Show a single API Key



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.APIKeysApi()
id = 56 # int | API Key ID
include = 'include_example' # str | Related objects that can be included in the response:  user See Including Objects for more information. (optional)

try: 
    # Show a single API Key
    api_response = api_instance.show(id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIKeysApi->show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| API Key ID | 
 **include** | **str**| Related objects that can be included in the response:  user See Including Objects for more information. | [optional] 

### Return type

[**ApiKey**](ApiKey.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> ApiKey update(id, include=include, name=name)

Update a(n) API Key



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.APIKeysApi()
id = 56 # int | API Key ID
include = 'include_example' # str | Related objects that can be included in the response:  user See Including Objects for more information. (optional)
name = 'name_example' # str | The name of the API Key (optional)

try: 
    # Update a(n) API Key
    api_response = api_instance.update(id, include=include, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIKeysApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| API Key ID | 
 **include** | **str**| Related objects that can be included in the response:  user See Including Objects for more information. | [optional] 
 **name** | **str**| The name of the API Key | [optional] 

### Return type

[**ApiKey**](ApiKey.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

