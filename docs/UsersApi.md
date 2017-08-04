# esp_sdk.UsersApi

All URIs are relative to *http://localhost/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](UsersApi.md#create) | **POST** /api/v2/users.json_api | Create a(n) User
[**destroy**](UsersApi.md#destroy) | **DELETE** /api/v2/users/{id}.json_api | Remove a(n) User
[**list**](UsersApi.md#list) | **PUT** /api/v2/users.json_api | Get a list of Users
[**show**](UsersApi.md#show) | **GET** /api/v2/users/{id}.json_api | Show a single User
[**update**](UsersApi.md#update) | **PATCH** /api/v2/users/{id}.json_api | Update a(n) User


# **create**
> User create(first_name, last_name, email, role_id=role_id, sub_organization_ids=sub_organization_ids, team_ids=team_ids, disable_daily_emails=disable_daily_emails, phone=phone, time_zone=time_zone)

Create a(n) User

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.UsersApi()
first_name = 'first_name_example' # str | The first name of the user
last_name = 'last_name_example' # str | The last name of the user
email = 'email_example' # str | The email of the user
role_id = 'role_id_example' # str | The role of the user (optional)
sub_organization_ids = [56] # list[int] | A list of sub organization IDs that the user should have access to (optional)
team_ids = [56] # list[int] | A list of team IDs that the user should have access to (optional)
disable_daily_emails = true # bool | Whether the daily emails should be turned off or not. (optional)
phone = 'phone_example' # str | The phone number of the user (optional)
time_zone = 'time_zone_example' # str | The time zone of the user. See Time Zones for a list of valid time zones (optional)

try: 
    # Create a(n) User
    api_response = api_instance.create(first_name, last_name, email, role_id=role_id, sub_organization_ids=sub_organization_ids, team_ids=team_ids, disable_daily_emails=disable_daily_emails, phone=phone, time_zone=time_zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **first_name** | **str**| The first name of the user | 
 **last_name** | **str**| The last name of the user | 
 **email** | **str**| The email of the user | 
 **role_id** | **str**| The role of the user | [optional] 
 **sub_organization_ids** | [**list[int]**](int.md)| A list of sub organization IDs that the user should have access to | [optional] 
 **team_ids** | [**list[int]**](int.md)| A list of team IDs that the user should have access to | [optional] 
 **disable_daily_emails** | **bool**| Whether the daily emails should be turned off or not. | [optional] 
 **phone** | **str**| The phone number of the user | [optional] 
 **time_zone** | **str**| The time zone of the user. See Time Zones for a list of valid time zones | [optional] 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy**
> User destroy(id)

Remove a(n) User

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.UsersApi()
id = 56 # int | User Id

try: 
    # Remove a(n) User
    api_response = api_instance.destroy(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->destroy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| User Id | 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> PaginatedCollection list(filter=filter, include=include, page=page)

Get a list of Users

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.UsersApi()
filter = {'key': 'filter_example'} # dict(str, str) | Filter Params for Searching.  Equality Searchable Attributes: [id, email] Matching Searchable Attribute: [email]  Sortable Attributes: [email, current_sign_in_at, updated_at, created_at, id] Searchable Associations: [role, organization, sub_organizations, teams] See the filter parameter of the association's list action to see what attributes are searchable on each association. See Searching on Relationships for more information. See Searching Lists for more information. Example: filter: {name_eq: 'Bob'} (optional)
include = 'include_example' # str | Objects that can be included in the response:  organization,sub_organizations,teams,role  See Including Objects for more information. (optional)
page = {'key': 'page_example'} # dict(str, str) | Page Number and Page Size.  Example: page: {number: 1, size: 20} (optional)

try: 
    # Get a list of Users
    api_response = api_instance.list(filter=filter, include=include, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | [**dict(str, str)**](str.md)| Filter Params for Searching.  Equality Searchable Attributes: [id, email] Matching Searchable Attribute: [email]  Sortable Attributes: [email, current_sign_in_at, updated_at, created_at, id] Searchable Associations: [role, organization, sub_organizations, teams] See the filter parameter of the association&#39;s list action to see what attributes are searchable on each association. See Searching on Relationships for more information. See Searching Lists for more information. Example: filter: {name_eq: &#39;Bob&#39;} | [optional] 
 **include** | **str**| Objects that can be included in the response:  organization,sub_organizations,teams,role  See Including Objects for more information. | [optional] 
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
> User show(id, include=include)

Show a single User

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.UsersApi()
id = 56 # int | User Id
include = 'include_example' # str | Objects that can be included in the response:  organization,sub_organizations,teams,role  See Including Objects for more information. (optional)

try: 
    # Show a single User
    api_response = api_instance.show(id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| User Id | 
 **include** | **str**| Objects that can be included in the response:  organization,sub_organizations,teams,role  See Including Objects for more information. | [optional] 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> User update(id, first_name, last_name, email, role_id=role_id, sub_organization_ids=sub_organization_ids, team_ids=team_ids, disable_daily_emails=disable_daily_emails, phone=phone, time_zone=time_zone)

Update a(n) User

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.UsersApi()
id = 56 # int | User Id
first_name = 'first_name_example' # str | The first name of the user
last_name = 'last_name_example' # str | The last name of the user
email = 'email_example' # str | The email of the user
role_id = 'role_id_example' # str | The role of the user (optional)
sub_organization_ids = [56] # list[int] | A list of sub organization IDs that the user should have access to (optional)
team_ids = [56] # list[int] | A list of team IDs that the user should have access to (optional)
disable_daily_emails = true # bool | Whether the daily emails should be turned off or not. (optional)
phone = 'phone_example' # str | The phone number of the user (optional)
time_zone = 'time_zone_example' # str | The time zone of the user. See Time Zones for a list of valid time zones (optional)

try: 
    # Update a(n) User
    api_response = api_instance.update(id, first_name, last_name, email, role_id=role_id, sub_organization_ids=sub_organization_ids, team_ids=team_ids, disable_daily_emails=disable_daily_emails, phone=phone, time_zone=time_zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| User Id | 
 **first_name** | **str**| The first name of the user | 
 **last_name** | **str**| The last name of the user | 
 **email** | **str**| The email of the user | 
 **role_id** | **str**| The role of the user | [optional] 
 **sub_organization_ids** | [**list[int]**](int.md)| A list of sub organization IDs that the user should have access to | [optional] 
 **team_ids** | [**list[int]**](int.md)| A list of team IDs that the user should have access to | [optional] 
 **disable_daily_emails** | **bool**| Whether the daily emails should be turned off or not. | [optional] 
 **phone** | **str**| The phone number of the user | [optional] 
 **time_zone** | **str**| The time zone of the user. See Time Zones for a list of valid time zones | [optional] 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

