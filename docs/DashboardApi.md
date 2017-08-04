# esp_sdk.DashboardApi

All URIs are relative to *http://localhost/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**recent**](DashboardApi.md#recent) | **GET** /api/v2/dashboard/recent.json_api | The data for the dashboard.  The stat, external_account and team objects will be included in the response


# **recent**
> PaginatedCollection recent(filter=filter, include=include, page=page)

The data for the dashboard.  The stat, external_account and team objects will be included in the response

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.DashboardApi()
filter = {'key': 'filter_example'} # dict(str, str) | Filter Params for Searching.  Equality Searchable Attributes: [id, created_at]   Sortable Attributes: [created_at, id] Searchable Associations: [organization, sub_organization, team, external_account] See the filter parameter of the association's list action to see what attributes are searchable on each association. See Searching on Relationships for more information. See Searching Lists for more information. Example: filter: {name_eq: 'Bob'} (optional)
include = 'include_example' # str | Objects that can be included in the response:  stat,external_account,team  See Including Objects for more information. (optional)
page = {'key': 'page_example'} # dict(str, str) | Page Number and Page Size.  Example: page: {number: 1, size: 20} (optional)

try: 
    # The data for the dashboard.  The stat, external_account and team objects will be included in the response
    api_response = api_instance.recent(filter=filter, include=include, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardApi->recent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | [**dict(str, str)**](str.md)| Filter Params for Searching.  Equality Searchable Attributes: [id, created_at]   Sortable Attributes: [created_at, id] Searchable Associations: [organization, sub_organization, team, external_account] See the filter parameter of the association&#39;s list action to see what attributes are searchable on each association. See Searching on Relationships for more information. See Searching Lists for more information. Example: filter: {name_eq: &#39;Bob&#39;} | [optional] 
 **include** | **str**| Objects that can be included in the response:  stat,external_account,team  See Including Objects for more information. | [optional] 
 **page** | [**dict(str, str)**](str.md)| Page Number and Page Size.  Example: page: {number: 1, size: 20} | [optional] 

### Return type

[**PaginatedCollection**](PaginatedCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

