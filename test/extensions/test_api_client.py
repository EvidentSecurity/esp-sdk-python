# coding: utf-8
from base import TestBase
from mock import Mock
from esp_sdk.rest import *
from esp_sdk.api_client import ApiClient

import esp_sdk

class TestApiClient(TestBase):
    """ ApiClient unit tests """

    # def test_deserialize_model_handles_paginated_collection(self):
    #     api_client = ApiClient()
    #     response = Mock(data=str(self.json_list([self.organization_response()])))
    #     data = api_client.deserialize(response, 'PaginatedCollection')
    #     self.assertIsInstance(data, esp_sdk.models.paginated_collection.PaginatedCollection)
    #     self.assertIsInstance(data.data[0], esp_sdk.models.organization.Organization)
    #
    # def test_deserialize_model_handles_esp_objects(self):
    #     api_client = ApiClient()
    #     response = Mock(data=self.alert_response())
    #     data = api_client.deserialize(response, 'Alert')
    #     self.assertIsInstance(data, esp_sdk.models.alert.Alert)

    def test_call_api_sets_original_params_and_path_on_PaginatedCollection(self):
        rest_client = RESTClientObject()
        response = Mock(status=200, data=self.json_list([self.organization_response()], {'page': {'number': 1, 'size': 1}}))
        rest_client.pool_manager.request = Mock(return_value=response)
        api_client = ApiClient()
        api_client.rest_client = rest_client

        response, status, headers = api_client.call_api('resource_path', 'PUT',
                     path_params={'path': 'params'}, query_params={'query': 'params'}, header_params={'header': 'params'},
                     body={'body': 'param'}, post_params={'post': 'params'}, files=None,
                     response_type='PaginatedCollection', auth_settings='auth_settings', callback=None,
                     _return_http_data_only=None, collection_formats=None, _preload_content=True,
                     _request_timeout=None)

        self.assertEqual('resource_path', response._resource_path)
        self.assertEqual('PUT', response._method)
        self.assertEqual([('path', 'params')], response._path_params)
        self.assertEqual([('query', 'params')], response._query_params)
        self.assertIn(('header', 'params'), response._header_params.items())
        self.assertEqual('param', response._body['body'])
        self.assertEqual([('post', 'params')], response._post_params)
        self.assertIsNone(response._files)
        self.assertEqual('PaginatedCollection', response._response_type)
        self.assertEqual('auth_settings', response._auth_settings)
        self.assertIsNone(response._callback)
        self.assertIsNone(response._return_http_data_only)
        self.assertIsNone(response._collection_formats)
        self.assertTrue(response._preload_content)
        self.assertIsNone(response._request_timeout)
