# esp_sdk.SuppressionsApi

All URIs are relative to https://api.evident.io

Method | HTTP request | Description
------------- | ------------- | -------------
[**deactivate**](SuppressionsApi.md#deactivate) | **PATCH** /api/v2/suppressions/{id}/deactivate.json_api | A successful call to this API will deactivate a suppression identified by the id parameter.
[**list**](SuppressionsApi.md#list) | **PUT** /api/v2/suppressions.json_api | Get a list of Suppressions
[**show**](SuppressionsApi.md#show) | **GET** /api/v2/suppressions/{id}.json_api | Show a single Suppression
[**suppress_region**](SuppressionsApi.md#suppress_region) | **POST** /api/v2/suppressions/regions.json_api | A successful call to this API creates a new region suppression for the supplied regions. The body of the request must contain a json api compliant hash of attributes with type suppression/regions.
[**suppress_region_from_alert**](SuppressionsApi.md#suppress_region_from_alert) | **POST** /api/v2/suppressions/alert/{alert_id}/regions.json_api | A successful call to this API creates a new signature suppression based on the supplied alert_id. The body of the request must contain a json api compliant hash of attributes with type suppression/regions.
[**suppress_signature**](SuppressionsApi.md#suppress_signature) | **POST** /api/v2/suppressions/signatures.json_api | A successful call to this API creates a new signature suppression for the supplied signature_ids or custom_signature_ids. The body of the request must contain a json API compliant hash of attributes with type suppression/signatures.
[**suppress_signature_from_alert**](SuppressionsApi.md#suppress_signature_from_alert) | **POST** /api/v2/suppressions/alert/{alert_id}/signatures.json_api | A successful call to this API creates a new signature suppression based on the supplied alert_id. The body of the request must contain a json api compliant hash of attributes with type suppression/signatures.
[**suppress_unique_identifier_from_alert**](SuppressionsApi.md#suppress_unique_identifier_from_alert) | **POST** /api/v2/suppressions/alert/{alert_id}/unique_identifiers.json_api | A successful call to this API creates a new unique identifier suppression based on the supplied alert_id. The body of the request must contain a json api compliant hash of attributes with type suppression/unique_identifier.


# **deactivate**
> Suppression deactivate(id)

A successful call to this API will deactivate a suppression identified by the id parameter.

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.SuppressionsApi()
id = 56 # int | Suppression ID

try: 
    # A successful call to this API will deactivate a suppression identified by the id parameter.
    api_response = api_instance.deactivate(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SuppressionsApi->deactivate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Suppression ID | 

### Return type

[**Suppression**](Suppression.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> PaginatedCollection list(filter=filter, include=include, page=page)

Get a list of Suppressions

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.SuppressionsApi()
filter = {'key': 'filter_example'} # dict(str, str) | Filter Params for Searching.  See Searching Lists for more information. (optional)
include = 'include_example' # str | Related objects that can be included in the response.  See Including Objects for more information. (optional)
page = '{:number=>1,+:size=>20}' # str | Page Number and Page Size.  number is the page number of the collection to return, size is the number of items to return per page (optional) (default to {:number=>1,+:size=>20})

try: 
    # Get a list of Suppressions
    api_response = api_instance.list(filter=filter, include=include, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SuppressionsApi->list: %s\n" % e)
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
> Suppression show(id, include=include)

Show a single Suppression

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.SuppressionsApi()
id = 56 # int | Suppression ID
include = 'include_example' # str | Related objects that can be included in the response.  See Including Objects for more information. (optional)

try: 
    # Show a single Suppression
    api_response = api_instance.show(id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SuppressionsApi->show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Suppression ID | 
 **include** | **str**| Related objects that can be included in the response.  See Including Objects for more information. | [optional] 

### Return type

[**Suppression**](Suppression.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suppress_region**
> Suppression suppress_region(regions, external_account_ids, reason, resource=resource)

A successful call to this API creates a new region suppression for the supplied regions. The body of the request must contain a json api compliant hash of attributes with type suppression/regions.

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.SuppressionsApi()
regions = ['regions_example'] # list[str] | An array of region names to suppress
external_account_ids = [56] # list[int] | An Array of the external accounts identified by external_account_id to suppress the signature or custom signature on
reason = 'reason_example' # str | The reason for creating the suppression
resource = 'resource_example' # str | The resource string this suppression will suppress alerts for (optional)

try: 
    # A successful call to this API creates a new region suppression for the supplied regions. The body of the request must contain a json api compliant hash of attributes with type suppression/regions.
    api_response = api_instance.suppress_region(regions, external_account_ids, reason, resource=resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SuppressionsApi->suppress_region: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **regions** | [**list[str]**](str.md)| An array of region names to suppress | 
 **external_account_ids** | [**list[int]**](int.md)| An Array of the external accounts identified by external_account_id to suppress the signature or custom signature on | 
 **reason** | **str**| The reason for creating the suppression | 
 **resource** | **str**| The resource string this suppression will suppress alerts for | [optional] 

### Return type

[**Suppression**](Suppression.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suppress_region_from_alert**
> Suppression suppress_region_from_alert(alert_id, reason)

A successful call to this API creates a new signature suppression based on the supplied alert_id. The body of the request must contain a json api compliant hash of attributes with type suppression/regions.

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.SuppressionsApi()
alert_id = 56 # int | The ID for the alert you want to create a suppression for
reason = 'reason_example' # str | The reason for creating the suppression

try: 
    # A successful call to this API creates a new signature suppression based on the supplied alert_id. The body of the request must contain a json api compliant hash of attributes with type suppression/regions.
    api_response = api_instance.suppress_region_from_alert(alert_id, reason)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SuppressionsApi->suppress_region_from_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_id** | **int**| The ID for the alert you want to create a suppression for | 
 **reason** | **str**| The reason for creating the suppression | 

### Return type

[**Suppression**](Suppression.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suppress_signature**
> Suppression suppress_signature(regions, external_account_ids, reason, signature_ids=signature_ids, custom_signature_ids=custom_signature_ids, resource=resource)

A successful call to this API creates a new signature suppression for the supplied signature_ids or custom_signature_ids. The body of the request must contain a json API compliant hash of attributes with type suppression/signatures.

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.SuppressionsApi()
regions = ['regions_example'] # list[str] | An array of region names to suppress
external_account_ids = [56] # list[int] | An Array of the external accounts identified by external_account_id to suppress the signature or custom signature on
reason = 'reason_example' # str | The reason for creating the suppression
signature_ids = [56] # list[int] | An array of signatures identified by signature_id to suppress. Required if custom_signature_ids is blank. (optional)
custom_signature_ids = [56] # list[int] | An array of custom signatures identified by custom_signature_id to suppress. Required if signature_ids is blank. (optional)
resource = 'resource_example' # str | The resource string this suppression will suppress alerts for (optional)

try: 
    # A successful call to this API creates a new signature suppression for the supplied signature_ids or custom_signature_ids. The body of the request must contain a json API compliant hash of attributes with type suppression/signatures.
    api_response = api_instance.suppress_signature(regions, external_account_ids, reason, signature_ids=signature_ids, custom_signature_ids=custom_signature_ids, resource=resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SuppressionsApi->suppress_signature: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **regions** | [**list[str]**](str.md)| An array of region names to suppress | 
 **external_account_ids** | [**list[int]**](int.md)| An Array of the external accounts identified by external_account_id to suppress the signature or custom signature on | 
 **reason** | **str**| The reason for creating the suppression | 
 **signature_ids** | [**list[int]**](int.md)| An array of signatures identified by signature_id to suppress. Required if custom_signature_ids is blank. | [optional] 
 **custom_signature_ids** | [**list[int]**](int.md)| An array of custom signatures identified by custom_signature_id to suppress. Required if signature_ids is blank. | [optional] 
 **resource** | **str**| The resource string this suppression will suppress alerts for | [optional] 

### Return type

[**Suppression**](Suppression.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suppress_signature_from_alert**
> Suppression suppress_signature_from_alert(alert_id, reason)

A successful call to this API creates a new signature suppression based on the supplied alert_id. The body of the request must contain a json api compliant hash of attributes with type suppression/signatures.

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.SuppressionsApi()
alert_id = 56 # int | The ID for the alert you want to create a suppression for
reason = 'reason_example' # str | The reason for creating the suppression

try: 
    # A successful call to this API creates a new signature suppression based on the supplied alert_id. The body of the request must contain a json api compliant hash of attributes with type suppression/signatures.
    api_response = api_instance.suppress_signature_from_alert(alert_id, reason)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SuppressionsApi->suppress_signature_from_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_id** | **int**| The ID for the alert you want to create a suppression for | 
 **reason** | **str**| The reason for creating the suppression | 

### Return type

[**Suppression**](Suppression.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suppress_unique_identifier_from_alert**
> Suppression suppress_unique_identifier_from_alert(alert_id, reason)

A successful call to this API creates a new unique identifier suppression based on the supplied alert_id. The body of the request must contain a json api compliant hash of attributes with type suppression/unique_identifier.

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.SuppressionsApi()
alert_id = 56 # int | The ID for the alert you want to create a suppression for
reason = 'reason_example' # str | The reason for creating the suppression

try: 
    # A successful call to this API creates a new unique identifier suppression based on the supplied alert_id. The body of the request must contain a json api compliant hash of attributes with type suppression/unique_identifier.
    api_response = api_instance.suppress_unique_identifier_from_alert(alert_id, reason)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SuppressionsApi->suppress_unique_identifier_from_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_id** | **int**| The ID for the alert you want to create a suppression for | 
 **reason** | **str**| The reason for creating the suppression | 

### Return type

[**Suppression**](Suppression.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

