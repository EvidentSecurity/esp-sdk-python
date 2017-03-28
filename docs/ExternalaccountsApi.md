# esp_sdk.ExternalaccountsApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](ExternalaccountsApi.md#create) | **POST** /v2/external_accounts.json | Create a(n) External Account
[**destroy**](ExternalaccountsApi.md#destroy) | **DELETE** /v2/external_accounts/{id}.json | Remove a(n) External Account
[**list**](ExternalaccountsApi.md#list) | **PUT** /v2/external_accounts.json | Get a list of External Accounts
[**show**](ExternalaccountsApi.md#show) | **GET** /v2/external_accounts/{id}.json | Show a single External Account
[**update**](ExternalaccountsApi.md#update) | **PATCH** /v2/external_accounts/{id}.json | Update a(n) External Account
[**v2_external_accounts_id_complete_json_patch**](ExternalaccountsApi.md#v2_external_accounts_id_complete_json_patch) | **PATCH** /v2/external_accounts/{id}/complete.json | Show the latest completed report for an External Account
[**v2_external_accounts_subscribed_accounts_json_get**](ExternalaccountsApi.md#v2_external_accounts_subscribed_accounts_json_get) | **GET** /v2/external_accounts/subscribed_accounts.json | Show a list of Subscribed Accounts


# **create**
> ExternalAccount create(name=name, nickname=nickname, team_id=team_id, arn=arn, external_id=external_id, agency=agency, mission=mission, role=role)

Create a(n) External Account

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.ExternalaccountsApi()
name = 'name_example' # str | Name (optional)
nickname = 'nickname_example' # str | Nickname (optional)
team_id = 56 # int | Team Id (optional)
arn = 'arn_example' # str | ARN (optional)
external_id = 'external_id_example' # str | External Id (optional)
agency = 'agency_example' # str | Agency (optional)
mission = 'mission_example' # str | Mission (optional)
role = 'role_example' # str | Role (optional)

try: 
    # Create a(n) External Account
    api_response = api_instance.create(name=name, nickname=nickname, team_id=team_id, arn=arn, external_id=external_id, agency=agency, mission=mission, role=role)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalaccountsApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name | [optional] 
 **nickname** | **str**| Nickname | [optional] 
 **team_id** | **int**| Team Id | [optional] 
 **arn** | **str**| ARN | [optional] 
 **external_id** | **str**| External Id | [optional] 
 **agency** | **str**| Agency | [optional] 
 **mission** | **str**| Mission | [optional] 
 **role** | **str**| Role | [optional] 

### Return type

[**ExternalAccount**](ExternalAccount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy**
> ExternalAccount destroy(id)

Remove a(n) External Account

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.ExternalaccountsApi()
id = 56 # int | External Account Id

try: 
    # Remove a(n) External Account
    api_response = api_instance.destroy(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalaccountsApi->destroy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| External Account Id | 

### Return type

[**ExternalAccount**](ExternalAccount.md)

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
api_instance = esp_sdk.ExternalaccountsApi()
page = {'key': 'page_example'} # dict(str, str) | Page Number (optional)
filter = {'key': 'filter_example'} # dict(str, str) | Filter Params for Searching (optional)
include = 'include_example' # str | Included Objects (optional)

try: 
    # Get a list of External Accounts
    api_response = api_instance.list(page=page, filter=filter, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalaccountsApi->list: %s\n" % e)
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
api_instance = esp_sdk.ExternalaccountsApi()
id = 56 # int | External Account Id
include = 'include_example' # str | Included Objects (optional)

try: 
    # Show a single External Account
    api_response = api_instance.show(id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalaccountsApi->show: %s\n" % e)
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
> ExternalAccount update(id, name=name, nickname=nickname, team_id=team_id)

Update a(n) External Account

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.ExternalaccountsApi()
id = 56 # int | External Account Id
name = 'name_example' # str | Name (optional)
nickname = 'nickname_example' # str | Nickname (optional)
team_id = 56 # int | Team Id (optional)

try: 
    # Update a(n) External Account
    api_response = api_instance.update(id, name=name, nickname=nickname, team_id=team_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalaccountsApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| External Account Id | 
 **name** | **str**| Name | [optional] 
 **nickname** | **str**| Nickname | [optional] 
 **team_id** | **int**| Team Id | [optional] 

### Return type

[**ExternalAccount**](ExternalAccount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_external_accounts_id_complete_json_patch**
> v2_external_accounts_id_complete_json_patch(id)

Show the latest completed report for an External Account

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.ExternalaccountsApi()
id = 56 # int | External Account Id

try: 
    # Show the latest completed report for an External Account
    api_instance.v2_external_accounts_id_complete_json_patch(id)
except ApiException as e:
    print("Exception when calling ExternalaccountsApi->v2_external_accounts_id_complete_json_patch: %s\n" % e)
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

# **v2_external_accounts_subscribed_accounts_json_get**
> v2_external_accounts_subscribed_accounts_json_get()

Show a list of Subscribed Accounts

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.ExternalaccountsApi()

try: 
    # Show a list of Subscribed Accounts
    api_instance.v2_external_accounts_subscribed_accounts_json_get()
except ApiException as e:
    print("Exception when calling ExternalaccountsApi->v2_external_accounts_subscribed_accounts_json_get: %s\n" % e)
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

