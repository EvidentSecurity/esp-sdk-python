# esp_sdk.UsersApi

All URIs are relative to https://api.evident.io

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](UsersApi.md#create) | **POST** /api/v2/users.json_api | Create a(n) User
[**delete**](UsersApi.md#delete) | **DELETE** /api/v2/users/{id}.json_api | Delete a(n) User
[**list**](UsersApi.md#list) | **PUT** /api/v2/users.json_api | Get a list of Users
[**show**](UsersApi.md#show) | **GET** /api/v2/users/{id}.json_api | Show a single User
[**update**](UsersApi.md#update) | **PATCH** /api/v2/users/{id}.json_api | Update a(n) User


# **create**
> User create(email, first_name, last_name, include=include, access_level=access_level, disable_daily_emails=disable_daily_emails, phone=phone, role_id=role_id, sub_organization_ids=sub_organization_ids, team_ids=team_ids, time_zone=time_zone)

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
email = 'email_example' # str | The email of the user
first_name = 'first_name_example' # str | The first name of the user
last_name = 'last_name_example' # str | The last name of the user
include = 'include_example' # str | Related objects that can be included in the response:  organization, sub_organizations, teams, role See Including Objects for more information. (optional)
access_level = 'access_level_example' # str | The level of access this user has. Team access has access to items belonging only to that team. Sub Organization access has access to items belonging only to all teams under that sub organization. Organization access has access to all sub organizations and teams under that organization. Valid values are organization_level, sub_organization_level, team_level (optional)
disable_daily_emails = true # bool | Specifies whether the daily emails should be turned off or not (optional)
phone = 'phone_example' # str | The phone number of the user (optional)
role_id = 56 # int | The ID of the role of the user. Only a manager can set or modify the role id. (optional)
sub_organization_ids = [56] # list[int] | A list of sub organization IDs that the user should have access to. Only a manager can set or modify the sub organization ids. (optional)
team_ids = [56] # list[int] | A list of team IDs that the user should have access to. Only a manager can set or modify the team ids. (optional)
time_zone = 'time_zone_example' # str | The time zone of the user. See Time Zones for a list of valid time zones (optional)

try: 
    # Create a(n) User
    api_response = api_instance.create(email, first_name, last_name, include=include, access_level=access_level, disable_daily_emails=disable_daily_emails, phone=phone, role_id=role_id, sub_organization_ids=sub_organization_ids, team_ids=team_ids, time_zone=time_zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| The email of the user | 
 **first_name** | **str**| The first name of the user | 
 **last_name** | **str**| The last name of the user | 
 **include** | **str**| Related objects that can be included in the response:  organization, sub_organizations, teams, role See Including Objects for more information. | [optional] 
 **access_level** | **str**| The level of access this user has. Team access has access to items belonging only to that team. Sub Organization access has access to items belonging only to all teams under that sub organization. Organization access has access to all sub organizations and teams under that organization. Valid values are organization_level, sub_organization_level, team_level | [optional] 
 **disable_daily_emails** | **bool**| Specifies whether the daily emails should be turned off or not | [optional] 
 **phone** | **str**| The phone number of the user | [optional] 
 **role_id** | **int**| The ID of the role of the user. Only a manager can set or modify the role id. | [optional] 
 **sub_organization_ids** | [**list[int]**](int.md)| A list of sub organization IDs that the user should have access to. Only a manager can set or modify the sub organization ids. | [optional] 
 **team_ids** | [**list[int]**](int.md)| A list of team IDs that the user should have access to. Only a manager can set or modify the team ids. | [optional] 
 **time_zone** | **str**| The time zone of the user. See Time Zones for a list of valid time zones | [optional] 

### Return type

[**User**](User.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> Meta delete(id, current_password=current_password)

Delete a(n) User

The users current password is required when deleting yourself.

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.UsersApi()
id = 56 # int | User ID
current_password = 'current_password_example' # str | The user's currently stored password (optional)

try: 
    # Delete a(n) User
    api_response = api_instance.delete(id, current_password=current_password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| User ID | 
 **current_password** | **str**| The user&#39;s currently stored password | [optional] 

### Return type

[**Meta**](Meta.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> PaginatedCollection list(include=include, filter=filter, page=page)

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
include = 'include_example' # str | Related objects that can be included in the response:  organization, sub_organizations, teams, role See Including Objects for more information. (optional)
filter = {'key': 'filter_example'} # dict(str, str) | Filter Params for Searching.  Equality Searchable Attributes: [id, email] Matching Searchable Attribute: [email]  Sortable Attributes: [email, current_sign_in_at, updated_at, created_at, id] Searchable Associations: [role, organization, sub_organizations, teams] See Searching Lists for more information. See the filter parameter of the association's list action to see what attributes are searchable on each association. See Conditions on Relationships in Searching Lists for more information. (optional)
page = '{:number=>1,+:size=>20}' # str | Page Number and Page Size.  Number is the page number of the collection to return, size is the number of items to return per page. (optional) (default to {:number=>1,+:size=>20})

try: 
    # Get a list of Users
    api_response = api_instance.list(include=include, filter=filter, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include** | **str**| Related objects that can be included in the response:  organization, sub_organizations, teams, role See Including Objects for more information. | [optional] 
 **filter** | [**dict(str, str)**](str.md)| Filter Params for Searching.  Equality Searchable Attributes: [id, email] Matching Searchable Attribute: [email]  Sortable Attributes: [email, current_sign_in_at, updated_at, created_at, id] Searchable Associations: [role, organization, sub_organizations, teams] See Searching Lists for more information. See the filter parameter of the association&#39;s list action to see what attributes are searchable on each association. See Conditions on Relationships in Searching Lists for more information. | [optional] 
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
id = 56 # int | User ID
include = 'include_example' # str | Related objects that can be included in the response:  organization, sub_organizations, teams, role See Including Objects for more information. (optional)

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
 **id** | **int**| User ID | 
 **include** | **str**| Related objects that can be included in the response:  organization, sub_organizations, teams, role See Including Objects for more information. | [optional] 

### Return type

[**User**](User.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> User update(id, include=include, access_level=access_level, disable_daily_emails=disable_daily_emails, first_name=first_name, last_name=last_name, phone=phone, role_id=role_id, sub_organization_ids=sub_organization_ids, team_ids=team_ids, time_zone=time_zone)

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
id = 56 # int | User ID
include = 'include_example' # str | Related objects that can be included in the response:  organization, sub_organizations, teams, role See Including Objects for more information. (optional)
access_level = 'access_level_example' # str | The level of access this user has. Team access has access to items belonging only to that team. Sub Organization access has access to items belonging only to all teams under that sub organization. Organization access has access to all sub organizations and teams under that organization. Valid values are organization_level, sub_organization_level, team_level (optional)
disable_daily_emails = true # bool | Specifies whether the daily emails should be turned off or not (optional)
first_name = 'first_name_example' # str | The first name of the user (optional)
last_name = 'last_name_example' # str | The last name of the user (optional)
phone = 'phone_example' # str | The phone number of the user (optional)
role_id = 56 # int | The ID of the role of the user. Only a manager can set or modify the role id. (optional)
sub_organization_ids = [56] # list[int] | A list of sub organization IDs that the user should have access to. Only a manager can set or modify the sub organization ids. (optional)
team_ids = [56] # list[int] | A list of team IDs that the user should have access to. Only a manager can set or modify the team ids. (optional)
time_zone = 'time_zone_example' # str | The time zone of the user. See Time Zones for a list of valid time zones (optional)

try: 
    # Update a(n) User
    api_response = api_instance.update(id, include=include, access_level=access_level, disable_daily_emails=disable_daily_emails, first_name=first_name, last_name=last_name, phone=phone, role_id=role_id, sub_organization_ids=sub_organization_ids, team_ids=team_ids, time_zone=time_zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| User ID | 
 **include** | **str**| Related objects that can be included in the response:  organization, sub_organizations, teams, role See Including Objects for more information. | [optional] 
 **access_level** | **str**| The level of access this user has. Team access has access to items belonging only to that team. Sub Organization access has access to items belonging only to all teams under that sub organization. Organization access has access to all sub organizations and teams under that organization. Valid values are organization_level, sub_organization_level, team_level | [optional] 
 **disable_daily_emails** | **bool**| Specifies whether the daily emails should be turned off or not | [optional] 
 **first_name** | **str**| The first name of the user | [optional] 
 **last_name** | **str**| The last name of the user | [optional] 
 **phone** | **str**| The phone number of the user | [optional] 
 **role_id** | **int**| The ID of the role of the user. Only a manager can set or modify the role id. | [optional] 
 **sub_organization_ids** | [**list[int]**](int.md)| A list of sub organization IDs that the user should have access to. Only a manager can set or modify the sub organization ids. | [optional] 
 **team_ids** | [**list[int]**](int.md)| A list of team IDs that the user should have access to. Only a manager can set or modify the team ids. | [optional] 
 **time_zone** | **str**| The time zone of the user. See Time Zones for a list of valid time zones | [optional] 

### Return type

[**User**](User.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

