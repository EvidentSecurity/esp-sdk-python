# esp_sdk.SuppressionsApi

All URIs are relative to https://api.evident.io

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](SuppressionsApi.md#create) | **POST** /api/v2/suppressions.json_api | Create a suppression
[**create_from_alert**](SuppressionsApi.md#create_from_alert) | **POST** /api/v2/suppressions/alerts.json_api | Creates a suppression from an alert
[**deactivate**](SuppressionsApi.md#deactivate) | **PATCH** /api/v2/suppressions/{id}/deactivate.json_api | Deactivate a suppression
[**list**](SuppressionsApi.md#list) | **PUT** /api/v2/suppressions.json_api | Get a list of Suppressions
[**show**](SuppressionsApi.md#show) | **GET** /api/v2/suppressions/{id}.json_api | Show a single Suppression
[**update**](SuppressionsApi.md#update) | **PATCH** /api/v2/suppressions/{id}.json_api | Update a(n) Suppression


# **create**
> Suppression create(external_account_ids, reason, regions, include=include, custom_signature_ids=custom_signature_ids, include_new_accounts=include_new_accounts, resource=resource, signature_ids=signature_ids)

Create a suppression



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.SuppressionsApi()
external_account_ids = [56] # list[int] | IDs of external accounts to be suppressed
reason = 'reason_example' # str | The reason for the suppresion
regions = ['regions_example'] # list[str] | Codes of regions to be suppressed
include = 'include_example' # str | Related objects that can be included in the response:  organization, created_by, regions, external_accounts, signatures, custom_signatures See Including Objects for more information. (optional)
custom_signature_ids = [56] # list[int] | IDs of custom signatures to be suppressed (optional)
include_new_accounts = true # bool | When enabled, automatically adds new accounts to this suppression. This field can only be set by an organization level user. (optional)
resource = 'resource_example' # str | The resource string this suppression will suppress alerts for (optional)
signature_ids = [56] # list[int] | IDs of signatures to be suppressed (optional)

try: 
    # Create a suppression
    api_response = api_instance.create(external_account_ids, reason, regions, include=include, custom_signature_ids=custom_signature_ids, include_new_accounts=include_new_accounts, resource=resource, signature_ids=signature_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SuppressionsApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_account_ids** | [**list[int]**](int.md)| IDs of external accounts to be suppressed | 
 **reason** | **str**| The reason for the suppresion | 
 **regions** | [**list[str]**](str.md)| Codes of regions to be suppressed | 
 **include** | **str**| Related objects that can be included in the response:  organization, created_by, regions, external_accounts, signatures, custom_signatures See Including Objects for more information. | [optional] 
 **custom_signature_ids** | [**list[int]**](int.md)| IDs of custom signatures to be suppressed | [optional] 
 **include_new_accounts** | **bool**| When enabled, automatically adds new accounts to this suppression. This field can only be set by an organization level user. | [optional] 
 **resource** | **str**| The resource string this suppression will suppress alerts for | [optional] 
 **signature_ids** | [**list[int]**](int.md)| IDs of signatures to be suppressed | [optional] 

### Return type

[**Suppression**](Suppression.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_from_alert**
> Suppression create_from_alert(alert_id, reason, include=include)

Creates a suppression from an alert

A successful call to this API creates a new suppression based on the supplied alert_id. The body of the request must contain a json api compliant hash of the suppression reason and an alert id.

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
    # Creates a suppression from an alert
    api_response = api_instance.create_from_alert(alert_id, reason, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SuppressionsApi->create_from_alert: %s\n" % e)
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

See https://github.com/EvidentSecurity/esp-sdk-python#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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

See https://github.com/EvidentSecurity/esp-sdk-python#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> PaginatedCollection list(include=include, filter=filter, page=page)

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
include = 'include_example' # str | Related objects that can be included in the response:  organization, created_by, regions, external_accounts, signatures, custom_signatures See Including Objects for more information. (optional)
filter = {'key': 'filter_example'} # dict(str, str) | Filter Params for Searching.  Equality Searchable Attributes: [id, aasm_state, status, suppression_type, resource, reason] Matching Searchable Attributes: [resource, reason]  Sortable Attributes: [updated_at, created_at, id, status] Searchable Associations: [regions, external_accounts, created_by, user, signatures, custom_signatures] See Searching Lists for more information. See the filter parameter of the association's list action to see what attributes are searchable on each association. See Conditions on Relationships in Searching Lists for more information. (optional)
page = '{:number=>1,+:size=>20}' # str | Page Number and Page Size.  Number is the page number of the collection to return, size is the number of items to return per page. (optional) (default to {:number=>1,+:size=>20})

try: 
    # Get a list of Suppressions
    api_response = api_instance.list(include=include, filter=filter, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SuppressionsApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include** | **str**| Related objects that can be included in the response:  organization, created_by, regions, external_accounts, signatures, custom_signatures See Including Objects for more information. | [optional] 
 **filter** | [**dict(str, str)**](str.md)| Filter Params for Searching.  Equality Searchable Attributes: [id, aasm_state, status, suppression_type, resource, reason] Matching Searchable Attributes: [resource, reason]  Sortable Attributes: [updated_at, created_at, id, status] Searchable Associations: [regions, external_accounts, created_by, user, signatures, custom_signatures] See Searching Lists for more information. See the filter parameter of the association&#39;s list action to see what attributes are searchable on each association. See Conditions on Relationships in Searching Lists for more information. | [optional] 
 **page** | **str**| Page Number and Page Size.  Number is the page number of the collection to return, size is the number of items to return per page. | [optional] [default to {:number&#x3D;&gt;1,+:size&#x3D;&gt;20}]

### Return type

[**PaginatedCollection**](PaginatedCollection.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python#set-your-hmac-security-keys

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

See https://github.com/EvidentSecurity/esp-sdk-python#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> Suppression update(id, include=include, custom_signature_ids=custom_signature_ids, external_account_ids=external_account_ids, include_new_accounts=include_new_accounts, reason=reason, regions=regions, resource=resource, signature_ids=signature_ids)

Update a(n) Suppression



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
custom_signature_ids = [56] # list[int] | IDs of custom signatures to be suppressed (optional)
external_account_ids = [56] # list[int] | IDs of external accounts to be suppressed (optional)
include_new_accounts = true # bool | When enabled, automatically adds new accounts to this suppression. This field can only be set by an organization level user. (optional)
reason = 'reason_example' # str | The reason for the suppresion (optional)
regions = ['regions_example'] # list[str] | Codes of regions to be suppressed (optional)
resource = 'resource_example' # str | The resource string this suppression will suppress alerts for (optional)
signature_ids = [56] # list[int] | IDs of signatures to be suppressed (optional)

try: 
    # Update a(n) Suppression
    api_response = api_instance.update(id, include=include, custom_signature_ids=custom_signature_ids, external_account_ids=external_account_ids, include_new_accounts=include_new_accounts, reason=reason, regions=regions, resource=resource, signature_ids=signature_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SuppressionsApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Suppression ID | 
 **include** | **str**| Related objects that can be included in the response:  organization, created_by, regions, external_accounts, signatures, custom_signatures See Including Objects for more information. | [optional] 
 **custom_signature_ids** | [**list[int]**](int.md)| IDs of custom signatures to be suppressed | [optional] 
 **external_account_ids** | [**list[int]**](int.md)| IDs of external accounts to be suppressed | [optional] 
 **include_new_accounts** | **bool**| When enabled, automatically adds new accounts to this suppression. This field can only be set by an organization level user. | [optional] 
 **reason** | **str**| The reason for the suppresion | [optional] 
 **regions** | [**list[str]**](str.md)| Codes of regions to be suppressed | [optional] 
 **resource** | **str**| The resource string this suppression will suppress alerts for | [optional] 
 **signature_ids** | [**list[int]**](int.md)| IDs of signatures to be suppressed | [optional] 

### Return type

[**Suppression**](Suppression.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

