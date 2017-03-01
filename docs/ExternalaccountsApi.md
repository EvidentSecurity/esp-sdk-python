# esp_sdk.ExternalaccountsApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2_external_accounts_id_complete_json_patch**](ExternalaccountsApi.md#v2_external_accounts_id_complete_json_patch) | **PATCH** /v2/external_accounts/{id}/complete.json | Show the latest completed report for an External Account
[**v2_external_accounts_id_json_delete**](ExternalaccountsApi.md#v2_external_accounts_id_json_delete) | **DELETE** /v2/external_accounts/{id}.json | Remove an External Account
[**v2_external_accounts_id_json_get**](ExternalaccountsApi.md#v2_external_accounts_id_json_get) | **GET** /v2/external_accounts/{id}.json | Show a single External Account
[**v2_external_accounts_id_json_patch**](ExternalaccountsApi.md#v2_external_accounts_id_json_patch) | **PATCH** /v2/external_accounts/{id}.json | Update an External Account
[**v2_external_accounts_json_post**](ExternalaccountsApi.md#v2_external_accounts_json_post) | **POST** /v2/external_accounts.json | Create an External Account
[**v2_external_accounts_json_put**](ExternalaccountsApi.md#v2_external_accounts_json_put) | **PUT** /v2/external_accounts.json | Get a list of External Accounts
[**v2_external_accounts_subscribed_accounts_json_get**](ExternalaccountsApi.md#v2_external_accounts_subscribed_accounts_json_get) | **GET** /v2/external_accounts/subscribed_accounts.json | Show a list of Subscribed Accounts


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

# **v2_external_accounts_id_json_delete**
> v2_external_accounts_id_json_delete(id)

Remove an External Account

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
    # Remove an External Account
    api_instance.v2_external_accounts_id_json_delete(id)
except ApiException as e:
    print("Exception when calling ExternalaccountsApi->v2_external_accounts_id_json_delete: %s\n" % e)
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

# **v2_external_accounts_id_json_get**
> v2_external_accounts_id_json_get(id)

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

try: 
    # Show a single External Account
    api_instance.v2_external_accounts_id_json_get(id)
except ApiException as e:
    print("Exception when calling ExternalaccountsApi->v2_external_accounts_id_json_get: %s\n" % e)
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

# **v2_external_accounts_id_json_patch**
> v2_external_accounts_id_json_patch(id, name=name, nickname=nickname, team_id=team_id)

Update an External Account

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
    # Update an External Account
    api_instance.v2_external_accounts_id_json_patch(id, name=name, nickname=nickname, team_id=team_id)
except ApiException as e:
    print("Exception when calling ExternalaccountsApi->v2_external_accounts_id_json_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| External Account Id | 
 **name** | **str**| Name | [optional] 
 **nickname** | **str**| Nickname | [optional] 
 **team_id** | **int**| Team Id | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_external_accounts_json_post**
> v2_external_accounts_json_post(name=name, nickname=nickname, team_id=team_id, arn=arn, external_id=external_id, agency=agency, mission=mission, role=role)

Create an External Account

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
    # Create an External Account
    api_instance.v2_external_accounts_json_post(name=name, nickname=nickname, team_id=team_id, arn=arn, external_id=external_id, agency=agency, mission=mission, role=role)
except ApiException as e:
    print("Exception when calling ExternalaccountsApi->v2_external_accounts_json_post: %s\n" % e)
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

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_external_accounts_json_put**
> v2_external_accounts_json_put()

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

try: 
    # Get a list of External Accounts
    api_instance.v2_external_accounts_json_put()
except ApiException as e:
    print("Exception when calling ExternalaccountsApi->v2_external_accounts_json_put: %s\n" % e)
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

