# esp_sdk.ExternalAccountsAzureApi

All URIs are relative to https://api.evident.io

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](ExternalAccountsAzureApi.md#create) | **POST** /api/v2/external_accounts/azure.json_api | Create an Azure External Account
[**reset_url**](ExternalAccountsAzureApi.md#reset_url) | **PATCH** /api/v2/external_accounts/{external_account_id}/azure/log_url.json_api | Reset Log URL for an Azure External Account
[**show**](ExternalAccountsAzureApi.md#show) | **GET** /api/v2/external_accounts/{external_account_id}/azure.json_api | Show an Azure External Account
[**update**](ExternalAccountsAzureApi.md#update) | **PATCH** /api/v2/external_accounts/{external_account_id}/azure.json_api | Update an Azure External Account


# **create**
> ExternalAccountAzure create(app_key, client_id, name, subscription_id, team_id, tenant_id)

Create an Azure External Account

The channel_url will only be returned in this response and will not be accessible again. The related external_account object will be returned with the response.

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.ExternalAccountsAzureApi()
app_key = 'app_key_example' # str | Azure app key
client_id = 'client_id_example' # str | Azure client ID
name = 'name_example' # str | Name
subscription_id = 'subscription_id_example' # str | Azure subscription ID
team_id = 56 # int | The ID of the team the external account belongs to
tenant_id = 'tenant_id_example' # str | Azure tenant ID

try: 
    # Create an Azure External Account
    api_response = api_instance.create(app_key, client_id, name, subscription_id, team_id, tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalAccountsAzureApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**| Azure app key | 
 **client_id** | **str**| Azure client ID | 
 **name** | **str**| Name | 
 **subscription_id** | **str**| Azure subscription ID | 
 **team_id** | **int**| The ID of the team the external account belongs to | 
 **tenant_id** | **str**| Azure tenant ID | 

### Return type

[**ExternalAccountAzure**](ExternalAccountAzure.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_url**
> ExternalAccountAzure reset_url(external_account_id)

Reset Log URL for an Azure External Account

This endpoint invalidates the previous URL and generates a new one. The channel_url will only be returned in this response and will not be accessible again. The related external_account object will be returned with the response.

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.ExternalAccountsAzureApi()
external_account_id = 56 # int | The ID of the external account to reset an Azure log URL for

try: 
    # Reset Log URL for an Azure External Account
    api_response = api_instance.reset_url(external_account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalAccountsAzureApi->reset_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_account_id** | **int**| The ID of the external account to reset an Azure log URL for | 

### Return type

[**ExternalAccountAzure**](ExternalAccountAzure.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show**
> ExternalAccountAzure show(external_account_id, include=include)

Show an Azure External Account



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.ExternalAccountsAzureApi()
external_account_id = 56 # int | The ID of the external account to show an Azure credential for
include = 'include_example' # str | Related objects that can be included in the response:  external_account See Including Objects for more information. (optional)

try: 
    # Show an Azure External Account
    api_response = api_instance.show(external_account_id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalAccountsAzureApi->show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_account_id** | **int**| The ID of the external account to show an Azure credential for | 
 **include** | **str**| Related objects that can be included in the response:  external_account See Including Objects for more information. | [optional] 

### Return type

[**ExternalAccountAzure**](ExternalAccountAzure.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> ExternalAccountAzure update(external_account_id, app_key=app_key, client_id=client_id, name=name, subscription_id=subscription_id, team_id=team_id, tenant_id=tenant_id)

Update an Azure External Account

 The related external_account object will be returned with the response.

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.ExternalAccountsAzureApi()
external_account_id = 56 # int | The ID of the external account to update an Azure credential for
app_key = 'app_key_example' # str | Azure app key (optional)
client_id = 'client_id_example' # str | Azure client ID (optional)
name = 'name_example' # str | Name (optional)
subscription_id = 'subscription_id_example' # str | Azure subscription ID (optional)
team_id = 56 # int | The ID of the team the external account belongs to (optional)
tenant_id = 'tenant_id_example' # str | Azure tenant ID (optional)

try: 
    # Update an Azure External Account
    api_response = api_instance.update(external_account_id, app_key=app_key, client_id=client_id, name=name, subscription_id=subscription_id, team_id=team_id, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalAccountsAzureApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_account_id** | **int**| The ID of the external account to update an Azure credential for | 
 **app_key** | **str**| Azure app key | [optional] 
 **client_id** | **str**| Azure client ID | [optional] 
 **name** | **str**| Name | [optional] 
 **subscription_id** | **str**| Azure subscription ID | [optional] 
 **team_id** | **int**| The ID of the team the external account belongs to | [optional] 
 **tenant_id** | **str**| Azure tenant ID | [optional] 

### Return type

[**ExternalAccountAzure**](ExternalAccountAzure.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

