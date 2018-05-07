# esp_sdk.CustomComplianceControlsApi

All URIs are relative to https://api.evident.io

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_custom_signature**](CustomComplianceControlsApi.md#add_custom_signature) | **POST** /api/v2/custom_compliance_controls/{custom_compliance_control_id}/custom_signatures.json_api | Add a Custom Signature to a Custom Compliance Control
[**add_signature**](CustomComplianceControlsApi.md#add_signature) | **POST** /api/v2/custom_compliance_controls/{custom_compliance_control_id}/signatures.json_api | Add a Signature to a Custom Compliance Control
[**create**](CustomComplianceControlsApi.md#create) | **POST** /api/v2/custom_compliance_controls.json_api | Create a(n) Custom Compliance Control
[**delete**](CustomComplianceControlsApi.md#delete) | **DELETE** /api/v2/custom_compliance_controls/{id}.json_api | Delete a(n) Custom Compliance Control
[**list_custom_signatures**](CustomComplianceControlsApi.md#list_custom_signatures) | **GET** /api/v2/custom_compliance_controls/{custom_compliance_control_id}/custom_signatures.json_api | Get a list of Custom Signatures for a Custom Compliance Control
[**list_signatures**](CustomComplianceControlsApi.md#list_signatures) | **GET** /api/v2/custom_compliance_controls/{custom_compliance_control_id}/signatures.json_api | Get a list of Signatures for a Custom Compliance Control
[**remove_custom_signature**](CustomComplianceControlsApi.md#remove_custom_signature) | **DELETE** /api/v2/custom_compliance_controls/{custom_compliance_control_id}/custom_signatures/{custom_signature_id}.json_api | Remove a Custom Signature from a Custom Compliance Control
[**remove_signature**](CustomComplianceControlsApi.md#remove_signature) | **DELETE** /api/v2/custom_compliance_controls/{custom_compliance_control_id}/signatures/{signature_id}.json_api | Remove a Signature from a Custom Compliance Control
[**show**](CustomComplianceControlsApi.md#show) | **GET** /api/v2/custom_compliance_controls/{id}.json_api | Show a single Custom Compliance Control
[**update**](CustomComplianceControlsApi.md#update) | **PATCH** /api/v2/custom_compliance_controls/{id}.json_api | Update a(n) Custom Compliance Control


# **add_custom_signature**
> CustomSignature add_custom_signature(custom_compliance_control_id, custom_signature_id, include=include)

Add a Custom Signature to a Custom Compliance Control



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.CustomComplianceControlsApi()
custom_compliance_control_id = 56 # int | The ID of the Custom Compliance Control this custom signature belongs to
custom_signature_id = 56 # int | The ID of the custom signature that belongs to this custom control
include = 'include_example' # str | Related objects that can be included in the response:  organization, teams, external_accounts, definitions, suppressions See Including Objects for more information. (optional)

try: 
    # Add a Custom Signature to a Custom Compliance Control
    api_response = api_instance.add_custom_signature(custom_compliance_control_id, custom_signature_id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomComplianceControlsApi->add_custom_signature: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_compliance_control_id** | **int**| The ID of the Custom Compliance Control this custom signature belongs to | 
 **custom_signature_id** | **int**| The ID of the custom signature that belongs to this custom control | 
 **include** | **str**| Related objects that can be included in the response:  organization, teams, external_accounts, definitions, suppressions See Including Objects for more information. | [optional] 

### Return type

[**CustomSignature**](CustomSignature.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_signature**
> Signature add_signature(custom_compliance_control_id, signature_id, include=include)

Add a Signature to a Custom Compliance Control



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.CustomComplianceControlsApi()
custom_compliance_control_id = 56 # int | The ID of the Custom Compliance Control this signature belongs to
signature_id = 56 # int | The ID of the signature that belongs to this custom control
include = 'include_example' # str | Related objects that can be included in the response:  service, suppressions See Including Objects for more information. (optional)

try: 
    # Add a Signature to a Custom Compliance Control
    api_response = api_instance.add_signature(custom_compliance_control_id, signature_id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomComplianceControlsApi->add_signature: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_compliance_control_id** | **int**| The ID of the Custom Compliance Control this signature belongs to | 
 **signature_id** | **int**| The ID of the signature that belongs to this custom control | 
 **include** | **str**| Related objects that can be included in the response:  service, suppressions See Including Objects for more information. | [optional] 

### Return type

[**Signature**](Signature.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create**
> CustomComplianceControl create(custom_compliance_domain_id, identifier, name, include=include, custom_signature_ids=custom_signature_ids, description=description, position=position, signature_ids=signature_ids)

Create a(n) Custom Compliance Control



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.CustomComplianceControlsApi()
custom_compliance_domain_id = 56 # int | The ID of the Custom Compliance Domain this custom control belongs to
identifier = 'identifier_example' # str | The identifier of this custom control
name = 'name_example' # str | Name
include = 'include_example' # str | Related objects that can be included in the response:  custom_compliance_standard, custom_compliance_domain, signatures, custom_signatures See Including Objects for more information. (optional)
custom_signature_ids = [56] # list[int] | An array of custom signatures identified by custom_signature_id that belong to this custom control (optional)
description = 'description_example' # str | The description for this custom control (optional)
position = 56 # int | The position of this custom control within the custom domain (optional)
signature_ids = [56] # list[int] | An array of signatures identified by signature_id that belong to this custom control (optional)

try: 
    # Create a(n) Custom Compliance Control
    api_response = api_instance.create(custom_compliance_domain_id, identifier, name, include=include, custom_signature_ids=custom_signature_ids, description=description, position=position, signature_ids=signature_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomComplianceControlsApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_compliance_domain_id** | **int**| The ID of the Custom Compliance Domain this custom control belongs to | 
 **identifier** | **str**| The identifier of this custom control | 
 **name** | **str**| Name | 
 **include** | **str**| Related objects that can be included in the response:  custom_compliance_standard, custom_compliance_domain, signatures, custom_signatures See Including Objects for more information. | [optional] 
 **custom_signature_ids** | [**list[int]**](int.md)| An array of custom signatures identified by custom_signature_id that belong to this custom control | [optional] 
 **description** | **str**| The description for this custom control | [optional] 
 **position** | **int**| The position of this custom control within the custom domain | [optional] 
 **signature_ids** | [**list[int]**](int.md)| An array of signatures identified by signature_id that belong to this custom control | [optional] 

### Return type

[**CustomComplianceControl**](CustomComplianceControl.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> Meta delete(id)

Delete a(n) Custom Compliance Control



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.CustomComplianceControlsApi()
id = 56 # int | Custom Compliance Control ID

try: 
    # Delete a(n) Custom Compliance Control
    api_response = api_instance.delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomComplianceControlsApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Custom Compliance Control ID | 

### Return type

[**Meta**](Meta.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_custom_signatures**
> PaginatedCollection list_custom_signatures(custom_compliance_control_id, include=include, page=page)

Get a list of Custom Signatures for a Custom Compliance Control



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.CustomComplianceControlsApi()
custom_compliance_control_id = 56 # int | The ID of the Custom Compliance Control this custom signature belongs to
include = 'include_example' # str | Related objects that can be included in the response:  organization, teams, external_accounts, definitions, suppressions See Including Objects for more information. (optional)
page = '{:number=>1,+:size=>20}' # str | Page Number and Page Size.  Number is the page number of the collection to return, size is the number of items to return per page. (optional) (default to {:number=>1,+:size=>20})

try: 
    # Get a list of Custom Signatures for a Custom Compliance Control
    api_response = api_instance.list_custom_signatures(custom_compliance_control_id, include=include, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomComplianceControlsApi->list_custom_signatures: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_compliance_control_id** | **int**| The ID of the Custom Compliance Control this custom signature belongs to | 
 **include** | **str**| Related objects that can be included in the response:  organization, teams, external_accounts, definitions, suppressions See Including Objects for more information. | [optional] 
 **page** | **str**| Page Number and Page Size.  Number is the page number of the collection to return, size is the number of items to return per page. | [optional] [default to {:number&#x3D;&gt;1,+:size&#x3D;&gt;20}]

### Return type

[**PaginatedCollection**](PaginatedCollection.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_signatures**
> PaginatedCollection list_signatures(custom_compliance_control_id, include=include, page=page)

Get a list of Signatures for a Custom Compliance Control



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.CustomComplianceControlsApi()
custom_compliance_control_id = 56 # int | The ID of the Custom Compliance Control this signature belongs to
include = 'include_example' # str | Related objects that can be included in the response:  service, suppressions See Including Objects for more information. (optional)
page = '{:number=>1,+:size=>20}' # str | Page Number and Page Size.  Number is the page number of the collection to return, size is the number of items to return per page. (optional) (default to {:number=>1,+:size=>20})

try: 
    # Get a list of Signatures for a Custom Compliance Control
    api_response = api_instance.list_signatures(custom_compliance_control_id, include=include, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomComplianceControlsApi->list_signatures: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_compliance_control_id** | **int**| The ID of the Custom Compliance Control this signature belongs to | 
 **include** | **str**| Related objects that can be included in the response:  service, suppressions See Including Objects for more information. | [optional] 
 **page** | **str**| Page Number and Page Size.  Number is the page number of the collection to return, size is the number of items to return per page. | [optional] [default to {:number&#x3D;&gt;1,+:size&#x3D;&gt;20}]

### Return type

[**PaginatedCollection**](PaginatedCollection.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_custom_signature**
> Meta remove_custom_signature(custom_compliance_control_id, custom_signature_id)

Remove a Custom Signature from a Custom Compliance Control



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.CustomComplianceControlsApi()
custom_compliance_control_id = 56 # int | The ID of the Custom Compliance Control this custom signature belongs to
custom_signature_id = 56 # int | The ID of the custom signature that belongs to this custom control

try: 
    # Remove a Custom Signature from a Custom Compliance Control
    api_response = api_instance.remove_custom_signature(custom_compliance_control_id, custom_signature_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomComplianceControlsApi->remove_custom_signature: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_compliance_control_id** | **int**| The ID of the Custom Compliance Control this custom signature belongs to | 
 **custom_signature_id** | **int**| The ID of the custom signature that belongs to this custom control | 

### Return type

[**Meta**](Meta.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_signature**
> Meta remove_signature(custom_compliance_control_id, signature_id)

Remove a Signature from a Custom Compliance Control



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.CustomComplianceControlsApi()
custom_compliance_control_id = 56 # int | The ID of the Custom Compliance Control this signature belongs to
signature_id = 56 # int | The ID of the signature that belongs to this custom control

try: 
    # Remove a Signature from a Custom Compliance Control
    api_response = api_instance.remove_signature(custom_compliance_control_id, signature_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomComplianceControlsApi->remove_signature: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_compliance_control_id** | **int**| The ID of the Custom Compliance Control this signature belongs to | 
 **signature_id** | **int**| The ID of the signature that belongs to this custom control | 

### Return type

[**Meta**](Meta.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show**
> CustomComplianceControl show(id, include=include)

Show a single Custom Compliance Control



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.CustomComplianceControlsApi()
id = 56 # int | Custom Compliance Control ID
include = 'include_example' # str | Related objects that can be included in the response:  custom_compliance_standard, custom_compliance_domain, signatures, custom_signatures See Including Objects for more information. (optional)

try: 
    # Show a single Custom Compliance Control
    api_response = api_instance.show(id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomComplianceControlsApi->show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Custom Compliance Control ID | 
 **include** | **str**| Related objects that can be included in the response:  custom_compliance_standard, custom_compliance_domain, signatures, custom_signatures See Including Objects for more information. | [optional] 

### Return type

[**CustomComplianceControl**](CustomComplianceControl.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> CustomComplianceControl update(id, include=include, custom_compliance_domain_id=custom_compliance_domain_id, custom_signature_ids=custom_signature_ids, description=description, identifier=identifier, name=name, position=position, signature_ids=signature_ids)

Update a(n) Custom Compliance Control



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.CustomComplianceControlsApi()
id = 56 # int | Custom Compliance Control ID
include = 'include_example' # str | Related objects that can be included in the response:  custom_compliance_standard, custom_compliance_domain, signatures, custom_signatures See Including Objects for more information. (optional)
custom_compliance_domain_id = 56 # int | The ID of the Custom Compliance Domain this custom control belongs to (optional)
custom_signature_ids = [56] # list[int] | An array of custom signatures identified by custom_signature_id that belong to this custom control (optional)
description = 'description_example' # str | The description for this custom control (optional)
identifier = 'identifier_example' # str | The identifier of this custom control (optional)
name = 'name_example' # str | Name (optional)
position = 56 # int | The position of this custom control within the custom domain (optional)
signature_ids = [56] # list[int] | An array of signatures identified by signature_id that belong to this custom control (optional)

try: 
    # Update a(n) Custom Compliance Control
    api_response = api_instance.update(id, include=include, custom_compliance_domain_id=custom_compliance_domain_id, custom_signature_ids=custom_signature_ids, description=description, identifier=identifier, name=name, position=position, signature_ids=signature_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomComplianceControlsApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Custom Compliance Control ID | 
 **include** | **str**| Related objects that can be included in the response:  custom_compliance_standard, custom_compliance_domain, signatures, custom_signatures See Including Objects for more information. | [optional] 
 **custom_compliance_domain_id** | **int**| The ID of the Custom Compliance Domain this custom control belongs to | [optional] 
 **custom_signature_ids** | [**list[int]**](int.md)| An array of custom signatures identified by custom_signature_id that belong to this custom control | [optional] 
 **description** | **str**| The description for this custom control | [optional] 
 **identifier** | **str**| The identifier of this custom control | [optional] 
 **name** | **str**| Name | [optional] 
 **position** | **int**| The position of this custom control within the custom domain | [optional] 
 **signature_ids** | [**list[int]**](int.md)| An array of signatures identified by signature_id that belong to this custom control | [optional] 

### Return type

[**CustomComplianceControl**](CustomComplianceControl.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

