# esp_sdk.ScanIntervalsApi

All URIs are relative to https://api.evident.io

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](ScanIntervalsApi.md#create) | **POST** /api/v2/scan_intervals.json_api | Create a(n) Scan Interval
[**delete**](ScanIntervalsApi.md#delete) | **DELETE** /api/v2/scan_intervals/{id}.json_api | Delete a(n) Scan Interval
[**list_for_external_account**](ScanIntervalsApi.md#list_for_external_account) | **GET** /api/v2/external_accounts/{external_account_id}/scan_intervals.json_api | Get a list of Scan Intervals
[**show**](ScanIntervalsApi.md#show) | **GET** /api/v2/scan_intervals/{id}.json_api | Show a single Scan Interval
[**update**](ScanIntervalsApi.md#update) | **PATCH** /api/v2/scan_intervals/{id}.json_api | Update a(n) Scan Interval


# **create**
> ScanInterval create(external_account_id, interval, service_id, include=include)

Create a(n) Scan Interval



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
include = 'include_example' # str | Related objects that can be included in the response:  external_account, service See Including Objects for more information. (optional)

try: 
    # Create a(n) Scan Interval
    api_response = api_instance.create(external_account_id, interval, service_id, include=include)
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
 **include** | **str**| Related objects that can be included in the response:  external_account, service See Including Objects for more information. | [optional] 

### Return type

[**ScanInterval**](ScanInterval.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> Meta delete(id)

Delete a(n) Scan Interval



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.ScanIntervalsApi()
id = 56 # int |  ID

try: 
    # Delete a(n) Scan Interval
    api_response = api_instance.delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScanIntervalsApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  ID | 

### Return type

[**Meta**](Meta.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_for_external_account**
> PaginatedCollection list_for_external_account(external_account_id, page=page, include=include)

Get a list of Scan Intervals



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
page = '{:number=>1,+:size=>20}' # str | Page Number and Page Size.  number is the page number of the collection to return, size is the number of items to return per page (optional) (default to {:number=>1,+:size=>20})
include = 'include_example' # str | Related objects that can be included in the response:  external_account, service See Including Objects for more information. (optional)

try: 
    # Get a list of Scan Intervals
    api_response = api_instance.list_for_external_account(external_account_id, page=page, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScanIntervalsApi->list_for_external_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_account_id** | **int**| The ID of the external account to retrieve | 
 **page** | **str**| Page Number and Page Size.  number is the page number of the collection to return, size is the number of items to return per page | [optional] [default to {:number&#x3D;&gt;1,+:size&#x3D;&gt;20}]
 **include** | **str**| Related objects that can be included in the response:  external_account, service See Including Objects for more information. | [optional] 

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

Show a single Scan Interval



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.ScanIntervalsApi()
id = 56 # int | Scan Interval ID
include = 'include_example' # str | Related objects that can be included in the response:  external_account, service See Including Objects for more information. (optional)

try: 
    # Show a single Scan Interval
    api_response = api_instance.show(id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScanIntervalsApi->show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Scan Interval ID | 
 **include** | **str**| Related objects that can be included in the response:  external_account, service See Including Objects for more information. | [optional] 

### Return type

[**ScanInterval**](ScanInterval.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> ScanInterval update(id, external_account_id=external_account_id, interval=interval, service_id=service_id, include=include)

Update a(n) Scan Interval



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.ScanIntervalsApi()
id = 56 # int | Scan Interval ID
external_account_id = 56 # int | The ID of the external account this scan interval is for (optional)
interval = 56 # int | The interval, in minutes, this service will be scanned (optional)
service_id = 56 # int | The service ID for the scan interval (optional)
include = 'include_example' # str | Related objects that can be included in the response:  external_account, service See Including Objects for more information. (optional)

try: 
    # Update a(n) Scan Interval
    api_response = api_instance.update(id, external_account_id=external_account_id, interval=interval, service_id=service_id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScanIntervalsApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Scan Interval ID | 
 **external_account_id** | **int**| The ID of the external account this scan interval is for | [optional] 
 **interval** | **int**| The interval, in minutes, this service will be scanned | [optional] 
 **service_id** | **int**| The service ID for the scan interval | [optional] 
 **include** | **str**| Related objects that can be included in the response:  external_account, service See Including Objects for more information. | [optional] 

### Return type

[**ScanInterval**](ScanInterval.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

