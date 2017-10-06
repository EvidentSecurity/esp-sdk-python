# esp_sdk.ExternalAccountsApi

All URIs are relative to https://api.evident.io

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](ExternalAccountsApi.md#create) | **POST** /api/v2/external_accounts.json_api | Create a(n) ExternalAccount
[**destroy**](ExternalAccountsApi.md#destroy) | **DELETE** /api/v2/external_accounts/{id}.json_api | Remove a(n) ExternalAccount
[**list**](ExternalAccountsApi.md#list) | **PUT** /api/v2/external_accounts.json_api | Get a list of ExternalAccounts
[**show**](ExternalAccountsApi.md#show) | **GET** /api/v2/external_accounts/{id}.json_api | Show a single ExternalAccount
[**update**](ExternalAccountsApi.md#update) | **PATCH** /api/v2/external_accounts/{id}.json_api | Update a(n) ExternalAccount


# **create**
> ExternalAccount create(team_id, arn, external_id, name=name)

Create a(n) ExternalAccount

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
external_id = 'external_id_example' # str | External Identifier set on the role
name = 'name_example' # str | Name (optional)

try: 
    # Create a(n) ExternalAccount
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
 **external_id** | **str**| External Identifier set on the role | 
 **name** | **str**| Name | [optional] 

### Return type

[**ExternalAccount**](ExternalAccount.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy**
> Meta destroy(id)

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
id = 56 # int | ExternalAccount ID

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
 **id** | **int**| ExternalAccount ID | 

### Return type

[**Meta**](Meta.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> PaginatedCollection list(filter=filter, include=include, page=page)

Get a list of ExternalAccounts

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.ExternalAccountsApi()
filter = {'key': 'filter_example'} # dict(str, str) | Filter Params for Searching.  See Searching Lists for more information. (optional)
include = 'include_example' # str | Related objects that can be included in the response.  See Including Objects for more information. (optional)
page = '{:number=>1,+:size=>20}' # str | Page Number and Page Size.  number is the page number of the collection to return, size is the number of items to return per page (optional) (default to {:number=>1,+:size=>20})

try: 
    # Get a list of ExternalAccounts
    api_response = api_instance.list(filter=filter, include=include, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalAccountsApi->list: %s\n" % e)
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
> ExternalAccount show(id, include=include)

Show a single ExternalAccount

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.ExternalAccountsApi()
id = 56 # int | ExternalAccount ID
include = 'include_example' # str | Related objects that can be included in the response.  See Including Objects for more information. (optional)

try: 
    # Show a single ExternalAccount
    api_response = api_instance.show(id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalAccountsApi->show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ExternalAccount ID | 
 **include** | **str**| Related objects that can be included in the response.  See Including Objects for more information. | [optional] 

### Return type

[**ExternalAccount**](ExternalAccount.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> ExternalAccount update(id, team_id, name=name)

Update a(n) ExternalAccount

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.ExternalAccountsApi()
id = 56 # int | ExternalAccount ID
team_id = 56 # int | The ID of the team the external account will belong to
name = 'name_example' # str | Name (optional)

try: 
    # Update a(n) ExternalAccount
    api_response = api_instance.update(id, team_id, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalAccountsApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ExternalAccount ID | 
 **team_id** | **int**| The ID of the team the external account will belong to | 
 **name** | **str**| Name | [optional] 

### Return type

[**ExternalAccount**](ExternalAccount.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

