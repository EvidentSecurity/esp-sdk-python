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


class AlertsApi(object):
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

    def list_compliance_controls(self, alert_id, **kwargs):
        """
        Get a list of Compliance Controls for an Alert
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_compliance_controls(alert_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int alert_id: The ID of the alert the compliance controls belong to (required)
        :param str page: Page Number and Page Size.  number is the page number of the collection to return, size is the number of items to return per page
        :param str include: Related objects that can be included in the response:  compliance_standard, compliance_domain, signatures See Including Objects for more information.
        :return: PaginatedCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.list_compliance_controls_with_http_info(alert_id, **kwargs)
        else:
            (data) = self.list_compliance_controls_with_http_info(alert_id, **kwargs)
            return data

    def list_compliance_controls_with_http_info(self, alert_id, **kwargs):
        """
        Get a list of Compliance Controls for an Alert
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_compliance_controls_with_http_info(alert_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int alert_id: The ID of the alert the compliance controls belong to (required)
        :param str page: Page Number and Page Size.  number is the page number of the collection to return, size is the number of items to return per page
        :param str include: Related objects that can be included in the response:  compliance_standard, compliance_domain, signatures See Including Objects for more information.
        :return: PaginatedCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['alert_id', 'page', 'include']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_compliance_controls" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'alert_id' is set
        if ('alert_id' not in params) or (params['alert_id'] is None):
            raise ValueError("Missing the required parameter `alert_id` when calling `list_compliance_controls`")


        collection_formats = {}

        resource_path = '/api/v2/alerts/{alert_id}/compliance_controls.json_api'.replace('{format}', 'json_api')
        path_params = {}
        if 'alert_id' in params:
            path_params['alert_id'] = params['alert_id']

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

    def list_custom_compliance_controls(self, alert_id, **kwargs):
        """
        Get a list of Custom Compliance Controls for an Alert
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_custom_compliance_controls(alert_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int alert_id: The ID of the alert the custom compliance controls belong to (required)
        :param str page: Page Number and Page Size.  number is the page number of the collection to return, size is the number of items to return per page
        :param str include: Related objects that can be included in the response:  custom_compliance_standard, custom_compliance_domain, signatures, custom_signatures See Including Objects for more information.
        :return: PaginatedCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.list_custom_compliance_controls_with_http_info(alert_id, **kwargs)
        else:
            (data) = self.list_custom_compliance_controls_with_http_info(alert_id, **kwargs)
            return data

    def list_custom_compliance_controls_with_http_info(self, alert_id, **kwargs):
        """
        Get a list of Custom Compliance Controls for an Alert
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_custom_compliance_controls_with_http_info(alert_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int alert_id: The ID of the alert the custom compliance controls belong to (required)
        :param str page: Page Number and Page Size.  number is the page number of the collection to return, size is the number of items to return per page
        :param str include: Related objects that can be included in the response:  custom_compliance_standard, custom_compliance_domain, signatures, custom_signatures See Including Objects for more information.
        :return: PaginatedCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['alert_id', 'page', 'include']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_custom_compliance_controls" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'alert_id' is set
        if ('alert_id' not in params) or (params['alert_id'] is None):
            raise ValueError("Missing the required parameter `alert_id` when calling `list_custom_compliance_controls`")


        collection_formats = {}

        resource_path = '/api/v2/alerts/{alert_id}/custom_compliance_controls.json_api'.replace('{format}', 'json_api')
        path_params = {}
        if 'alert_id' in params:
            path_params['alert_id'] = params['alert_id']

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

    def list_for_report(self, report_id, **kwargs):
        """
        Get a list of Alerts for a Report
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_for_report(report_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int report_id: ID of the Report to Return Alerts For (required)
        :param dict(str, str) filter: Filter Params for Searching.  Equality Searchable Attribute: [id]  Limited Searchable Attributes: [signature_service_id_in, signature_risk_level_in, risk_level_in, risk_level_eq, resource_or_tag_cont, suppressed, not_suppressed, signature_name_cont, signature_identifier_cont, external_account_id_in, external_account_id_eq, external_account_team_id_in, external_account_team_id_eq, region_id_in, region_id_eq, status_in, status_eq, cloud_trail_events_present, open_as_of, signature_id_in, signature_id_eq, external_account_provider_eq]  
        :param str page: Page Number and Page Size.  number is the page number of the collection to return, size is the number of items to return per page
        :param str include: Related objects that can be included in the response:  external_account, region, signature, custom_signature, suppression, metadata, cloud_trail_events, tags, compliance_controls, custom_compliance_controls See Including Objects for more information.
        :return: PaginatedCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.list_for_report_with_http_info(report_id, **kwargs)
        else:
            (data) = self.list_for_report_with_http_info(report_id, **kwargs)
            return data

    def list_for_report_with_http_info(self, report_id, **kwargs):
        """
        Get a list of Alerts for a Report
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_for_report_with_http_info(report_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int report_id: ID of the Report to Return Alerts For (required)
        :param dict(str, str) filter: Filter Params for Searching.  Equality Searchable Attribute: [id]  Limited Searchable Attributes: [signature_service_id_in, signature_risk_level_in, risk_level_in, risk_level_eq, resource_or_tag_cont, suppressed, not_suppressed, signature_name_cont, signature_identifier_cont, external_account_id_in, external_account_id_eq, external_account_team_id_in, external_account_team_id_eq, region_id_in, region_id_eq, status_in, status_eq, cloud_trail_events_present, open_as_of, signature_id_in, signature_id_eq, external_account_provider_eq]  
        :param str page: Page Number and Page Size.  number is the page number of the collection to return, size is the number of items to return per page
        :param str include: Related objects that can be included in the response:  external_account, region, signature, custom_signature, suppression, metadata, cloud_trail_events, tags, compliance_controls, custom_compliance_controls See Including Objects for more information.
        :return: PaginatedCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['report_id', 'filter', 'page', 'include']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_for_report" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'report_id' is set
        if ('report_id' not in params) or (params['report_id'] is None):
            raise ValueError("Missing the required parameter `report_id` when calling `list_for_report`")


        collection_formats = {}

        resource_path = '/api/v2/reports/{report_id}/alerts.json_api'.replace('{format}', 'json_api')
        path_params = {}
        if 'report_id' in params:
            path_params['report_id'] = params['report_id']

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

    def show(self, id, **kwargs):
        """
        Show a single Alert
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.show(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: Alert ID (required)
        :param str include: Related objects that can be included in the response:  external_account, region, signature, custom_signature, suppression, metadata, cloud_trail_events, tags, compliance_controls, custom_compliance_controls See Including Objects for more information.
        :return: Alert
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
        Show a single Alert
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.show_with_http_info(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: Alert ID (required)
        :param str include: Related objects that can be included in the response:  external_account, region, signature, custom_signature, suppression, metadata, cloud_trail_events, tags, compliance_controls, custom_compliance_controls See Including Objects for more information.
        :return: Alert
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

        resource_path = '/api/v2/alerts/{id}.json_api'.replace('{format}', 'json_api')
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
                                        response_type='Alert',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
