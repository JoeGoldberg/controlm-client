# coding: utf-8

"""
    Control-M Services

    Provides access to BMC Control-M Services  # noqa: E501

    OpenAPI spec version: 9.18.3
    Contact: support@bmc.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class LoginResult(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'username': 'str',
        'token': 'str',
        'version': 'str'
    }

    attribute_map = {
        'username': 'username',
        'token': 'token',
        'version': 'version'
    }

    def __init__(self, username=None, token=None, version=None):  # noqa: E501
        """LoginResult - a model defined in Swagger"""  # noqa: E501

        self._username = None
        self._token = None
        self._version = None
        self.discriminator = None

        if username is not None:
            self.username = username
        if token is not None:
            self.token = token
        if version is not None:
            self.version = version

    @property
    def username(self):
        """Gets the username of this LoginResult.  # noqa: E501


        :return: The username of this LoginResult.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this LoginResult.


        :param username: The username of this LoginResult.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def token(self):
        """Gets the token of this LoginResult.  # noqa: E501


        :return: The token of this LoginResult.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this LoginResult.


        :param token: The token of this LoginResult.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def version(self):
        """Gets the version of this LoginResult.  # noqa: E501


        :return: The version of this LoginResult.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this LoginResult.


        :param version: The version of this LoginResult.  # noqa: E501
        :type: str
        """

        self._version = version

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(LoginResult, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, LoginResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
