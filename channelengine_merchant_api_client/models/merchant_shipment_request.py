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


class MerchantShipmentRequest(object):
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
        'merchant_shipment_no': 'str',
        'merchant_order_no': 'str',
        'lines': 'list[MerchantShipmentLineRequest]',
        'extra_data': 'dict(str, str)',
        'track_trace_no': 'str',
        'track_trace_url': 'str',
        'return_track_trace_no': 'str',
        'method': 'str',
        'shipped_from_country_code': 'str'
    }

    attribute_map = {
        'merchant_shipment_no': 'MerchantShipmentNo',
        'merchant_order_no': 'MerchantOrderNo',
        'lines': 'Lines',
        'extra_data': 'ExtraData',
        'track_trace_no': 'TrackTraceNo',
        'track_trace_url': 'TrackTraceUrl',
        'return_track_trace_no': 'ReturnTrackTraceNo',
        'method': 'Method',
        'shipped_from_country_code': 'ShippedFromCountryCode'
    }

    def __init__(self, merchant_shipment_no=None, merchant_order_no=None, lines=None, extra_data=None, track_trace_no=None, track_trace_url=None, return_track_trace_no=None, method=None, shipped_from_country_code=None, local_vars_configuration=None):  # noqa: E501
        """MerchantShipmentRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._merchant_shipment_no = None
        self._merchant_order_no = None
        self._lines = None
        self._extra_data = None
        self._track_trace_no = None
        self._track_trace_url = None
        self._return_track_trace_no = None
        self._method = None
        self._shipped_from_country_code = None
        self.discriminator = None

        self.merchant_shipment_no = merchant_shipment_no
        self.merchant_order_no = merchant_order_no
        self.lines = lines
        self.extra_data = extra_data
        self.track_trace_no = track_trace_no
        self.track_trace_url = track_trace_url
        self.return_track_trace_no = return_track_trace_no
        self.method = method
        self.shipped_from_country_code = shipped_from_country_code

    @property
    def merchant_shipment_no(self):
        """Gets the merchant_shipment_no of this MerchantShipmentRequest.  # noqa: E501

        The unique shipment reference used by the Merchant.  # noqa: E501

        :return: The merchant_shipment_no of this MerchantShipmentRequest.  # noqa: E501
        :rtype: str
        """
        return self._merchant_shipment_no

    @merchant_shipment_no.setter
    def merchant_shipment_no(self, merchant_shipment_no):
        """Sets the merchant_shipment_no of this MerchantShipmentRequest.

        The unique shipment reference used by the Merchant.  # noqa: E501

        :param merchant_shipment_no: The merchant_shipment_no of this MerchantShipmentRequest.  # noqa: E501
        :type merchant_shipment_no: str
        """
        if self.local_vars_configuration.client_side_validation and merchant_shipment_no is None:  # noqa: E501
            raise ValueError("Invalid value for `merchant_shipment_no`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                merchant_shipment_no is not None and len(merchant_shipment_no) > 250):
            raise ValueError("Invalid value for `merchant_shipment_no`, length must be less than or equal to `250`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                merchant_shipment_no is not None and len(merchant_shipment_no) < 0):
            raise ValueError("Invalid value for `merchant_shipment_no`, length must be greater than or equal to `0`")  # noqa: E501

        self._merchant_shipment_no = merchant_shipment_no

    @property
    def merchant_order_no(self):
        """Gets the merchant_order_no of this MerchantShipmentRequest.  # noqa: E501

        The unique order reference used by the Merchant.  # noqa: E501

        :return: The merchant_order_no of this MerchantShipmentRequest.  # noqa: E501
        :rtype: str
        """
        return self._merchant_order_no

    @merchant_order_no.setter
    def merchant_order_no(self, merchant_order_no):
        """Sets the merchant_order_no of this MerchantShipmentRequest.

        The unique order reference used by the Merchant.  # noqa: E501

        :param merchant_order_no: The merchant_order_no of this MerchantShipmentRequest.  # noqa: E501
        :type merchant_order_no: str
        """
        if self.local_vars_configuration.client_side_validation and merchant_order_no is None:  # noqa: E501
            raise ValueError("Invalid value for `merchant_order_no`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                merchant_order_no is not None and len(merchant_order_no) > 50):
            raise ValueError("Invalid value for `merchant_order_no`, length must be less than or equal to `50`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                merchant_order_no is not None and len(merchant_order_no) < 0):
            raise ValueError("Invalid value for `merchant_order_no`, length must be greater than or equal to `0`")  # noqa: E501

        self._merchant_order_no = merchant_order_no

    @property
    def lines(self):
        """Gets the lines of this MerchantShipmentRequest.  # noqa: E501


        :return: The lines of this MerchantShipmentRequest.  # noqa: E501
        :rtype: list[MerchantShipmentLineRequest]
        """
        return self._lines

    @lines.setter
    def lines(self, lines):
        """Sets the lines of this MerchantShipmentRequest.


        :param lines: The lines of this MerchantShipmentRequest.  # noqa: E501
        :type lines: list[MerchantShipmentLineRequest]
        """
        if self.local_vars_configuration.client_side_validation and lines is None:  # noqa: E501
            raise ValueError("Invalid value for `lines`, must not be `None`")  # noqa: E501

        self._lines = lines

    @property
    def extra_data(self):
        """Gets the extra_data of this MerchantShipmentRequest.  # noqa: E501

        Extra data on the order. Each item must have an unqiue key  # noqa: E501

        :return: The extra_data of this MerchantShipmentRequest.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._extra_data

    @extra_data.setter
    def extra_data(self, extra_data):
        """Sets the extra_data of this MerchantShipmentRequest.

        Extra data on the order. Each item must have an unqiue key  # noqa: E501

        :param extra_data: The extra_data of this MerchantShipmentRequest.  # noqa: E501
        :type extra_data: dict(str, str)
        """

        self._extra_data = extra_data

    @property
    def track_trace_no(self):
        """Gets the track_trace_no of this MerchantShipmentRequest.  # noqa: E501

        The unique shipping reference used by the Shipping carrier (track&trace number).  # noqa: E501

        :return: The track_trace_no of this MerchantShipmentRequest.  # noqa: E501
        :rtype: str
        """
        return self._track_trace_no

    @track_trace_no.setter
    def track_trace_no(self, track_trace_no):
        """Sets the track_trace_no of this MerchantShipmentRequest.

        The unique shipping reference used by the Shipping carrier (track&trace number).  # noqa: E501

        :param track_trace_no: The track_trace_no of this MerchantShipmentRequest.  # noqa: E501
        :type track_trace_no: str
        """
        if (self.local_vars_configuration.client_side_validation and
                track_trace_no is not None and len(track_trace_no) > 50):
            raise ValueError("Invalid value for `track_trace_no`, length must be less than or equal to `50`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                track_trace_no is not None and len(track_trace_no) < 0):
            raise ValueError("Invalid value for `track_trace_no`, length must be greater than or equal to `0`")  # noqa: E501

        self._track_trace_no = track_trace_no

    @property
    def track_trace_url(self):
        """Gets the track_trace_url of this MerchantShipmentRequest.  # noqa: E501

        A link to a page of the carrier where the customer can track the shipping of her package.  # noqa: E501

        :return: The track_trace_url of this MerchantShipmentRequest.  # noqa: E501
        :rtype: str
        """
        return self._track_trace_url

    @track_trace_url.setter
    def track_trace_url(self, track_trace_url):
        """Sets the track_trace_url of this MerchantShipmentRequest.

        A link to a page of the carrier where the customer can track the shipping of her package.  # noqa: E501

        :param track_trace_url: The track_trace_url of this MerchantShipmentRequest.  # noqa: E501
        :type track_trace_url: str
        """
        if (self.local_vars_configuration.client_side_validation and
                track_trace_url is not None and len(track_trace_url) > 250):
            raise ValueError("Invalid value for `track_trace_url`, length must be less than or equal to `250`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                track_trace_url is not None and len(track_trace_url) < 0):
            raise ValueError("Invalid value for `track_trace_url`, length must be greater than or equal to `0`")  # noqa: E501

        self._track_trace_url = track_trace_url

    @property
    def return_track_trace_no(self):
        """Gets the return_track_trace_no of this MerchantShipmentRequest.  # noqa: E501

        The unique return shipping reference that may be used by the Shipping carrier (track & trace number) if the shipment is returned.  # noqa: E501

        :return: The return_track_trace_no of this MerchantShipmentRequest.  # noqa: E501
        :rtype: str
        """
        return self._return_track_trace_no

    @return_track_trace_no.setter
    def return_track_trace_no(self, return_track_trace_no):
        """Sets the return_track_trace_no of this MerchantShipmentRequest.

        The unique return shipping reference that may be used by the Shipping carrier (track & trace number) if the shipment is returned.  # noqa: E501

        :param return_track_trace_no: The return_track_trace_no of this MerchantShipmentRequest.  # noqa: E501
        :type return_track_trace_no: str
        """
        if (self.local_vars_configuration.client_side_validation and
                return_track_trace_no is not None and len(return_track_trace_no) > 50):
            raise ValueError("Invalid value for `return_track_trace_no`, length must be less than or equal to `50`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                return_track_trace_no is not None and len(return_track_trace_no) < 0):
            raise ValueError("Invalid value for `return_track_trace_no`, length must be greater than or equal to `0`")  # noqa: E501

        self._return_track_trace_no = return_track_trace_no

    @property
    def method(self):
        """Gets the method of this MerchantShipmentRequest.  # noqa: E501

        Shipment method: the carrier used for shipping the package. E.g. DHL, postNL.  # noqa: E501

        :return: The method of this MerchantShipmentRequest.  # noqa: E501
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this MerchantShipmentRequest.

        Shipment method: the carrier used for shipping the package. E.g. DHL, postNL.  # noqa: E501

        :param method: The method of this MerchantShipmentRequest.  # noqa: E501
        :type method: str
        """
        if (self.local_vars_configuration.client_side_validation and
                method is not None and len(method) > 50):
            raise ValueError("Invalid value for `method`, length must be less than or equal to `50`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                method is not None and len(method) < 0):
            raise ValueError("Invalid value for `method`, length must be greater than or equal to `0`")  # noqa: E501

        self._method = method

    @property
    def shipped_from_country_code(self):
        """Gets the shipped_from_country_code of this MerchantShipmentRequest.  # noqa: E501

        The code of the country from where the package is being shipped.  # noqa: E501

        :return: The shipped_from_country_code of this MerchantShipmentRequest.  # noqa: E501
        :rtype: str
        """
        return self._shipped_from_country_code

    @shipped_from_country_code.setter
    def shipped_from_country_code(self, shipped_from_country_code):
        """Sets the shipped_from_country_code of this MerchantShipmentRequest.

        The code of the country from where the package is being shipped.  # noqa: E501

        :param shipped_from_country_code: The shipped_from_country_code of this MerchantShipmentRequest.  # noqa: E501
        :type shipped_from_country_code: str
        """
        if (self.local_vars_configuration.client_side_validation and
                shipped_from_country_code is not None and len(shipped_from_country_code) > 3):
            raise ValueError("Invalid value for `shipped_from_country_code`, length must be less than or equal to `3`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                shipped_from_country_code is not None and len(shipped_from_country_code) < 0):
            raise ValueError("Invalid value for `shipped_from_country_code`, length must be greater than or equal to `0`")  # noqa: E501

        self._shipped_from_country_code = shipped_from_country_code

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
        if not isinstance(other, MerchantShipmentRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MerchantShipmentRequest):
            return True

        return self.to_dict() != other.to_dict()
