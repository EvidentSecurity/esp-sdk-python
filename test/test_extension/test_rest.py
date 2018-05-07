# coding: utf-8
from six import PY3
from test.test_extension.base import TestBase
from mock import Mock
from esp_sdk.rest import *
from esp_sdk.api_client import ApiClient
from esp_sdk.apis.sub_organizations_api import SubOrganizationsApi
from esp_sdk.apis.teams_api import TeamsApi

import json


class TestRESTClientObject(TestBase):
    """ Rest unit tests """

    def test_request_puts_filter_params_in_the_body(self):
        rest_client = RESTClientObject()
        response = Mock(status=200, data=self.organization_response())
        rest_client.pool_manager.request = Mock(return_value=response)
        api_client = ApiClient()
        api_client.rest_client = rest_client
        api = SubOrganizationsApi(api_client)

        api.list(filter={"name_cont": 'Evid'})

        args, kwargs = rest_client.pool_manager.request.call_args
        self.assertEqual(args[0], 'PUT')
        if PY3:
            self.assertRegex(args[1], "/v2/sub_organizations.json_api")
        else:
            self.assertRegexpMatches(args[1], "/v2/sub_organizations.json_api")
        self.assertEqual(kwargs['body'], json.dumps({"filter": {"name_cont": "Evid"}}))

    def test_request_puts_page_params_in_the_body(self):
        rest_client = RESTClientObject()
        response = Mock(status=200, data=self.organization_response())
        rest_client.pool_manager.request = Mock(return_value=response)
        api_client = ApiClient()
        api_client.rest_client = rest_client
        api = SubOrganizationsApi(api_client)

        api.list(page={"number": 3})

        args, kwargs = rest_client.pool_manager.request.call_args
        self.assertEqual(args[0], 'PUT')
        if PY3:
            self.assertRegex(args[1], "/v2/sub_organizations.json_api")
        else:
            self.assertRegexpMatches(args[1], "/v2/sub_organizations.json_api")
        self.assertEqual(kwargs['body'], json.dumps({"page": {"number": 3}}))

    def test_request_puts_form_params_in_json_api_format(self):
        rest_client = RESTClientObject()
        response = Mock(status=200, data=self.organization_response())
        rest_client.pool_manager.request = Mock(return_value=response)
        api_client = ApiClient()
        api_client.rest_client = rest_client
        api = SubOrganizationsApi(api_client)

        api.create('Evident', 1)

        args, kwargs = rest_client.pool_manager.request.call_args
        self.assertEqual(args[0], 'POST')
        if PY3:
            self.assertRegex(args[1], "/v2/sub_organizations.json_api")
        else:
            self.assertRegexpMatches(args[1], "/v2/sub_organizations.json_api")
        self.assertEqual(kwargs['body'], json.dumps({'data': {'attributes': {"organization_id": 1, 'name': 'Evident'}}}))

    def test_request_sets_authorization_headers_for_non_GET(self):
        rest_client = RESTClientObject()
        response = Mock(status=200, data=self.organization_response())
        rest_client.pool_manager.request = Mock(return_value=response)
        api_client = ApiClient()
        api_client.rest_client = rest_client
        api = SubOrganizationsApi(api_client)

        api.create(1, 'Evident')

        args, kwargs = rest_client.pool_manager.request.call_args
        self.assertEqual(args[0], 'POST')
        if PY3:
            self.assertRegex(args[1], "/v2/sub_organizations.json_api")
        else:
            self.assertRegexpMatches(args[1], "/v2/sub_organizations.json_api")
        self.assertIsNotNone(kwargs['headers']['Authorization'])
        self.assertIsNotNone(kwargs['headers']['Date'])
        self.assertIsNotNone(kwargs['headers']['Content-MD5'])
        self.assertEqual(kwargs['headers']['Content-Type'], 'application/vnd.api+json')
        self.assertEqual(kwargs['headers']['Accept'], 'application/vnd.api+json')

    def test_request_sets_authorization_headers_for_GET(self):
        rest_client = RESTClientObject()
        response = Mock(status=200, data=self.organization_response())
        rest_client.pool_manager.request = Mock(return_value=response)
        api_client = ApiClient()
        api_client.rest_client = rest_client
        api = SubOrganizationsApi(api_client)

        api.show(1)

        args, kwargs = rest_client.pool_manager.request.call_args
        self.assertEqual(args[0], 'GET')
        if PY3:
            self.assertRegex(args[1], "/v2/sub_organizations/1.json_api")
        else:
            self.assertRegexpMatches(args[1], "/v2/sub_organizations/1.json_api")
        self.assertIsNotNone(kwargs['headers']['Authorization'])
        self.assertIsNotNone(kwargs['headers']['Date'])
        self.assertIsNotNone(kwargs['headers']['Content-MD5'])
        self.assertEqual(kwargs['headers']['Content-Type'], 'application/vnd.api+json')
        self.assertEqual(kwargs['headers']['Accept'], 'application/vnd.api+json')

    def test_raises_an_ApiException_if_response_is_not_success(self):
        rest_client = RESTClientObject()
        response = Mock(status=422, data=self.active_record_error_response())
        rest_client.pool_manager.request = Mock(return_value=response)
        api_client = ApiClient()
        api_client.rest_client = rest_client
        api = TeamsApi(api_client)

        with self.assertRaises(ApiException) as cm:
            api.show(1)

        self.assertEqual(cm.exception.status, 422)
        self.assertEqual(cm.exception.reason, "Failed.  Response code = 422.  Response message = Name can't be blank Name is invalid Description can't be blank")
