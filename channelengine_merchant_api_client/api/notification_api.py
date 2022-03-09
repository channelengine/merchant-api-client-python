"""
    ChannelEngine Merchant API

    ChannelEngine API for merchants  # noqa: E501

    The version of the OpenAPI document: 2.9.12
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from channelengine_merchant_api_client.api_client import ApiClient, Endpoint as _Endpoint
from channelengine_merchant_api_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from channelengine_merchant_api_client.model.collection_of_merchant_notification_response import CollectionOfMerchantNotificationResponse
from channelengine_merchant_api_client.model.notification_type import NotificationType


class NotificationApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __notification_index(
            self,
            **kwargs
        ):
            """Get Notifications.  # noqa: E501

            Gets all notifications based on filter.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.notification_index(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                from_date (datetime): Filter on the notification date, starting from this date. This date is inclusive.. [optional]
                to_date (datetime): Filter on the notification date, until this date. This date is exclusive.. [optional]
                types ([NotificationType]): Notification type(s) to filter on.. [optional]
                merchant_order_nos ([str]): Filter on unique order reference used by the merchant.. [optional]
                channel_order_nos ([str]): Filter on unique order reference used by the channel.. [optional]
                merchant_return_nos ([str]): Filter on unique return reference used by the merchant.. [optional]
                channel_return_nos ([str]): Filter on unique return reference used by the channel.. [optional]
                merchant_shipment_nos ([str]): Filter on unique shipment reference used by the merchant.. [optional]
                page (int): The page to filter on. Starts at 1.. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                CollectionOfMerchantNotificationResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            return self.call_with_http_info(**kwargs)

        self.notification_index = _Endpoint(
            settings={
                'response_type': (CollectionOfMerchantNotificationResponse,),
                'auth': [
                    'apiKey'
                ],
                'endpoint_path': '/v2/notifications',
                'operation_id': 'notification_index',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'from_date',
                    'to_date',
                    'types',
                    'merchant_order_nos',
                    'channel_order_nos',
                    'merchant_return_nos',
                    'channel_return_nos',
                    'merchant_shipment_nos',
                    'page',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'from_date':
                        (datetime,),
                    'to_date':
                        (datetime,),
                    'types':
                        ([NotificationType],),
                    'merchant_order_nos':
                        ([str],),
                    'channel_order_nos':
                        ([str],),
                    'merchant_return_nos':
                        ([str],),
                    'channel_return_nos':
                        ([str],),
                    'merchant_shipment_nos':
                        ([str],),
                    'page':
                        (int,),
                },
                'attribute_map': {
                    'from_date': 'fromDate',
                    'to_date': 'toDate',
                    'types': 'types',
                    'merchant_order_nos': 'merchantOrderNos',
                    'channel_order_nos': 'channelOrderNos',
                    'merchant_return_nos': 'merchantReturnNos',
                    'channel_return_nos': 'channelReturnNos',
                    'merchant_shipment_nos': 'merchantShipmentNos',
                    'page': 'page',
                },
                'location_map': {
                    'from_date': 'query',
                    'to_date': 'query',
                    'types': 'query',
                    'merchant_order_nos': 'query',
                    'channel_order_nos': 'query',
                    'merchant_return_nos': 'query',
                    'channel_return_nos': 'query',
                    'merchant_shipment_nos': 'query',
                    'page': 'query',
                },
                'collection_format_map': {
                    'types': 'multi',
                    'merchant_order_nos': 'multi',
                    'channel_order_nos': 'multi',
                    'merchant_return_nos': 'multi',
                    'channel_return_nos': 'multi',
                    'merchant_shipment_nos': 'multi',
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__notification_index
        )
