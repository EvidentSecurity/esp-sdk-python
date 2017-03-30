from __future__ import absolute_import

import unittest
import json
import math
from esp_sdk.configuration import Configuration

c = Configuration()
c.access_key_id = 'abc'
c.secret_access_key = '345'

class TestBase(unittest.TestCase):
    import esp_sdk as esp_sdk
    import json as json
    from mock import Mock as mock

    def active_record_error_response(self):
        return json.dumps({"errors": [{"status": "401", "title": "Name can't be blank", "meta": {"name": "can't be blank"}}, {"status": "401", "title": "Name is invalid", "meta": {"name": "is invalid"}}, {"status": "401", "title": "Description can't be blank", "meta": {"description": "can't be blank"}}]})

    def organization_response(self):
        return json.dumps({"included": None, "data": {"id": 1, "type": "organizations", "relationships": {"sub_organizations": {"data": [{"type": "sub_organizations", "id": "24"}, {"type": "sub_organizations", "id": "2"}], "links": {"related": "http://localhost:3000/api/v2/sub_organizations.json?filter%5Borganization_id_eq%5D=2"}}, "teams": {"data": [{"type": "teams", "id": "2"}, {"type": "teams", "id": "20"}, {"type": "teams", "id": "21"}], "links": {"related": "http://localhost:3000/api/v2/teams.json?filter%5Borganization_id_eq%5D=2"}}}, "attributes": {"created_at": "2017-03-13 11:44:31 -0400", "name": "Test Org", "updated_at": "2017-03-13 11:44:31 -0400"}}})

    def alert_response(self):
        return json.dumps({"included": [{"id": "1015", "type": "external_accounts", "attributes": {"account": "5", "arn": "arn:aws:iam::5:role/test_sts_role", "created_at": "2015-09-11T21:12:15.183Z", "external_id": "test_sts_external_id_1", "name": None, "updated_at": None, "user_attribution_role": None}, "relationships": {"organization": {"data": {"type": "organizations", "id": "5"}, "links": {"related": "http://test.host/api/v2/organizations/5.json"}}, "sub_organization": {"data": {"type": "sub_organizations", "id": "5"}, "links": {"related": "http://test.host/api/v2/sub_organizations/5.json"}}, "team": {"data": {"type": "teams", "id": "5"}, "links": {"related": "http://test.host/api/v2/teams/5.json"}}, "user_attribution_role": {"data": None}}}, {"id": "5", "type": "teams", "name": "Default Team", "created_at": "2015-09-11T21:12:15.183Z", "updated_at": "2015-09-11T21:12:15.183Z", "relationships": {"sub_organization": {"data": {"type": "sub_organizations", "id": "5"}, "links": {"related": "http://localhost:3000/api/v2/sub_organizations/2.json"}}, "organization": {"data": {"type": "organizations", "id": "5"}, "links": {"related": "http://localhost:3000/api/v2/organizations/2.json"}}}}, {"id": "5", "type": "organizations", "created_at": "2015-09-11T21:12:15.183Z", "name": "Test Org", "updated_at": "2015-09-11T21:12:15.183Z", "relationships": {"sub_organizations": {"data": [{"type": "sub_organizations", "id": "24"}, {"type": "sub_organizations", "id": "2"}], "links": {"related": "http://localhost:3000/api/v2/sub_organizations.json?filter%5Borganization_id_eq%5D=2"}}, "teams": {"data": [{"type": "teams", "id": "2"}, {"type": "teams", "id": "20"}, {"type": "teams", "id": "21"}], "links": {"related": "http://localhost:3000/api/v2/teams.json?filter%5Borganization_id_eq%5D=2"}}}}, {"id": "1014", "type": "regions", "attributes": {"code": "us_east_test_3"}}, {"id": "1013", "type": "signatures", "attributes": {"created_at": "2015-09-11T21:12:15.192Z", "description": "\"Some description for some test\"", "identifier": "3 Unique ID", "name": "3_test_signature", "resolution": "\"Turn on some setting\"", "risk_level": "High", "updated_at": None}, "relationships": {"service": {"data": {"type": "services", "id": "3"}, "links": {"related": "http://test.host/api/v2/services/3.json"}}}}, {"id": "1", "type": "cloud_trail_events", "attributes": {"event_id": "1", "event_name": "1", "event_time": "2015-09-11T21:12:14.661Z", "username": "johndoe", "ip_address": "123.0.0.123", "user_agent": "Chrome"}}, {"id": "1", "type": "suppressions", "attributes": {"created_at": "2015-10-16T18:34:19.464Z", "reason": "I dont like this", "status": "setup", "updated_at": "2015-10-16T18:34:19.464Z", "configuration": {"suppression_type": "regions", "resource": None, "regions": [{"id": "4", "type": "regions", "attributes": {"code": "us_east_test_4"}}], "external_accounts": []}}, "relationships": {"organization": {"data": {"id": "4", "type": "organizations"}, "links": {"related": "http://test.host/api/v2/organizations/4.json"}}, "created_by": {"data": {"id": "1", "type": "users"}, "links": {"related": "http://test.host/api/v2/users/1.json"}}}}, {"id": "1", "type": "tags", "attributes": {"key": "Name", "value": "abc123", "created_at": "2015-10-16T18:34:19.569Z", "updated_at": "2015-10-16T18:34:19.569Z"}}, {"id": "2", "type": "tags", "attributes": {"key": "Name", "value": "abc123", "created_at": "2015-10-16T18:34:19.571Z", "updated_at": "2015-10-16T18:34:19.571Z"}}], "data": {"id": 1, "type": "alerts", "relationships": {"external_account": {"data": {"type": "external_accounts", "id": "1015"}, "links": {"related": "http://test.host/api/v2/external_accounts/1015.json"}}, "region": {"data": {"type": "regions", "id": "1014"}}, "signature": {"data": {"type": "signatures", "id": "1013"}, "links": {"related": "http://test.host/api/v2/signatures/1013.json"}}, "custom_signature": {"data": None}, "suppression": {"data": {"id": "1", "type": "suppressions"}, "links": {"related": "http://test.host/api/v2/suppressions/1.json"}}, "metadata": {"links": {"related": "http://test.host/api/v2/alerts/1017/metadata.json"}}, "cloud_trail_events": {"data": [{"type": "cloud_trail_events", "id": "1"}], "links": {"related": "http://test.host/api/v2/alerts/1017/cloud_trail_events.json"}}, "tags": {"data": [{"id": "1", "type": "tags"}, {"id": "2", "type": "tags"}]}}, "attributes": {"created_at": "2017-03-13 10:03:08 -0400", "status": "fail", "resource": "resource-3", "updated_at": None, "started_at": "2017-03-13 10:03:08 -0400", "ended_at": None}}})

    def dashboard_response(self):
        return json.dumps({"included": [{"id": "1", "type": "stats", "attributes": {"total": 59, "stat_signatures": [{"signature": {"id": 1, "name": "1_test_signature", "risk_level": "High", "service": {"code": "S1", "id": 1, "name": "SSS"}}, "total_pass": 2, "total_fail": 6, "total_warn": 8, "total_error": 1, "total_new_1h": 7, "total_new_1d": 14}], "stat_custom_signatures": [{"custom_signature": {"id": 1, "name": "Test", "risk_level": "Medium"}, "total_pass": 8, "total_fail": 2, "total_warn": 4, "total_error": 6, "total_new_1h": 8, "total_new_1d": 12}], "stat_regions": [{"region": {"id": 1, "code": "us_east_test_1"}, "total_pass": 16, "total_fail": 18, "total_warn": 12, "total_error": 11, "total_high": 16, "total_medium": 18, "total_low": 20, "total_new_1h_high": 4, "total_new_1h_medium": 5, "total_new_1h_low": 9, "total_new_1d_high": 8, "total_new_1d_medium": 8, "total_new_1d_low": 13}]}}], "data": {"id": None, "type": "reports", "relationships": {"stat": {"data": {"type": "stats", "id": "1"}, "links": {"related": "http://test.host/api/v2/reports/1/stats.json"}}}, "attributes": {"team_name": "Operations 1", "sub_organization_name": "IT Department 1", "organization_name": "Test Organization 1", "created_at": "2017-03-13 10:17:07 -0400", "updated_at": "2017-03-13 10:17:07 -0400"}}})

    # helper to form the correct object when getting a collection of objects
    def json_list(self, json_array, page_args=None):
        page_args = page_args or {'page': {'number': 1, 'size': 20}}
        data = [json.loads(j)['data'] for j in json_array]
        links = self._build_links(data, page_args['page'])
        list = {'data': data[0:page_args['page']['size']],
                "links": links}
        if json_array[0]:
            list['included'] = json.loads(json_array[0]).get('included', None)
        return json.dumps(list)

    def _build_links(self, data, page):
        current_page = page['number']
        last_page = math.ceil(float(len(data)) / page['size'])
        links = {"self": "http://localhost:3000/api/v2/not_the_real_url/but_useful_for_testing.json?page%5Bnumber%5D={0}&page%5Bsize%5D={1}".format(current_page, page['size'])}
        if current_page != 1:
            links["prev"] = "http://localhost:3000/api/v2/not_the_real_url/but_useful_for_testing.json?page%5Bnumber%5D={0}&page%5Bsize%5D={1}".format(current_page - 1, page['size'])
        if current_page != last_page:
            links["next"] = "http://localhost:3000/api/v2/not_the_real_url/but_useful_for_testing.json?page%5Bnumber%5D={0}&page%5Bsize%5D={1}".format(current_page + 1, page['size'])
            links["last"] = "http://localhost:3000/api/v2/not_the_real_url/but_useful_for_testing.json?page%5Bnumber%5D={0}&page%5Bsize%5D={1}".format(last_page, page['size'])
        return links
