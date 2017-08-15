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


class ScanIntervalsApi(object):
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

    def create(self, external_account_id, interval, service_id, **kwargs):
        """
        Create a(n) Scan Interval
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create(external_account_id, interval, service_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int external_account_id: The ID of the external account this scan interval is for (required)
        :param int interval: The interval, in minutes, this service will be scanned (required)
        :param int service_id: The service ID this scan interval is for (required)
        :return: ScanInterval
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_with_http_info(external_account_id, interval, service_id, **kwargs)
        else:
            (data) = self.create_with_http_info(external_account_id, interval, service_id, **kwargs)
            return data

    def create_with_http_info(self, external_account_id, interval, service_id, **kwargs):
        """
        Create a(n) Scan Interval
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_with_http_info(external_account_id, interval, service_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int external_account_id: The ID of the external account this scan interval is for (required)
        :param int interval: The interval, in minutes, this service will be scanned (required)
        :param int service_id: The service ID this scan interval is for (required)
        :return: ScanInterval
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['external_account_id', 'interval', 'service_id']
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
        # verify the required parameter 'external_account_id' is set
        if ('external_account_id' not in params) or (params['external_account_id'] is None):
            raise ValueError("Missing the required parameter `external_account_id` when calling `create`")
        # verify the required parameter 'interval' is set
        if ('interval' not in params) or (params['interval'] is None):
            raise ValueError("Missing the required parameter `interval` when calling `create`")
        # verify the required parameter 'service_id' is set
        if ('service_id' not in params) or (params['service_id'] is None):
            raise ValueError("Missing the required parameter `service_id` when calling `create`")


        collection_formats = {}

        resource_path = '/api/v2/scan_intervals.json_api'.replace('{format}', 'json_api')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'external_account_id' in params:
            form_params.append(('external_account_id', params['external_account_id']))
        if 'interval' in params:
            form_params.append(('interval', params['interval']))
        if 'service_id' in params:
            form_params.append(('service_id', params['service_id']))

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
                                        response_type='ScanInterval',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def destroy(self, id, **kwargs):
        """
        Remove a(n) ScanInterval
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.destroy(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: ScanInterval Id (required)
        :return: ScanInterval
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.destroy_with_http_info(id, **kwargs)
        else:
            (data) = self.destroy_with_http_info(id, **kwargs)
            return data

    def destroy_with_http_info(self, id, **kwargs):
        """
        Remove a(n) ScanInterval
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.destroy_with_http_info(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: ScanInterval Id (required)
        :return: ScanInterval
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
                    " to method destroy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `destroy`")


        collection_formats = {}

        resource_path = '/api/v2/scan_intervals/{id}.json_api'.replace('{format}', 'json_api')
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
                                        response_type='ScanInterval',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def list(self, external_account_id, **kwargs):
        """
        Get a list of Scan Intervals
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list(external_account_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int external_account_id: (required)
        :param str include: Objects that can be included in the response:  external_account,service  See Including Objects for more information.
        :param dict(str, str) page: Page Number and Page Size.  Example: page: {number: 1, size: 20}
        :return: PaginatedCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.list_with_http_info(external_account_id, **kwargs)
        else:
            (data) = self.list_with_http_info(external_account_id, **kwargs)
            return data

    def list_with_http_info(self, external_account_id, **kwargs):
        """
        Get a list of Scan Intervals
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_with_http_info(external_account_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int external_account_id: (required)
        :param str include: Objects that can be included in the response:  external_account,service  See Including Objects for more information.
        :param dict(str, str) page: Page Number and Page Size.  Example: page: {number: 1, size: 20}
        :return: PaginatedCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['external_account_id', 'include', 'page']
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
        # verify the required parameter 'external_account_id' is set
        if ('external_account_id' not in params) or (params['external_account_id'] is None):
            raise ValueError("Missing the required parameter `external_account_id` when calling `list`")


        collection_formats = {}

        resource_path = '/api/v2/external_accounts/{external_account_id}/scan_intervals.json_api'.replace('{format}', 'json_api')
        path_params = {}
        if 'external_account_id' in params:
            path_params['external_account_id'] = params['external_account_id']

        query_params = {}
        if 'include' in params:
            query_params['include'] = params['include']

        header_params = {}

        form_params = []
        local_var_files = {}
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

        return self.api_client.call_api(resource_path, 'GET',
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

    def show(self, id, **kwargs):
        """
        Show a single Scan Interval
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.show(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: Scan Interval Id (required)
        :param str include: Objects that can be included in the response:  external_account,service  See Including Objects for more information.
        :return: ScanInterval
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
        Show a single Scan Interval
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.show_with_http_info(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: Scan Interval Id (required)
        :param str include: Objects that can be included in the response:  external_account,service  See Including Objects for more information.
        :return: ScanInterval
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

        resource_path = '/api/v2/scan_intervals/{id}.json_api'.replace('{format}', 'json_api')
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
                                        response_type='ScanInterval',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def update(self, id, external_account_id, interval, service_id, **kwargs):
        """
        Update a(n) Scan Interval
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update(id, external_account_id, interval, service_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: Scan Interval Id (required)
        :param int external_account_id: The ID of the external account this scan interval is for (required)
        :param int interval: The interval, in minutes, this service will be scanned (required)
        :param int service_id: The service ID this scan interval is for (required)
        :return: ScanInterval
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_with_http_info(id, external_account_id, interval, service_id, **kwargs)
        else:
            (data) = self.update_with_http_info(id, external_account_id, interval, service_id, **kwargs)
            return data

    def update_with_http_info(self, id, external_account_id, interval, service_id, **kwargs):
        """
        Update a(n) Scan Interval
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_with_http_info(id, external_account_id, interval, service_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: Scan Interval Id (required)
        :param int external_account_id: The ID of the external account this scan interval is for (required)
        :param int interval: The interval, in minutes, this service will be scanned (required)
        :param int service_id: The service ID this scan interval is for (required)
        :return: ScanInterval
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'external_account_id', 'interval', 'service_id']
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
        # verify the required parameter 'external_account_id' is set
        if ('external_account_id' not in params) or (params['external_account_id'] is None):
            raise ValueError("Missing the required parameter `external_account_id` when calling `update`")
        # verify the required parameter 'interval' is set
        if ('interval' not in params) or (params['interval'] is None):
            raise ValueError("Missing the required parameter `interval` when calling `update`")
        # verify the required parameter 'service_id' is set
        if ('service_id' not in params) or (params['service_id'] is None):
            raise ValueError("Missing the required parameter `service_id` when calling `update`")


        collection_formats = {}

        resource_path = '/api/v2/scan_intervals/{id}.json_api'.replace('{format}', 'json_api')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'external_account_id' in params:
            form_params.append(('external_account_id', params['external_account_id']))
        if 'interval' in params:
            form_params.append(('interval', params['interval']))
        if 'service_id' in params:
            form_params.append(('service_id', params['service_id']))

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
                                        response_type='ScanInterval',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
