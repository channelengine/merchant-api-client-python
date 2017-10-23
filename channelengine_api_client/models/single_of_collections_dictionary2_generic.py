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


class SingleOfCollectionsDictionary2Generic(object):
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
        'content': 'dict(str, list[str])',
        'status_code': 'int',
        'success': 'bool',
        'message': 'str',
        'validation_errors': 'dict(str, list[str])'
    }

    attribute_map = {
        'content': 'Content',
        'status_code': 'StatusCode',
        'success': 'Success',
        'message': 'Message',
        'validation_errors': 'ValidationErrors'
    }

    def __init__(self, content=None, status_code=None, success=None, message=None, validation_errors=None):
        """
        SingleOfCollectionsDictionary2Generic - a model defined in Swagger
        """

        self._content = None
        self._status_code = None
        self._success = None
        self._message = None
        self._validation_errors = None
        self.discriminator = None

        if content is not None:
          self.content = content
        if status_code is not None:
          self.status_code = status_code
        if success is not None:
          self.success = success
        if message is not None:
          self.message = message
        if validation_errors is not None:
          self.validation_errors = validation_errors

    @property
    def content(self):
        """
        Gets the content of this SingleOfCollectionsDictionary2Generic.

        :return: The content of this SingleOfCollectionsDictionary2Generic.
        :rtype: dict(str, list[str])
        """
        return self._content

    @content.setter
    def content(self, content):
        """
        Sets the content of this SingleOfCollectionsDictionary2Generic.

        :param content: The content of this SingleOfCollectionsDictionary2Generic.
        :type: dict(str, list[str])
        """

        self._content = content

    @property
    def status_code(self):
        """
        Gets the status_code of this SingleOfCollectionsDictionary2Generic.

        :return: The status_code of this SingleOfCollectionsDictionary2Generic.
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """
        Sets the status_code of this SingleOfCollectionsDictionary2Generic.

        :param status_code: The status_code of this SingleOfCollectionsDictionary2Generic.
        :type: int
        """

        self._status_code = status_code

    @property
    def success(self):
        """
        Gets the success of this SingleOfCollectionsDictionary2Generic.

        :return: The success of this SingleOfCollectionsDictionary2Generic.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """
        Sets the success of this SingleOfCollectionsDictionary2Generic.

        :param success: The success of this SingleOfCollectionsDictionary2Generic.
        :type: bool
        """

        self._success = success

    @property
    def message(self):
        """
        Gets the message of this SingleOfCollectionsDictionary2Generic.

        :return: The message of this SingleOfCollectionsDictionary2Generic.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this SingleOfCollectionsDictionary2Generic.

        :param message: The message of this SingleOfCollectionsDictionary2Generic.
        :type: str
        """

        self._message = message

    @property
    def validation_errors(self):
        """
        Gets the validation_errors of this SingleOfCollectionsDictionary2Generic.

        :return: The validation_errors of this SingleOfCollectionsDictionary2Generic.
        :rtype: dict(str, list[str])
        """
        return self._validation_errors

    @validation_errors.setter
    def validation_errors(self, validation_errors):
        """
        Sets the validation_errors of this SingleOfCollectionsDictionary2Generic.

        :param validation_errors: The validation_errors of this SingleOfCollectionsDictionary2Generic.
        :type: dict(str, list[str])
        """

        self._validation_errors = validation_errors

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
        if not isinstance(other, SingleOfCollectionsDictionary2Generic):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
