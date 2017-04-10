# esp_sdk.ExternalAccountsApi

All URIs are relative to *http://localhost/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_external_accounts_id_complete_json_api_patch**](ExternalAccountsApi.md#api_v2_external_accounts_id_complete_json_api_patch) | **PATCH** /api/v2/external_accounts/{id}/complete.json_api | Show the latest completed report for an External Account
[**api_v2_external_accounts_subscribed_accounts_json_api_get**](ExternalAccountsApi.md#api_v2_external_accounts_subscribed_accounts_json_api_get) | **GET** /api/v2/external_accounts/subscribed_accounts.json_api | Show a list of Subscribed Accounts
[**create**](ExternalAccountsApi.md#create) | **POST** /api/v2/external_accounts.json_api | Create a(n) External Account
[**destroy**](ExternalAccountsApi.md#destroy) | **DELETE** /api/v2/external_accounts/{id}.json_api | Remove a(n) External Account
[**list**](ExternalAccountsApi.md#list) | **PUT** /api/v2/external_accounts.json_api | Get a list of External Accounts
[**show**](ExternalAccountsApi.md#show) | **GET** /api/v2/external_accounts/{id}.json_api | Show a single External Account
[**update**](ExternalAccountsApi.md#update) | **PATCH** /api/v2/external_accounts/{id}.json_api | Update a(n) External Account


# **api_v2_external_accounts_id_complete_json_api_patch**
> api_v2_external_accounts_id_complete_json_api_patch(id)

Show the latest completed report for an External Account

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

try: 
    # Show the latest completed report for an External Account
    api_instance.api_v2_external_accounts_id_complete_json_api_patch(id)
except ApiException as e:
    print("Exception when calling ExternalAccountsApi->api_v2_external_accounts_id_complete_json_api_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| External Account Id | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_external_accounts_subscribed_accounts_json_api_get**
> api_v2_external_accounts_subscribed_accounts_json_api_get()

Show a list of Subscribed Accounts

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.ExternalAccountsApi()

try: 
    # Show a list of Subscribed Accounts
    api_instance.api_v2_external_accounts_subscribed_accounts_json_api_get()
except ApiException as e:
    print("Exception when calling ExternalAccountsApi->api_v2_external_accounts_subscribed_accounts_json_api_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
team_id = 56 # int | Team Id
arn = 'arn_example' # str | ARN
external_id = 'external_id_example' # str | External Id
name = 'name_example' # str | Name (optional)

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
 **team_id** | **int**| Team Id | 
 **arn** | **str**| ARN | 
 **external_id** | **str**| External Id | 
 **name** | **str**| Name | [optional] 

### Return type

[**ExternalAccount**](ExternalAccount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy**
> object destroy(id)

Remove a(n) External Account

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

try: 
    # Remove a(n) External Account
    api_response = api_instance.destroy(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalAccountsApi->destroy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| External Account Id | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> PaginatedCollection list(page=page, filter=filter, include=include)

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
page = {'key': 'page_example'} # dict(str, str) | Page Number (optional)
filter = {'key': 'filter_example'} # dict(str, str) | Filter Params for Searching (optional)
include = 'include_example' # str | Included Objects (optional)

try: 
    # Get a list of External Accounts
    api_response = api_instance.list(page=page, filter=filter, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalAccountsApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
include = 'include_example' # str | Included Objects (optional)

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
 **include** | **str**| Included Objects | [optional] 

### Return type

[**ExternalAccount**](ExternalAccount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

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
arn = 'arn_example' # str | ARN
external_id = 56 # int | External Id
sub_organization_id = 56 # int | Sub Organization Id
team_id = 56 # int | Team Id
name = 'name_example' # str | Name (optional)

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
 **arn** | **str**| ARN | 
 **external_id** | **int**| External Id | 
 **sub_organization_id** | **int**| Sub Organization Id | 
 **team_id** | **int**| Team Id | 
 **name** | **str**| Name | [optional] 

### Return type

[**ExternalAccount**](ExternalAccount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

