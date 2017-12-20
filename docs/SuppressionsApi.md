# esp_sdk.SuppressionsApi

All URIs are relative to https://api.evident.io

Method | HTTP request | Description
------------- | ------------- | -------------
[**deactivate**](SuppressionsApi.md#deactivate) | **PATCH** /api/v2/suppressions/{id}/deactivate.json_api | Deactivate a suppression
[**list**](SuppressionsApi.md#list) | **PUT** /api/v2/suppressions.json_api | Get a list of Suppressions
[**show**](SuppressionsApi.md#show) | **GET** /api/v2/suppressions/{id}.json_api | Show a single Suppression
[**suppress_region**](SuppressionsApi.md#suppress_region) | **POST** /api/v2/suppressions/regions.json_api | Creates a region suppression
[**suppress_region_from_alert**](SuppressionsApi.md#suppress_region_from_alert) | **POST** /api/v2/suppressions/alert/{alert_id}/regions.json_api | Creates a region suppression from an alert
[**suppress_signature**](SuppressionsApi.md#suppress_signature) | **POST** /api/v2/suppressions/signatures.json_api | Creates a signature suppression
[**suppress_signature_from_alert**](SuppressionsApi.md#suppress_signature_from_alert) | **POST** /api/v2/suppressions/alert/{alert_id}/signatures.json_api | Creates a signature suppression from an alert
[**suppress_unique_identifier_from_alert**](SuppressionsApi.md#suppress_unique_identifier_from_alert) | **POST** /api/v2/suppressions/alert/{alert_id}/unique_identifiers.json_api | Creates a unique identifier suppression from an alert


# **deactivate**
> Suppression deactivate(id, include=include)

Deactivate a suppression



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
include = 'include_example' # str | Related objects that can be included in the response:  organization, created_by, regions, external_accounts, signatures, custom_signatures See Including Objects for more information. (optional)

try: 
    # Deactivate a suppression
    api_response = api_instance.deactivate(id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SuppressionsApi->deactivate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Suppression ID | 
 **include** | **str**| Related objects that can be included in the response:  organization, created_by, regions, external_accounts, signatures, custom_signatures See Including Objects for more information. | [optional] 

### Return type

[**Suppression**](Suppression.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> PaginatedCollection list(page=page, include=include, filter=filter)

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
page = '{:number=>1,+:size=>20}' # str | Page Number and Page Size.  number is the page number of the collection to return, size is the number of items to return per page (optional) (default to {:number=>1,+:size=>20})
include = 'include_example' # str | Related objects that can be included in the response:  organization, created_by, regions, external_accounts, signatures, custom_signatures See Including Objects for more information. (optional)
filter = {'key': 'filter_example'} # dict(str, str) | Filter Params for Searching.  Equality Searchable Attributes: [id, status, suppression_type, resource, reason] Matching Searchable Attributes: [resource, reason] Limited Searchable Attributes: [signature_name_cont, signature_identifier_cont] Sortable Attributes: [suppression_type, updated_at, created_at, id, status] Searchable Associations: [regions, created_by, signatures, custom_signatures, unique_identifier_signature, unique_identifier_custom_signature] See Searching Lists for more information. See the filter parameter of the association's list action to see what attributes are searchable on each association. See Conditions on Relationships in Searching Lists for more information. (optional)

try: 
    # Get a list of Suppressions
    api_response = api_instance.list(page=page, include=include, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SuppressionsApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **str**| Page Number and Page Size.  number is the page number of the collection to return, size is the number of items to return per page | [optional] [default to {:number&#x3D;&gt;1,+:size&#x3D;&gt;20}]
 **include** | **str**| Related objects that can be included in the response:  organization, created_by, regions, external_accounts, signatures, custom_signatures See Including Objects for more information. | [optional] 
 **filter** | [**dict(str, str)**](str.md)| Filter Params for Searching.  Equality Searchable Attributes: [id, status, suppression_type, resource, reason] Matching Searchable Attributes: [resource, reason] Limited Searchable Attributes: [signature_name_cont, signature_identifier_cont] Sortable Attributes: [suppression_type, updated_at, created_at, id, status] Searchable Associations: [regions, created_by, signatures, custom_signatures, unique_identifier_signature, unique_identifier_custom_signature] See Searching Lists for more information. See the filter parameter of the association&#39;s list action to see what attributes are searchable on each association. See Conditions on Relationships in Searching Lists for more information. | [optional] 

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
include = 'include_example' # str | Related objects that can be included in the response:  organization, created_by, regions, external_accounts, signatures, custom_signatures See Including Objects for more information. (optional)

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
 **include** | **str**| Related objects that can be included in the response:  organization, created_by, regions, external_accounts, signatures, custom_signatures See Including Objects for more information. | [optional] 

### Return type

[**Suppression**](Suppression.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suppress_region**
> Suppression suppress_region(regions, external_account_ids, reason, resource=resource, include=include)

Creates a region suppression

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
include = 'include_example' # str | Related objects that can be included in the response:  organization, created_by, regions, external_accounts, signatures, custom_signatures See Including Objects for more information. (optional)

try: 
    # Creates a region suppression
    api_response = api_instance.suppress_region(regions, external_account_ids, reason, resource=resource, include=include)
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
 **include** | **str**| Related objects that can be included in the response:  organization, created_by, regions, external_accounts, signatures, custom_signatures See Including Objects for more information. | [optional] 

### Return type

[**Suppression**](Suppression.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suppress_region_from_alert**
> Suppression suppress_region_from_alert(alert_id, reason, include=include)

Creates a region suppression from an alert

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
include = 'include_example' # str | Related objects that can be included in the response:  organization, created_by, regions, external_accounts, signatures, custom_signatures See Including Objects for more information. (optional)

try: 
    # Creates a region suppression from an alert
    api_response = api_instance.suppress_region_from_alert(alert_id, reason, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SuppressionsApi->suppress_region_from_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_id** | **int**| The ID for the alert you want to create a suppression for | 
 **reason** | **str**| The reason for creating the suppression | 
 **include** | **str**| Related objects that can be included in the response:  organization, created_by, regions, external_accounts, signatures, custom_signatures See Including Objects for more information. | [optional] 

### Return type

[**Suppression**](Suppression.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suppress_signature**
> Suppression suppress_signature(regions, external_account_ids, reason, signature_ids=signature_ids, custom_signature_ids=custom_signature_ids, resource=resource, include=include)

Creates a signature suppression

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
include = 'include_example' # str | Related objects that can be included in the response:  organization, created_by, regions, external_accounts, signatures, custom_signatures See Including Objects for more information. (optional)

try: 
    # Creates a signature suppression
    api_response = api_instance.suppress_signature(regions, external_account_ids, reason, signature_ids=signature_ids, custom_signature_ids=custom_signature_ids, resource=resource, include=include)
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
 **include** | **str**| Related objects that can be included in the response:  organization, created_by, regions, external_accounts, signatures, custom_signatures See Including Objects for more information. | [optional] 

### Return type

[**Suppression**](Suppression.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suppress_signature_from_alert**
> Suppression suppress_signature_from_alert(alert_id, reason, include=include)

Creates a signature suppression from an alert

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
include = 'include_example' # str | Related objects that can be included in the response:  organization, created_by, regions, external_accounts, signatures, custom_signatures See Including Objects for more information. (optional)

try: 
    # Creates a signature suppression from an alert
    api_response = api_instance.suppress_signature_from_alert(alert_id, reason, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SuppressionsApi->suppress_signature_from_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_id** | **int**| The ID for the alert you want to create a suppression for | 
 **reason** | **str**| The reason for creating the suppression | 
 **include** | **str**| Related objects that can be included in the response:  organization, created_by, regions, external_accounts, signatures, custom_signatures See Including Objects for more information. | [optional] 

### Return type

[**Suppression**](Suppression.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suppress_unique_identifier_from_alert**
> Suppression suppress_unique_identifier_from_alert(alert_id, reason, include=include)

Creates a unique identifier suppression from an alert

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
include = 'include_example' # str | Related objects that can be included in the response:  organization, created_by, regions, external_accounts, signatures, custom_signatures See Including Objects for more information. (optional)

try: 
    # Creates a unique identifier suppression from an alert
    api_response = api_instance.suppress_unique_identifier_from_alert(alert_id, reason, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SuppressionsApi->suppress_unique_identifier_from_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_id** | **int**| The ID for the alert you want to create a suppression for | 
 **reason** | **str**| The reason for creating the suppression | 
 **include** | **str**| Related objects that can be included in the response:  organization, created_by, regions, external_accounts, signatures, custom_signatures See Including Objects for more information. | [optional] 

### Return type

[**Suppression**](Suppression.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

