# esp_sdk.CustomComplianceDomainsApi

All URIs are relative to https://api.evident.io

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](CustomComplianceDomainsApi.md#create) | **POST** /api/v2/custom_compliance_domains.json_api | Create a(n) Custom Compliance Domain
[**delete**](CustomComplianceDomainsApi.md#delete) | **DELETE** /api/v2/custom_compliance_domains/{id}.json_api | Delete a(n) Custom Compliance Domain
[**show**](CustomComplianceDomainsApi.md#show) | **GET** /api/v2/custom_compliance_domains/{id}.json_api | Show a single Custom Compliance Domain
[**update**](CustomComplianceDomainsApi.md#update) | **PATCH** /api/v2/custom_compliance_domains/{id}.json_api | Update a(n) Custom Compliance Domain


# **create**
> CustomComplianceDomain create(identifier, custom_compliance_standard_id, name, position=position, include=include)

Create a(n) Custom Compliance Domain



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.CustomComplianceDomainsApi()
identifier = 'identifier_example' # str | The identifier of this custom domain
custom_compliance_standard_id = 56 # int | The ID of the Custom Compliance Standard this custom domain belongs to
name = 'name_example' # str | Name
position = 56 # int | The position of this custom domain within the custom standard (optional)
include = 'include_example' # str | Related objects that can be included in the response:  custom_compliance_standard, custom_compliance_controls See Including Objects for more information. (optional)

try: 
    # Create a(n) Custom Compliance Domain
    api_response = api_instance.create(identifier, custom_compliance_standard_id, name, position=position, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomComplianceDomainsApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| The identifier of this custom domain | 
 **custom_compliance_standard_id** | **int**| The ID of the Custom Compliance Standard this custom domain belongs to | 
 **name** | **str**| Name | 
 **position** | **int**| The position of this custom domain within the custom standard | [optional] 
 **include** | **str**| Related objects that can be included in the response:  custom_compliance_standard, custom_compliance_controls See Including Objects for more information. | [optional] 

### Return type

[**CustomComplianceDomain**](CustomComplianceDomain.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> Meta delete(id)

Delete a(n) Custom Compliance Domain



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.CustomComplianceDomainsApi()
id = 56 # int |  ID

try: 
    # Delete a(n) Custom Compliance Domain
    api_response = api_instance.delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomComplianceDomainsApi->delete: %s\n" % e)
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
> CustomComplianceDomain show(id, include=include)

Show a single Custom Compliance Domain



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.CustomComplianceDomainsApi()
id = 56 # int | Custom Compliance Domain ID
include = 'include_example' # str | Related objects that can be included in the response:  custom_compliance_standard, custom_compliance_controls See Including Objects for more information. (optional)

try: 
    # Show a single Custom Compliance Domain
    api_response = api_instance.show(id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomComplianceDomainsApi->show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Custom Compliance Domain ID | 
 **include** | **str**| Related objects that can be included in the response:  custom_compliance_standard, custom_compliance_controls See Including Objects for more information. | [optional] 

### Return type

[**CustomComplianceDomain**](CustomComplianceDomain.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> CustomComplianceDomain update(id, identifier=identifier, custom_compliance_standard_id=custom_compliance_standard_id, name=name, position=position, include=include)

Update a(n) Custom Compliance Domain



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.CustomComplianceDomainsApi()
id = 56 # int | Custom Compliance Domain ID
identifier = 'identifier_example' # str | The identifier of this custom domain (optional)
custom_compliance_standard_id = 56 # int | The ID of the Custom Compliance Standard this custom domain belongs to (optional)
name = 'name_example' # str | Name (optional)
position = 56 # int | The position of this custom domain within the custom standard (optional)
include = 'include_example' # str | Related objects that can be included in the response:  custom_compliance_standard, custom_compliance_controls See Including Objects for more information. (optional)

try: 
    # Update a(n) Custom Compliance Domain
    api_response = api_instance.update(id, identifier=identifier, custom_compliance_standard_id=custom_compliance_standard_id, name=name, position=position, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomComplianceDomainsApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Custom Compliance Domain ID | 
 **identifier** | **str**| The identifier of this custom domain | [optional] 
 **custom_compliance_standard_id** | **int**| The ID of the Custom Compliance Standard this custom domain belongs to | [optional] 
 **name** | **str**| Name | [optional] 
 **position** | **int**| The position of this custom domain within the custom standard | [optional] 
 **include** | **str**| Related objects that can be included in the response:  custom_compliance_standard, custom_compliance_controls See Including Objects for more information. | [optional] 

### Return type

[**CustomComplianceDomain**](CustomComplianceDomain.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

