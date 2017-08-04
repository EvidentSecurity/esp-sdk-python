# esp_sdk.PermissionsApi

All URIs are relative to *http://localhost/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list**](PermissionsApi.md#list) | **GET** /api/v2/permissions.json_api | This API provides a list of all the permissions that the current user has


# **list**
> list[UserPermission] list()

This API provides a list of all the permissions that the current user has

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.PermissionsApi()

try: 
    # This API provides a list of all the permissions that the current user has
    api_response = api_instance.list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermissionsApi->list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[UserPermission]**](UserPermission.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

