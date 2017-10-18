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


class Region(BaseObject):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, code=None, name=None, created_at=None, updated_at=None, provider=None):
        """
        Region - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'code': 'str',
            'name': 'str',
            'created_at': 'datetime',
            'updated_at': 'datetime',
            'provider': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'code': 'code',
            'name': 'name',
            'created_at': 'created_at',
            'updated_at': 'updated_at',
            'provider': 'provider'
        }

        self._id = id
        self._code = code
        self._name = name
        self._created_at = created_at
        self._updated_at = updated_at
        self._provider = provider

    @property
    def id(self):
        """
        Gets the id of this Region.
        Unique ID

        :return: The id of this Region.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Region.
        Unique ID

        :param id: The id of this Region.
        :type: int
        """

        self._id = id

    @property
    def code(self):
        """
        Gets the code of this Region.
        AWS region code. This code is underscored

        :return: The code of this Region.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this Region.
        AWS region code. This code is underscored

        :param code: The code of this Region.
        :type: str
        """

        self._code = code

    @property
    def name(self):
        """
        Gets the name of this Region.
        The display name associated with the code

        :return: The name of this Region.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Region.
        The display name associated with the code

        :param name: The name of this Region.
        :type: str
        """

        self._name = name

    @property
    def created_at(self):
        """
        Gets the created_at of this Region.
        ISO 8601 timestamp when the resource was created

        :return: The created_at of this Region.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this Region.
        ISO 8601 timestamp when the resource was created

        :param created_at: The created_at of this Region.
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """
        Gets the updated_at of this Region.
        ISO 8601 timestamp when the resource was updated

        :return: The updated_at of this Region.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this Region.
        ISO 8601 timestamp when the resource was updated

        :param updated_at: The updated_at of this Region.
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def provider(self):
        """
        Gets the provider of this Region.
        The cloud provider this account is for

        :return: The provider of this Region.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """
        Sets the provider of this Region.
        The cloud provider this account is for

        :param provider: The provider of this Region.
        :type: str
        """

        self._provider = provider

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
        if not isinstance(other, Region):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
