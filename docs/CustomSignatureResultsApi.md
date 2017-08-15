# esp_sdk.CustomSignatureResultsApi

All URIs are relative to https://api.evident.io

Method | HTTP request | Description
------------- | ------------- | -------------
[**alerts**](CustomSignatureResultsApi.md#alerts) | **GET** /api/v2/custom_signature_results/{custom_signature_result_id}/alerts.json_api | Returns the alerts for a given result. Note that this format is slightly different than the standard alert format. A successful call to this API returns a list of alerts for the custom signature result identified by the id parameter.
[**create**](CustomSignatureResultsApi.md#create) | **POST** /api/v2/custom_signature_results.json_api | Create a(n) Custom Signature/Result
[**list**](CustomSignatureResultsApi.md#list) | **PUT** /api/v2/custom_signature_results.json_api | Get a list of Custom Signature/Results
[**show**](CustomSignatureResultsApi.md#show) | **GET** /api/v2/custom_signature_results/{id}.json_api | Show a single Custom Signature/Result


# **alerts**
> PaginatedCollection alerts(custom_signature_result_id, include=include, page=page)

Returns the alerts for a given result. Note that this format is slightly different than the standard alert format. A successful call to this API returns a list of alerts for the custom signature result identified by the id parameter.

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.CustomSignatureResultsApi()
custom_signature_result_id = 56 # int | Custom Signature Result Id
include = 'include_example' # str | Objects that can be included in the response:  external_account,region,custom_signature  See Including Objects for more information. (optional)
page = {'key': 'page_example'} # dict(str, str) | Page Number and Page Size.  Example: page: {number: 1, size: 20} (optional)

try: 
    # Returns the alerts for a given result. Note that this format is slightly different than the standard alert format. A successful call to this API returns a list of alerts for the custom signature result identified by the id parameter.
    api_response = api_instance.alerts(custom_signature_result_id, include=include, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSignatureResultsApi->alerts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_signature_result_id** | **int**| Custom Signature Result Id | 
 **include** | **str**| Objects that can be included in the response:  external_account,region,custom_signature  See Including Objects for more information. | [optional] 
 **page** | [**dict(str, str)**](str.md)| Page Number and Page Size.  Example: page: {number: 1, size: 20} | [optional] 

### Return type

[**PaginatedCollection**](PaginatedCollection.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create**
> CustomSignatureResult create(code, custom_signature_definition_id, external_account_id, language, region_id, region=region)

Create a(n) Custom Signature/Result

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
    # Create a(n) Custom Signature/Result
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

[**CustomSignatureResult**](CustomSignatureResult.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> PaginatedCollection list(filter=filter, include=include, page=page)

Get a list of Custom Signature/Results

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.CustomSignatureResultsApi()
filter = {'key': 'filter_example'} # dict(str, str) | Filter Params for Searching.  Equality Searchable Attributes: [id, language, status]    Searchable Associations: [definition, region, external_account] See the filter parameter of the association's list action to see what attributes are searchable on each association. See Searching on Relationships for more information. See Searching Lists for more information. Example: filter: {name_eq: 'Bob'} (optional)
include = 'include_example' # str | Objects that can be included in the response:  external_account,region,definition,alerts  See Including Objects for more information. (optional)
page = {'key': 'page_example'} # dict(str, str) | Page Number and Page Size.  Example: page: {number: 1, size: 20} (optional)

try: 
    # Get a list of Custom Signature/Results
    api_response = api_instance.list(filter=filter, include=include, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSignatureResultsApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | [**dict(str, str)**](str.md)| Filter Params for Searching.  Equality Searchable Attributes: [id, language, status]    Searchable Associations: [definition, region, external_account] See the filter parameter of the association&#39;s list action to see what attributes are searchable on each association. See Searching on Relationships for more information. See Searching Lists for more information. Example: filter: {name_eq: &#39;Bob&#39;} | [optional] 
 **include** | **str**| Objects that can be included in the response:  external_account,region,definition,alerts  See Including Objects for more information. | [optional] 
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
> CustomSignatureResult show(id, include=include)

Show a single Custom Signature/Result

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.CustomSignatureResultsApi()
id = 56 # int | Custom Signature/Result Id
include = 'include_example' # str | Objects that can be included in the response:  external_account,region,definition,alerts  See Including Objects for more information. (optional)

try: 
    # Show a single Custom Signature/Result
    api_response = api_instance.show(id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSignatureResultsApi->show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Custom Signature/Result Id | 
 **include** | **str**| Objects that can be included in the response:  external_account,region,definition,alerts  See Including Objects for more information. | [optional] 

### Return type

[**CustomSignatureResult**](CustomSignatureResult.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

