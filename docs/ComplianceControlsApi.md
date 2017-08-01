# esp_sdk.ComplianceControlsApi

All URIs are relative to *http://localhost/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list**](ComplianceControlsApi.md#list) | **PUT** /api/v2/compliance_controls.json_api | Get a list of Compliance Controls
[**show**](ComplianceControlsApi.md#show) | **GET** /api/v2/compliance_controls/{id}.json_api | Show a single Compliance Control


# **list**
> PaginatedCollection list(filter=filter, include=include, page=page)

Get a list of Compliance Controls

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.ComplianceControlsApi()
filter = {'key': 'filter_example'} # dict(str, str) | Filter Params for Searching.  Equality Searchable Attributes: [id, identifier, name] Matching Searchable Attributes: [identifier, name]  Sortable Attributes: [id, identifier, name, position] Searchable Associations: [compliance_standard, compliance_domain] See the filter parameter of the association's list action to see what attributes are searchable on each association. See Searching on Relationships for more information. See Searching Lists for more information. Example: filter: {name_eq: 'Bob'} (optional)
include = 'include_example' # str | Objects that can be included in the response:  compliance_standard,compliance_domain,signatures  See Including Objects for more information. (optional)
page = {'key': 'page_example'} # dict(str, str) | Page Number and Page Size.  Example: page: {number: 1, size: 20} (optional)

try: 
    # Get a list of Compliance Controls
    api_response = api_instance.list(filter=filter, include=include, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComplianceControlsApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | [**dict(str, str)**](str.md)| Filter Params for Searching.  Equality Searchable Attributes: [id, identifier, name] Matching Searchable Attributes: [identifier, name]  Sortable Attributes: [id, identifier, name, position] Searchable Associations: [compliance_standard, compliance_domain] See the filter parameter of the association&#39;s list action to see what attributes are searchable on each association. See Searching on Relationships for more information. See Searching Lists for more information. Example: filter: {name_eq: &#39;Bob&#39;} | [optional] 
 **include** | **str**| Objects that can be included in the response:  compliance_standard,compliance_domain,signatures  See Including Objects for more information. | [optional] 
 **page** | [**dict(str, str)**](str.md)| Page Number and Page Size.  Example: page: {number: 1, size: 20} | [optional] 

### Return type

[**PaginatedCollection**](PaginatedCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show**
> ComplianceControl show(id, include=include)

Show a single Compliance Control

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.ComplianceControlsApi()
id = 56 # int | Compliance Control Id
include = 'include_example' # str | Objects that can be included in the response:  compliance_standard,compliance_domain,signatures  See Including Objects for more information. (optional)

try: 
    # Show a single Compliance Control
    api_response = api_instance.show(id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComplianceControlsApi->show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Compliance Control Id | 
 **include** | **str**| Objects that can be included in the response:  compliance_standard,compliance_domain,signatures  See Including Objects for more information. | [optional] 

### Return type

[**ComplianceControl**](ComplianceControl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

