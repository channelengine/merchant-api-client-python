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


class MerchantShipmentTrackingRequest(object):
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
        'method': 'str',
        'track_trace_no': 'str',
        'track_trace_url': 'str'
    }

    attribute_map = {
        'method': 'Method',
        'track_trace_no': 'TrackTraceNo',
        'track_trace_url': 'TrackTraceUrl'
    }

    def __init__(self, method=None, track_trace_no=None, track_trace_url=None):
        """
        MerchantShipmentTrackingRequest - a model defined in Swagger
        """

        self._method = None
        self._track_trace_no = None
        self._track_trace_url = None
        self.discriminator = None

        self.method = method
        self.track_trace_no = track_trace_no
        if track_trace_url is not None:
          self.track_trace_url = track_trace_url

    @property
    def method(self):
        """
        Gets the method of this MerchantShipmentTrackingRequest.

        :return: The method of this MerchantShipmentTrackingRequest.
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """
        Sets the method of this MerchantShipmentTrackingRequest.

        :param method: The method of this MerchantShipmentTrackingRequest.
        :type: str
        """
        if method is None:
            raise ValueError("Invalid value for `method`, must not be `None`")
        if method is not None and len(method) > 50:
            raise ValueError("Invalid value for `method`, length must be less than or equal to `50`")
        if method is not None and len(method) < 0:
            raise ValueError("Invalid value for `method`, length must be greater than or equal to `0`")

        self._method = method

    @property
    def track_trace_no(self):
        """
        Gets the track_trace_no of this MerchantShipmentTrackingRequest.

        :return: The track_trace_no of this MerchantShipmentTrackingRequest.
        :rtype: str
        """
        return self._track_trace_no

    @track_trace_no.setter
    def track_trace_no(self, track_trace_no):
        """
        Sets the track_trace_no of this MerchantShipmentTrackingRequest.

        :param track_trace_no: The track_trace_no of this MerchantShipmentTrackingRequest.
        :type: str
        """
        if track_trace_no is None:
            raise ValueError("Invalid value for `track_trace_no`, must not be `None`")
        if track_trace_no is not None and len(track_trace_no) > 50:
            raise ValueError("Invalid value for `track_trace_no`, length must be less than or equal to `50`")
        if track_trace_no is not None and len(track_trace_no) < 0:
            raise ValueError("Invalid value for `track_trace_no`, length must be greater than or equal to `0`")

        self._track_trace_no = track_trace_no

    @property
    def track_trace_url(self):
        """
        Gets the track_trace_url of this MerchantShipmentTrackingRequest.

        :return: The track_trace_url of this MerchantShipmentTrackingRequest.
        :rtype: str
        """
        return self._track_trace_url

    @track_trace_url.setter
    def track_trace_url(self, track_trace_url):
        """
        Sets the track_trace_url of this MerchantShipmentTrackingRequest.

        :param track_trace_url: The track_trace_url of this MerchantShipmentTrackingRequest.
        :type: str
        """
        if track_trace_url is not None and len(track_trace_url) > 250:
            raise ValueError("Invalid value for `track_trace_url`, length must be less than or equal to `250`")
        if track_trace_url is not None and len(track_trace_url) < 0:
            raise ValueError("Invalid value for `track_trace_url`, length must be greater than or equal to `0`")

        self._track_trace_url = track_trace_url

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
        if not isinstance(other, MerchantShipmentTrackingRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
