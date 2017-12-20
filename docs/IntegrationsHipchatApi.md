# esp_sdk.IntegrationsHipchatApi

All URIs are relative to https://api.evident.io

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](IntegrationsHipchatApi.md#create) | **POST** /api/v2/integrations/hipchat.json_api | Create a Hipchat Integration
[**show**](IntegrationsHipchatApi.md#show) | **GET** /api/v2/integrations/{integration_id}/hipchat.json_api | Show a single Hipchat Integration
[**update**](IntegrationsHipchatApi.md#update) | **PATCH** /api/v2/integrations/{integration_id}/hipchat.json_api | Update a Hipchat Integration


# **create**
> IntegrationHipchat create(token, room, name, external_account_ids, all_high_risk=all_high_risk, all_medium_risk=all_medium_risk, all_low_risk=all_low_risk, send_updates=send_updates, send_when_suppressed=send_when_suppressed, signature_ids=signature_ids, statuses=statuses, custom_signature_ids=custom_signature_ids, include=include)

Create a Hipchat Integration



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.IntegrationsHipchatApi()
token = 'token_example' # str | The Hipchat token
room = 'room_example' # str | The Hipchat room
name = 'name_example' # str | Name of the integration
external_account_ids = [56] # list[int] | External accounts for integration
all_high_risk = true # bool | Send all high risk alerts (optional)
all_medium_risk = true # bool | Send all medium risk alerts (optional)
all_low_risk = true # bool | Send all low risk alerts (optional)
send_updates = true # bool | This feature enables the integration to send alerts when they are updated. When disabled, alerts will only be sent when they are initially created. When enabled, alerts will additionally be sent when a change is made such as the alert ending. An alert may end for multiple reasons. (optional)
send_when_suppressed = true # bool | Send notifications for suppressed alerts (optional)
signature_ids = [56] # list[int] | Signatures for integration (optional)
statuses = ['statuses_example'] # list[str] | Only send alerts that have the status in this list. Valid values are fail, warn, error, pass, info (optional)
custom_signature_ids = [56] # list[int] | Custom signatures for integration (optional)
include = 'include_example' # str | Related objects that can be included in the response:  integration See Including Objects for more information. (optional)

try: 
    # Create a Hipchat Integration
    api_response = api_instance.create(token, room, name, external_account_ids, all_high_risk=all_high_risk, all_medium_risk=all_medium_risk, all_low_risk=all_low_risk, send_updates=send_updates, send_when_suppressed=send_when_suppressed, signature_ids=signature_ids, statuses=statuses, custom_signature_ids=custom_signature_ids, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsHipchatApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| The Hipchat token | 
 **room** | **str**| The Hipchat room | 
 **name** | **str**| Name of the integration | 
 **external_account_ids** | [**list[int]**](int.md)| External accounts for integration | 
 **all_high_risk** | **bool**| Send all high risk alerts | [optional] 
 **all_medium_risk** | **bool**| Send all medium risk alerts | [optional] 
 **all_low_risk** | **bool**| Send all low risk alerts | [optional] 
 **send_updates** | **bool**| This feature enables the integration to send alerts when they are updated. When disabled, alerts will only be sent when they are initially created. When enabled, alerts will additionally be sent when a change is made such as the alert ending. An alert may end for multiple reasons. | [optional] 
 **send_when_suppressed** | **bool**| Send notifications for suppressed alerts | [optional] 
 **signature_ids** | [**list[int]**](int.md)| Signatures for integration | [optional] 
 **statuses** | [**list[str]**](str.md)| Only send alerts that have the status in this list. Valid values are fail, warn, error, pass, info | [optional] 
 **custom_signature_ids** | [**list[int]**](int.md)| Custom signatures for integration | [optional] 
 **include** | **str**| Related objects that can be included in the response:  integration See Including Objects for more information. | [optional] 

### Return type

[**IntegrationHipchat**](IntegrationHipchat.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show**
> IntegrationHipchat show(integration_id, include=include)

Show a single Hipchat Integration



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.IntegrationsHipchatApi()
integration_id = 56 # int | The ID of the integration
include = 'include_example' # str | Related objects that can be included in the response:  integration See Including Objects for more information. (optional)

try: 
    # Show a single Hipchat Integration
    api_response = api_instance.show(integration_id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsHipchatApi->show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_id** | **int**| The ID of the integration | 
 **include** | **str**| Related objects that can be included in the response:  integration See Including Objects for more information. | [optional] 

### Return type

[**IntegrationHipchat**](IntegrationHipchat.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> IntegrationHipchat update(integration_id, token=token, room=room, name=name, all_high_risk=all_high_risk, all_medium_risk=all_medium_risk, all_low_risk=all_low_risk, send_updates=send_updates, send_when_suppressed=send_when_suppressed, signature_ids=signature_ids, statuses=statuses, external_account_ids=external_account_ids, custom_signature_ids=custom_signature_ids, include=include)

Update a Hipchat Integration



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.IntegrationsHipchatApi()
integration_id = 56 # int | The ID of the integration
token = 'token_example' # str | The Hipchat token (optional)
room = 'room_example' # str | The Hipchat room (optional)
name = 'name_example' # str | Name of the integration (optional)
all_high_risk = true # bool | Send all high risk alerts (optional)
all_medium_risk = true # bool | Send all medium risk alerts (optional)
all_low_risk = true # bool | Send all low risk alerts (optional)
send_updates = true # bool | This feature enables the integration to send alerts when they are updated. When disabled, alerts will only be sent when they are initially created. When enabled, alerts will additionally be sent when a change is made such as the alert ending. An alert may end for multiple reasons. (optional)
send_when_suppressed = true # bool | Send notifications for suppressed alerts (optional)
signature_ids = [56] # list[int] | Signatures for integration (optional)
statuses = ['statuses_example'] # list[str] | Only send alerts that have the status in this list. Valid values are fail, warn, error, pass, info (optional)
external_account_ids = [56] # list[int] | External accounts for integration (optional)
custom_signature_ids = [56] # list[int] | Custom signatures for integration (optional)
include = 'include_example' # str | Related objects that can be included in the response:  integration See Including Objects for more information. (optional)

try: 
    # Update a Hipchat Integration
    api_response = api_instance.update(integration_id, token=token, room=room, name=name, all_high_risk=all_high_risk, all_medium_risk=all_medium_risk, all_low_risk=all_low_risk, send_updates=send_updates, send_when_suppressed=send_when_suppressed, signature_ids=signature_ids, statuses=statuses, external_account_ids=external_account_ids, custom_signature_ids=custom_signature_ids, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsHipchatApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_id** | **int**| The ID of the integration | 
 **token** | **str**| The Hipchat token | [optional] 
 **room** | **str**| The Hipchat room | [optional] 
 **name** | **str**| Name of the integration | [optional] 
 **all_high_risk** | **bool**| Send all high risk alerts | [optional] 
 **all_medium_risk** | **bool**| Send all medium risk alerts | [optional] 
 **all_low_risk** | **bool**| Send all low risk alerts | [optional] 
 **send_updates** | **bool**| This feature enables the integration to send alerts when they are updated. When disabled, alerts will only be sent when they are initially created. When enabled, alerts will additionally be sent when a change is made such as the alert ending. An alert may end for multiple reasons. | [optional] 
 **send_when_suppressed** | **bool**| Send notifications for suppressed alerts | [optional] 
 **signature_ids** | [**list[int]**](int.md)| Signatures for integration | [optional] 
 **statuses** | [**list[str]**](str.md)| Only send alerts that have the status in this list. Valid values are fail, warn, error, pass, info | [optional] 
 **external_account_ids** | [**list[int]**](int.md)| External accounts for integration | [optional] 
 **custom_signature_ids** | [**list[int]**](int.md)| Custom signatures for integration | [optional] 
 **include** | **str**| Related objects that can be included in the response:  integration See Including Objects for more information. | [optional] 

### Return type

[**IntegrationHipchat**](IntegrationHipchat.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

