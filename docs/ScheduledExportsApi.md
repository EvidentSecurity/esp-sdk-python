# esp_sdk.ScheduledExportsApi

All URIs are relative to https://api.evident.io

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_export**](ScheduledExportsApi.md#activate_export) | **PATCH** /api/v2/scheduled_exports/{scheduled_export_id}/activate.json_api | Update a(n) Scheduled Export
[**create**](ScheduledExportsApi.md#create) | **POST** /api/v2/scheduled_exports.json_api | Create a(n) Scheduled Export
[**delete**](ScheduledExportsApi.md#delete) | **DELETE** /api/v2/scheduled_exports/{id}.json_api | Delete a(n) Scheduled Export
[**disable_export**](ScheduledExportsApi.md#disable_export) | **PATCH** /api/v2/scheduled_exports/{scheduled_export_id}/disable.json_api | Update a(n) Scheduled Export
[**list**](ScheduledExportsApi.md#list) | **PUT** /api/v2/scheduled_exports.json_api | Get a list of Scheduled Exports
[**show**](ScheduledExportsApi.md#show) | **GET** /api/v2/scheduled_exports/{id}.json_api | Show a single Scheduled Export
[**show_file_details**](ScheduledExportsApi.md#show_file_details) | **GET** /api/v2/reports/scheduled_export/files/{uuid}.json_api | Show a single Scheduled Export Result
[**unsubscribe_export**](ScheduledExportsApi.md#unsubscribe_export) | **PATCH** /api/v2/scheduled_exports/{uuid}/unsubscribe.json_api | Update a(n) Scheduled Export
[**update**](ScheduledExportsApi.md#update) | **PATCH** /api/v2/scheduled_exports/{id}.json_api | Update a(n) Scheduled Export


# **activate_export**
> ScheduledExport activate_export(scheduled_export_id, include=include)

Update a(n) Scheduled Export



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.ScheduledExportsApi()
scheduled_export_id = 56 # int | The id of the scheduled export to be activated
include = 'include_example' # str | Related objects that can be included in the response:  external_accounts, creator See Including Objects for more information. (optional)

try: 
    # Update a(n) Scheduled Export
    api_response = api_instance.activate_export(scheduled_export_id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduledExportsApi->activate_export: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scheduled_export_id** | **int**| The id of the scheduled export to be activated | 
 **include** | **str**| Related objects that can be included in the response:  external_accounts, creator See Including Objects for more information. | [optional] 

### Return type

[**ScheduledExport**](ScheduledExport.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create**
> ScheduledExport create(external_account_ids, frequency, hour, time_zone, include=include, day=day, filter=filter, name=name, recipients=recipients)

Create a(n) Scheduled Export



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.ScheduledExportsApi()
external_account_ids = [56] # list[int] | The ids of the external accounts the report will be exported for
frequency = 'frequency_example' # str | Frequency of the export. Valid values are weekly, daily, monthly
hour = 56 # int | Hour of the day to perform the export. Valid values are 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23
time_zone = 'time_zone_example' # str | Time zone to use when calculating hour and day
include = 'include_example' # str | Related objects that can be included in the response:  external_accounts, creator See Including Objects for more information. (optional)
day = 'day_example' # str | Day of the week or day of the month to perform the export.  Allowed Values: Daily: nil - Weekly: sunday, monday, tuesday, wednesday, thursday, friday, or saturday - Monthly: 1 to 31. Valid values are sunday, monday, tuesday, wednesday, thursday, friday, saturday, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31 (optional)
filter = {'key': 'filter_example'} # dict(str, str) | Params used to filter the alerts that will be exported (optional)
name = 'name_example' # str | A name that describes the export (optional)
recipients = ['recipients_example'] # list[str] | Email addresses the export will be sent to (optional)

try: 
    # Create a(n) Scheduled Export
    api_response = api_instance.create(external_account_ids, frequency, hour, time_zone, include=include, day=day, filter=filter, name=name, recipients=recipients)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduledExportsApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_account_ids** | [**list[int]**](int.md)| The ids of the external accounts the report will be exported for | 
 **frequency** | **str**| Frequency of the export. Valid values are weekly, daily, monthly | 
 **hour** | **int**| Hour of the day to perform the export. Valid values are 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23 | 
 **time_zone** | **str**| Time zone to use when calculating hour and day | 
 **include** | **str**| Related objects that can be included in the response:  external_accounts, creator See Including Objects for more information. | [optional] 
 **day** | **str**| Day of the week or day of the month to perform the export.  Allowed Values: Daily: nil - Weekly: sunday, monday, tuesday, wednesday, thursday, friday, or saturday - Monthly: 1 to 31. Valid values are sunday, monday, tuesday, wednesday, thursday, friday, saturday, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31 | [optional] 
 **filter** | [**dict(str, str)**](str.md)| Params used to filter the alerts that will be exported | [optional] 
 **name** | **str**| A name that describes the export | [optional] 
 **recipients** | [**list[str]**](str.md)| Email addresses the export will be sent to | [optional] 

### Return type

[**ScheduledExport**](ScheduledExport.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> Meta delete(id)

Delete a(n) Scheduled Export



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.ScheduledExportsApi()
id = 56 # int | Scheduled Export ID

try: 
    # Delete a(n) Scheduled Export
    api_response = api_instance.delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduledExportsApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Scheduled Export ID | 

### Return type

[**Meta**](Meta.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_export**
> ScheduledExport disable_export(scheduled_export_id, include=include)

Update a(n) Scheduled Export



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.ScheduledExportsApi()
scheduled_export_id = 56 # int | The id of the scheduled export to be disabled
include = 'include_example' # str | Related objects that can be included in the response:  external_accounts, creator See Including Objects for more information. (optional)

try: 
    # Update a(n) Scheduled Export
    api_response = api_instance.disable_export(scheduled_export_id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduledExportsApi->disable_export: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scheduled_export_id** | **int**| The id of the scheduled export to be disabled | 
 **include** | **str**| Related objects that can be included in the response:  external_accounts, creator See Including Objects for more information. | [optional] 

### Return type

[**ScheduledExport**](ScheduledExport.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> PaginatedCollection list(include=include, filter=filter, page=page)

Get a list of Scheduled Exports



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.ScheduledExportsApi()
include = 'include_example' # str | Related objects that can be included in the response:  external_accounts, creator See Including Objects for more information. (optional)
filter = {'key': 'filter_example'} # dict(str, str) | Filter Params for Searching.  Equality Searchable Attributes: [id, hour, day, status, recipients, time_zone, name] Matching Searchable Attributes: [recipients, time_zone, name] Limited Searchable Attribute: [frequency_eq] Sortable Attributes: [updated_at, created_at, id, name] Searchable Associations: [creator, external_accounts] See Searching Lists for more information. See the filter parameter of the association's list action to see what attributes are searchable on each association. See Conditions on Relationships in Searching Lists for more information. (optional)
page = '{:number=>1,+:size=>20}' # str | Page Number and Page Size.  Number is the page number of the collection to return, size is the number of items to return per page. (optional) (default to {:number=>1,+:size=>20})

try: 
    # Get a list of Scheduled Exports
    api_response = api_instance.list(include=include, filter=filter, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduledExportsApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include** | **str**| Related objects that can be included in the response:  external_accounts, creator See Including Objects for more information. | [optional] 
 **filter** | [**dict(str, str)**](str.md)| Filter Params for Searching.  Equality Searchable Attributes: [id, hour, day, status, recipients, time_zone, name] Matching Searchable Attributes: [recipients, time_zone, name] Limited Searchable Attribute: [frequency_eq] Sortable Attributes: [updated_at, created_at, id, name] Searchable Associations: [creator, external_accounts] See Searching Lists for more information. See the filter parameter of the association&#39;s list action to see what attributes are searchable on each association. See Conditions on Relationships in Searching Lists for more information. | [optional] 
 **page** | **str**| Page Number and Page Size.  Number is the page number of the collection to return, size is the number of items to return per page. | [optional] [default to {:number&#x3D;&gt;1,+:size&#x3D;&gt;20}]

### Return type

[**PaginatedCollection**](PaginatedCollection.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show**
> ScheduledExport show(id, include=include)

Show a single Scheduled Export



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.ScheduledExportsApi()
id = 56 # int | Scheduled Export ID
include = 'include_example' # str | Related objects that can be included in the response:  external_accounts, creator See Including Objects for more information. (optional)

try: 
    # Show a single Scheduled Export
    api_response = api_instance.show(id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduledExportsApi->show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Scheduled Export ID | 
 **include** | **str**| Related objects that can be included in the response:  external_accounts, creator See Including Objects for more information. | [optional] 

### Return type

[**ScheduledExport**](ScheduledExport.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_file_details**
> ScheduledExportResult show_file_details(uuid, include=include)

Show a single Scheduled Export Result

The URL provided is temporary and will expire shortly after the request. To download the exported file you will need to follow the URL provided.

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.ScheduledExportsApi()
uuid = 'uuid_example' # str | The uuid to access the result
include = 'include_example' # str | Related objects that can be included in the response:  scheduled_export See Including Objects for more information. (optional)

try: 
    # Show a single Scheduled Export Result
    api_response = api_instance.show_file_details(uuid, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduledExportsApi->show_file_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The uuid to access the result | 
 **include** | **str**| Related objects that can be included in the response:  scheduled_export See Including Objects for more information. | [optional] 

### Return type

[**ScheduledExportResult**](ScheduledExportResult.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unsubscribe_export**
> ScheduledExport unsubscribe_export(uuid, email, include=include)

Update a(n) Scheduled Export



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.ScheduledExportsApi()
uuid = 'uuid_example' # str | The uuid of the export to unsubscribe
email = 'email_example' # str | The email to unsubscribe. Nested under: \"data\": { \"meta\": { \"email\": ... } }
include = 'include_example' # str | Related objects that can be included in the response:  external_accounts, creator See Including Objects for more information. (optional)

try: 
    # Update a(n) Scheduled Export
    api_response = api_instance.unsubscribe_export(uuid, email, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduledExportsApi->unsubscribe_export: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The uuid of the export to unsubscribe | 
 **email** | **str**| The email to unsubscribe. Nested under: \&quot;data\&quot;: { \&quot;meta\&quot;: { \&quot;email\&quot;: ... } } | 
 **include** | **str**| Related objects that can be included in the response:  external_accounts, creator See Including Objects for more information. | [optional] 

### Return type

[**ScheduledExport**](ScheduledExport.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> ScheduledExport update(id, include=include, day=day, external_account_ids=external_account_ids, filter=filter, hour=hour, name=name, recipients=recipients, time_zone=time_zone)

Update a(n) Scheduled Export



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.ScheduledExportsApi()
id = 56 # int | Scheduled Export ID
include = 'include_example' # str | Related objects that can be included in the response:  external_accounts, creator See Including Objects for more information. (optional)
day = 'day_example' # str | Day of the week or day of the month to perform the export.  Allowed Values: Daily: nil - Weekly: sunday, monday, tuesday, wednesday, thursday, friday, or saturday - Monthly: 1 to 31. Valid values are sunday, monday, tuesday, wednesday, thursday, friday, saturday, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31 (optional)
external_account_ids = [56] # list[int] | The ids of the external accounts the report will be exported for (optional)
filter = {'key': 'filter_example'} # dict(str, str) | Params used to filter the alerts that will be exported (optional)
hour = 56 # int | Hour of the day to perform the export. Valid values are 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23 (optional)
name = 'name_example' # str | A name that describes the export (optional)
recipients = ['recipients_example'] # list[str] | Email addresses the export will be sent to (optional)
time_zone = 'time_zone_example' # str | Time zone to use when calculating hour and day (optional)

try: 
    # Update a(n) Scheduled Export
    api_response = api_instance.update(id, include=include, day=day, external_account_ids=external_account_ids, filter=filter, hour=hour, name=name, recipients=recipients, time_zone=time_zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduledExportsApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Scheduled Export ID | 
 **include** | **str**| Related objects that can be included in the response:  external_accounts, creator See Including Objects for more information. | [optional] 
 **day** | **str**| Day of the week or day of the month to perform the export.  Allowed Values: Daily: nil - Weekly: sunday, monday, tuesday, wednesday, thursday, friday, or saturday - Monthly: 1 to 31. Valid values are sunday, monday, tuesday, wednesday, thursday, friday, saturday, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31 | [optional] 
 **external_account_ids** | [**list[int]**](int.md)| The ids of the external accounts the report will be exported for | [optional] 
 **filter** | [**dict(str, str)**](str.md)| Params used to filter the alerts that will be exported | [optional] 
 **hour** | **int**| Hour of the day to perform the export. Valid values are 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23 | [optional] 
 **name** | **str**| A name that describes the export | [optional] 
 **recipients** | [**list[str]**](str.md)| Email addresses the export will be sent to | [optional] 
 **time_zone** | **str**| Time zone to use when calculating hour and day | [optional] 

### Return type

[**ScheduledExport**](ScheduledExport.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

