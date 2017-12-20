# esp_sdk.CustomComplianceStandardsApi

All URIs are relative to https://api.evident.io

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](CustomComplianceStandardsApi.md#create) | **POST** /api/v2/custom_compliance_standards.json_api | Create a(n) Custom Compliance Standard
[**delete**](CustomComplianceStandardsApi.md#delete) | **DELETE** /api/v2/custom_compliance_standards/{id}.json_api | Delete a(n) Custom Compliance Standard
[**show**](CustomComplianceStandardsApi.md#show) | **GET** /api/v2/custom_compliance_standards/{id}.json_api | Show a single Custom Compliance Standard
[**update**](CustomComplianceStandardsApi.md#update) | **PATCH** /api/v2/custom_compliance_standards/{id}.json_api | Update a(n) Custom Compliance Standard


# **create**
> CustomComplianceStandard create(name, description, include=include)

Create a(n) Custom Compliance Standard



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.CustomComplianceStandardsApi()
name = 'name_example' # str | Name
description = 'description_example' # str | The description for this Compliance Standard
include = 'include_example' # str | Related objects that can be included in the response:  custom_compliance_domains, custom_compliance_controls See Including Objects for more information. (optional)

try: 
    # Create a(n) Custom Compliance Standard
    api_response = api_instance.create(name, description, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomComplianceStandardsApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name | 
 **description** | **str**| The description for this Compliance Standard | 
 **include** | **str**| Related objects that can be included in the response:  custom_compliance_domains, custom_compliance_controls See Including Objects for more information. | [optional] 

### Return type

[**CustomComplianceStandard**](CustomComplianceStandard.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> Meta delete(id)

Delete a(n) Custom Compliance Standard



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.CustomComplianceStandardsApi()
id = 56 # int |  ID

try: 
    # Delete a(n) Custom Compliance Standard
    api_response = api_instance.delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomComplianceStandardsApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  ID | 

### Return type

[**Meta**](Meta.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show**
> CustomComplianceStandard show(id, include=include)

Show a single Custom Compliance Standard



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.CustomComplianceStandardsApi()
id = 56 # int | Custom Compliance Standard ID
include = 'include_example' # str | Related objects that can be included in the response:  custom_compliance_domains, custom_compliance_controls See Including Objects for more information. (optional)

try: 
    # Show a single Custom Compliance Standard
    api_response = api_instance.show(id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomComplianceStandardsApi->show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Custom Compliance Standard ID | 
 **include** | **str**| Related objects that can be included in the response:  custom_compliance_domains, custom_compliance_controls See Including Objects for more information. | [optional] 

### Return type

[**CustomComplianceStandard**](CustomComplianceStandard.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> CustomComplianceStandard update(id, name=name, description=description, include=include)

Update a(n) Custom Compliance Standard



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.CustomComplianceStandardsApi()
id = 56 # int | Custom Compliance Standard ID
name = 'name_example' # str | Name (optional)
description = 'description_example' # str | The description for this Compliance Standard (optional)
include = 'include_example' # str | Related objects that can be included in the response:  custom_compliance_domains, custom_compliance_controls See Including Objects for more information. (optional)

try: 
    # Update a(n) Custom Compliance Standard
    api_response = api_instance.update(id, name=name, description=description, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomComplianceStandardsApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Custom Compliance Standard ID | 
 **name** | **str**| Name | [optional] 
 **description** | **str**| The description for this Compliance Standard | [optional] 
 **include** | **str**| Related objects that can be included in the response:  custom_compliance_domains, custom_compliance_controls See Including Objects for more information. | [optional] 

### Return type

[**CustomComplianceStandard**](CustomComplianceStandard.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

