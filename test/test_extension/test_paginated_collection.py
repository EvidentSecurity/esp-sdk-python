# coding: utf-8
from six import PY3
from test.test_extension.base import TestBase
from mock import Mock
from esp_sdk.rest import *
from esp_sdk.api_client import ApiClient
from esp_sdk.apis.organizations_api import OrganizationsApi
from esp_sdk.extensions.paginated_collection import PaginatedCollection


class TestPaginatedCollection(TestBase):

    """ PaginatedCollection unit tests """

    def test_parse_pagination_links_does_not_set_previous_next_or_last_page_when_only_1_page(self):
        rest_client = RESTClientObject()
        response = Mock(status=200, data=self.json_list([self.organization_response(), self.organization_response()], {'page': {'number': 1, 'size': 20}}))
        rest_client.pool_manager.request = Mock(return_value=response)
        api_client = ApiClient()
        api_client.rest_client = rest_client
        api = OrganizationsApi(api_client)

        orgs = api.list()

        self.assertEqual(orgs.current_page_number, '1')
        self.assertIsNone(orgs.next_page_number)
        self.assertIsNone(orgs.previous_page_number)
        self.assertIsNone(orgs.last_page_number)
        self.assertFalse(orgs.has_next_page)
        self.assertFalse(orgs.has_previous_page)
        self.assertTrue(orgs.is_last_page)

    def test_previous_page_is_not_set_when_on_first_page(self):
        rest_client = RESTClientObject()
        response = Mock(status=200, data=self.json_list([self.organization_response(), self.organization_response()], {'page': {'number': 1, 'size': 1}}))
        rest_client.pool_manager.request = Mock(return_value=response)
        api_client = ApiClient()
        api_client.rest_client = rest_client
        api = OrganizationsApi(api_client)

        orgs = api.list()

        self.assertEqual(orgs.current_page_number, '1')
        self.assertEqual(orgs.next_page_number, '2')
        self.assertIsNone(orgs.previous_page_number)
        self.assertEqual(orgs.last_page_number, '2')
        self.assertTrue(orgs.has_next_page)
        self.assertFalse(orgs.has_previous_page)
        self.assertFalse(orgs.is_last_page)

    def test_last_and_nextpage_is_not_set_when_on_last_page(self):
        rest_client = RESTClientObject()
        response = Mock(status=200, data=self.json_list([self.organization_response(), self.organization_response()], {'page': {'number': 2, 'size': 1}}))
        rest_client.pool_manager.request = Mock(return_value=response)
        api_client = ApiClient()
        api_client.rest_client = rest_client
        api = OrganizationsApi(api_client)

        orgs = api.list()

        self.assertEqual(orgs.current_page_number, '2')
        self.assertIsNone(orgs.next_page_number)
        self.assertEqual(orgs.previous_page_number, '1')
        self.assertIsNone(orgs.last_page_number)
        self.assertFalse(orgs.has_next_page)
        self.assertTrue(orgs.has_previous_page)
        self.assertTrue(orgs.is_last_page)

    def test_next_last_and_previous_pages_are_set_when_not_on_last_page(self):
        rest_client = RESTClientObject()
        response = Mock(status=200, data=self.json_list([self.organization_response(), self.organization_response(), self.organization_response()], {'page': {'number': 2, 'size': 1}}))
        rest_client.pool_manager.request = Mock(return_value=response)
        api_client = ApiClient()
        api_client.rest_client = rest_client
        api = OrganizationsApi(api_client)

        orgs = api.list()

        self.assertEqual(orgs.current_page_number, '2')
        self.assertEqual(orgs.next_page_number, '3')
        self.assertEqual(orgs.previous_page_number, '1')
        self.assertEqual(orgs.last_page_number, '3')
        self.assertTrue(orgs.has_next_page)
        self.assertTrue(orgs.has_previous_page)
        self.assertFalse(orgs.is_last_page)

    def test_page_size_is_set_on_each_link(self):
        rest_client = RESTClientObject()
        response = Mock(status=200, data=self.json_list([self.organization_response(), self.organization_response(), self.organization_response()], {'page': {'number': 2, 'size': 1}}))
        rest_client.pool_manager.request = Mock(return_value=response)
        api_client = ApiClient()
        api_client.rest_client = rest_client
        api = OrganizationsApi(api_client)

        orgs = api.list()

        self.assertEqual(orgs._next_page_params['size'], '1')
        self.assertEqual(orgs._previous_page_params['size'], '1')
        self.assertEqual(orgs._last_page_params['size'], '1')

    def test_page_size_on_previous_link_is_not_set_if_on_last_page(self):
        rest_client = RESTClientObject()
        response = Mock(status=200, data=self.json_list([self.organization_response(), self.organization_response(), self.organization_response()], {'page': {'number': 2, 'size': 2}}))
        rest_client.pool_manager.request = Mock(return_value=response)
        api_client = ApiClient()
        api_client.rest_client = rest_client
        api = OrganizationsApi(api_client)

        orgs = api.list()

        self.assertNotIn('size', orgs._previous_page_params)

    def test_first_page_calls_the_api_with_original_url_and_params_and_page_number_1_param(self):
        rest_client = RESTClientObject()
        response1 = Mock(status=200, data=self.json_list([self.organization_response(), self.organization_response(), self.organization_response()], {'page': {'number': 2, 'size': 1}}))
        response2 = Mock(status=200, data=self.json_list([self.organization_response(), self.organization_response(), self.organization_response()], {'page': {'number': 1, 'size': 1}}))
        responses = Mock()
        responses.side_effect = iter([response1, response2])
        rest_client.pool_manager.request = responses
        api_client = ApiClient()
        api_client.rest_client = rest_client
        api = OrganizationsApi(api_client)
        orgs = api.list(filter={'name_eq': 'name'})

        args1, kwargs1 = rest_client.pool_manager.request.call_args
        self.assertEqual(args1[0], 'PUT')
        if PY3:
            self.assertRegex(args1[1], "/v2/organizations.json_api")
        else:
            self.assertRegexpMatches(args1[1], "/v2/organizations.json_api")
        self.assertEqual(kwargs1['body'], json.dumps({"filter": {"name_eq": "name"}}))
        self.assertNotIn('page', json.loads(kwargs1['body']))

        page = orgs.first_page()

        self.assertEqual(rest_client.pool_manager.request.call_count, 2)
        self.assertEqual(page.current_page_number, '1')
        self.assertEqual(orgs.current_page_number, '2')
        args2, kwargs2 = rest_client.pool_manager.request.call_args
        self.assertEqual(args2[0], args1[0])
        if PY3:
            self.assertRegex(args2[1], args1[1])
        else:
            self.assertRegexpMatches(args2[1], args1[1])
        expected_body = {"filter": {"name_eq": "name"}, "page": {"number": 1}}
        body = json.loads(kwargs2['body'])
        self.assertEqual(body['filter'], expected_body['filter'])
        self.assertEqual(body['page']['number'], expected_body['page']['number'])
        self.assertEqual(kwargs2['preload_content'], kwargs1['preload_content'])
        self.assertEqual(kwargs2['timeout'], kwargs1['timeout'])

    def test_first_page_does_not_call_the_api_and_returns_self_when_already_on_page_1(self):
        rest_client = RESTClientObject()
        response1 = Mock(status=200, data=self.json_list([self.organization_response(), self.organization_response()], {'page': {'number': 1, 'size': 1}}))
        responses = Mock()
        responses.side_effect = iter([response1])
        rest_client.pool_manager.request = responses
        api_client = ApiClient()
        api_client.rest_client = rest_client
        api = OrganizationsApi(api_client)
        orgs = api.list()

        page = orgs.first_page()

        self.assertEqual(rest_client.pool_manager.request.call_count, 1)
        self.assertEqual(page.current_page_number, '1')

    def test_first_page_does_not_error_if_no_initial_params_are_supplied(self):
        rest_client = RESTClientObject()
        response1 = Mock(status=200, data=self.json_list([self.organization_response(), self.organization_response(), self.organization_response()], {'page': {'number': 2, 'size': 2}}))
        response2 = Mock(status=200, data=self.json_list([self.organization_response(), self.organization_response(), self.organization_response()], {'page': {'number': 1, 'size': 2}}))
        responses = Mock()
        responses.side_effect = iter([response1, response2])
        rest_client.pool_manager.request = responses
        api_client = ApiClient()
        api_client.rest_client = rest_client
        api = OrganizationsApi(api_client)
        orgs = api.list()

        page = orgs.first_page()

        self.assertEqual(rest_client.pool_manager.request.call_count, 2)
        self.assertEqual(page.current_page_number, '1')
        self.assertEqual(orgs.current_page_number, '2')

    def test_previous_page_calls_the_api_with_original_url_and_params_and_the_previous_page_number_param(self):
        rest_client = RESTClientObject()
        response1 = Mock(status=200, data=self.json_list([self.organization_response(), self.organization_response(), self.organization_response()], {'page': {'number': 2, 'size': 1}}))
        response2 = Mock(status=200, data=self.json_list([self.organization_response(), self.organization_response(), self.organization_response()], {'page': {'number': 1, 'size': 1}}))
        responses = Mock()
        responses.side_effect = iter([response1, response2])
        rest_client.pool_manager.request = responses
        api_client = ApiClient()
        api_client.rest_client = rest_client
        api = OrganizationsApi(api_client)
        orgs = api.list(filter={'name_eq': 'name'})

        args1, kwargs1 = rest_client.pool_manager.request.call_args
        self.assertEqual(args1[0], 'PUT')
        if PY3:
            self.assertRegex(args1[1], "/v2/organizations.json_api")
        else:
            self.assertRegexpMatches(args1[1], "/v2/organizations.json_api")
        self.assertEqual(kwargs1['body'], json.dumps({"filter": {"name_eq": "name"}}))
        self.assertNotIn('page', json.loads(kwargs1['body']))

        page = orgs.previous_page()

        self.assertEqual(rest_client.pool_manager.request.call_count, 2)
        self.assertEqual(page.current_page_number, '1')
        self.assertEqual(orgs.current_page_number, '2')
        args2, kwargs2 = rest_client.pool_manager.request.call_args
        self.assertEqual(args2[0], args1[0])
        if PY3:
            self.assertRegex(args2[1], args1[1])
        else:
            self.assertRegexpMatches(args2[1], args1[1])
        expected_body = {"filter": {"name_eq": "name"}, "page": {"number": '1', "size": '1'}}
        body = json.loads(kwargs2['body'])
        self.assertEqual(body['filter'], expected_body['filter'])
        self.assertEqual(body['page']['number'], expected_body['page']['number'])
        self.assertEqual(body['page']['size'], expected_body['page']['size'])
        self.assertEqual(kwargs2['preload_content'], kwargs1['preload_content'])
        self.assertEqual(kwargs2['timeout'], kwargs1['timeout'])

    def test_previous_page_does_not_call_the_api_and_returns_self_when_already_on_page_1(self):
        rest_client = RESTClientObject()
        response1 = Mock(status=200, data=self.json_list([self.organization_response(), self.organization_response(), self.organization_response()], {'page': {'number': 1, 'size': 1}}))
        responses = Mock()
        responses.side_effect = iter([response1])
        rest_client.pool_manager.request = responses
        api_client = ApiClient()
        api_client.rest_client = rest_client
        api = OrganizationsApi(api_client)
        orgs = api.list()

        page = orgs.previous_page()

        self.assertEqual(rest_client.pool_manager.request.call_count, 1)
        self.assertEqual(page.current_page_number, '1')

    def test_previous_page_does_not_error_if_no_initial_params_are_supplied(self):
        rest_client = RESTClientObject()
        response1 = Mock(status=200, data=self.json_list([self.organization_response(), self.organization_response(), self.organization_response()], {'page': {'number': 2, 'size': 2}}))
        response2 = Mock(status=200, data=self.json_list([self.organization_response(), self.organization_response(), self.organization_response()], {'page': {'number': 1, 'size': 2}}))
        responses = Mock()
        responses.side_effect = iter([response1, response2])
        rest_client.pool_manager.request = responses
        api_client = ApiClient()
        api_client.rest_client = rest_client
        api = OrganizationsApi(api_client)
        orgs = api.list()

        page = orgs.previous_page()

        self.assertEqual(rest_client.pool_manager.request.call_count, 2)
        self.assertEqual(page.current_page_number, '1')
        self.assertEqual(orgs.current_page_number, '2')

    def test_next_page_calls_the_api_with_original_url_and_params_and_the_next_page_number_param(self):
        rest_client = RESTClientObject()
        response1 = Mock(status=200, data=self.json_list([self.organization_response(), self.organization_response(), self.organization_response()], {'page': {'number': 2, 'size': 1}}))
        response2 = Mock(status=200, data=self.json_list([self.organization_response(), self.organization_response(), self.organization_response()], {'page': {'number': 3, 'size': 1}}))
        responses = Mock()
        responses.side_effect = iter([response1, response2])
        rest_client.pool_manager.request = responses
        api_client = ApiClient()
        api_client.rest_client = rest_client
        api = OrganizationsApi(api_client)
        orgs = api.list(filter={'name_eq': 'name'})

        args1, kwargs1 = rest_client.pool_manager.request.call_args
        self.assertEqual(args1[0], 'PUT')
        if PY3:
            self.assertRegex(args1[1], "/v2/organizations.json_api")
        else:
            self.assertRegexpMatches(args1[1], "/v2/organizations.json_api")
        self.assertEqual(kwargs1['body'], json.dumps({"filter": {"name_eq": "name"}}))
        self.assertNotIn('page', json.loads(kwargs1['body']))

        page = orgs.next_page()

        self.assertEqual(rest_client.pool_manager.request.call_count, 2)
        self.assertEqual(page.current_page_number, '3')
        self.assertEqual(orgs.current_page_number, '2')
        args2, kwargs2 = rest_client.pool_manager.request.call_args
        self.assertEqual(args2[0], args1[0])
        if PY3:
            self.assertRegex(args2[1], args1[1])
        else:
            self.assertRegexpMatches(args2[1], args1[1])
        expected_body = {"filter": {"name_eq": "name"}, "page": {"number": '3', "size": '1'}}
        body = json.loads(kwargs2['body'])
        self.assertEqual(body['filter'], expected_body['filter'])
        self.assertEqual(body['page']['number'], expected_body['page']['number'])
        self.assertEqual(body['page']['size'], expected_body['page']['size'])
        self.assertEqual(kwargs2['preload_content'], kwargs1['preload_content'])
        self.assertEqual(kwargs2['timeout'], kwargs1['timeout'])

    def test_next_page_does_not_call_the_api_and_returns_self_when_already_on_last_page(self):
        rest_client = RESTClientObject()
        response1 = Mock(status=200, data=self.json_list([self.organization_response(), self.organization_response(), self.organization_response()], {'page': {'number': 3, 'size': 1}}))
        responses = Mock()
        responses.side_effect = iter([response1])
        rest_client.pool_manager.request = responses
        api_client = ApiClient()
        api_client.rest_client = rest_client
        api = OrganizationsApi(api_client)
        orgs = api.list()

        page = orgs.next_page()

        self.assertEqual(rest_client.pool_manager.request.call_count, 1)
        self.assertEqual(page.current_page_number, '3')

    def test_next_page_does_not_error_if_no_initial_params_are_supplied(self):
        rest_client = RESTClientObject()
        response1 = Mock(status=200, data=self.json_list([self.organization_response(), self.organization_response(), self.organization_response()], {'page': {'number': 2, 'size': 1}}))
        response2 = Mock(status=200, data=self.json_list([self.organization_response(), self.organization_response(), self.organization_response()], {'page': {'number': 3, 'size': 1}}))
        responses = Mock()
        responses.side_effect = iter([response1, response2])
        rest_client.pool_manager.request = responses
        api_client = ApiClient()
        api_client.rest_client = rest_client
        api = OrganizationsApi(api_client)
        orgs = api.list()

        page = orgs.next_page()

        self.assertEqual(rest_client.pool_manager.request.call_count, 2)
        self.assertEqual(page.current_page_number, '3')
        self.assertEqual(orgs.current_page_number, '2')

    def test_last_page_calls_the_api_with_original_url_and_params_and_the_last_page_number_param(self):
        rest_client = RESTClientObject()
        response1 = Mock(status=200, data=self.json_list([self.organization_response(), self.organization_response(), self.organization_response()], {'page': {'number': 2, 'size': 1}}))
        response2 = Mock(status=200, data=self.json_list([self.organization_response(), self.organization_response(), self.organization_response()], {'page': {'number': 3, 'size': 1}}))
        responses = Mock()
        responses.side_effect = iter([response1, response2])
        rest_client.pool_manager.request = responses
        api_client = ApiClient()
        api_client.rest_client = rest_client
        api = OrganizationsApi(api_client)
        orgs = api.list(filter={'name_eq': 'name'})

        args1, kwargs1 = rest_client.pool_manager.request.call_args
        self.assertEqual(args1[0], 'PUT')
        if PY3:
            self.assertRegex(args1[1], "/v2/organizations.json_api")
        else:
            self.assertRegexpMatches(args1[1], "/v2/organizations.json_api")
        self.assertEqual(kwargs1['body'], json.dumps({"filter": {"name_eq": "name"}}))
        self.assertNotIn('page', json.loads(kwargs1['body']))

        page = orgs.last_page()

        self.assertEqual(rest_client.pool_manager.request.call_count, 2)
        self.assertEqual(page.current_page_number, '3')
        self.assertEqual(orgs.current_page_number, '2')
        args2, kwargs2 = rest_client.pool_manager.request.call_args
        self.assertEqual(args2[0], args1[0])
        if PY3:
            self.assertRegex(args2[1], args1[1])
        else:
            self.assertRegexpMatches(args2[1], args1[1])
        expected_body = {"filter": {"name_eq": "name"}, "page": {"number": '3', "size": '1'}}
        body = json.loads(kwargs2['body'])
        self.assertEqual(body['filter'], expected_body['filter'])
        self.assertEqual(body['page']['number'], expected_body['page']['number'])
        self.assertEqual(body['page']['size'], expected_body['page']['size'])
        self.assertEqual(kwargs2['preload_content'], kwargs1['preload_content'])
        self.assertEqual(kwargs2['timeout'], kwargs1['timeout'])

    def test_last_page_does_not_call_the_api_and_returns_self_when_already_on_last_page(self):
        rest_client = RESTClientObject()
        response1 = Mock(status=200, data=self.json_list([self.organization_response(), self.organization_response(), self.organization_response()], {'page': {'number': 3, 'size': 1}}))
        responses = Mock()
        responses.side_effect = iter([response1])
        rest_client.pool_manager.request = responses
        api_client = ApiClient()
        api_client.rest_client = rest_client
        api = OrganizationsApi(api_client)
        orgs = api.list()

        page = orgs.last_page()

        self.assertEqual(rest_client.pool_manager.request.call_count, 1)
        self.assertEqual(page.current_page_number, '3')

    def test_last_page_does_not_error_if_no_initial_params_are_supplied(self):
        rest_client = RESTClientObject()
        response1 = Mock(status=200, data=self.json_list([self.organization_response(), self.organization_response(), self.organization_response()], {'page': {'number': 2, 'size': 1}}))
        response2 = Mock(status=200, data=self.json_list([self.organization_response(), self.organization_response(), self.organization_response()], {'page': {'number': 3, 'size': 1}}))
        responses = Mock()
        responses.side_effect = iter([response1, response2])
        rest_client.pool_manager.request = responses
        api_client = ApiClient()
        api_client.rest_client = rest_client
        api = OrganizationsApi(api_client)
        orgs = api.list()

        page = orgs.last_page()

        self.assertEqual(rest_client.pool_manager.request.call_count, 2)
        self.assertEqual(page.current_page_number, '3')
        self.assertEqual(orgs.current_page_number, '2')

    def test_error_raised_if_page_number_is_not_given(self):
        rest_client = RESTClientObject()
        response1 = Mock(status=200, data=self.json_list([self.organization_response(), self.organization_response(), self.organization_response()], {'page': {'number': 2, 'size': 1}}))
        responses = Mock()
        responses.side_effect = iter([response1])
        rest_client.pool_manager.request = responses
        api_client = ApiClient()
        api_client.rest_client = rest_client
        api = OrganizationsApi(api_client)
        orgs = api.list()

        if PY3:
            with self.assertRaisesRegex(ValueError, 'You must supply a page number.'):
                page = orgs.page()
        else:
            with self.assertRaisesRegexp(ValueError, 'You must supply a page number.'):
                page = orgs.page()

    def test_error_raised_if_page_number_is_not_positive(self):
        rest_client = RESTClientObject()
        response1 = Mock(status=200, data=self.json_list([self.organization_response(), self.organization_response(), self.organization_response()], {'page': {'number': 2, 'size': 1}}))
        responses = Mock()
        responses.side_effect = iter([response1])
        rest_client.pool_manager.request = responses
        api_client = ApiClient()
        api_client.rest_client = rest_client
        api = OrganizationsApi(api_client)
        orgs = api.list()

        if PY3:
            with self.assertRaisesRegex(ValueError, 'Page number cannot be less than 1.'):
                page = orgs.page(0)
        else:
            with self.assertRaisesRegexp(ValueError, 'Page number cannot be less than 1.'):
                page = orgs.page(0)

    def test_error_raised_if_page_number_is_greater_than_last_page_number(self):
        rest_client = RESTClientObject()
        response1 = Mock(status=200, data=self.json_list([self.organization_response(), self.organization_response(), self.organization_response()], {'page': {'number': 2, 'size': 1}}))
        responses = Mock()
        responses.side_effect = iter([response1])
        rest_client.pool_manager.request = responses
        api_client = ApiClient()
        api_client.rest_client = rest_client
        api = OrganizationsApi(api_client)
        orgs = api.list()

        if PY3:
            with self.assertRaisesRegex(ValueError, 'Page number cannot be greater than the last page number.'):
                page = orgs.page(4)
        else:
            with self.assertRaisesRegexp(ValueError, 'Page number cannot be greater than the last page number.'):
                page = orgs.page(4)

    def test_page_calls_the_api_with_original_url_and_params_and_the_page_number_param(self):
        rest_client = RESTClientObject()
        response1 = Mock(status=200, data=self.json_list([self.organization_response(), self.organization_response(), self.organization_response()], {'page': {'number': 2, 'size': 1}}))
        response2 = Mock(status=200, data=self.json_list([self.organization_response(), self.organization_response(), self.organization_response()], {'page': {'number': 3, 'size': 1}}))
        responses = Mock()
        responses.side_effect = iter([response1, response2])
        rest_client.pool_manager.request = responses
        api_client = ApiClient()
        api_client.rest_client = rest_client
        api = OrganizationsApi(api_client)
        orgs = api.list(filter={'name_eq': 'name'})

        args1, kwargs1 = rest_client.pool_manager.request.call_args
        self.assertEqual(args1[0], 'PUT')
        if PY3:
            self.assertRegex(args1[1], "/v2/organizations.json_api")
        else:
            self.assertRegexpMatches(args1[1], "/v2/organizations.json_api")
        self.assertEqual(kwargs1['body'], json.dumps({"filter": {"name_eq": "name"}}))
        self.assertNotIn('page', json.loads(kwargs1['body']))

        page = orgs.page(3)

        self.assertEqual(rest_client.pool_manager.request.call_count, 2)
        self.assertEqual(page.current_page_number, '3')
        self.assertEqual(orgs.current_page_number, '2')
        args2, kwargs2 = rest_client.pool_manager.request.call_args
        self.assertEqual(args2[0], args1[0])
        if PY3:
            self.assertRegex(args2[1], args1[1])
        else:
            self.assertRegexpMatches(args2[1], args1[1])
        expected_body = {"filter": {"name_eq": "name"}, "page": {"number": '3', "size": '1'}}
        body = json.loads(kwargs2['body'])
        self.assertEqual(body['filter'], expected_body['filter'])
        self.assertEqual(body['page']['number'], expected_body['page']['number'])
        self.assertEqual(body['page']['size'], expected_body['page']['size'])
        self.assertEqual(kwargs2['preload_content'], kwargs1['preload_content'])
        self.assertEqual(kwargs2['timeout'], kwargs1['timeout'])

    def test_page_does_not_call_the_api_and_returns_self_when_already_on_page(self):
        rest_client = RESTClientObject()
        response1 = Mock(status=200, data=self.json_list([self.organization_response(), self.organization_response(), self.organization_response()], {'page': {'number': 2, 'size': 1}}))
        responses = Mock()
        responses.side_effect = iter([response1])
        rest_client.pool_manager.request = responses
        api_client = ApiClient()
        api_client.rest_client = rest_client
        api = OrganizationsApi(api_client)
        orgs = api.list()

        page = orgs.page(2)

        self.assertEqual(rest_client.pool_manager.request.call_count, 1)
        self.assertEqual(page.current_page_number, '2')

    def test_page_does_not_error_if_no_initial_params_are_supplied(self):
        rest_client = RESTClientObject()
        response1 = Mock(status=200, data=self.json_list([self.organization_response(), self.organization_response(), self.organization_response()], {'page': {'number': 2, 'size': 1}}))
        response2 = Mock(status=200, data=self.json_list([self.organization_response(), self.organization_response(), self.organization_response()], {'page': {'number': 3, 'size': 1}}))
        responses = Mock()
        responses.side_effect = iter([response1, response2])
        rest_client.pool_manager.request = responses
        api_client = ApiClient()
        api_client.rest_client = rest_client
        api = OrganizationsApi(api_client)
        orgs = api.list()

        page = orgs.page(3)

        self.assertEqual(rest_client.pool_manager.request.call_count, 2)
        self.assertEqual(page.current_page_number, '3')
        self.assertEqual(orgs.current_page_number, '2')
