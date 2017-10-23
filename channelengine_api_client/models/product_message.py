# coding: utf-8

"""
    ChannelEngine API V2

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.4.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ProductMessage(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'name': 'str',
        'reference': 'str',
        'warnings': 'list[str]',
        'errors': 'list[str]'
    }

    attribute_map = {
        'name': 'Name',
        'reference': 'Reference',
        'warnings': 'Warnings',
        'errors': 'Errors'
    }

    def __init__(self, name=None, reference=None, warnings=None, errors=None):
        """
        ProductMessage - a model defined in Swagger
        """

        self._name = None
        self._reference = None
        self._warnings = None
        self._errors = None
        self.discriminator = None

        if name is not None:
          self.name = name
        if reference is not None:
          self.reference = reference
        if warnings is not None:
          self.warnings = warnings
        if errors is not None:
          self.errors = errors

    @property
    def name(self):
        """
        Gets the name of this ProductMessage.

        :return: The name of this ProductMessage.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ProductMessage.

        :param name: The name of this ProductMessage.
        :type: str
        """

        self._name = name

    @property
    def reference(self):
        """
        Gets the reference of this ProductMessage.

        :return: The reference of this ProductMessage.
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """
        Sets the reference of this ProductMessage.

        :param reference: The reference of this ProductMessage.
        :type: str
        """

        self._reference = reference

    @property
    def warnings(self):
        """
        Gets the warnings of this ProductMessage.

        :return: The warnings of this ProductMessage.
        :rtype: list[str]
        """
        return self._warnings

    @warnings.setter
    def warnings(self, warnings):
        """
        Sets the warnings of this ProductMessage.

        :param warnings: The warnings of this ProductMessage.
        :type: list[str]
        """

        self._warnings = warnings

    @property
    def errors(self):
        """
        Gets the errors of this ProductMessage.

        :return: The errors of this ProductMessage.
        :rtype: list[str]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """
        Sets the errors of this ProductMessage.

        :param errors: The errors of this ProductMessage.
        :type: list[str]
        """

        self._errors = errors

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
        if not isinstance(other, ProductMessage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
