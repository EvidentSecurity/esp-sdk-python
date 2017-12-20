# esp_sdk.IntegrationsAmazonSNSApi

All URIs are relative to https://api.evident.io

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](IntegrationsAmazonSNSApi.md#create) | **POST** /api/v2/integrations/amazon_sns.json_api | Create an Amazon SNS Integration
[**show**](IntegrationsAmazonSNSApi.md#show) | **GET** /api/v2/integrations/{integration_id}/amazon_sns.json_api | Show a single Amazon SNS Integration
[**update**](IntegrationsAmazonSNSApi.md#update) | **PATCH** /api/v2/integrations/{integration_id}/amazon_sns.json_api | Update an Amazon SNS Integration


# **create**
> IntegrationAmazonSns create(arn, external_id, topic, name, external_account_ids, all_high_risk=all_high_risk, all_medium_risk=all_medium_risk, all_low_risk=all_low_risk, send_updates=send_updates, send_when_suppressed=send_when_suppressed, signature_ids=signature_ids, statuses=statuses, custom_signature_ids=custom_signature_ids, include=include)

Create an Amazon SNS Integration



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.IntegrationsAmazonSNSApi()
arn = 'arn_example' # str | The role arn for accessing the SNS topic
external_id = 'external_id_example' # str | The external ID for the IAM role
topic = 'topic_example' # str | The SNS topic arn
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
include = 'include_example' # str | Related objects that can be included in the response:  region, integration See Including Objects for more information. (optional)

try: 
    # Create an Amazon SNS Integration
    api_response = api_instance.create(arn, external_id, topic, name, external_account_ids, all_high_risk=all_high_risk, all_medium_risk=all_medium_risk, all_low_risk=all_low_risk, send_updates=send_updates, send_when_suppressed=send_when_suppressed, signature_ids=signature_ids, statuses=statuses, custom_signature_ids=custom_signature_ids, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsAmazonSNSApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arn** | **str**| The role arn for accessing the SNS topic | 
 **external_id** | **str**| The external ID for the IAM role | 
 **topic** | **str**| The SNS topic arn | 
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
 **include** | **str**| Related objects that can be included in the response:  region, integration See Including Objects for more information. | [optional] 

### Return type

[**IntegrationAmazonSns**](IntegrationAmazonSns.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show**
> IntegrationAmazonSns show(integration_id, include=include)

Show a single Amazon SNS Integration



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.IntegrationsAmazonSNSApi()
integration_id = 56 # int | The ID of the integration
include = 'include_example' # str | Related objects that can be included in the response:  region, integration See Including Objects for more information. (optional)

try: 
    # Show a single Amazon SNS Integration
    api_response = api_instance.show(integration_id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsAmazonSNSApi->show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_id** | **int**| The ID of the integration | 
 **include** | **str**| Related objects that can be included in the response:  region, integration See Including Objects for more information. | [optional] 

### Return type

[**IntegrationAmazonSns**](IntegrationAmazonSns.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> IntegrationAmazonSns update(integration_id, arn=arn, external_id=external_id, topic=topic, name=name, all_high_risk=all_high_risk, all_medium_risk=all_medium_risk, all_low_risk=all_low_risk, send_updates=send_updates, send_when_suppressed=send_when_suppressed, signature_ids=signature_ids, statuses=statuses, external_account_ids=external_account_ids, custom_signature_ids=custom_signature_ids, include=include)

Update an Amazon SNS Integration



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.IntegrationsAmazonSNSApi()
integration_id = 56 # int | The ID of the integration
arn = 'arn_example' # str | The role arn for accessing the SNS topic (optional)
external_id = 'external_id_example' # str | The external ID for the IAM role (optional)
topic = 'topic_example' # str | The SNS topic arn (optional)
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
include = 'include_example' # str | Related objects that can be included in the response:  region, integration See Including Objects for more information. (optional)

try: 
    # Update an Amazon SNS Integration
    api_response = api_instance.update(integration_id, arn=arn, external_id=external_id, topic=topic, name=name, all_high_risk=all_high_risk, all_medium_risk=all_medium_risk, all_low_risk=all_low_risk, send_updates=send_updates, send_when_suppressed=send_when_suppressed, signature_ids=signature_ids, statuses=statuses, external_account_ids=external_account_ids, custom_signature_ids=custom_signature_ids, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsAmazonSNSApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_id** | **int**| The ID of the integration | 
 **arn** | **str**| The role arn for accessing the SNS topic | [optional] 
 **external_id** | **str**| The external ID for the IAM role | [optional] 
 **topic** | **str**| The SNS topic arn | [optional] 
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
 **include** | **str**| Related objects that can be included in the response:  region, integration See Including Objects for more information. | [optional] 

### Return type

[**IntegrationAmazonSns**](IntegrationAmazonSns.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

