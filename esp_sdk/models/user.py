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


class User(BaseObject):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, created_at=None, email=None, time_zone=None, updated_at=None, first_name=None, last_name=None, phone=None, mfa_enabled=None, disable_daily_emails=None, locked=None, locked_at=None, access_level=None, organization=None, organization_id=None, sub_organizations=None, sub_organization_ids=None, teams=None, team_ids=None, role=None, role_id=None):
        """
        User - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'created_at': 'datetime',
            'email': 'str',
            'time_zone': 'str',
            'updated_at': 'datetime',
            'first_name': 'str',
            'last_name': 'str',
            'phone': 'str',
            'mfa_enabled': 'bool',
            'disable_daily_emails': 'bool',
            'locked': 'bool',
            'locked_at': 'datetime',
            'access_level': 'str',
            'organization': 'Organization',
            'organization_id': 'int',
            'sub_organizations': 'list[SubOrganization]',
            'sub_organization_ids': 'list[int]',
            'teams': 'list[Team]',
            'team_ids': 'list[int]',
            'role': 'Role',
            'role_id': 'int'
        }

        self.attribute_map = {
            'id': 'id',
            'created_at': 'created_at',
            'email': 'email',
            'time_zone': 'time_zone',
            'updated_at': 'updated_at',
            'first_name': 'first_name',
            'last_name': 'last_name',
            'phone': 'phone',
            'mfa_enabled': 'mfa_enabled',
            'disable_daily_emails': 'disable_daily_emails',
            'locked': 'locked',
            'locked_at': 'locked_at',
            'access_level': 'access_level',
            'organization': 'organization',
            'organization_id': 'organization_id',
            'sub_organizations': 'sub_organizations',
            'sub_organization_ids': 'sub_organization_ids',
            'teams': 'teams',
            'team_ids': 'team_ids',
            'role': 'role',
            'role_id': 'role_id'
        }

        self._id = id
        self._created_at = created_at
        self._email = email
        self._time_zone = time_zone
        self._updated_at = updated_at
        self._first_name = first_name
        self._last_name = last_name
        self._phone = phone
        self._mfa_enabled = mfa_enabled
        self._disable_daily_emails = disable_daily_emails
        self._locked = locked
        self._locked_at = locked_at
        self._access_level = access_level
        self._organization = organization
        self._organization_id = organization_id
        self._sub_organizations = sub_organizations
        self._sub_organization_ids = sub_organization_ids
        self._teams = teams
        self._team_ids = team_ids
        self._role = role
        self._role_id = role_id

    @property
    def id(self):
        """
        Gets the id of this User.
        Unique ID

        :return: The id of this User.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this User.
        Unique ID

        :param id: The id of this User.
        :type: int
        """

        self._id = id

    @property
    def created_at(self):
        """
        Gets the created_at of this User.
        ISO 8601 timestamp when the resource was created

        :return: The created_at of this User.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this User.
        ISO 8601 timestamp when the resource was created

        :param created_at: The created_at of this User.
        :type: datetime
        """

        self._created_at = created_at

    @property
    def email(self):
        """
        Gets the email of this User.
        The email of the user

        :return: The email of this User.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this User.
        The email of the user

        :param email: The email of this User.
        :type: str
        """

        self._email = email

    @property
    def time_zone(self):
        """
        Gets the time_zone of this User.
        The time zone of the user. See Time Zones for a list of valid time zones

        :return: The time_zone of this User.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """
        Sets the time_zone of this User.
        The time zone of the user. See Time Zones for a list of valid time zones

        :param time_zone: The time_zone of this User.
        :type: str
        """

        self._time_zone = time_zone

    @property
    def updated_at(self):
        """
        Gets the updated_at of this User.
        ISO 8601 timestamp when the resource was updated

        :return: The updated_at of this User.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this User.
        ISO 8601 timestamp when the resource was updated

        :param updated_at: The updated_at of this User.
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def first_name(self):
        """
        Gets the first_name of this User.
        The first name of the user

        :return: The first_name of this User.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """
        Sets the first_name of this User.
        The first name of the user

        :param first_name: The first_name of this User.
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """
        Gets the last_name of this User.
        The last name of the user

        :return: The last_name of this User.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """
        Sets the last_name of this User.
        The last name of the user

        :param last_name: The last_name of this User.
        :type: str
        """

        self._last_name = last_name

    @property
    def phone(self):
        """
        Gets the phone of this User.
        The phone number of the user

        :return: The phone of this User.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """
        Sets the phone of this User.
        The phone number of the user

        :param phone: The phone of this User.
        :type: str
        """

        self._phone = phone

    @property
    def mfa_enabled(self):
        """
        Gets the mfa_enabled of this User.
        Specifies whether Multi Factor Authentication is enabled or not

        :return: The mfa_enabled of this User.
        :rtype: bool
        """
        return self._mfa_enabled

    @mfa_enabled.setter
    def mfa_enabled(self, mfa_enabled):
        """
        Sets the mfa_enabled of this User.
        Specifies whether Multi Factor Authentication is enabled or not

        :param mfa_enabled: The mfa_enabled of this User.
        :type: bool
        """

        self._mfa_enabled = mfa_enabled

    @property
    def disable_daily_emails(self):
        """
        Gets the disable_daily_emails of this User.
        Specifies whether the daily emails should be turned off or not

        :return: The disable_daily_emails of this User.
        :rtype: bool
        """
        return self._disable_daily_emails

    @disable_daily_emails.setter
    def disable_daily_emails(self, disable_daily_emails):
        """
        Sets the disable_daily_emails of this User.
        Specifies whether the daily emails should be turned off or not

        :param disable_daily_emails: The disable_daily_emails of this User.
        :type: bool
        """

        self._disable_daily_emails = disable_daily_emails

    @property
    def locked(self):
        """
        Gets the locked of this User.
        Specifies whether the user account is locked from accessing ESP

        :return: The locked of this User.
        :rtype: bool
        """
        return self._locked

    @locked.setter
    def locked(self, locked):
        """
        Sets the locked of this User.
        Specifies whether the user account is locked from accessing ESP

        :param locked: The locked of this User.
        :type: bool
        """

        self._locked = locked

    @property
    def locked_at(self):
        """
        Gets the locked_at of this User.
        The time the user account was locked

        :return: The locked_at of this User.
        :rtype: datetime
        """
        return self._locked_at

    @locked_at.setter
    def locked_at(self, locked_at):
        """
        Sets the locked_at of this User.
        The time the user account was locked

        :param locked_at: The locked_at of this User.
        :type: datetime
        """

        self._locked_at = locked_at

    @property
    def access_level(self):
        """
        Gets the access_level of this User.
        The level of access this user has. Team access has access to items belonging only to that team. Sub Organization access has access to items belonging only to all teams under that sub organization. Organization access has access to all sub organizations and teams under that organization. Valid values are organization, sub_organization, team

        :return: The access_level of this User.
        :rtype: str
        """
        return self._access_level

    @access_level.setter
    def access_level(self, access_level):
        """
        Sets the access_level of this User.
        The level of access this user has. Team access has access to items belonging only to that team. Sub Organization access has access to items belonging only to all teams under that sub organization. Organization access has access to all sub organizations and teams under that organization. Valid values are organization, sub_organization, team

        :param access_level: The access_level of this User.
        :type: str
        """

        self._access_level = access_level

    @property
    def organization(self):
        """
        Gets the organization of this User.
        Associated Organization

        :return: The organization of this User.
        :rtype: Organization
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """
        Sets the organization of this User.
        Associated Organization

        :param organization: The organization of this User.
        :type: Organization
        """

        self._organization = organization

    @property
    def organization_id(self):
        """
        Gets the organization_id of this User.
        Associated Organization ID

        :return: The organization_id of this User.
        :rtype: int
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """
        Sets the organization_id of this User.
        Associated Organization ID

        :param organization_id: The organization_id of this User.
        :type: int
        """

        self._organization_id = organization_id

    @property
    def sub_organizations(self):
        """
        Gets the sub_organizations of this User.
        Associated Sub Organizations

        :return: The sub_organizations of this User.
        :rtype: list[SubOrganization]
        """
        return self._sub_organizations

    @sub_organizations.setter
    def sub_organizations(self, sub_organizations):
        """
        Sets the sub_organizations of this User.
        Associated Sub Organizations

        :param sub_organizations: The sub_organizations of this User.
        :type: list[SubOrganization]
        """

        self._sub_organizations = sub_organizations

    @property
    def sub_organization_ids(self):
        """
        Gets the sub_organization_ids of this User.
        Associated Sub Organizations IDs

        :return: The sub_organization_ids of this User.
        :rtype: list[int]
        """
        return self._sub_organization_ids

    @sub_organization_ids.setter
    def sub_organization_ids(self, sub_organization_ids):
        """
        Sets the sub_organization_ids of this User.
        Associated Sub Organizations IDs

        :param sub_organization_ids: The sub_organization_ids of this User.
        :type: list[int]
        """

        self._sub_organization_ids = sub_organization_ids

    @property
    def teams(self):
        """
        Gets the teams of this User.
        Associated Teams

        :return: The teams of this User.
        :rtype: list[Team]
        """
        return self._teams

    @teams.setter
    def teams(self, teams):
        """
        Sets the teams of this User.
        Associated Teams

        :param teams: The teams of this User.
        :type: list[Team]
        """

        self._teams = teams

    @property
    def team_ids(self):
        """
        Gets the team_ids of this User.
        Associated Teams IDs

        :return: The team_ids of this User.
        :rtype: list[int]
        """
        return self._team_ids

    @team_ids.setter
    def team_ids(self, team_ids):
        """
        Sets the team_ids of this User.
        Associated Teams IDs

        :param team_ids: The team_ids of this User.
        :type: list[int]
        """

        self._team_ids = team_ids

    @property
    def role(self):
        """
        Gets the role of this User.
        Associated Role

        :return: The role of this User.
        :rtype: Role
        """
        return self._role

    @role.setter
    def role(self, role):
        """
        Sets the role of this User.
        Associated Role

        :param role: The role of this User.
        :type: Role
        """

        self._role = role

    @property
    def role_id(self):
        """
        Gets the role_id of this User.
        Associated Role ID

        :return: The role_id of this User.
        :rtype: int
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        """
        Sets the role_id of this User.
        Associated Role ID

        :param role_id: The role_id of this User.
        :type: int
        """

        self._role_id = role_id

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
        if not isinstance(other, User):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
