# esp_sdk.ExternalAccountsAmazonApi

All URIs are relative to https://api.evident.io

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](ExternalAccountsAmazonApi.md#create) | **POST** /api/v2/external_accounts/amazon.json_api | Create an Amazon External Account
[**show**](ExternalAccountsAmazonApi.md#show) | **GET** /api/v2/external_accounts/{external_account_id}/amazon.json_api | Show an Amazon External Account
[**update**](ExternalAccountsAmazonApi.md#update) | **PATCH** /api/v2/external_accounts/{external_account_id}/amazon.json_api | Update an Amazon External Account


# **create**
> ExternalAccountAmazonIAM create(arn, external_id, name, team_id)

Create an Amazon External Account

 The related external_account object will be returned with the response.

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.ExternalAccountsAmazonApi()
arn = 'arn_example' # str | Amazon Resource Name for the IAM role
external_id = 'external_id_example' # str | External Identifier set on the role
name = 'name_example' # str | Name
team_id = 56 # int | The ID of the team the external account belongs to

try: 
    # Create an Amazon External Account
    api_response = api_instance.create(arn, external_id, name, team_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalAccountsAmazonApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arn** | **str**| Amazon Resource Name for the IAM role | 
 **external_id** | **str**| External Identifier set on the role | 
 **name** | **str**| Name | 
 **team_id** | **int**| The ID of the team the external account belongs to | 

### Return type

[**ExternalAccountAmazonIAM**](ExternalAccountAmazonIAM.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show**
> ExternalAccountAmazonIAM show(external_account_id, include=include)

Show an Amazon External Account



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.ExternalAccountsAmazonApi()
external_account_id = 56 # int | The ID of the external account to show an Amazon IAM credential for
include = 'include_example' # str | Related objects that can be included in the response:  external_account See Including Objects for more information. (optional)

try: 
    # Show an Amazon External Account
    api_response = api_instance.show(external_account_id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalAccountsAmazonApi->show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_account_id** | **int**| The ID of the external account to show an Amazon IAM credential for | 
 **include** | **str**| Related objects that can be included in the response:  external_account See Including Objects for more information. | [optional] 

### Return type

[**ExternalAccountAmazonIAM**](ExternalAccountAmazonIAM.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> ExternalAccountAmazonIAM update(external_account_id, arn=arn, external_id=external_id, name=name, team_id=team_id)

Update an Amazon External Account

 The related external_account object will be returned with the response.

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.ExternalAccountsAmazonApi()
external_account_id = 56 # int | The ID of the external account to update an Amazon IAM credential of
arn = 'arn_example' # str | Amazon Resource Name for the IAM role (optional)
external_id = 'external_id_example' # str | External Identifier set on the role (optional)
name = 'name_example' # str | Name (optional)
team_id = 56 # int | The ID of the team the external account belongs to (optional)

try: 
    # Update an Amazon External Account
    api_response = api_instance.update(external_account_id, arn=arn, external_id=external_id, name=name, team_id=team_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalAccountsAmazonApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_account_id** | **int**| The ID of the external account to update an Amazon IAM credential of | 
 **arn** | **str**| Amazon Resource Name for the IAM role | [optional] 
 **external_id** | **str**| External Identifier set on the role | [optional] 
 **name** | **str**| Name | [optional] 
 **team_id** | **int**| The ID of the team the external account belongs to | [optional] 

### Return type

[**ExternalAccountAmazonIAM**](ExternalAccountAmazonIAM.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

