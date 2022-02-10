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


class ReturnReason(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    PRODUCT_DEFECT = "PRODUCT_DEFECT"
    PRODUCT_UNSATISFACTORY = "PRODUCT_UNSATISFACTORY"
    WRONG_PRODUCT = "WRONG_PRODUCT"
    TOO_MANY_PRODUCTS = "TOO_MANY_PRODUCTS"
    REFUSED = "REFUSED"
    REFUSED_DAMAGED = "REFUSED_DAMAGED"
    WRONG_ADDRESS = "WRONG_ADDRESS"
    NOT_COLLECTED = "NOT_COLLECTED"
    WRONG_SIZE = "WRONG_SIZE"
    OTHER = "OTHER"

    allowable_values = [PRODUCT_DEFECT, PRODUCT_UNSATISFACTORY, WRONG_PRODUCT, TOO_MANY_PRODUCTS, REFUSED, REFUSED_DAMAGED, WRONG_ADDRESS, NOT_COLLECTED, WRONG_SIZE, OTHER]  # noqa: E501

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
    }

    attribute_map = {
    }

    def __init__(self, local_vars_configuration=None):  # noqa: E501
        """ReturnReason - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self.discriminator = None

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
        if not isinstance(other, ReturnReason):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReturnReason):
            return True

        return self.to_dict() != other.to_dict()