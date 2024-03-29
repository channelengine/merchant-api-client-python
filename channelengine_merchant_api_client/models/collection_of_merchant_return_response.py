# coding: utf-8

"""
    ChannelEngine Merchant API

    ChannelEngine API for merchants  # noqa: E501

    The version of the OpenAPI document: 2.9.10
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from channelengine_merchant_api_client.configuration import Configuration


class CollectionOfMerchantReturnResponse(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'content': 'list[MerchantReturnResponse]',
        'count': 'int',
        'total_count': 'int',
        'items_per_page': 'int',
        'status_code': 'int',
        'log_id': 'int',
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
        'log_id': 'LogId',
        'success': 'Success',
        'message': 'Message',
        'validation_errors': 'ValidationErrors'
    }

    def __init__(self, content=None, count=None, total_count=None, items_per_page=None, status_code=None, log_id=None, success=None, message=None, validation_errors=None, local_vars_configuration=None):  # noqa: E501
        """CollectionOfMerchantReturnResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._content = None
        self._count = None
        self._total_count = None
        self._items_per_page = None
        self._status_code = None
        self._log_id = None
        self._success = None
        self._message = None
        self._validation_errors = None
        self.discriminator = None

        self.content = content
        if count is not None:
            self.count = count
        if total_count is not None:
            self.total_count = total_count
        if items_per_page is not None:
            self.items_per_page = items_per_page
        if status_code is not None:
            self.status_code = status_code
        self.log_id = log_id
        if success is not None:
            self.success = success
        self.message = message
        self.validation_errors = validation_errors

    @property
    def content(self):
        """Gets the content of this CollectionOfMerchantReturnResponse.  # noqa: E501


        :return: The content of this CollectionOfMerchantReturnResponse.  # noqa: E501
        :rtype: list[MerchantReturnResponse]
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this CollectionOfMerchantReturnResponse.


        :param content: The content of this CollectionOfMerchantReturnResponse.  # noqa: E501
        :type content: list[MerchantReturnResponse]
        """

        self._content = content

    @property
    def count(self):
        """Gets the count of this CollectionOfMerchantReturnResponse.  # noqa: E501


        :return: The count of this CollectionOfMerchantReturnResponse.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this CollectionOfMerchantReturnResponse.


        :param count: The count of this CollectionOfMerchantReturnResponse.  # noqa: E501
        :type count: int
        """

        self._count = count

    @property
    def total_count(self):
        """Gets the total_count of this CollectionOfMerchantReturnResponse.  # noqa: E501


        :return: The total_count of this CollectionOfMerchantReturnResponse.  # noqa: E501
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this CollectionOfMerchantReturnResponse.


        :param total_count: The total_count of this CollectionOfMerchantReturnResponse.  # noqa: E501
        :type total_count: int
        """

        self._total_count = total_count

    @property
    def items_per_page(self):
        """Gets the items_per_page of this CollectionOfMerchantReturnResponse.  # noqa: E501


        :return: The items_per_page of this CollectionOfMerchantReturnResponse.  # noqa: E501
        :rtype: int
        """
        return self._items_per_page

    @items_per_page.setter
    def items_per_page(self, items_per_page):
        """Sets the items_per_page of this CollectionOfMerchantReturnResponse.


        :param items_per_page: The items_per_page of this CollectionOfMerchantReturnResponse.  # noqa: E501
        :type items_per_page: int
        """

        self._items_per_page = items_per_page

    @property
    def status_code(self):
        """Gets the status_code of this CollectionOfMerchantReturnResponse.  # noqa: E501


        :return: The status_code of this CollectionOfMerchantReturnResponse.  # noqa: E501
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this CollectionOfMerchantReturnResponse.


        :param status_code: The status_code of this CollectionOfMerchantReturnResponse.  # noqa: E501
        :type status_code: int
        """

        self._status_code = status_code

    @property
    def log_id(self):
        """Gets the log_id of this CollectionOfMerchantReturnResponse.  # noqa: E501


        :return: The log_id of this CollectionOfMerchantReturnResponse.  # noqa: E501
        :rtype: int
        """
        return self._log_id

    @log_id.setter
    def log_id(self, log_id):
        """Sets the log_id of this CollectionOfMerchantReturnResponse.


        :param log_id: The log_id of this CollectionOfMerchantReturnResponse.  # noqa: E501
        :type log_id: int
        """

        self._log_id = log_id

    @property
    def success(self):
        """Gets the success of this CollectionOfMerchantReturnResponse.  # noqa: E501


        :return: The success of this CollectionOfMerchantReturnResponse.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this CollectionOfMerchantReturnResponse.


        :param success: The success of this CollectionOfMerchantReturnResponse.  # noqa: E501
        :type success: bool
        """

        self._success = success

    @property
    def message(self):
        """Gets the message of this CollectionOfMerchantReturnResponse.  # noqa: E501


        :return: The message of this CollectionOfMerchantReturnResponse.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this CollectionOfMerchantReturnResponse.


        :param message: The message of this CollectionOfMerchantReturnResponse.  # noqa: E501
        :type message: str
        """

        self._message = message

    @property
    def validation_errors(self):
        """Gets the validation_errors of this CollectionOfMerchantReturnResponse.  # noqa: E501


        :return: The validation_errors of this CollectionOfMerchantReturnResponse.  # noqa: E501
        :rtype: dict(str, list[str])
        """
        return self._validation_errors

    @validation_errors.setter
    def validation_errors(self, validation_errors):
        """Sets the validation_errors of this CollectionOfMerchantReturnResponse.


        :param validation_errors: The validation_errors of this CollectionOfMerchantReturnResponse.  # noqa: E501
        :type validation_errors: dict(str, list[str])
        """

        self._validation_errors = validation_errors

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CollectionOfMerchantReturnResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CollectionOfMerchantReturnResponse):
            return True

        return self.to_dict() != other.to_dict()
