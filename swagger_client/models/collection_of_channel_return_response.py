# coding: utf-8

"""
    ChannelEngine API V2

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.4.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class CollectionOfChannelReturnResponse(object):
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
        'content': 'list[ChannelReturnResponse]',
        'count': 'int',
        'total_count': 'int',
        'items_per_page': 'int',
        'status_code': 'int',
        'success': 'bool',
        'message': 'str',
        'validation_errors': 'dict(str, list[str])'
    }

    attribute_map = {
        'content': 'Content',
        'count': 'Count',
        'total_count': 'TotalCount',
        'items_per_page': 'ItemsPerPage',
        'status_code': 'StatusCode',
        'success': 'Success',
        'message': 'Message',
        'validation_errors': 'ValidationErrors'
    }

    def __init__(self, content=None, count=None, total_count=None, items_per_page=None, status_code=None, success=None, message=None, validation_errors=None):
        """
        CollectionOfChannelReturnResponse - a model defined in Swagger
        """

        self._content = None
        self._count = None
        self._total_count = None
        self._items_per_page = None
        self._status_code = None
        self._success = None
        self._message = None
        self._validation_errors = None
        self.discriminator = None

        if content is not None:
          self.content = content
        if count is not None:
          self.count = count
        if total_count is not None:
          self.total_count = total_count
        if items_per_page is not None:
          self.items_per_page = items_per_page
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
        Gets the content of this CollectionOfChannelReturnResponse.

        :return: The content of this CollectionOfChannelReturnResponse.
        :rtype: list[ChannelReturnResponse]
        """
        return self._content

    @content.setter
    def content(self, content):
        """
        Sets the content of this CollectionOfChannelReturnResponse.

        :param content: The content of this CollectionOfChannelReturnResponse.
        :type: list[ChannelReturnResponse]
        """

        self._content = content

    @property
    def count(self):
        """
        Gets the count of this CollectionOfChannelReturnResponse.
        The number of items in the current response

        :return: The count of this CollectionOfChannelReturnResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """
        Sets the count of this CollectionOfChannelReturnResponse.
        The number of items in the current response

        :param count: The count of this CollectionOfChannelReturnResponse.
        :type: int
        """

        self._count = count

    @property
    def total_count(self):
        """
        Gets the total_count of this CollectionOfChannelReturnResponse.
        The total number of items

        :return: The total_count of this CollectionOfChannelReturnResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """
        Sets the total_count of this CollectionOfChannelReturnResponse.
        The total number of items

        :param total_count: The total_count of this CollectionOfChannelReturnResponse.
        :type: int
        """

        self._total_count = total_count

    @property
    def items_per_page(self):
        """
        Gets the items_per_page of this CollectionOfChannelReturnResponse.
        The number of items per page

        :return: The items_per_page of this CollectionOfChannelReturnResponse.
        :rtype: int
        """
        return self._items_per_page

    @items_per_page.setter
    def items_per_page(self, items_per_page):
        """
        Sets the items_per_page of this CollectionOfChannelReturnResponse.
        The number of items per page

        :param items_per_page: The items_per_page of this CollectionOfChannelReturnResponse.
        :type: int
        """

        self._items_per_page = items_per_page

    @property
    def status_code(self):
        """
        Gets the status_code of this CollectionOfChannelReturnResponse.

        :return: The status_code of this CollectionOfChannelReturnResponse.
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """
        Sets the status_code of this CollectionOfChannelReturnResponse.

        :param status_code: The status_code of this CollectionOfChannelReturnResponse.
        :type: int
        """

        self._status_code = status_code

    @property
    def success(self):
        """
        Gets the success of this CollectionOfChannelReturnResponse.

        :return: The success of this CollectionOfChannelReturnResponse.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """
        Sets the success of this CollectionOfChannelReturnResponse.

        :param success: The success of this CollectionOfChannelReturnResponse.
        :type: bool
        """

        self._success = success

    @property
    def message(self):
        """
        Gets the message of this CollectionOfChannelReturnResponse.

        :return: The message of this CollectionOfChannelReturnResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this CollectionOfChannelReturnResponse.

        :param message: The message of this CollectionOfChannelReturnResponse.
        :type: str
        """

        self._message = message

    @property
    def validation_errors(self):
        """
        Gets the validation_errors of this CollectionOfChannelReturnResponse.

        :return: The validation_errors of this CollectionOfChannelReturnResponse.
        :rtype: dict(str, list[str])
        """
        return self._validation_errors

    @validation_errors.setter
    def validation_errors(self, validation_errors):
        """
        Sets the validation_errors of this CollectionOfChannelReturnResponse.

        :param validation_errors: The validation_errors of this CollectionOfChannelReturnResponse.
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
        if not isinstance(other, CollectionOfChannelReturnResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
