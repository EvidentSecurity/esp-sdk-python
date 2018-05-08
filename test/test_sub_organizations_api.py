# coding: utf-8

"""
    ESP Documentation

    The Evident Security Platform API (version 2.0) is designed to allow users granular control over their Amazon Web Service security experience by allowing them to review alerts, monitor signatures, and create custom signatures.

    OpenAPI spec version: v2_sdk
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import esp_sdk
from esp_sdk.rest import ApiException
from esp_sdk.apis.sub_organizations_api import SubOrganizationsApi


class TestSubOrganizationsApi(unittest.TestCase):
    """ SubOrganizationsApi unit test stubs """

    def setUp(self):
        self.api = esp_sdk.apis.sub_organizations_api.SubOrganizationsApi()

    def tearDown(self):
        pass

    def test_create(self):
        """
        Test case for create

        Create a(n) Sub Organization
        """
        pass

    def test_delete(self):
        """
        Test case for delete

        Delete a(n) Sub Organization
        """
        pass

    def test_list(self):
        """
        Test case for list

        Get a list of Sub Organizations
        """
        pass

    def test_show(self):
        """
        Test case for show

        Show a single Sub Organization
        """
        pass

    def test_update(self):
        """
        Test case for update

        Update a(n) Sub Organization
        """
        pass


if __name__ == '__main__':
    unittest.main()
