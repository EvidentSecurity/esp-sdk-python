# esp_sdk.ReportsApi

All URIs are relative to https://api.evident.io

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](ReportsApi.md#create) | **POST** /api/v2/reports.json_api | Create a(n) Report
[**list**](ReportsApi.md#list) | **PUT** /api/v2/reports.json_api | Get a list of Reports
[**show**](ReportsApi.md#show) | **GET** /api/v2/reports/{id}.json_api | Show a single Report


# **create**
> Report create(team_id, include=include)

Create a(n) Report



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.ReportsApi()
team_id = 56 # int | The ID of the team to create a report for
include = 'include_example' # str | Related objects that can be included in the response:  organization, sub_organization, team, external_account, stat See Including Objects for more information. (optional)

try: 
    # Create a(n) Report
    api_response = api_instance.create(team_id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| The ID of the team to create a report for | 
 **include** | **str**| Related objects that can be included in the response:  organization, sub_organization, team, external_account, stat See Including Objects for more information. | [optional] 

### Return type

[**Report**](Report.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> PaginatedCollection list(filter=filter, page=page, include=include)

Get a list of Reports



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.ReportsApi()
filter = {'key': 'filter_example'} # dict(str, str) | Filter Params for Searching.  Equality Searchable Attributes: [id, created_at]  Limited Searchable Attributes: [external_account_arn_eq, external_account_provider_eq] Sortable Attributes: [created_at, id] Searchable Associations: [organization, sub_organization, team, external_account] See Searching Lists for more information. See the filter parameter of the association's list action to see what attributes are searchable on each association. See Conditions on Relationships in Searching Lists for more information. (optional)
page = '{:number=>1,+:size=>20}' # str | Page Number and Page Size.  number is the page number of the collection to return, size is the number of items to return per page (optional) (default to {:number=>1,+:size=>20})
include = 'include_example' # str | Related objects that can be included in the response:  organization, sub_organization, team, external_account, stat See Including Objects for more information. (optional)

try: 
    # Get a list of Reports
    api_response = api_instance.list(filter=filter, page=page, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | [**dict(str, str)**](str.md)| Filter Params for Searching.  Equality Searchable Attributes: [id, created_at]  Limited Searchable Attributes: [external_account_arn_eq, external_account_provider_eq] Sortable Attributes: [created_at, id] Searchable Associations: [organization, sub_organization, team, external_account] See Searching Lists for more information. See the filter parameter of the association&#39;s list action to see what attributes are searchable on each association. See Conditions on Relationships in Searching Lists for more information. | [optional] 
 **page** | **str**| Page Number and Page Size.  number is the page number of the collection to return, size is the number of items to return per page | [optional] [default to {:number&#x3D;&gt;1,+:size&#x3D;&gt;20}]
 **include** | **str**| Related objects that can be included in the response:  organization, sub_organization, team, external_account, stat See Including Objects for more information. | [optional] 

### Return type

[**PaginatedCollection**](PaginatedCollection.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show**
> Report show(id, include=include)

Show a single Report



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.ReportsApi()
id = 56 # int | Report ID
include = 'include_example' # str | Related objects that can be included in the response:  organization, sub_organization, team, external_account, stat See Including Objects for more information. (optional)

try: 
    # Show a single Report
    api_response = api_instance.show(id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Report ID | 
 **include** | **str**| Related objects that can be included in the response:  organization, sub_organization, team, external_account, stat See Including Objects for more information. | [optional] 

### Return type

[**Report**](Report.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

