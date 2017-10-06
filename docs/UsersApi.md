# esp_sdk.UsersApi

All URIs are relative to https://api.evident.io

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
role_id = 56 # int | The ID of the role of the user (optional)
sub_organization_ids = [56] # list[int] | A list of sub organization IDs that the user should have access to (optional)
team_ids = [56] # list[int] | A list of team IDs that the user should have access to (optional)
disable_daily_emails = true # bool | Specifies whether the daily emails should be turned off or not (optional)
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
 **role_id** | **int**| The ID of the role of the user | [optional] 
 **sub_organization_ids** | [**list[int]**](int.md)| A list of sub organization IDs that the user should have access to | [optional] 
 **team_ids** | [**list[int]**](int.md)| A list of team IDs that the user should have access to | [optional] 
 **disable_daily_emails** | **bool**| Specifies whether the daily emails should be turned off or not | [optional] 
 **phone** | **str**| The phone number of the user | [optional] 
 **time_zone** | **str**| The time zone of the user. See Time Zones for a list of valid time zones | [optional] 

### Return type

[**User**](User.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy**
> Meta destroy(id)

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
id = 56 # int | User ID

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
 **id** | **int**| User ID | 

### Return type

[**Meta**](Meta.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
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
filter = {'key': 'filter_example'} # dict(str, str) | Filter Params for Searching.  See Searching Lists for more information. (optional)
include = 'include_example' # str | Related objects that can be included in the response.  See Including Objects for more information. (optional)
page = '{:number=>1,+:size=>20}' # str | Page Number and Page Size.  number is the page number of the collection to return, size is the number of items to return per page (optional) (default to {:number=>1,+:size=>20})

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
 **filter** | [**dict(str, str)**](str.md)| Filter Params for Searching.  See Searching Lists for more information. | [optional] 
 **include** | **str**| Related objects that can be included in the response.  See Including Objects for more information. | [optional] 
 **page** | **str**| Page Number and Page Size.  number is the page number of the collection to return, size is the number of items to return per page | [optional] [default to {:number&#x3D;&gt;1,+:size&#x3D;&gt;20}]

### Return type

[**PaginatedCollection**](PaginatedCollection.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

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
include = 'include_example' # str | Related objects that can be included in the response.  See Including Objects for more information. (optional)

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
 **include** | **str**| Related objects that can be included in the response.  See Including Objects for more information. | [optional] 

### Return type

[**User**](User.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
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
id = 56 # int | User ID
first_name = 'first_name_example' # str | The first name of the user
last_name = 'last_name_example' # str | The last name of the user
email = 'email_example' # str | The email of the user
role_id = 56 # int | The ID of the role of the user (optional)
sub_organization_ids = [56] # list[int] | A list of sub organization IDs that the user should have access to (optional)
team_ids = [56] # list[int] | A list of team IDs that the user should have access to (optional)
disable_daily_emails = true # bool | Specifies whether the daily emails should be turned off or not (optional)
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
 **id** | **int**| User ID | 
 **first_name** | **str**| The first name of the user | 
 **last_name** | **str**| The last name of the user | 
 **email** | **str**| The email of the user | 
 **role_id** | **int**| The ID of the role of the user | [optional] 
 **sub_organization_ids** | [**list[int]**](int.md)| A list of sub organization IDs that the user should have access to | [optional] 
 **team_ids** | [**list[int]**](int.md)| A list of team IDs that the user should have access to | [optional] 
 **disable_daily_emails** | **bool**| Specifies whether the daily emails should be turned off or not | [optional] 
 **phone** | **str**| The phone number of the user | [optional] 
 **time_zone** | **str**| The time zone of the user. See Time Zones for a list of valid time zones | [optional] 

### Return type

[**User**](User.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

