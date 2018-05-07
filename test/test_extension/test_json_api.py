# coding: utf-8
from test.test_extension.base import TestBase
from mock import Mock
import json
import esp_sdk

from esp_sdk.rest import RESTClientObject
from esp_sdk.api_client import ApiClient
from esp_sdk.apis.alerts_api import AlertsApi


class TestJsonApi(TestBase):
    """ JsonApi unit tests """

    def test_merges_nested_included_objects(self):
        data = self.alert_response()
        parsed_json = json.loads(data)
        rest_client = RESTClientObject()
        response = Mock(status=200, data=data)
        rest_client.pool_manager.request = Mock(return_value=response)
        api_client = ApiClient()
        api_client.rest_client = rest_client
        api = AlertsApi(api_client)

        alert = api.show(1, include='external_account.team.sub_organization,region,signature')

        self.assertEqual(str(alert.external_account.id), next(obj for obj in parsed_json['included'] if obj['type'] == 'external_accounts')['id'])
        self.assertEqual(str(alert.external_account.team.id), next(obj for obj in parsed_json['included'] if obj['type'] == 'teams')['id'])
        self.assertEqual(str(alert.external_account.team.sub_organization.id), next(obj for obj in parsed_json['included'] if obj['type'] == 'sub_organizations')['id'])
        self.assertEqual(str(alert.region.id), next(obj for obj in parsed_json['included'] if obj['type'] == 'regions')['id'])
        self.assertEqual(str(alert.signature.id), next(obj for obj in parsed_json['included'] if obj['type'] == 'signatures')['id'])

    def test_assigns_foreign_keys(self):
        data = self.json_list([self.alert_response()])
        parsed_json = json.loads(data)
        rest_client = RESTClientObject()
        response = Mock(status=200, data=data)
        rest_client.pool_manager.request = Mock(return_value=response)
        api_client = ApiClient()
        api_client.rest_client = rest_client
        api = AlertsApi(api_client)

        alert = api.list_for_report(1).data[0]

        self.assertEqual(str(alert.external_account_id), next(obj for obj in parsed_json['included'] if obj['type'] == 'external_accounts')['id'])
        self.assertEqual(str(alert.region_id), next(obj for obj in parsed_json['included'] if obj['type'] == 'regions')['id'])
        self.assertEqual(str(alert.signature_id), next(obj for obj in parsed_json['included'] if obj['type'] == 'signatures')['id'])

        # nested objects too
        self.assertEqual(str(alert.external_account.team_id), next(obj for obj in parsed_json['included'] if obj['type'] == 'external_accounts')['relationships']['team']['data']['id'])

    def test_does_not_error_with_included_nulls(self):
        data = json.loads(self.json_list([self.alert_response()]))
        data['included'] += [None]
        rest_client = RESTClientObject()
        response = Mock(status=200, data=json.dumps(data))
        rest_client.pool_manager.request = Mock(return_value=response)
        api_client = ApiClient()
        api_client.rest_client = rest_client
        api = AlertsApi(api_client)

        alert = api.list_for_report(1).data[0]

        self.assertIsNotNone(alert.external_account_id)
        self.assertIsNotNone(alert.region_id)
        self.assertIsNotNone(alert.signature_id)
        self.assertIsNotNone(alert.external_account.team_id)
