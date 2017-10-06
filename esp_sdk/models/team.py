# coding: utf-8

"""
    ESP Documentation

    The Evident Security Platform API (version 2.0) is designed to allow users granular control over their Amazon Web Service security experience by allowing them to review alerts, monitor signatures, and create custom signatures.

    OpenAPI spec version: v2_sdk
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
from ..extensions.base_object import BaseObject
import re


class Team(BaseObject):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, name=None, created_at=None, updated_at=None, custom_signatures=None, custom_signature_ids=None, external_accounts=None, external_account_ids=None, organization=None, organization_id=None, sub_organization=None, sub_organization_id=None):
        """
        Team - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'name': 'str',
            'created_at': 'datetime',
            'updated_at': 'datetime',
            'custom_signatures': 'list[CustomSignature]',
            'custom_signature_ids': 'list[int]',
            'external_accounts': 'list[ExternalAccount]',
            'external_account_ids': 'list[int]',
            'organization': 'Organization',
            'organization_id': 'int',
            'sub_organization': 'SubOrganization',
            'sub_organization_id': 'int'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'created_at': 'created_at',
            'updated_at': 'updated_at',
            'custom_signatures': 'custom_signatures',
            'custom_signature_ids': 'custom_signature_ids',
            'external_accounts': 'external_accounts',
            'external_account_ids': 'external_account_ids',
            'organization': 'organization',
            'organization_id': 'organization_id',
            'sub_organization': 'sub_organization',
            'sub_organization_id': 'sub_organization_id'
        }

        self._id = id
        self._name = name
        self._created_at = created_at
        self._updated_at = updated_at
        self._custom_signatures = custom_signatures
        self._custom_signature_ids = custom_signature_ids
        self._external_accounts = external_accounts
        self._external_account_ids = external_account_ids
        self._organization = organization
        self._organization_id = organization_id
        self._sub_organization = sub_organization
        self._sub_organization_id = sub_organization_id

    @property
    def id(self):
        """
        Gets the id of this Team.
        Unique ID

        :return: The id of this Team.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Team.
        Unique ID

        :param id: The id of this Team.
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this Team.
        Name of the team

        :return: The name of this Team.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Team.
        Name of the team

        :param name: The name of this Team.
        :type: str
        """

        self._name = name

    @property
    def created_at(self):
        """
        Gets the created_at of this Team.
        ISO 8601 timestamp when the resource was created

        :return: The created_at of this Team.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this Team.
        ISO 8601 timestamp when the resource was created

        :param created_at: The created_at of this Team.
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """
        Gets the updated_at of this Team.
        ISO 8601 timestamp when the resource was updated

        :return: The updated_at of this Team.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this Team.
        ISO 8601 timestamp when the resource was updated

        :param updated_at: The updated_at of this Team.
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def custom_signatures(self):
        """
        Gets the custom_signatures of this Team.
        Associated Custom Signatures

        :return: The custom_signatures of this Team.
        :rtype: list[CustomSignature]
        """
        return self._custom_signatures

    @custom_signatures.setter
    def custom_signatures(self, custom_signatures):
        """
        Sets the custom_signatures of this Team.
        Associated Custom Signatures

        :param custom_signatures: The custom_signatures of this Team.
        :type: list[CustomSignature]
        """

        self._custom_signatures = custom_signatures

    @property
    def custom_signature_ids(self):
        """
        Gets the custom_signature_ids of this Team.
        Associated Custom Signatures IDs

        :return: The custom_signature_ids of this Team.
        :rtype: list[int]
        """
        return self._custom_signature_ids

    @custom_signature_ids.setter
    def custom_signature_ids(self, custom_signature_ids):
        """
        Sets the custom_signature_ids of this Team.
        Associated Custom Signatures IDs

        :param custom_signature_ids: The custom_signature_ids of this Team.
        :type: list[int]
        """

        self._custom_signature_ids = custom_signature_ids

    @property
    def external_accounts(self):
        """
        Gets the external_accounts of this Team.
        Associated External Accounts

        :return: The external_accounts of this Team.
        :rtype: list[ExternalAccount]
        """
        return self._external_accounts

    @external_accounts.setter
    def external_accounts(self, external_accounts):
        """
        Sets the external_accounts of this Team.
        Associated External Accounts

        :param external_accounts: The external_accounts of this Team.
        :type: list[ExternalAccount]
        """

        self._external_accounts = external_accounts

    @property
    def external_account_ids(self):
        """
        Gets the external_account_ids of this Team.
        Associated External Accounts IDs

        :return: The external_account_ids of this Team.
        :rtype: list[int]
        """
        return self._external_account_ids

    @external_account_ids.setter
    def external_account_ids(self, external_account_ids):
        """
        Sets the external_account_ids of this Team.
        Associated External Accounts IDs

        :param external_account_ids: The external_account_ids of this Team.
        :type: list[int]
        """

        self._external_account_ids = external_account_ids

    @property
    def organization(self):
        """
        Gets the organization of this Team.
        Associated Organization

        :return: The organization of this Team.
        :rtype: Organization
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """
        Sets the organization of this Team.
        Associated Organization

        :param organization: The organization of this Team.
        :type: Organization
        """

        self._organization = organization

    @property
    def organization_id(self):
        """
        Gets the organization_id of this Team.
        Associated Organization ID

        :return: The organization_id of this Team.
        :rtype: int
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """
        Sets the organization_id of this Team.
        Associated Organization ID

        :param organization_id: The organization_id of this Team.
        :type: int
        """

        self._organization_id = organization_id

    @property
    def sub_organization(self):
        """
        Gets the sub_organization of this Team.
        Associated Sub Organization

        :return: The sub_organization of this Team.
        :rtype: SubOrganization
        """
        return self._sub_organization

    @sub_organization.setter
    def sub_organization(self, sub_organization):
        """
        Sets the sub_organization of this Team.
        Associated Sub Organization

        :param sub_organization: The sub_organization of this Team.
        :type: SubOrganization
        """

        self._sub_organization = sub_organization

    @property
    def sub_organization_id(self):
        """
        Gets the sub_organization_id of this Team.
        Associated Sub Organization ID

        :return: The sub_organization_id of this Team.
        :rtype: int
        """
        return self._sub_organization_id

    @sub_organization_id.setter
    def sub_organization_id(self, sub_organization_id):
        """
        Sets the sub_organization_id of this Team.
        Associated Sub Organization ID

        :param sub_organization_id: The sub_organization_id of this Team.
        :type: int
        """

        self._sub_organization_id = sub_organization_id

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, Team):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
