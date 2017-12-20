# esp_sdk.UserAttributionsApi

All URIs are relative to https://api.evident.io

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_channel**](UserAttributionsApi.md#add_channel) | **POST** /api/v2/external_accounts/{external_account_id}/user_attribution/channel.json_api | Create a User Attribution Channel for an external account
[**remove_channel**](UserAttributionsApi.md#remove_channel) | **DELETE** /api/v2/external_accounts/{external_account_id}/user_attribution/channel.json_api | Remove the User Attribution Channel for an external account
[**show_channel**](UserAttributionsApi.md#show_channel) | **GET** /api/v2/external_accounts/{external_account_id}/user_attribution/channel.json_api | Show the User Attribution Channel of an external account
[**update**](UserAttributionsApi.md#update) | **PATCH** /api/v2/external_accounts/{external_account_id}/user_attribution.json_api | Update the user attributions on an external account


# **add_channel**
> ExternalAccountUserAttributionChannel add_channel(external_account_id, include=include)

Create a User Attribution Channel for an external account

URL will only be returned in this response and will not be accessible again.

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.UserAttributionsApi()
external_account_id = 56 # int | The ID of the external account to create a User Attribution Channel for
include = 'include_example' # str | Related objects that can be included in the response:   See Including Objects for more information. (optional)

try: 
    # Create a User Attribution Channel for an external account
    api_response = api_instance.add_channel(external_account_id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserAttributionsApi->add_channel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_account_id** | **int**| The ID of the external account to create a User Attribution Channel for | 
 **include** | **str**| Related objects that can be included in the response:   See Including Objects for more information. | [optional] 

### Return type

[**ExternalAccountUserAttributionChannel**](ExternalAccountUserAttributionChannel.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_channel**
> Meta remove_channel(external_account_id)

Remove the User Attribution Channel for an external account



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.UserAttributionsApi()
external_account_id = 56 # int | The ID of the external account to remove the User Attribution Channel from

try: 
    # Remove the User Attribution Channel for an external account
    api_response = api_instance.remove_channel(external_account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserAttributionsApi->remove_channel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_account_id** | **int**| The ID of the external account to remove the User Attribution Channel from | 

### Return type

[**Meta**](Meta.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_channel**
> ExternalAccountUserAttributionChannel show_channel(external_account_id, include=include)

Show the User Attribution Channel of an external account

The channel url will not be returned.

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.UserAttributionsApi()
external_account_id = 56 # int | The ID of the external account to show the user attribution channel for
include = 'include_example' # str | Related objects that can be included in the response:   See Including Objects for more information. (optional)

try: 
    # Show the User Attribution Channel of an external account
    api_response = api_instance.show_channel(external_account_id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserAttributionsApi->show_channel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_account_id** | **int**| The ID of the external account to show the user attribution channel for | 
 **include** | **str**| Related objects that can be included in the response:   See Including Objects for more information. | [optional] 

### Return type

[**ExternalAccountUserAttributionChannel**](ExternalAccountUserAttributionChannel.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> ExternalAccount update(external_account_id, cloudtrail_name=cloudtrail_name, include=include)

Update the user attributions on an external account



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.UserAttributionsApi()
external_account_id = 56 # int | The ID of the external account to update the user attributions of
cloudtrail_name = 'cloudtrail_name_example' # str | The name of the cloudetrail associated with the user attribution. (optional)
include = 'include_example' # str | Related objects that can be included in the response:  organization, sub_organization, team, scan_intervals, disabled_signatures, azure_group, credentials See Including Objects for more information. (optional)

try: 
    # Update the user attributions on an external account
    api_response = api_instance.update(external_account_id, cloudtrail_name=cloudtrail_name, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserAttributionsApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_account_id** | **int**| The ID of the external account to update the user attributions of | 
 **cloudtrail_name** | **str**| The name of the cloudetrail associated with the user attribution. | [optional] 
 **include** | **str**| Related objects that can be included in the response:  organization, sub_organization, team, scan_intervals, disabled_signatures, azure_group, credentials See Including Objects for more information. | [optional] 

### Return type

[**ExternalAccount**](ExternalAccount.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

