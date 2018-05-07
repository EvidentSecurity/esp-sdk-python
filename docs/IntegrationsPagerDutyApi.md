# esp_sdk.IntegrationsPagerDutyApi

All URIs are relative to https://api.evident.io

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](IntegrationsPagerDutyApi.md#create) | **POST** /api/v2/integrations/pager_duty.json_api | Create a Pager Duty Integration
[**show**](IntegrationsPagerDutyApi.md#show) | **GET** /api/v2/integrations/{integration_id}/pager_duty.json_api | Show a single Pager Duty Integration
[**update**](IntegrationsPagerDutyApi.md#update) | **PATCH** /api/v2/integrations/{integration_id}/pager_duty.json_api | Update a Pager Duty Integration


# **create**
> IntegrationPagerDuty create(api_key, external_account_ids, name, include=include, all_high_risk=all_high_risk, all_low_risk=all_low_risk, all_medium_risk=all_medium_risk, custom_signature_ids=custom_signature_ids, send_updates=send_updates, send_when_suppressed=send_when_suppressed, signature_ids=signature_ids, statuses=statuses)

Create a Pager Duty Integration



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.IntegrationsPagerDutyApi()
api_key = 'api_key_example' # str | The API Key for the PagerDuty Integration
external_account_ids = [56] # list[int] | External accounts for integration
name = 'name_example' # str | Name of the integration
include = 'include_example' # str | Related objects that can be included in the response:  integration See Including Objects for more information. (optional)
all_high_risk = true # bool | Send all high risk alerts (optional)
all_low_risk = true # bool | Send all low risk alerts (optional)
all_medium_risk = true # bool | Send all medium risk alerts (optional)
custom_signature_ids = [56] # list[int] | Custom signatures for integration (optional)
send_updates = true # bool | This feature enables the integration to send alerts when they are updated. When disabled, alerts will only be sent when they are initially created. When enabled, alerts will additionally be sent when a change is made such as the alert ending. An alert may end for multiple reasons. (optional)
send_when_suppressed = true # bool | Send notifications for suppressed alerts (optional)
signature_ids = [56] # list[int] | Signatures for integration (optional)
statuses = ['statuses_example'] # list[str] | Only send alerts that have the status in this list. Valid values are fail, warn, error, pass, info (optional)

try: 
    # Create a Pager Duty Integration
    api_response = api_instance.create(api_key, external_account_ids, name, include=include, all_high_risk=all_high_risk, all_low_risk=all_low_risk, all_medium_risk=all_medium_risk, custom_signature_ids=custom_signature_ids, send_updates=send_updates, send_when_suppressed=send_when_suppressed, signature_ids=signature_ids, statuses=statuses)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsPagerDutyApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| The API Key for the PagerDuty Integration | 
 **external_account_ids** | [**list[int]**](int.md)| External accounts for integration | 
 **name** | **str**| Name of the integration | 
 **include** | **str**| Related objects that can be included in the response:  integration See Including Objects for more information. | [optional] 
 **all_high_risk** | **bool**| Send all high risk alerts | [optional] 
 **all_low_risk** | **bool**| Send all low risk alerts | [optional] 
 **all_medium_risk** | **bool**| Send all medium risk alerts | [optional] 
 **custom_signature_ids** | [**list[int]**](int.md)| Custom signatures for integration | [optional] 
 **send_updates** | **bool**| This feature enables the integration to send alerts when they are updated. When disabled, alerts will only be sent when they are initially created. When enabled, alerts will additionally be sent when a change is made such as the alert ending. An alert may end for multiple reasons. | [optional] 
 **send_when_suppressed** | **bool**| Send notifications for suppressed alerts | [optional] 
 **signature_ids** | [**list[int]**](int.md)| Signatures for integration | [optional] 
 **statuses** | [**list[str]**](str.md)| Only send alerts that have the status in this list. Valid values are fail, warn, error, pass, info | [optional] 

### Return type

[**IntegrationPagerDuty**](IntegrationPagerDuty.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show**
> IntegrationPagerDuty show(integration_id, include=include)

Show a single Pager Duty Integration



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.IntegrationsPagerDutyApi()
integration_id = 56 # int | The ID of the integration
include = 'include_example' # str | Related objects that can be included in the response:  integration See Including Objects for more information. (optional)

try: 
    # Show a single Pager Duty Integration
    api_response = api_instance.show(integration_id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsPagerDutyApi->show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_id** | **int**| The ID of the integration | 
 **include** | **str**| Related objects that can be included in the response:  integration See Including Objects for more information. | [optional] 

### Return type

[**IntegrationPagerDuty**](IntegrationPagerDuty.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> IntegrationPagerDuty update(integration_id, include=include, all_high_risk=all_high_risk, all_low_risk=all_low_risk, all_medium_risk=all_medium_risk, api_key=api_key, custom_signature_ids=custom_signature_ids, external_account_ids=external_account_ids, name=name, send_updates=send_updates, send_when_suppressed=send_when_suppressed, signature_ids=signature_ids, statuses=statuses)

Update a Pager Duty Integration



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.IntegrationsPagerDutyApi()
integration_id = 56 # int | The ID of the integration
include = 'include_example' # str | Related objects that can be included in the response:  integration See Including Objects for more information. (optional)
all_high_risk = true # bool | Send all high risk alerts (optional)
all_low_risk = true # bool | Send all low risk alerts (optional)
all_medium_risk = true # bool | Send all medium risk alerts (optional)
api_key = 'api_key_example' # str | The API Key for the PagerDuty Integration (optional)
custom_signature_ids = [56] # list[int] | Custom signatures for integration (optional)
external_account_ids = [56] # list[int] | External accounts for integration (optional)
name = 'name_example' # str | Name of the integration (optional)
send_updates = true # bool | This feature enables the integration to send alerts when they are updated. When disabled, alerts will only be sent when they are initially created. When enabled, alerts will additionally be sent when a change is made such as the alert ending. An alert may end for multiple reasons. (optional)
send_when_suppressed = true # bool | Send notifications for suppressed alerts (optional)
signature_ids = [56] # list[int] | Signatures for integration (optional)
statuses = ['statuses_example'] # list[str] | Only send alerts that have the status in this list. Valid values are fail, warn, error, pass, info (optional)

try: 
    # Update a Pager Duty Integration
    api_response = api_instance.update(integration_id, include=include, all_high_risk=all_high_risk, all_low_risk=all_low_risk, all_medium_risk=all_medium_risk, api_key=api_key, custom_signature_ids=custom_signature_ids, external_account_ids=external_account_ids, name=name, send_updates=send_updates, send_when_suppressed=send_when_suppressed, signature_ids=signature_ids, statuses=statuses)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsPagerDutyApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_id** | **int**| The ID of the integration | 
 **include** | **str**| Related objects that can be included in the response:  integration See Including Objects for more information. | [optional] 
 **all_high_risk** | **bool**| Send all high risk alerts | [optional] 
 **all_low_risk** | **bool**| Send all low risk alerts | [optional] 
 **all_medium_risk** | **bool**| Send all medium risk alerts | [optional] 
 **api_key** | **str**| The API Key for the PagerDuty Integration | [optional] 
 **custom_signature_ids** | [**list[int]**](int.md)| Custom signatures for integration | [optional] 
 **external_account_ids** | [**list[int]**](int.md)| External accounts for integration | [optional] 
 **name** | **str**| Name of the integration | [optional] 
 **send_updates** | **bool**| This feature enables the integration to send alerts when they are updated. When disabled, alerts will only be sent when they are initially created. When enabled, alerts will additionally be sent when a change is made such as the alert ending. An alert may end for multiple reasons. | [optional] 
 **send_when_suppressed** | **bool**| Send notifications for suppressed alerts | [optional] 
 **signature_ids** | [**list[int]**](int.md)| Signatures for integration | [optional] 
 **statuses** | [**list[str]**](str.md)| Only send alerts that have the status in this list. Valid values are fail, warn, error, pass, info | [optional] 

### Return type

[**IntegrationPagerDuty**](IntegrationPagerDuty.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

