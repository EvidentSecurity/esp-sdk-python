# esp_sdk.OrganizationsApi

All URIs are relative to https://api.evident.io

Method | HTTP request | Description
------------- | ------------- | -------------
[**list**](OrganizationsApi.md#list) | **PUT** /api/v2/organizations.json_api | Get a list of Organizations
[**list_compliance_standards**](OrganizationsApi.md#list_compliance_standards) | **GET** /api/v2/organizations/{organization_id}/compliance_standards.json_api | Get a list of compliance standards for an organization
[**show**](OrganizationsApi.md#show) | **GET** /api/v2/organizations/{id}.json_api | Show a single Organization
[**update**](OrganizationsApi.md#update) | **PATCH** /api/v2/organizations/{id}.json_api | Update a(n) Organization


# **list**
> PaginatedCollection list(include=include, filter=filter, page=page)

Get a list of Organizations



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.OrganizationsApi()
include = 'include_example' # str | Related objects that can be included in the response:  subscription, custom_signatures, external_accounts, sub_organizations, teams, users, compliance_standards, integrations See Including Objects for more information. (optional)
filter = {'key': 'filter_example'} # dict(str, str) | Filter Params for Searching.  Equality Searchable Attributes: [id, name] Matching Searchable Attribute: [name]  Sortable Attributes: [name, updated_at, created_at, id]  (optional)
page = '{:number=>1,+:size=>20}' # str | Page Number and Page Size.  Number is the page number of the collection to return, size is the number of items to return per page. (optional) (default to {:number=>1,+:size=>20})

try: 
    # Get a list of Organizations
    api_response = api_instance.list(include=include, filter=filter, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include** | **str**| Related objects that can be included in the response:  subscription, custom_signatures, external_accounts, sub_organizations, teams, users, compliance_standards, integrations See Including Objects for more information. | [optional] 
 **filter** | [**dict(str, str)**](str.md)| Filter Params for Searching.  Equality Searchable Attributes: [id, name] Matching Searchable Attribute: [name]  Sortable Attributes: [name, updated_at, created_at, id]  | [optional] 
 **page** | **str**| Page Number and Page Size.  Number is the page number of the collection to return, size is the number of items to return per page. | [optional] [default to {:number&#x3D;&gt;1,+:size&#x3D;&gt;20}]

### Return type

[**PaginatedCollection**](PaginatedCollection.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_compliance_standards**
> PaginatedCollection list_compliance_standards(organization_id, include=include, page=page)

Get a list of compliance standards for an organization



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.OrganizationsApi()
organization_id = 56 # int | The ID of the organization this compliance standard belongs to
include = 'include_example' # str | Related objects that can be included in the response:  compliance_domains, compliance_controls See Including Objects for more information. (optional)
page = '{:number=>1,+:size=>20}' # str | Page Number and Page Size.  Number is the page number of the collection to return, size is the number of items to return per page. (optional) (default to {:number=>1,+:size=>20})

try: 
    # Get a list of compliance standards for an organization
    api_response = api_instance.list_compliance_standards(organization_id, include=include, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->list_compliance_standards: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| The ID of the organization this compliance standard belongs to | 
 **include** | **str**| Related objects that can be included in the response:  compliance_domains, compliance_controls See Including Objects for more information. | [optional] 
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
> Organization show(id, include=include)

Show a single Organization



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.OrganizationsApi()
id = 56 # int | Organization ID
include = 'include_example' # str | Related objects that can be included in the response:  subscription, custom_signatures, external_accounts, sub_organizations, teams, users, compliance_standards, integrations See Including Objects for more information. (optional)

try: 
    # Show a single Organization
    api_response = api_instance.show(id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Organization ID | 
 **include** | **str**| Related objects that can be included in the response:  subscription, custom_signatures, external_accounts, sub_organizations, teams, users, compliance_standards, integrations See Including Objects for more information. | [optional] 

### Return type

[**Organization**](Organization.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> Organization update(id, include=include, name=name, require_mfa=require_mfa)

Update a(n) Organization



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.OrganizationsApi()
id = 56 # int | Organization ID
include = 'include_example' # str | Related objects that can be included in the response:  subscription, custom_signatures, external_accounts, sub_organizations, teams, users, compliance_standards, integrations See Including Objects for more information. (optional)
name = 'name_example' # str | Name of the organization (optional)
require_mfa = true # bool | Whether or not users for this organization are required to enable Multi Factor Authentication (optional)

try: 
    # Update a(n) Organization
    api_response = api_instance.update(id, include=include, name=name, require_mfa=require_mfa)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Organization ID | 
 **include** | **str**| Related objects that can be included in the response:  subscription, custom_signatures, external_accounts, sub_organizations, teams, users, compliance_standards, integrations See Including Objects for more information. | [optional] 
 **name** | **str**| Name of the organization | [optional] 
 **require_mfa** | **bool**| Whether or not users for this organization are required to enable Multi Factor Authentication | [optional] 

### Return type

[**Organization**](Organization.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

