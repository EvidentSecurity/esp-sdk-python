# esp_sdk.SignatureCustomRiskLevelsApi

All URIs are relative to https://api.evident.io

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](SignatureCustomRiskLevelsApi.md#create) | **POST** /api/v2/signature_custom_risk_levels.json_api | Create a(n) Signature Custom Risk Level
[**destroy**](SignatureCustomRiskLevelsApi.md#destroy) | **DELETE** /api/v2/signature_custom_risk_levels/{id}.json_api | Remove a(n) SignatureCustomRiskLevel
[**list**](SignatureCustomRiskLevelsApi.md#list) | **GET** /api/v2/external_accounts/{external_account_id}/signature_custom_risk_levels.json_api | Get a list of Signature Custom Risk Levels
[**show**](SignatureCustomRiskLevelsApi.md#show) | **GET** /api/v2/signature_custom_risk_levels/{id}.json_api | Show a single Signature Custom Risk Level
[**update**](SignatureCustomRiskLevelsApi.md#update) | **PATCH** /api/v2/signature_custom_risk_levels/{id}.json_api | Update a(n) Signature Custom Risk Level


# **create**
> SignatureCustomRiskLevel create(external_account_id, risk_level, signature_id)

Create a(n) Signature Custom Risk Level

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
risk_level = 'risk_level_example' # str | The risk-level of the problem identified by the signature. Valid values are Low, Medium, High
signature_id = 56 # int | The signature ID this signature custom risk level is for

try: 
    # Create a(n) Signature Custom Risk Level
    api_response = api_instance.create(external_account_id, risk_level, signature_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SignatureCustomRiskLevelsApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_account_id** | **int**| The ID of the external account this signature custom risk level is for | 
 **risk_level** | **str**| The risk-level of the problem identified by the signature. Valid values are Low, Medium, High | 
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
> SignatureCustomRiskLevel destroy(id)

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
id = 56 # int | SignatureCustomRiskLevel Id

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
 **id** | **int**| SignatureCustomRiskLevel Id | 

### Return type

[**SignatureCustomRiskLevel**](SignatureCustomRiskLevel.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> PaginatedCollection list(external_account_id, include=include, page=page)

Get a list of Signature Custom Risk Levels

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
include = 'include_example' # str | Objects that can be included in the response:  external_account,signature  See Including Objects for more information. (optional)
page = {'key': 'page_example'} # dict(str, str) | Page Number and Page Size.  Example: page: {number: 1, size: 20} (optional)

try: 
    # Get a list of Signature Custom Risk Levels
    api_response = api_instance.list(external_account_id, include=include, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SignatureCustomRiskLevelsApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_account_id** | **int**| The ID of the external account to retrieve | 
 **include** | **str**| Objects that can be included in the response:  external_account,signature  See Including Objects for more information. | [optional] 
 **page** | [**dict(str, str)**](str.md)| Page Number and Page Size.  Example: page: {number: 1, size: 20} | [optional] 

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

Show a single Signature Custom Risk Level

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.SignatureCustomRiskLevelsApi()
id = 56 # int | Signature Custom Risk Level Id
include = 'include_example' # str | Objects that can be included in the response:  external_account,signature  See Including Objects for more information. (optional)

try: 
    # Show a single Signature Custom Risk Level
    api_response = api_instance.show(id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SignatureCustomRiskLevelsApi->show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Signature Custom Risk Level Id | 
 **include** | **str**| Objects that can be included in the response:  external_account,signature  See Including Objects for more information. | [optional] 

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

Update a(n) Signature Custom Risk Level

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.SignatureCustomRiskLevelsApi()
id = 56 # int | Signature Custom Risk Level Id
external_account_id = 56 # int | The ID of the external account this signature custom risk level is for
risk_level = 'risk_level_example' # str | The risk-level of the problem identified by the signature. Valid values are Low, Medium, High
signature_id = 56 # int | The signature ID this signature custom risk level is for

try: 
    # Update a(n) Signature Custom Risk Level
    api_response = api_instance.update(id, external_account_id, risk_level, signature_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SignatureCustomRiskLevelsApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Signature Custom Risk Level Id | 
 **external_account_id** | **int**| The ID of the external account this signature custom risk level is for | 
 **risk_level** | **str**| The risk-level of the problem identified by the signature. Valid values are Low, Medium, High | 
 **signature_id** | **int**| The signature ID this signature custom risk level is for | 

### Return type

[**SignatureCustomRiskLevel**](SignatureCustomRiskLevel.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

