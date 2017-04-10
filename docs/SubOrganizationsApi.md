# esp_sdk.SubOrganizationsApi

All URIs are relative to *http://localhost/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](SubOrganizationsApi.md#create) | **POST** /api/v2/sub_organizations.json_api | Create a(n) Sub Organization
[**destroy**](SubOrganizationsApi.md#destroy) | **DELETE** /api/v2/sub_organizations/{id}.json_api | Remove a(n) Sub Organization
[**list**](SubOrganizationsApi.md#list) | **PUT** /api/v2/sub_organizations.json_api | Get a list of Sub Organizations
[**show**](SubOrganizationsApi.md#show) | **GET** /api/v2/sub_organizations/{id}.json_api | Show a single Sub Organization
[**update**](SubOrganizationsApi.md#update) | **PATCH** /api/v2/sub_organizations/{id}.json_api | Update a(n) Sub Organization


# **create**
> SubOrganization create(name)

Create a(n) Sub Organization

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.SubOrganizationsApi()
name = 'name_example' # str | The name of the sub organization

try: 
    # Create a(n) Sub Organization
    api_response = api_instance.create(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubOrganizationsApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the sub organization | 

### Return type

[**SubOrganization**](SubOrganization.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy**
> object destroy(id)

Remove a(n) Sub Organization

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.SubOrganizationsApi()
id = 56 # int | Sub Organization Id

try: 
    # Remove a(n) Sub Organization
    api_response = api_instance.destroy(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubOrganizationsApi->destroy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Sub Organization Id | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> PaginatedCollection list(page=page, filter=filter, include=include)

Get a list of Sub Organizations

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.SubOrganizationsApi()
page = {'key': 'page_example'} # dict(str, str) | Page Number (optional)
filter = {'key': 'filter_example'} # dict(str, str) | Filter Params for Searching (optional)
include = 'include_example' # str | Included Objects (optional)

try: 
    # Get a list of Sub Organizations
    api_response = api_instance.list(page=page, filter=filter, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubOrganizationsApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | [**dict(str, str)**](str.md)| Page Number | [optional] 
 **filter** | [**dict(str, str)**](str.md)| Filter Params for Searching | [optional] 
 **include** | **str**| Included Objects | [optional] 

### Return type

[**PaginatedCollection**](PaginatedCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show**
> SubOrganization show(id, include=include)

Show a single Sub Organization

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.SubOrganizationsApi()
id = 56 # int | Sub Organization Id
include = 'include_example' # str | Included Objects (optional)

try: 
    # Show a single Sub Organization
    api_response = api_instance.show(id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubOrganizationsApi->show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Sub Organization Id | 
 **include** | **str**| Included Objects | [optional] 

### Return type

[**SubOrganization**](SubOrganization.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> SubOrganization update(id, name)

Update a(n) Sub Organization

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.SubOrganizationsApi()
id = 56 # int | Sub Organization Id
name = 'name_example' # str | The name of the sub organization

try: 
    # Update a(n) Sub Organization
    api_response = api_instance.update(id, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubOrganizationsApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Sub Organization Id | 
 **name** | **str**| The name of the sub organization | 

### Return type

[**SubOrganization**](SubOrganization.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

