# esp_sdk.SignatureCustomRiskLevelsApi

All URIs are relative to *http://localhost/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](SignatureCustomRiskLevelsApi.md#create) | **POST** /api/v2/signature_custom_risk_levels.json_api | Create a(n) Signature Custom Risk Level
[**destroy**](SignatureCustomRiskLevelsApi.md#destroy) | **DELETE** /api/v2/signature_custom_risk_levels/{id}.json_api | Remove a(n) Signature Custom Risk Level
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy**
> object destroy(id)

Remove a(n) Signature Custom Risk Level

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

try: 
    # Remove a(n) Signature Custom Risk Level
    api_response = api_instance.destroy(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SignatureCustomRiskLevelsApi->destroy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Signature Custom Risk Level Id | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> PaginatedCollection list(external_account_id, page=page, filter=filter, include=include)

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
page = {'key': 'page_example'} # dict(str, str) | Page Number (optional)
filter = {'key': 'filter_example'} # dict(str, str) | Filter Params for Searching (optional)
include = 'include_example' # str | Included Objects (optional)

try: 
    # Get a list of Signature Custom Risk Levels
    api_response = api_instance.list(external_account_id, page=page, filter=filter, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SignatureCustomRiskLevelsApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_account_id** | **int**| The ID of the external account to retrieve | 
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
include = 'include_example' # str | Included Objects (optional)

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
 **include** | **str**| Included Objects | [optional] 

### Return type

[**SignatureCustomRiskLevel**](SignatureCustomRiskLevel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

