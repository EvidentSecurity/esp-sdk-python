# coding: utf-8
from base import TestBase
from esp_sdk.extensions.api_authentication import ApiAuthentication

class TestApiAuthentication(TestBase):

    """ ApiAuthentication unit tests """

    def test_sign_request(self):
        auth_headers = ApiAuthentication('PATCH',
                                         'http://example.com/api/v2/organizations.json_api',
                                         '{"data":{"attributes":{"name":"Testing"}}}').auth_headers()

        self.assertIsNotNone(auth_headers['Date'])
        self.assertIsNotNone(auth_headers['Content-MD5'])
        self.assertEqual(auth_headers['Accept'], 'application/vnd.api+json')
        self.assertEqual(auth_headers['Content-Type'], 'application/vnd.api+json')
        self.assertRegexpMatches(auth_headers['Authorization'], 'APIAuth')
