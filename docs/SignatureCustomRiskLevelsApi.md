# esp_sdk.SignatureCustomRiskLevelsApi

All URIs are relative to https://api.evident.io

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](SignatureCustomRiskLevelsApi.md#create) | **POST** /api/v2/signature_custom_risk_levels.json_api | Create a(n) SignatureCustomRiskLevel
[**destroy**](SignatureCustomRiskLevelsApi.md#destroy) | **DELETE** /api/v2/signature_custom_risk_levels/{id}.json_api | Remove a(n) SignatureCustomRiskLevel
[**list**](SignatureCustomRiskLevelsApi.md#list) | **GET** /api/v2/external_accounts/{external_account_id}/signature_custom_risk_levels.json_api | Get a list of SignatureCustomRiskLevels
[**show**](SignatureCustomRiskLevelsApi.md#show) | **GET** /api/v2/signature_custom_risk_levels/{id}.json_api | Show a single SignatureCustomRiskLevel
[**update**](SignatureCustomRiskLevelsApi.md#update) | **PATCH** /api/v2/signature_custom_risk_levels/{id}.json_api | Update a(n) SignatureCustomRiskLevel


# **create**
> SignatureCustomRiskLevel create(external_account_id, risk_level, signature_id)

Create a(n) SignatureCustomRiskLevel

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.SignatureCustomRiskLevelsApi()
external_account_id = 56 # int | The ID of the external account this signature custom risk level is for
risk_level = 'risk_level_example' # str | The risk-level of the problem identified by the signature. Valid values are low, medium, high
signature_id = 56 # int | The signature ID this signature custom risk level is for

try: 
    # Create a(n) SignatureCustomRiskLevel
    api_response = api_instance.create(external_account_id, risk_level, signature_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SignatureCustomRiskLevelsApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_account_id** | **int**| The ID of the external account this signature custom risk level is for | 
 **risk_level** | **str**| The risk-level of the problem identified by the signature. Valid values are low, medium, high | 
 **signature_id** | **int**| The signature ID this signature custom risk level is for | 

### Return type

[**SignatureCustomRiskLevel**](SignatureCustomRiskLevel.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy**
> Meta destroy(id)

Remove a(n) SignatureCustomRiskLevel

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.SignatureCustomRiskLevelsApi()
id = 56 # int | SignatureCustomRiskLevel ID

try: 
    # Remove a(n) SignatureCustomRiskLevel
    api_response = api_instance.destroy(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SignatureCustomRiskLevelsApi->destroy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| SignatureCustomRiskLevel ID | 

### Return type

[**Meta**](Meta.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> PaginatedCollection list(external_account_id, include=include, page=page)

Get a list of SignatureCustomRiskLevels

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.SignatureCustomRiskLevelsApi()
external_account_id = 56 # int | The ID of the external account to retrieve
include = 'include_example' # str | Related objects that can be included in the response.  See Including Objects for more information. (optional)
page = '{:number=>1,+:size=>20}' # str | Page Number and Page Size.  number is the page number of the collection to return, size is the number of items to return per page (optional) (default to {:number=>1,+:size=>20})

try: 
    # Get a list of SignatureCustomRiskLevels
    api_response = api_instance.list(external_account_id, include=include, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SignatureCustomRiskLevelsApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_account_id** | **int**| The ID of the external account to retrieve | 
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
> SignatureCustomRiskLevel show(id, include=include)

Show a single SignatureCustomRiskLevel

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.SignatureCustomRiskLevelsApi()
id = 56 # int | SignatureCustomRiskLevel ID
include = 'include_example' # str | Related objects that can be included in the response.  See Including Objects for more information. (optional)

try: 
    # Show a single SignatureCustomRiskLevel
    api_response = api_instance.show(id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SignatureCustomRiskLevelsApi->show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| SignatureCustomRiskLevel ID | 
 **include** | **str**| Related objects that can be included in the response.  See Including Objects for more information. | [optional] 

### Return type

[**SignatureCustomRiskLevel**](SignatureCustomRiskLevel.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> SignatureCustomRiskLevel update(id, external_account_id, risk_level, signature_id)

Update a(n) SignatureCustomRiskLevel

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.SignatureCustomRiskLevelsApi()
id = 56 # int | SignatureCustomRiskLevel ID
external_account_id = 56 # int | The ID of the external account this signature custom risk level is for
risk_level = 'risk_level_example' # str | The risk-level of the problem identified by the signature. Valid values are low, medium, high
signature_id = 56 # int | The signature ID this signature custom risk level is for

try: 
    # Update a(n) SignatureCustomRiskLevel
    api_response = api_instance.update(id, external_account_id, risk_level, signature_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SignatureCustomRiskLevelsApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| SignatureCustomRiskLevel ID | 
 **external_account_id** | **int**| The ID of the external account this signature custom risk level is for | 
 **risk_level** | **str**| The risk-level of the problem identified by the signature. Valid values are low, medium, high | 
 **signature_id** | **int**| The signature ID this signature custom risk level is for | 

### Return type

[**SignatureCustomRiskLevel**](SignatureCustomRiskLevel.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

