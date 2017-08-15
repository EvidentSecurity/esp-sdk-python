# esp_sdk.TeamsApi

All URIs are relative to https://api.evident.io

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](TeamsApi.md#create) | **POST** /api/v2/teams.json_api | Create a(n) Team
[**destroy**](TeamsApi.md#destroy) | **DELETE** /api/v2/teams/{id}.json_api | Remove a(n) Team
[**list**](TeamsApi.md#list) | **PUT** /api/v2/teams.json_api | Get a list of Teams
[**show**](TeamsApi.md#show) | **GET** /api/v2/teams/{id}.json_api | Show a single Team
[**update**](TeamsApi.md#update) | **PATCH** /api/v2/teams/{id}.json_api | Update a(n) Team


# **create**
> Team create(sub_organization_id, name)

Create a(n) Team

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.TeamsApi()
sub_organization_id = 56 # int | The ID of the sub organization to attach this team to
name = 'name_example' # str | The name of the sub organization

try: 
    # Create a(n) Team
    api_response = api_instance.create(sub_organization_id, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_organization_id** | **int**| The ID of the sub organization to attach this team to | 
 **name** | **str**| The name of the sub organization | 

### Return type

[**Team**](Team.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy**
> Team destroy(id)

Remove a(n) Team

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.TeamsApi()
id = 56 # int | Team Id

try: 
    # Remove a(n) Team
    api_response = api_instance.destroy(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->destroy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Team Id | 

### Return type

[**Team**](Team.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> PaginatedCollection list(filter=filter, include=include, page=page)

Get a list of Teams

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.TeamsApi()
filter = {'key': 'filter_example'} # dict(str, str) | Filter Params for Searching.  Equality Searchable Attributes: [id, name] Matching Searchable Attribute: [name]  Sortable Attributes: [name, updated_at, created_at, id] Searchable Associations: [organization, sub_organization, custom_signatures, integrations] See the filter parameter of the association's list action to see what attributes are searchable on each association. See Searching on Relationships for more information. See Searching Lists for more information. Example: filter: {name_eq: 'Bob'} (optional)
include = 'include_example' # str | Objects that can be included in the response:  custom_signatures,external_accounts,organization,sub_organization  See Including Objects for more information. (optional)
page = {'key': 'page_example'} # dict(str, str) | Page Number and Page Size.  Example: page: {number: 1, size: 20} (optional)

try: 
    # Get a list of Teams
    api_response = api_instance.list(filter=filter, include=include, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | [**dict(str, str)**](str.md)| Filter Params for Searching.  Equality Searchable Attributes: [id, name] Matching Searchable Attribute: [name]  Sortable Attributes: [name, updated_at, created_at, id] Searchable Associations: [organization, sub_organization, custom_signatures, integrations] See the filter parameter of the association&#39;s list action to see what attributes are searchable on each association. See Searching on Relationships for more information. See Searching Lists for more information. Example: filter: {name_eq: &#39;Bob&#39;} | [optional] 
 **include** | **str**| Objects that can be included in the response:  custom_signatures,external_accounts,organization,sub_organization  See Including Objects for more information. | [optional] 
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
> Team show(id, include=include)

Show a single Team

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.TeamsApi()
id = 56 # int | Team Id
include = 'include_example' # str | Objects that can be included in the response:  custom_signatures,external_accounts,organization,sub_organization  See Including Objects for more information. (optional)

try: 
    # Show a single Team
    api_response = api_instance.show(id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Team Id | 
 **include** | **str**| Objects that can be included in the response:  custom_signatures,external_accounts,organization,sub_organization  See Including Objects for more information. | [optional] 

### Return type

[**Team**](Team.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> Team update(id, name)

Update a(n) Team

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.TeamsApi()
id = 56 # int | Team Id
name = 'name_example' # str | The name of the sub organization

try: 
    # Update a(n) Team
    api_response = api_instance.update(id, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Team Id | 
 **name** | **str**| The name of the sub organization | 

### Return type

[**Team**](Team.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

