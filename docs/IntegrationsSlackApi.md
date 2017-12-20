# esp_sdk.IntegrationsSlackApi

All URIs are relative to https://api.evident.io

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](IntegrationsSlackApi.md#create) | **POST** /api/v2/integrations/slack.json_api | Create a Slack Integration
[**show**](IntegrationsSlackApi.md#show) | **GET** /api/v2/integrations/{integration_id}/slack.json_api | Show a single Slack Integration
[**update**](IntegrationsSlackApi.md#update) | **PATCH** /api/v2/integrations/{integration_id}/slack.json_api | Update a Slack Integration


# **create**
> IntegrationSlack create(url, name, external_account_ids, all_high_risk=all_high_risk, all_medium_risk=all_medium_risk, all_low_risk=all_low_risk, send_updates=send_updates, send_when_suppressed=send_when_suppressed, signature_ids=signature_ids, statuses=statuses, custom_signature_ids=custom_signature_ids, include=include)

Create a Slack Integration



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.IntegrationsSlackApi()
url = 'url_example' # str | The URL for the Slack integration
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
    # Create a Slack Integration
    api_response = api_instance.create(url, name, external_account_ids, all_high_risk=all_high_risk, all_medium_risk=all_medium_risk, all_low_risk=all_low_risk, send_updates=send_updates, send_when_suppressed=send_when_suppressed, signature_ids=signature_ids, statuses=statuses, custom_signature_ids=custom_signature_ids, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsSlackApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | **str**| The URL for the Slack integration | 
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

[**IntegrationSlack**](IntegrationSlack.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show**
> IntegrationSlack show(integration_id, include=include)

Show a single Slack Integration



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.IntegrationsSlackApi()
integration_id = 56 # int | The ID of the integration
include = 'include_example' # str | Related objects that can be included in the response:  integration See Including Objects for more information. (optional)

try: 
    # Show a single Slack Integration
    api_response = api_instance.show(integration_id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsSlackApi->show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_id** | **int**| The ID of the integration | 
 **include** | **str**| Related objects that can be included in the response:  integration See Including Objects for more information. | [optional] 

### Return type

[**IntegrationSlack**](IntegrationSlack.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> IntegrationSlack update(integration_id, url=url, name=name, all_high_risk=all_high_risk, all_medium_risk=all_medium_risk, all_low_risk=all_low_risk, send_updates=send_updates, send_when_suppressed=send_when_suppressed, signature_ids=signature_ids, statuses=statuses, external_account_ids=external_account_ids, custom_signature_ids=custom_signature_ids, include=include)

Update a Slack Integration



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.IntegrationsSlackApi()
integration_id = 56 # int | The ID of the integration
url = 'url_example' # str | The URL for the Slack integration (optional)
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
    # Update a Slack Integration
    api_response = api_instance.update(integration_id, url=url, name=name, all_high_risk=all_high_risk, all_medium_risk=all_medium_risk, all_low_risk=all_low_risk, send_updates=send_updates, send_when_suppressed=send_when_suppressed, signature_ids=signature_ids, statuses=statuses, external_account_ids=external_account_ids, custom_signature_ids=custom_signature_ids, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsSlackApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_id** | **int**| The ID of the integration | 
 **url** | **str**| The URL for the Slack integration | [optional] 
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

[**IntegrationSlack**](IntegrationSlack.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

