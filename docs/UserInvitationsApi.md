# esp_sdk.UserInvitationsApi

All URIs are relative to *http://localhost/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**update**](UserInvitationsApi.md#update) | **PATCH** /api/v2/users/invitations.json_api | A successful call to this API updates and accepts a User Invitation


# **update**
> User update(password, password_confirmation, invitation_token)

A successful call to this API updates and accepts a User Invitation

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.UserInvitationsApi()
password = 'password_example' # str | The password for the new user
password_confirmation = 'password_confirmation_example' # str | The password confirmation for the new user
invitation_token = 'invitation_token_example' # str | The token generated with the User Invite

try: 
    # A successful call to this API updates and accepts a User Invitation
    api_response = api_instance.update(password, password_confirmation, invitation_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserInvitationsApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **password** | **str**| The password for the new user | 
 **password_confirmation** | **str**| The password confirmation for the new user | 
 **invitation_token** | **str**| The token generated with the User Invite | 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

