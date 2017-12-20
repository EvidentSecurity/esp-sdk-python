# esp_sdk.AzureGroupsApi

All URIs are relative to https://api.evident.io

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_external_account**](AzureGroupsApi.md#add_external_account) | **POST** /api/v2/azure_groups/{azure_group_id}/memberships.json_api | Add an External Account to an Azure Group
[**create**](AzureGroupsApi.md#create) | **POST** /api/v2/azure_groups.json_api | Create a(n) Azure Group
[**delete**](AzureGroupsApi.md#delete) | **DELETE** /api/v2/azure_groups/{id}.json_api | Delete a(n) Azure Group
[**list**](AzureGroupsApi.md#list) | **PUT** /api/v2/azure_groups.json_api | Get a list of Azure Groups
[**remove_external_account**](AzureGroupsApi.md#remove_external_account) | **DELETE** /api/v2/azure_groups/{azure_group_id}/memberships/{external_account_id}.json_api | Remove an External Account from an Azure Group
[**show**](AzureGroupsApi.md#show) | **GET** /api/v2/azure_groups/{id}.json_api | Show a single Azure Group
[**update**](AzureGroupsApi.md#update) | **PATCH** /api/v2/azure_groups/{id}.json_api | Update a(n) Azure Group


# **add_external_account**
> ExternalAccount add_external_account(azure_group_id, external_account_id, include=include)

Add an External Account to an Azure Group



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.AzureGroupsApi()
azure_group_id = 56 # int | The ID of the Azure group associated with this memberhsip
external_account_id = 56 # int | The ID of the External Account associated with this memberhsip
include = 'include_example' # str | Related objects that can be included in the response:  organization, sub_organization, team, scan_intervals, disabled_signatures, azure_group, credentials See Including Objects for more information. (optional)

try: 
    # Add an External Account to an Azure Group
    api_response = api_instance.add_external_account(azure_group_id, external_account_id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AzureGroupsApi->add_external_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **azure_group_id** | **int**| The ID of the Azure group associated with this memberhsip | 
 **external_account_id** | **int**| The ID of the External Account associated with this memberhsip | 
 **include** | **str**| Related objects that can be included in the response:  organization, sub_organization, team, scan_intervals, disabled_signatures, azure_group, credentials See Including Objects for more information. | [optional] 

### Return type

[**ExternalAccount**](ExternalAccount.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create**
> AzureGroup create(name, include=include)

Create a(n) Azure Group

The URL will only be returned once when the group is first created

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.AzureGroupsApi()
name = 'name_example' # str | Name
include = 'include_example' # str | Related objects that can be included in the response:  organization, external_accounts See Including Objects for more information. (optional)

try: 
    # Create a(n) Azure Group
    api_response = api_instance.create(name, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AzureGroupsApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name | 
 **include** | **str**| Related objects that can be included in the response:  organization, external_accounts See Including Objects for more information. | [optional] 

### Return type

[**AzureGroup**](AzureGroup.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> Meta delete(id)

Delete a(n) Azure Group



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.AzureGroupsApi()
id = 56 # int |  ID

try: 
    # Delete a(n) Azure Group
    api_response = api_instance.delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AzureGroupsApi->delete: %s\n" % e)
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

# **list**
> PaginatedCollection list(filter=filter, page=page, include=include)

Get a list of Azure Groups



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.AzureGroupsApi()
filter = {'key': 'filter_example'} # dict(str, str) | Filter Params for Searching.  Equality Searchable Attributes: [id, name] Matching Searchable Attribute: [name]  Sortable Attributes: [id, name] Searchable Associations: [organization, external_accounts] See Searching Lists for more information. See the filter parameter of the association's list action to see what attributes are searchable on each association. See Conditions on Relationships in Searching Lists for more information. (optional)
page = '{:number=>1,+:size=>20}' # str | Page Number and Page Size.  number is the page number of the collection to return, size is the number of items to return per page (optional) (default to {:number=>1,+:size=>20})
include = 'include_example' # str | Related objects that can be included in the response:  organization, external_accounts See Including Objects for more information. (optional)

try: 
    # Get a list of Azure Groups
    api_response = api_instance.list(filter=filter, page=page, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AzureGroupsApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | [**dict(str, str)**](str.md)| Filter Params for Searching.  Equality Searchable Attributes: [id, name] Matching Searchable Attribute: [name]  Sortable Attributes: [id, name] Searchable Associations: [organization, external_accounts] See Searching Lists for more information. See the filter parameter of the association&#39;s list action to see what attributes are searchable on each association. See Conditions on Relationships in Searching Lists for more information. | [optional] 
 **page** | **str**| Page Number and Page Size.  number is the page number of the collection to return, size is the number of items to return per page | [optional] [default to {:number&#x3D;&gt;1,+:size&#x3D;&gt;20}]
 **include** | **str**| Related objects that can be included in the response:  organization, external_accounts See Including Objects for more information. | [optional] 

### Return type

[**PaginatedCollection**](PaginatedCollection.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_external_account**
> Meta remove_external_account(azure_group_id, external_account_id)

Remove an External Account from an Azure Group



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.AzureGroupsApi()
azure_group_id = 56 # int | The ID of the Azure group associated with this memberhsip
external_account_id = 56 # int | The ID of the External Account associated with this memberhsip

try: 
    # Remove an External Account from an Azure Group
    api_response = api_instance.remove_external_account(azure_group_id, external_account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AzureGroupsApi->remove_external_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **azure_group_id** | **int**| The ID of the Azure group associated with this memberhsip | 
 **external_account_id** | **int**| The ID of the External Account associated with this memberhsip | 

### Return type

[**Meta**](Meta.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show**
> AzureGroup show(id, include=include)

Show a single Azure Group



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.AzureGroupsApi()
id = 56 # int | Azure Group ID
include = 'include_example' # str | Related objects that can be included in the response:  organization, external_accounts See Including Objects for more information. (optional)

try: 
    # Show a single Azure Group
    api_response = api_instance.show(id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AzureGroupsApi->show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Azure Group ID | 
 **include** | **str**| Related objects that can be included in the response:  organization, external_accounts See Including Objects for more information. | [optional] 

### Return type

[**AzureGroup**](AzureGroup.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> AzureGroup update(id, name=name, include=include)

Update a(n) Azure Group



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.AzureGroupsApi()
id = 56 # int | Azure Group ID
name = 'name_example' # str | Name (optional)
include = 'include_example' # str | Related objects that can be included in the response:  organization, external_accounts See Including Objects for more information. (optional)

try: 
    # Update a(n) Azure Group
    api_response = api_instance.update(id, name=name, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AzureGroupsApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Azure Group ID | 
 **name** | **str**| Name | [optional] 
 **include** | **str**| Related objects that can be included in the response:  organization, external_accounts See Including Objects for more information. | [optional] 

### Return type

[**AzureGroup**](AzureGroup.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

