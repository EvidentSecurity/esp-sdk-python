# coding: utf-8

"""
    ESP Documentation

    The Evident Security Platform API (version 2.0) is designed to allow users granular control over their Amazon Web Service security experience by allowing them to review alerts, monitor signatures, and create custom signatures.

    OpenAPI spec version: v2_sdk
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class AzureGroupsApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def add_external_account(self, azure_group_id, external_account_id, **kwargs):
        """
        Add an External Account to an Azure Group
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.add_external_account(azure_group_id, external_account_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int azure_group_id: The ID of the Azure group associated with this memberhsip (required)
        :param int external_account_id: The ID of the External Account associated with this memberhsip (required)
        :param str include: Related objects that can be included in the response:  organization, sub_organization, team, scan_intervals, disabled_signatures, suppressions, azure_group, credentials See Including Objects for more information.
        :return: ExternalAccount
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.add_external_account_with_http_info(azure_group_id, external_account_id, **kwargs)
        else:
            (data) = self.add_external_account_with_http_info(azure_group_id, external_account_id, **kwargs)
            return data

    def add_external_account_with_http_info(self, azure_group_id, external_account_id, **kwargs):
        """
        Add an External Account to an Azure Group
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.add_external_account_with_http_info(azure_group_id, external_account_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int azure_group_id: The ID of the Azure group associated with this memberhsip (required)
        :param int external_account_id: The ID of the External Account associated with this memberhsip (required)
        :param str include: Related objects that can be included in the response:  organization, sub_organization, team, scan_intervals, disabled_signatures, suppressions, azure_group, credentials See Including Objects for more information.
        :return: ExternalAccount
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['azure_group_id', 'external_account_id', 'include']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_external_account" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'azure_group_id' is set
        if ('azure_group_id' not in params) or (params['azure_group_id'] is None):
            raise ValueError("Missing the required parameter `azure_group_id` when calling `add_external_account`")
        # verify the required parameter 'external_account_id' is set
        if ('external_account_id' not in params) or (params['external_account_id'] is None):
            raise ValueError("Missing the required parameter `external_account_id` when calling `add_external_account`")


        collection_formats = {}

        resource_path = '/api/v2/azure_groups/{azure_group_id}/memberships.json_api'.replace('{format}', 'json_api')
        path_params = {}
        if 'azure_group_id' in params:
            path_params['azure_group_id'] = params['azure_group_id']

        query_params = {}
        if 'include' in params:
            query_params['include'] = params['include']

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'external_account_id' in params:
            form_params.append(('external_account_id', params['external_account_id']))

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/vnd.api+json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/vnd.api+json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ExternalAccount',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def create(self, name, **kwargs):
        """
        Create a(n) Azure Group
        The URL will only be returned once when the group is first created
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create(name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str name: Name (required)
        :param str include: Related objects that can be included in the response:  organization, external_accounts See Including Objects for more information.
        :return: AzureGroup
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_with_http_info(name, **kwargs)
        else:
            (data) = self.create_with_http_info(name, **kwargs)
            return data

    def create_with_http_info(self, name, **kwargs):
        """
        Create a(n) Azure Group
        The URL will only be returned once when the group is first created
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_with_http_info(name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str name: Name (required)
        :param str include: Related objects that can be included in the response:  organization, external_accounts See Including Objects for more information.
        :return: AzureGroup
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'include']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params) or (params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `create`")


        collection_formats = {}

        resource_path = '/api/v2/azure_groups.json_api'.replace('{format}', 'json_api')
        path_params = {}

        query_params = {}
        if 'include' in params:
            query_params['include'] = params['include']

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'name' in params:
            form_params.append(('name', params['name']))

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/vnd.api+json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/vnd.api+json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='AzureGroup',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def delete(self, id, **kwargs):
        """
        Delete a(n) Azure Group
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: Azure Group ID (required)
        :return: Meta
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_with_http_info(id, **kwargs)
        else:
            (data) = self.delete_with_http_info(id, **kwargs)
            return data

    def delete_with_http_info(self, id, **kwargs):
        """
        Delete a(n) Azure Group
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_with_http_info(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: Azure Group ID (required)
        :return: Meta
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete`")


        collection_formats = {}

        resource_path = '/api/v2/azure_groups/{id}.json_api'.replace('{format}', 'json_api')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/vnd.api+json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/vnd.api+json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Meta',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def list(self, **kwargs):
        """
        Get a list of Azure Groups
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str include: Related objects that can be included in the response:  organization, external_accounts See Including Objects for more information.
        :param dict(str, str) filter: Filter Params for Searching.  Equality Searchable Attributes: [id, name] Matching Searchable Attribute: [name]  Sortable Attributes: [id, name] Searchable Associations: [organization, external_accounts] See Searching Lists for more information. See the filter parameter of the association's list action to see what attributes are searchable on each association. See Conditions on Relationships in Searching Lists for more information.
        :param str page: Page Number and Page Size.  Number is the page number of the collection to return, size is the number of items to return per page.
        :return: PaginatedCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.list_with_http_info(**kwargs)
        else:
            (data) = self.list_with_http_info(**kwargs)
            return data

    def list_with_http_info(self, **kwargs):
        """
        Get a list of Azure Groups
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str include: Related objects that can be included in the response:  organization, external_accounts See Including Objects for more information.
        :param dict(str, str) filter: Filter Params for Searching.  Equality Searchable Attributes: [id, name] Matching Searchable Attribute: [name]  Sortable Attributes: [id, name] Searchable Associations: [organization, external_accounts] See Searching Lists for more information. See the filter parameter of the association's list action to see what attributes are searchable on each association. See Conditions on Relationships in Searching Lists for more information.
        :param str page: Page Number and Page Size.  Number is the page number of the collection to return, size is the number of items to return per page.
        :return: PaginatedCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['include', 'filter', 'page']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        resource_path = '/api/v2/azure_groups.json_api'.replace('{format}', 'json_api')
        path_params = {}

        query_params = {}
        if 'include' in params:
            query_params['include'] = params['include']

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'filter' in params:
            form_params.append(('filter', params['filter']))
        if 'page' in params:
            form_params.append(('page', params['page']))

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/vnd.api+json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/vnd.api+json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='PaginatedCollection',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def remove_external_account(self, azure_group_id, external_account_id, **kwargs):
        """
        Remove an External Account from an Azure Group
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.remove_external_account(azure_group_id, external_account_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int azure_group_id: The ID of the Azure group associated with this memberhsip (required)
        :param int external_account_id: The ID of the External Account associated with this memberhsip (required)
        :return: Meta
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.remove_external_account_with_http_info(azure_group_id, external_account_id, **kwargs)
        else:
            (data) = self.remove_external_account_with_http_info(azure_group_id, external_account_id, **kwargs)
            return data

    def remove_external_account_with_http_info(self, azure_group_id, external_account_id, **kwargs):
        """
        Remove an External Account from an Azure Group
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.remove_external_account_with_http_info(azure_group_id, external_account_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int azure_group_id: The ID of the Azure group associated with this memberhsip (required)
        :param int external_account_id: The ID of the External Account associated with this memberhsip (required)
        :return: Meta
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['azure_group_id', 'external_account_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method remove_external_account" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'azure_group_id' is set
        if ('azure_group_id' not in params) or (params['azure_group_id'] is None):
            raise ValueError("Missing the required parameter `azure_group_id` when calling `remove_external_account`")
        # verify the required parameter 'external_account_id' is set
        if ('external_account_id' not in params) or (params['external_account_id'] is None):
            raise ValueError("Missing the required parameter `external_account_id` when calling `remove_external_account`")


        collection_formats = {}

        resource_path = '/api/v2/azure_groups/{azure_group_id}/memberships/{external_account_id}.json_api'.replace('{format}', 'json_api')
        path_params = {}
        if 'azure_group_id' in params:
            path_params['azure_group_id'] = params['azure_group_id']
        if 'external_account_id' in params:
            path_params['external_account_id'] = params['external_account_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/vnd.api+json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/vnd.api+json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Meta',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def show(self, id, **kwargs):
        """
        Show a single Azure Group
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.show(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: Azure Group ID (required)
        :param str include: Related objects that can be included in the response:  organization, external_accounts See Including Objects for more information.
        :return: AzureGroup
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.show_with_http_info(id, **kwargs)
        else:
            (data) = self.show_with_http_info(id, **kwargs)
            return data

    def show_with_http_info(self, id, **kwargs):
        """
        Show a single Azure Group
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.show_with_http_info(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: Azure Group ID (required)
        :param str include: Related objects that can be included in the response:  organization, external_accounts See Including Objects for more information.
        :return: AzureGroup
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'include']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method show" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `show`")


        collection_formats = {}

        resource_path = '/api/v2/azure_groups/{id}.json_api'.replace('{format}', 'json_api')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = {}
        if 'include' in params:
            query_params['include'] = params['include']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/vnd.api+json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/vnd.api+json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='AzureGroup',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def update(self, id, **kwargs):
        """
        Update a(n) Azure Group
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: Azure Group ID (required)
        :param str include: Related objects that can be included in the response:  organization, external_accounts See Including Objects for more information.
        :param str name: Name
        :return: AzureGroup
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_with_http_info(id, **kwargs)
        else:
            (data) = self.update_with_http_info(id, **kwargs)
            return data

    def update_with_http_info(self, id, **kwargs):
        """
        Update a(n) Azure Group
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_with_http_info(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: Azure Group ID (required)
        :param str include: Related objects that can be included in the response:  organization, external_accounts See Including Objects for more information.
        :param str name: Name
        :return: AzureGroup
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'include', 'name']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update`")


        collection_formats = {}

        resource_path = '/api/v2/azure_groups/{id}.json_api'.replace('{format}', 'json_api')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = {}
        if 'include' in params:
            query_params['include'] = params['include']

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'name' in params:
            form_params.append(('name', params['name']))

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/vnd.api+json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/vnd.api+json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'PATCH',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='AzureGroup',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
