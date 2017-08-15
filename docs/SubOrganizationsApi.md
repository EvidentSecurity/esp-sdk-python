# esp_sdk.SubOrganizationsApi

All URIs are relative to https://api.evident.io

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](SubOrganizationsApi.md#create) | **POST** /api/v2/sub_organizations.json_api | Create a(n) Sub Organization
[**destroy**](SubOrganizationsApi.md#destroy) | **DELETE** /api/v2/sub_organizations/{id}.json_api | Remove a(n) SubOrganization
[**list**](SubOrganizationsApi.md#list) | **PUT** /api/v2/sub_organizations.json_api | Get a list of Sub Organizations
[**show**](SubOrganizationsApi.md#show) | **GET** /api/v2/sub_organizations/{id}.json_api | Show a single Sub Organization
[**update**](SubOrganizationsApi.md#update) | **PATCH** /api/v2/sub_organizations/{id}.json_api | Update a(n) Sub Organization


# **create**
> SubOrganization create(organization_id, name)

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
organization_id = 56 # int | The Id of the organization this sub organization should belong to
name = 'name_example' # str | The name of the sub organization

try: 
    # Create a(n) Sub Organization
    api_response = api_instance.create(organization_id, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubOrganizationsApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| The Id of the organization this sub organization should belong to | 
 **name** | **str**| The name of the sub organization | 

### Return type

[**SubOrganization**](SubOrganization.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy**
> SubOrganization destroy(id)

Remove a(n) SubOrganization

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.SubOrganizationsApi()
id = 56 # int | SubOrganization Id

try: 
    # Remove a(n) SubOrganization
    api_response = api_instance.destroy(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubOrganizationsApi->destroy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| SubOrganization Id | 

### Return type

[**SubOrganization**](SubOrganization.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> PaginatedCollection list(filter=filter, include=include, page=page)

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
filter = {'key': 'filter_example'} # dict(str, str) | Filter Params for Searching.  Equality Searchable Attributes: [id, name] Matching Searchable Attribute: [name]  Sortable Attributes: [name, updated_at, created_at, id] Searchable Association: [organization] See the filter parameter of the association's list action to see what attributes are searchable on each association. See Searching on Relationships for more information. See Searching Lists for more information. Example: filter: {name_eq: 'Bob'} (optional)
include = 'include_example' # str | Objects that can be included in the response:  external_accounts,organization,teams  See Including Objects for more information. (optional)
page = {'key': 'page_example'} # dict(str, str) | Page Number and Page Size.  Example: page: {number: 1, size: 20} (optional)

try: 
    # Get a list of Sub Organizations
    api_response = api_instance.list(filter=filter, include=include, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubOrganizationsApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | [**dict(str, str)**](str.md)| Filter Params for Searching.  Equality Searchable Attributes: [id, name] Matching Searchable Attribute: [name]  Sortable Attributes: [name, updated_at, created_at, id] Searchable Association: [organization] See the filter parameter of the association&#39;s list action to see what attributes are searchable on each association. See Searching on Relationships for more information. See Searching Lists for more information. Example: filter: {name_eq: &#39;Bob&#39;} | [optional] 
 **include** | **str**| Objects that can be included in the response:  external_accounts,organization,teams  See Including Objects for more information. | [optional] 
 **page** | [**dict(str, str)**](str.md)| Page Number and Page Size.  Example: page: {number: 1, size: 20} | [optional] 

### Return type

[**PaginatedCollection**](PaginatedCollection.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

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
include = 'include_example' # str | Objects that can be included in the response:  external_accounts,organization,teams  See Including Objects for more information. (optional)

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
 **include** | **str**| Objects that can be included in the response:  external_accounts,organization,teams  See Including Objects for more information. | [optional] 

### Return type

[**SubOrganization**](SubOrganization.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

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

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

