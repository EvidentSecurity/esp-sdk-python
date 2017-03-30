# coding: utf-8
from base import TestBase
from mock import Mock
import json
import esp_sdk

from esp_sdk.rest import RESTClientObject
from esp_sdk.api_client import ApiClient
from esp_sdk.apis.alerts_api import AlertsApi
from esp_sdk.apis.dashboard_api import DashboardApi


class TestJsonApi(TestBase):
    """ JsonApi unit tests """

    def test_parses_nested_objects_correctly(self):
        data = self.dashboard_response()
        parsed_json = json.loads(data)
        rest_client = RESTClientObject()
        response = Mock(status=200, data=self.json_list([data]))
        rest_client.pool_manager.request = Mock(return_value=response)
        api_client = ApiClient()
        api_client.rest_client = rest_client
        api = DashboardApi(api_client)

        dashboard = api.recent()

        self.assertEqual(dashboard.data[0].stat.stat_signatures[0].signature.name, parsed_json['included'][0]['attributes']['stat_signatures'][0]['signature']['name'])


    def test_merges_nested_included_objects(self):
        data = self.alert_response()
        parsed_json = json.loads(data)
        rest_client = RESTClientObject()
        response = Mock(status=200, data=data)
        rest_client.pool_manager.request = Mock(return_value=response)
        api_client = ApiClient()
        api_client.rest_client = rest_client
        api = AlertsApi(api_client)

        alert = api.show(1, include='external_account.team.organization,region,signature,cloud_trail_events')

        self.assertEqual(str(alert.external_account.id), next(obj for obj in parsed_json['included'] if obj['type'] == 'external_accounts')['id'])
        self.assertEqual(str(alert.external_account.organization.id), next(obj for obj in parsed_json['included'] if obj['type'] == 'organizations')['id'])
        self.assertEqual(str(alert.external_account.team.id), next(obj for obj in parsed_json['included'] if obj['type'] == 'teams')['id'])
        self.assertEqual(str(alert.external_account.team.organization.id), next(obj for obj in parsed_json['included'] if obj['type'] == 'organizations')['id'])
        self.assertEqual(str(alert.region.id), next(obj for obj in parsed_json['included'] if obj['type'] == 'regions')['id'])
        self.assertEqual(str(alert.signature.id), next(obj for obj in parsed_json['included'] if obj['type'] == 'signatures')['id'])
        self.assertEqual(str(alert.cloud_trail_events[0].id), next(obj for obj in parsed_json['included'] if obj['type'] == 'cloud_trail_events')['id'])

    def test_assigns_foreign_keys(self):
        data = self.json_list([self.alert_response()])
        parsed_json = json.loads(data)
        rest_client = RESTClientObject()
        response = Mock(status=200, data=data)
        rest_client.pool_manager.request = Mock(return_value=response)
        api_client = ApiClient()
        api_client.rest_client = rest_client
        api = AlertsApi(api_client)

        alert = api.list(1).data[0]

        self.assertEqual(str(alert.external_account_id), next(obj for obj in parsed_json['included'] if obj['type'] == 'external_accounts')['id'])
        self.assertEqual(str(alert.region_id), next(obj for obj in parsed_json['included'] if obj['type'] == 'regions')['id'])
        self.assertEqual(str(alert.signature_id), next(obj for obj in parsed_json['included'] if obj['type'] == 'signatures')['id'])
        self.assertIn(next(obj for obj in parsed_json['included'] if obj['type'] == 'tags')['id'], str(alert.tag_ids))
        self.assertIn(next(obj for obj in parsed_json['included'] if obj['type'] == 'cloud_trail_events')['id'], str(alert.cloud_trail_event_ids))

        # nested objects too
        self.assertEqual(str(alert.external_account.organization_id), next(obj for obj in parsed_json['included'] if obj['type'] == 'external_accounts')['relationships']['organization']['data']['id'])

    def test_does_not_error_with_included_nulls(self):
        data = json.loads(self.json_list([self.alert_response()]))
        data['included'] += [None]
        rest_client = RESTClientObject()
        response = Mock(status=200, data=json.dumps(data))
        rest_client.pool_manager.request = Mock(return_value=response)
        api_client = ApiClient()
        api_client.rest_client = rest_client
        api = AlertsApi(api_client)

        alert = api.list(1).data[0]

        self.assertIsNotNone(alert.external_account_id)
        self.assertIsNotNone(alert.region_id)
        self.assertIsNotNone(alert.signature_id)
        self.assertIsNotNone(alert.tag_ids)
        self.assertIsNotNone(alert.cloud_trail_event_ids)
        self.assertIsNotNone(alert.external_account.organization_id)

    def test_error_response_is_parsed_correctly(self):
        data = self.active_record_error_response()
        rest_client = RESTClientObject()
        response = Mock(status=200, data=data)
        rest_client.pool_manager.request = Mock(return_value=response)
        api_client = ApiClient()
        api_client.rest_client = rest_client
        api = AlertsApi(api_client)

        alert = api.show(1)

        self.assertIn("Name can't be blank", alert.errors)
        self.assertIn("Name is invalid", alert.errors)
        self.assertIn("Description can't be blank", alert.errors)
