# esp_sdk.ScanIntervalsApi

All URIs are relative to https://api.evident.io

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](ScanIntervalsApi.md#create) | **POST** /api/v2/scan_intervals.json_api | Create a(n) ScanInterval
[**destroy**](ScanIntervalsApi.md#destroy) | **DELETE** /api/v2/scan_intervals/{id}.json_api | Remove a(n) ScanInterval
[**list**](ScanIntervalsApi.md#list) | **GET** /api/v2/external_accounts/{external_account_id}/scan_intervals.json_api | Get a list of ScanIntervals
[**show**](ScanIntervalsApi.md#show) | **GET** /api/v2/scan_intervals/{id}.json_api | Show a single ScanInterval
[**update**](ScanIntervalsApi.md#update) | **PATCH** /api/v2/scan_intervals/{id}.json_api | Update a(n) ScanInterval


# **create**
> ScanInterval create(external_account_id, interval, service_id)

Create a(n) ScanInterval

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.ScanIntervalsApi()
external_account_id = 56 # int | The ID of the external account this scan interval is for
interval = 56 # int | The interval, in minutes, this service will be scanned
service_id = 56 # int | The service ID for the scan interval

try: 
    # Create a(n) ScanInterval
    api_response = api_instance.create(external_account_id, interval, service_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScanIntervalsApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_account_id** | **int**| The ID of the external account this scan interval is for | 
 **interval** | **int**| The interval, in minutes, this service will be scanned | 
 **service_id** | **int**| The service ID for the scan interval | 

### Return type

[**ScanInterval**](ScanInterval.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy**
> Meta destroy(id)

Remove a(n) ScanInterval

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.ScanIntervalsApi()
id = 56 # int | ScanInterval ID

try: 
    # Remove a(n) ScanInterval
    api_response = api_instance.destroy(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScanIntervalsApi->destroy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ScanInterval ID | 

### Return type

[**Meta**](Meta.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> PaginatedCollection list(external_account_id, include=include, page=page)

Get a list of ScanIntervals

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.ScanIntervalsApi()
external_account_id = 56 # int | The ID of the external account to retrieve
include = 'include_example' # str | Related objects that can be included in the response.  See Including Objects for more information. (optional)
page = '{:number=>1,+:size=>20}' # str | Page Number and Page Size.  number is the page number of the collection to return, size is the number of items to return per page (optional) (default to {:number=>1,+:size=>20})

try: 
    # Get a list of ScanIntervals
    api_response = api_instance.list(external_account_id, include=include, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScanIntervalsApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_account_id** | **int**| The ID of the external account to retrieve | 
 **include** | **str**| Related objects that can be included in the response.  See Including Objects for more information. | [optional] 
 **page** | **str**| Page Number and Page Size.  number is the page number of the collection to return, size is the number of items to return per page | [optional] [default to {:number&#x3D;&gt;1,+:size&#x3D;&gt;20}]

### Return type

[**PaginatedCollection**](PaginatedCollection.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show**
> ScanInterval show(id, include=include)

Show a single ScanInterval

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.ScanIntervalsApi()
id = 56 # int | ScanInterval ID
include = 'include_example' # str | Related objects that can be included in the response.  See Including Objects for more information. (optional)

try: 
    # Show a single ScanInterval
    api_response = api_instance.show(id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScanIntervalsApi->show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ScanInterval ID | 
 **include** | **str**| Related objects that can be included in the response.  See Including Objects for more information. | [optional] 

### Return type

[**ScanInterval**](ScanInterval.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> ScanInterval update(id, external_account_id, interval, service_id)

Update a(n) ScanInterval

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.ScanIntervalsApi()
id = 56 # int | ScanInterval ID
external_account_id = 56 # int | The ID of the external account this scan interval is for
interval = 56 # int | The interval, in minutes, this service will be scanned
service_id = 56 # int | The service ID for the scan interval

try: 
    # Update a(n) ScanInterval
    api_response = api_instance.update(id, external_account_id, interval, service_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScanIntervalsApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ScanInterval ID | 
 **external_account_id** | **int**| The ID of the external account this scan interval is for | 
 **interval** | **int**| The interval, in minutes, this service will be scanned | 
 **service_id** | **int**| The service ID for the scan interval | 

### Return type

[**ScanInterval**](ScanInterval.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

