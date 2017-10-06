# esp_sdk.CustomSignaturesApi

All URIs are relative to https://api.evident.io

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](CustomSignaturesApi.md#create) | **POST** /api/v2/custom_signatures.json_api | Create a(n) CustomSignature
[**destroy**](CustomSignaturesApi.md#destroy) | **DELETE** /api/v2/custom_signatures/{id}.json_api | Remove a(n) CustomSignature
[**list**](CustomSignaturesApi.md#list) | **PUT** /api/v2/custom_signatures.json_api | Get a list of CustomSignatures
[**show**](CustomSignaturesApi.md#show) | **GET** /api/v2/custom_signatures/{id}.json_api | Show a single CustomSignature
[**update**](CustomSignaturesApi.md#update) | **PATCH** /api/v2/custom_signatures/{id}.json_api | Update a(n) CustomSignature


# **create**
> CustomSignature create(identifier, name, risk_level, team_ids, description=description, resolution=resolution)

Create a(n) CustomSignature

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
team_ids = [56] # list[int] | The team IDs this custom signature should run for. If no teams are selected the custom signature will not be run.
description = 'description_example' # str | The description of the custom signature that is displayed on alerts (optional)
resolution = 'resolution_example' # str | Details for how to resolve this custom signature that is displayed on alerts (optional)

try: 
    # Create a(n) CustomSignature
    api_response = api_instance.create(identifier, name, risk_level, team_ids, description=description, resolution=resolution)
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
 **team_ids** | [**list[int]**](int.md)| The team IDs this custom signature should run for. If no teams are selected the custom signature will not be run. | 
 **description** | **str**| The description of the custom signature that is displayed on alerts | [optional] 
 **resolution** | **str**| Details for how to resolve this custom signature that is displayed on alerts | [optional] 

### Return type

[**CustomSignature**](CustomSignature.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy**
> Meta destroy(id)

Remove a(n) CustomSignature

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.CustomSignaturesApi()
id = 56 # int | CustomSignature ID

try: 
    # Remove a(n) CustomSignature
    api_response = api_instance.destroy(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSignaturesApi->destroy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| CustomSignature ID | 

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

Get a list of CustomSignatures

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.CustomSignaturesApi()
filter = {'key': 'filter_example'} # dict(str, str) | Filter Params for Searching.  See Searching Lists for more information. (optional)
include = 'include_example' # str | Related objects that can be included in the response.  See Including Objects for more information. (optional)
page = '{:number=>1,+:size=>20}' # str | Page Number and Page Size.  number is the page number of the collection to return, size is the number of items to return per page (optional) (default to {:number=>1,+:size=>20})

try: 
    # Get a list of CustomSignatures
    api_response = api_instance.list(filter=filter, include=include, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSignaturesApi->list: %s\n" % e)
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
> CustomSignature show(id, include=include)

Show a single CustomSignature

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.CustomSignaturesApi()
id = 56 # int | CustomSignature ID
include = 'include_example' # str | Related objects that can be included in the response.  See Including Objects for more information. (optional)

try: 
    # Show a single CustomSignature
    api_response = api_instance.show(id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSignaturesApi->show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| CustomSignature ID | 
 **include** | **str**| Related objects that can be included in the response.  See Including Objects for more information. | [optional] 

### Return type

[**CustomSignature**](CustomSignature.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> CustomSignature update(id, description=description, identifier=identifier, name=name, resolution=resolution, risk_level=risk_level, team_ids=team_ids)

Update a(n) CustomSignature

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.CustomSignaturesApi()
id = 56 # int | CustomSignature ID
description = 'description_example' # str | The description of the custom signature that is displayed on alerts (optional)
identifier = 'identifier_example' # str | The identifier to use for the custom signature. Common format is AWS:- such as AWS:IAM-001 (optional)
name = 'name_example' # str | The name of the custom signature (optional)
resolution = 'resolution_example' # str | Details for how to resolve this custom signature that is displayed on alerts (optional)
risk_level = 'risk_level_example' # str | The risk-level of the problem identified by the custom signature. Valid values are low, medium, high (optional)
team_ids = [56] # list[int] | The team IDs this custom signature should run for. If no teams are selected the custom signature will not be run. (optional)

try: 
    # Update a(n) CustomSignature
    api_response = api_instance.update(id, description=description, identifier=identifier, name=name, resolution=resolution, risk_level=risk_level, team_ids=team_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSignaturesApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| CustomSignature ID | 
 **description** | **str**| The description of the custom signature that is displayed on alerts | [optional] 
 **identifier** | **str**| The identifier to use for the custom signature. Common format is AWS:- such as AWS:IAM-001 | [optional] 
 **name** | **str**| The name of the custom signature | [optional] 
 **resolution** | **str**| Details for how to resolve this custom signature that is displayed on alerts | [optional] 
 **risk_level** | **str**| The risk-level of the problem identified by the custom signature. Valid values are low, medium, high | [optional] 
 **team_ids** | [**list[int]**](int.md)| The team IDs this custom signature should run for. If no teams are selected the custom signature will not be run. | [optional] 

### Return type

[**CustomSignature**](CustomSignature.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

