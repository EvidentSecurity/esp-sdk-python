# esp_sdk.ExternalAccountsApi

All URIs are relative to *http://localhost/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](ExternalAccountsApi.md#create) | **POST** /api/v2/external_accounts.json_api | Create a(n) External Account
[**destroy**](ExternalAccountsApi.md#destroy) | **DELETE** /api/v2/external_accounts/{id}.json_api | Remove a(n) ExternalAccount
[**list**](ExternalAccountsApi.md#list) | **PUT** /api/v2/external_accounts.json_api | Get a list of External Accounts
[**show**](ExternalAccountsApi.md#show) | **GET** /api/v2/external_accounts/{id}.json_api | Show a single External Account
[**update**](ExternalAccountsApi.md#update) | **PATCH** /api/v2/external_accounts/{id}.json_api | Update a(n) External Account


# **create**
> ExternalAccount create(team_id, arn, external_id, name=name)

Create a(n) External Account

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.ExternalAccountsApi()
team_id = 56 # int | The ID of the team the external account will belong to
arn = 'arn_example' # str | Amazon Resource Name for the IAM role
external_id = 'external_id_example' # str | External identifier set on the role
name = 'name_example' # str | The name for this external account (optional)

try: 
    # Create a(n) External Account
    api_response = api_instance.create(team_id, arn, external_id, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalAccountsApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| The ID of the team the external account will belong to | 
 **arn** | **str**| Amazon Resource Name for the IAM role | 
 **external_id** | **str**| External identifier set on the role | 
 **name** | **str**| The name for this external account | [optional] 

### Return type

[**ExternalAccount**](ExternalAccount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy**
> ExternalAccount destroy(id)

Remove a(n) ExternalAccount

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.ExternalAccountsApi()
id = 56 # int | ExternalAccount Id

try: 
    # Remove a(n) ExternalAccount
    api_response = api_instance.destroy(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalAccountsApi->destroy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ExternalAccount Id | 

### Return type

[**ExternalAccount**](ExternalAccount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> PaginatedCollection list(filter=filter, include=include, page=page)

Get a list of External Accounts

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.ExternalAccountsApi()
filter = {'key': 'filter_example'} # dict(str, str) | Filter Params for Searching.  Equality Searchable Attributes: [id, nickname, name] Matching Searchable Attributes: [nickname, name] Limited Searchable Attributes: [account_eq, arn_eq] Sortable Attributes: [name, updated_at, created_at, id] Searchable Associations: [organization, sub_organization, team, compliance_standards, disabled_signatures] See the filter parameter of the association's list action to see what attributes are searchable on each association. See Searching on Relationships for more information. See Searching Lists for more information. Example: filter: {name_eq: 'Bob'} (optional)
include = 'include_example' # str | Objects that can be included in the response:  organization,sub_organization,team,scan_intervals,disabled_signatures,credentials  See Including Objects for more information. (optional)
page = {'key': 'page_example'} # dict(str, str) | Page Number and Page Size.  Example: page: {number: 1, size: 20} (optional)

try: 
    # Get a list of External Accounts
    api_response = api_instance.list(filter=filter, include=include, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalAccountsApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | [**dict(str, str)**](str.md)| Filter Params for Searching.  Equality Searchable Attributes: [id, nickname, name] Matching Searchable Attributes: [nickname, name] Limited Searchable Attributes: [account_eq, arn_eq] Sortable Attributes: [name, updated_at, created_at, id] Searchable Associations: [organization, sub_organization, team, compliance_standards, disabled_signatures] See the filter parameter of the association&#39;s list action to see what attributes are searchable on each association. See Searching on Relationships for more information. See Searching Lists for more information. Example: filter: {name_eq: &#39;Bob&#39;} | [optional] 
 **include** | **str**| Objects that can be included in the response:  organization,sub_organization,team,scan_intervals,disabled_signatures,credentials  See Including Objects for more information. | [optional] 
 **page** | [**dict(str, str)**](str.md)| Page Number and Page Size.  Example: page: {number: 1, size: 20} | [optional] 

### Return type

[**PaginatedCollection**](PaginatedCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show**
> ExternalAccount show(id, include=include)

Show a single External Account

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.ExternalAccountsApi()
id = 56 # int | External Account Id
include = 'include_example' # str | Objects that can be included in the response:  organization,sub_organization,team,scan_intervals,disabled_signatures,credentials  See Including Objects for more information. (optional)

try: 
    # Show a single External Account
    api_response = api_instance.show(id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalAccountsApi->show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| External Account Id | 
 **include** | **str**| Objects that can be included in the response:  organization,sub_organization,team,scan_intervals,disabled_signatures,credentials  See Including Objects for more information. | [optional] 

### Return type

[**ExternalAccount**](ExternalAccount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> ExternalAccount update(id, arn, external_id, sub_organization_id, team_id, name=name)

Update a(n) External Account

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.ExternalAccountsApi()
id = 56 # int | External Account Id
arn = 'arn_example' # str | Amazon Resource Name for the IAM role
external_id = 56 # int | External identifier set on the role
sub_organization_id = 56 # int | The ID of the sub organization the external account will belong to
team_id = 56 # int | The ID of the team the external account will belong to
name = 'name_example' # str | The name for this external account (optional)

try: 
    # Update a(n) External Account
    api_response = api_instance.update(id, arn, external_id, sub_organization_id, team_id, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalAccountsApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| External Account Id | 
 **arn** | **str**| Amazon Resource Name for the IAM role | 
 **external_id** | **int**| External identifier set on the role | 
 **sub_organization_id** | **int**| The ID of the sub organization the external account will belong to | 
 **team_id** | **int**| The ID of the team the external account will belong to | 
 **name** | **str**| The name for this external account | [optional] 

### Return type

[**ExternalAccount**](ExternalAccount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

