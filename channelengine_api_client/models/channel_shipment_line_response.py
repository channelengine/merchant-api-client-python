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


class ChannelShipmentLineResponse(object):
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
        'channel_product_no': 'str',
        'quantity': 'int'
    }

    attribute_map = {
        'channel_product_no': 'ChannelProductNo',
        'quantity': 'Quantity'
    }

    def __init__(self, channel_product_no=None, quantity=None):
        """
        ChannelShipmentLineResponse - a model defined in Swagger
        """

        self._channel_product_no = None
        self._quantity = None
        self.discriminator = None

        self.channel_product_no = channel_product_no
        self.quantity = quantity

    @property
    def channel_product_no(self):
        """
        Gets the channel_product_no of this ChannelShipmentLineResponse.

        :return: The channel_product_no of this ChannelShipmentLineResponse.
        :rtype: str
        """
        return self._channel_product_no

    @channel_product_no.setter
    def channel_product_no(self, channel_product_no):
        """
        Sets the channel_product_no of this ChannelShipmentLineResponse.

        :param channel_product_no: The channel_product_no of this ChannelShipmentLineResponse.
        :type: str
        """
        if channel_product_no is None:
            raise ValueError("Invalid value for `channel_product_no`, must not be `None`")

        self._channel_product_no = channel_product_no

    @property
    def quantity(self):
        """
        Gets the quantity of this ChannelShipmentLineResponse.

        :return: The quantity of this ChannelShipmentLineResponse.
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """
        Sets the quantity of this ChannelShipmentLineResponse.

        :param quantity: The quantity of this ChannelShipmentLineResponse.
        :type: int
        """
        if quantity is None:
            raise ValueError("Invalid value for `quantity`, must not be `None`")

        self._quantity = quantity

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
        if not isinstance(other, ChannelShipmentLineResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
