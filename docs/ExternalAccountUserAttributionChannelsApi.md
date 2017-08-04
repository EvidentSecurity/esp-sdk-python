# esp_sdk.ExternalAccountUserAttributionChannelsApi

All URIs are relative to *http://localhost/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](ExternalAccountUserAttributionChannelsApi.md#create) | **POST** /api/v2/external_accounts/{external_account_id}/user_attribution/channel.json_api | A successful call to this API will create a User Attribution Channel for an external account.
[**destroy**](ExternalAccountUserAttributionChannelsApi.md#destroy) | **DELETE** /api/v2/external_accounts/{external_account_id}/user_attribution/channel.json_api | A successful call to this API will remove the User Attribution Channel for an external account.
[**show**](ExternalAccountUserAttributionChannelsApi.md#show) | **GET** /api/v2/external_accounts/{external_account_id}/user_attribution/channel.json_api | A successful call to this API will show the User Attribution Channel of an external account.


# **create**
> Channel create(external_account_id)

A successful call to this API will create a User Attribution Channel for an external account.

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.ExternalAccountUserAttributionChannelsApi()
external_account_id = 56 # int | The ID of the external account to create a User Attribution Channel for

try: 
    # A successful call to this API will create a User Attribution Channel for an external account.
    api_response = api_instance.create(external_account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalAccountUserAttributionChannelsApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_account_id** | **int**| The ID of the external account to create a User Attribution Channel for | 

### Return type

[**Channel**](Channel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy**
> Channel destroy(external_account_id)

A successful call to this API will remove the User Attribution Channel for an external account.

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.ExternalAccountUserAttributionChannelsApi()
external_account_id = 56 # int | The ID of the external account to remove the User Attribution Channel from

try: 
    # A successful call to this API will remove the User Attribution Channel for an external account.
    api_response = api_instance.destroy(external_account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalAccountUserAttributionChannelsApi->destroy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_account_id** | **int**| The ID of the external account to remove the User Attribution Channel from | 

### Return type

[**Channel**](Channel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show**
> Channel show(external_account_id)

A successful call to this API will show the User Attribution Channel of an external account.

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.ExternalAccountUserAttributionChannelsApi()
external_account_id = 56 # int | The ID of the external account to show the user attribution channel for

try: 
    # A successful call to this API will show the User Attribution Channel of an external account.
    api_response = api_instance.show(external_account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalAccountUserAttributionChannelsApi->show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_account_id** | **int**| The ID of the external account to show the user attribution channel for | 

### Return type

[**Channel**](Channel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

