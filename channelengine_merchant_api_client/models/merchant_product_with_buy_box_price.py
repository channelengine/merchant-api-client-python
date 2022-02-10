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


class MerchantProductWithBuyBoxPrice(object):
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
        'sku': 'str',
        'gtin': 'str',
        'buy_box_price': 'float',
        'buy_box_price_incl_shipping': 'float',
        'is_merchant_buy_box_winner': 'bool'
    }

    attribute_map = {
        'sku': 'Sku',
        'gtin': 'Gtin',
        'buy_box_price': 'BuyBoxPrice',
        'buy_box_price_incl_shipping': 'BuyBoxPriceInclShipping',
        'is_merchant_buy_box_winner': 'IsMerchantBuyBoxWinner'
    }

    def __init__(self, sku=None, gtin=None, buy_box_price=None, buy_box_price_incl_shipping=None, is_merchant_buy_box_winner=None, local_vars_configuration=None):  # noqa: E501
        """MerchantProductWithBuyBoxPrice - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._sku = None
        self._gtin = None
        self._buy_box_price = None
        self._buy_box_price_incl_shipping = None
        self._is_merchant_buy_box_winner = None
        self.discriminator = None

        self.sku = sku
        self.gtin = gtin
        self.buy_box_price = buy_box_price
        self.buy_box_price_incl_shipping = buy_box_price_incl_shipping
        if is_merchant_buy_box_winner is not None:
            self.is_merchant_buy_box_winner = is_merchant_buy_box_winner

    @property
    def sku(self):
        """Gets the sku of this MerchantProductWithBuyBoxPrice.  # noqa: E501

        Product SKU number  # noqa: E501

        :return: The sku of this MerchantProductWithBuyBoxPrice.  # noqa: E501
        :rtype: str
        """
        return self._sku

    @sku.setter
    def sku(self, sku):
        """Sets the sku of this MerchantProductWithBuyBoxPrice.

        Product SKU number  # noqa: E501

        :param sku: The sku of this MerchantProductWithBuyBoxPrice.  # noqa: E501
        :type sku: str
        """

        self._sku = sku

    @property
    def gtin(self):
        """Gets the gtin of this MerchantProductWithBuyBoxPrice.  # noqa: E501

        Product GTIN  # noqa: E501

        :return: The gtin of this MerchantProductWithBuyBoxPrice.  # noqa: E501
        :rtype: str
        """
        return self._gtin

    @gtin.setter
    def gtin(self, gtin):
        """Sets the gtin of this MerchantProductWithBuyBoxPrice.

        Product GTIN  # noqa: E501

        :param gtin: The gtin of this MerchantProductWithBuyBoxPrice.  # noqa: E501
        :type gtin: str
        """

        self._gtin = gtin

    @property
    def buy_box_price(self):
        """Gets the buy_box_price of this MerchantProductWithBuyBoxPrice.  # noqa: E501

        Price of Buy box winner (excl. shipping cost)  Note: not all channels have a separate shipping cost field (e.g. bol.com), so can be the same as BuyBoxPriceInclShipping  # noqa: E501

        :return: The buy_box_price of this MerchantProductWithBuyBoxPrice.  # noqa: E501
        :rtype: float
        """
        return self._buy_box_price

    @buy_box_price.setter
    def buy_box_price(self, buy_box_price):
        """Sets the buy_box_price of this MerchantProductWithBuyBoxPrice.

        Price of Buy box winner (excl. shipping cost)  Note: not all channels have a separate shipping cost field (e.g. bol.com), so can be the same as BuyBoxPriceInclShipping  # noqa: E501

        :param buy_box_price: The buy_box_price of this MerchantProductWithBuyBoxPrice.  # noqa: E501
        :type buy_box_price: float
        """

        self._buy_box_price = buy_box_price

    @property
    def buy_box_price_incl_shipping(self):
        """Gets the buy_box_price_incl_shipping of this MerchantProductWithBuyBoxPrice.  # noqa: E501

        Price of Buy box winner (incl. shipping cost).  If null, then there is no data or no Buy box winner  # noqa: E501

        :return: The buy_box_price_incl_shipping of this MerchantProductWithBuyBoxPrice.  # noqa: E501
        :rtype: float
        """
        return self._buy_box_price_incl_shipping

    @buy_box_price_incl_shipping.setter
    def buy_box_price_incl_shipping(self, buy_box_price_incl_shipping):
        """Sets the buy_box_price_incl_shipping of this MerchantProductWithBuyBoxPrice.

        Price of Buy box winner (incl. shipping cost).  If null, then there is no data or no Buy box winner  # noqa: E501

        :param buy_box_price_incl_shipping: The buy_box_price_incl_shipping of this MerchantProductWithBuyBoxPrice.  # noqa: E501
        :type buy_box_price_incl_shipping: float
        """

        self._buy_box_price_incl_shipping = buy_box_price_incl_shipping

    @property
    def is_merchant_buy_box_winner(self):
        """Gets the is_merchant_buy_box_winner of this MerchantProductWithBuyBoxPrice.  # noqa: E501

        Are you the Buy box winner or not?  # noqa: E501

        :return: The is_merchant_buy_box_winner of this MerchantProductWithBuyBoxPrice.  # noqa: E501
        :rtype: bool
        """
        return self._is_merchant_buy_box_winner

    @is_merchant_buy_box_winner.setter
    def is_merchant_buy_box_winner(self, is_merchant_buy_box_winner):
        """Sets the is_merchant_buy_box_winner of this MerchantProductWithBuyBoxPrice.

        Are you the Buy box winner or not?  # noqa: E501

        :param is_merchant_buy_box_winner: The is_merchant_buy_box_winner of this MerchantProductWithBuyBoxPrice.  # noqa: E501
        :type is_merchant_buy_box_winner: bool
        """

        self._is_merchant_buy_box_winner = is_merchant_buy_box_winner

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
        if not isinstance(other, MerchantProductWithBuyBoxPrice):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MerchantProductWithBuyBoxPrice):
            return True

        return self.to_dict() != other.to_dict()