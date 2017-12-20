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


class ExternalAccountAzure(BaseObject):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, subscription_id=None, client_id=None, tenant_id=None, created_at=None, updated_at=None, last_message_received_at=None, app_key=None, channel_url=None, channel_active=None, external_account=None, external_account_id=None):
        """
        ExternalAccountAzure - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'subscription_id': 'str',
            'client_id': 'str',
            'tenant_id': 'str',
            'created_at': 'datetime',
            'updated_at': 'datetime',
            'last_message_received_at': 'datetime',
            'app_key': 'str',
            'channel_url': 'str',
            'channel_active': 'bool',
            'external_account': 'ExternalAccount',
            'external_account_id': 'int'
        }

        self.attribute_map = {
            'id': 'id',
            'subscription_id': 'subscription_id',
            'client_id': 'client_id',
            'tenant_id': 'tenant_id',
            'created_at': 'created_at',
            'updated_at': 'updated_at',
            'last_message_received_at': 'last_message_received_at',
            'app_key': 'app_key',
            'channel_url': 'channel_url',
            'channel_active': 'channel_active',
            'external_account': 'external_account',
            'external_account_id': 'external_account_id'
        }

        self._id = id
        self._subscription_id = subscription_id
        self._client_id = client_id
        self._tenant_id = tenant_id
        self._created_at = created_at
        self._updated_at = updated_at
        self._last_message_received_at = last_message_received_at
        self._app_key = app_key
        self._channel_url = channel_url
        self._channel_active = channel_active
        self._external_account = external_account
        self._external_account_id = external_account_id

    @property
    def id(self):
        """
        Gets the id of this ExternalAccountAzure.
        Unique ID

        :return: The id of this ExternalAccountAzure.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ExternalAccountAzure.
        Unique ID

        :param id: The id of this ExternalAccountAzure.
        :type: int
        """

        self._id = id

    @property
    def subscription_id(self):
        """
        Gets the subscription_id of this ExternalAccountAzure.
        Azure subscription ID

        :return: The subscription_id of this ExternalAccountAzure.
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """
        Sets the subscription_id of this ExternalAccountAzure.
        Azure subscription ID

        :param subscription_id: The subscription_id of this ExternalAccountAzure.
        :type: str
        """

        self._subscription_id = subscription_id

    @property
    def client_id(self):
        """
        Gets the client_id of this ExternalAccountAzure.
        Azure client ID

        :return: The client_id of this ExternalAccountAzure.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """
        Sets the client_id of this ExternalAccountAzure.
        Azure client ID

        :param client_id: The client_id of this ExternalAccountAzure.
        :type: str
        """

        self._client_id = client_id

    @property
    def tenant_id(self):
        """
        Gets the tenant_id of this ExternalAccountAzure.
        Azure tenant ID

        :return: The tenant_id of this ExternalAccountAzure.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """
        Sets the tenant_id of this ExternalAccountAzure.
        Azure tenant ID

        :param tenant_id: The tenant_id of this ExternalAccountAzure.
        :type: str
        """

        self._tenant_id = tenant_id

    @property
    def created_at(self):
        """
        Gets the created_at of this ExternalAccountAzure.
        ISO 8601 timestamp when the resource was created

        :return: The created_at of this ExternalAccountAzure.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this ExternalAccountAzure.
        ISO 8601 timestamp when the resource was created

        :param created_at: The created_at of this ExternalAccountAzure.
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """
        Gets the updated_at of this ExternalAccountAzure.
        ISO 8601 timestamp when the resource was updated

        :return: The updated_at of this ExternalAccountAzure.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this ExternalAccountAzure.
        ISO 8601 timestamp when the resource was updated

        :param updated_at: The updated_at of this ExternalAccountAzure.
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def last_message_received_at(self):
        """
        Gets the last_message_received_at of this ExternalAccountAzure.
        ISO 8601 timestamp when the last event was received from Azure. This is updated hourly.

        :return: The last_message_received_at of this ExternalAccountAzure.
        :rtype: datetime
        """
        return self._last_message_received_at

    @last_message_received_at.setter
    def last_message_received_at(self, last_message_received_at):
        """
        Sets the last_message_received_at of this ExternalAccountAzure.
        ISO 8601 timestamp when the last event was received from Azure. This is updated hourly.

        :param last_message_received_at: The last_message_received_at of this ExternalAccountAzure.
        :type: datetime
        """

        self._last_message_received_at = last_message_received_at

    @property
    def app_key(self):
        """
        Gets the app_key of this ExternalAccountAzure.
        Azure app key

        :return: The app_key of this ExternalAccountAzure.
        :rtype: str
        """
        return self._app_key

    @app_key.setter
    def app_key(self, app_key):
        """
        Sets the app_key of this ExternalAccountAzure.
        Azure app key

        :param app_key: The app_key of this ExternalAccountAzure.
        :type: str
        """

        self._app_key = app_key

    @property
    def channel_url(self):
        """
        Gets the channel_url of this ExternalAccountAzure.
        The URL for the azure account channel.  It is only returned when first created or when reset.

        :return: The channel_url of this ExternalAccountAzure.
        :rtype: str
        """
        return self._channel_url

    @channel_url.setter
    def channel_url(self, channel_url):
        """
        Sets the channel_url of this ExternalAccountAzure.
        The URL for the azure account channel.  It is only returned when first created or when reset.

        :param channel_url: The channel_url of this ExternalAccountAzure.
        :type: str
        """

        self._channel_url = channel_url

    @property
    def channel_active(self):
        """
        Gets the channel_active of this ExternalAccountAzure.
        Returns true if the channel is active

        :return: The channel_active of this ExternalAccountAzure.
        :rtype: bool
        """
        return self._channel_active

    @channel_active.setter
    def channel_active(self, channel_active):
        """
        Sets the channel_active of this ExternalAccountAzure.
        Returns true if the channel is active

        :param channel_active: The channel_active of this ExternalAccountAzure.
        :type: bool
        """

        self._channel_active = channel_active

    @property
    def external_account(self):
        """
        Gets the external_account of this ExternalAccountAzure.
        Associated External Account

        :return: The external_account of this ExternalAccountAzure.
        :rtype: ExternalAccount
        """
        return self._external_account

    @external_account.setter
    def external_account(self, external_account):
        """
        Sets the external_account of this ExternalAccountAzure.
        Associated External Account

        :param external_account: The external_account of this ExternalAccountAzure.
        :type: ExternalAccount
        """

        self._external_account = external_account

    @property
    def external_account_id(self):
        """
        Gets the external_account_id of this ExternalAccountAzure.
        Associated External Account ID

        :return: The external_account_id of this ExternalAccountAzure.
        :rtype: int
        """
        return self._external_account_id

    @external_account_id.setter
    def external_account_id(self, external_account_id):
        """
        Sets the external_account_id of this ExternalAccountAzure.
        Associated External Account ID

        :param external_account_id: The external_account_id of this ExternalAccountAzure.
        :type: int
        """

        self._external_account_id = external_account_id

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
        if not isinstance(other, ExternalAccountAzure):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
