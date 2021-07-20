"""
    ChannelEngine Merchant API

    ChannelEngine API for merchants  # noqa: E501

    The version of the OpenAPI document: 2.9.8
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
from channelengine_merchant_api_client.model.api_response import ApiResponse
from channelengine_merchant_api_client.model.collection_of_merchant_order_response import CollectionOfMerchantOrderResponse
from channelengine_merchant_api_client.model.fulfillment_type import FulfillmentType
from channelengine_merchant_api_client.model.merchant_order_acknowledgement_request import MerchantOrderAcknowledgementRequest
from channelengine_merchant_api_client.model.merchant_order_comment_update_request import MerchantOrderCommentUpdateRequest
from channelengine_merchant_api_client.model.order_status_view import OrderStatusView


class OrderApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __order_acknowledge(
            self,
            **kwargs
        ):
            """Acknowledge Order.  # noqa: E501

            Acknowledge an order. By acknowledging the order the merchant can confirm that<br />the order has been imported. When acknowledging an order the merchant has to supply<br />references that uniquely identify the order and the order lines. These references<br />will be used in the other API calls.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.order_acknowledge(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                merchant_order_acknowledgement_request (MerchantOrderAcknowledgementRequest): Relations between the id's returned by ChannelEngine and the references which the merchant uses.. [optional]
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
                ApiResponse
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

        self.order_acknowledge = _Endpoint(
            settings={
                'response_type': (ApiResponse,),
                'auth': [
                    'apiKey'
                ],
                'endpoint_path': '/v2/orders/acknowledge',
                'operation_id': 'order_acknowledge',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'merchant_order_acknowledgement_request',
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
                    'merchant_order_acknowledgement_request':
                        (MerchantOrderAcknowledgementRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'merchant_order_acknowledgement_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json-patch+json',
                    'application/json',
                    'application/*+json'
                ]
            },
            api_client=api_client,
            callable=__order_acknowledge
        )

        def __order_get_by_filter(
            self,
            **kwargs
        ):
            """Get Orders By Filter.  # noqa: E501

            Fetch orders based on the provided OrderFilter.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.order_get_by_filter(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                statuses ([OrderStatusView], none_type): Order status(es) to filter on. AWAITING_PAYMENT orders will be excluded if it is not included in this Statuses filter.. [optional]
                email_addresses ([str], none_type): Client emailaddresses to filter on.. [optional]
                merchant_order_nos ([str], none_type): Filter on unique order reference used by the merchant.. [optional]
                channel_order_nos ([str], none_type): Filter on unique order reference used by the channel.. [optional]
                from_date (datetime, none_type): Filter on the order date, starting from this date. This date is inclusive.<br />The order date is based on the data we got from a channel.. [optional]
                to_date (datetime, none_type): Filter on the order date, until this date. This date is exclusive.<br />The order date is based on the data we got from a channel.. [optional]
                from_created_at_date (datetime, none_type): Filter on the created at date in ChannelEngine, starting from this date. This date is inclusive.<br />The created date is set on the date and time when the order is created.. [optional]
                exclude_marketplace_fulfilled_orders_and_lines (bool): Exclude order (lines) fulfilled by the marketplace (amazon:FBA, bol:LVB, etc.). [optional]
                fulfillment_type (FulfillmentType): Filter orders on fulfillment type. This will include all orders lines, even if they are partially fulfilled by the marketplace.<br />To exclude orders and lines that are fulfilled by the marketplace from the response, set ExcludeMarketplaceFulfilledOrdersAndLines to true.. [optional]
                only_with_cancellation_requests (bool): Filter on orders containing cancellation requests.<br />Some channels allow a customer to cancel an order until it has been shipped.<br />When an order has already been acknowledged in ChannelEngine, it can only be cancelled by creating a cancellation.. [optional]
                page (int, none_type): The page to filter on. Starts at 1.. [optional]
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
                CollectionOfMerchantOrderResponse
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

        self.order_get_by_filter = _Endpoint(
            settings={
                'response_type': (CollectionOfMerchantOrderResponse,),
                'auth': [
                    'apiKey'
                ],
                'endpoint_path': '/v2/orders',
                'operation_id': 'order_get_by_filter',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'statuses',
                    'email_addresses',
                    'merchant_order_nos',
                    'channel_order_nos',
                    'from_date',
                    'to_date',
                    'from_created_at_date',
                    'exclude_marketplace_fulfilled_orders_and_lines',
                    'fulfillment_type',
                    'only_with_cancellation_requests',
                    'page',
                ],
                'required': [],
                'nullable': [
                    'statuses',
                    'email_addresses',
                    'merchant_order_nos',
                    'channel_order_nos',
                    'from_date',
                    'to_date',
                    'from_created_at_date',
                    'page',
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
                    'statuses':
                        ([OrderStatusView], none_type,),
                    'email_addresses':
                        ([str], none_type,),
                    'merchant_order_nos':
                        ([str], none_type,),
                    'channel_order_nos':
                        ([str], none_type,),
                    'from_date':
                        (datetime, none_type,),
                    'to_date':
                        (datetime, none_type,),
                    'from_created_at_date':
                        (datetime, none_type,),
                    'exclude_marketplace_fulfilled_orders_and_lines':
                        (bool,),
                    'fulfillment_type':
                        (FulfillmentType,),
                    'only_with_cancellation_requests':
                        (bool,),
                    'page':
                        (int, none_type,),
                },
                'attribute_map': {
                    'statuses': 'statuses',
                    'email_addresses': 'emailAddresses',
                    'merchant_order_nos': 'merchantOrderNos',
                    'channel_order_nos': 'channelOrderNos',
                    'from_date': 'fromDate',
                    'to_date': 'toDate',
                    'from_created_at_date': 'fromCreatedAtDate',
                    'exclude_marketplace_fulfilled_orders_and_lines': 'excludeMarketplaceFulfilledOrdersAndLines',
                    'fulfillment_type': 'fulfillmentType',
                    'only_with_cancellation_requests': 'onlyWithCancellationRequests',
                    'page': 'page',
                },
                'location_map': {
                    'statuses': 'query',
                    'email_addresses': 'query',
                    'merchant_order_nos': 'query',
                    'channel_order_nos': 'query',
                    'from_date': 'query',
                    'to_date': 'query',
                    'from_created_at_date': 'query',
                    'exclude_marketplace_fulfilled_orders_and_lines': 'query',
                    'fulfillment_type': 'query',
                    'only_with_cancellation_requests': 'query',
                    'page': 'query',
                },
                'collection_format_map': {
                    'statuses': 'multi',
                    'email_addresses': 'multi',
                    'merchant_order_nos': 'multi',
                    'channel_order_nos': 'multi',
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__order_get_by_filter
        )

        def __order_get_new(
            self,
            **kwargs
        ):
            """Get New Orders.  # noqa: E501

            Fetch newly placed orders (order with status NEW).  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.order_get_new(async_req=True)
            >>> result = thread.get()


            Keyword Args:
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
                CollectionOfMerchantOrderResponse
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

        self.order_get_new = _Endpoint(
            settings={
                'response_type': (CollectionOfMerchantOrderResponse,),
                'auth': [
                    'apiKey'
                ],
                'endpoint_path': '/v2/orders/new',
                'operation_id': 'order_get_new',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
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
                },
                'attribute_map': {
                },
                'location_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__order_get_new
        )

        def __order_invoice(
            self,
            merchant_order_no,
            **kwargs
        ):
            """Download Invoice.  # noqa: E501

            Generates the ChannelEngine VAT invoice for this order in PDF.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.order_invoice(merchant_order_no, async_req=True)
            >>> result = thread.get()

            Args:
                merchant_order_no (str, none_type): The unique order reference as used by the merchant.

            Keyword Args:
                use_customer_culture (bool): Generate the invoice in the billing address' country's language.. [optional] if omitted the server will use the default value of False
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
                file
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
            kwargs['merchant_order_no'] = \
                merchant_order_no
            return self.call_with_http_info(**kwargs)

        self.order_invoice = _Endpoint(
            settings={
                'response_type': (file,),
                'auth': [
                    'apiKey'
                ],
                'endpoint_path': '/v2/orders/{merchantOrderNo}/invoice',
                'operation_id': 'order_invoice',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'merchant_order_no',
                    'use_customer_culture',
                ],
                'required': [
                    'merchant_order_no',
                ],
                'nullable': [
                    'merchant_order_no',
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
                    'merchant_order_no':
                        (str, none_type,),
                    'use_customer_culture':
                        (bool,),
                },
                'attribute_map': {
                    'merchant_order_no': 'merchantOrderNo',
                    'use_customer_culture': 'useCustomerCulture',
                },
                'location_map': {
                    'merchant_order_no': 'path',
                    'use_customer_culture': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/pdf',
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__order_invoice
        )

        def __order_packing_slip(
            self,
            merchant_order_no,
            **kwargs
        ):
            """Download Packing Slip.  # noqa: E501

            Generates the ChannelEngine packing slip for this order in PDF.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.order_packing_slip(merchant_order_no, async_req=True)
            >>> result = thread.get()

            Args:
                merchant_order_no (str, none_type): The unique order reference as used by the merchant.

            Keyword Args:
                use_customer_culture (bool): Generate the invoice in the billing address' country's language.. [optional] if omitted the server will use the default value of False
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
                file
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
            kwargs['merchant_order_no'] = \
                merchant_order_no
            return self.call_with_http_info(**kwargs)

        self.order_packing_slip = _Endpoint(
            settings={
                'response_type': (file,),
                'auth': [
                    'apiKey'
                ],
                'endpoint_path': '/v2/orders/{merchantOrderNo}/packingslip',
                'operation_id': 'order_packing_slip',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'merchant_order_no',
                    'use_customer_culture',
                ],
                'required': [
                    'merchant_order_no',
                ],
                'nullable': [
                    'merchant_order_no',
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
                    'merchant_order_no':
                        (str, none_type,),
                    'use_customer_culture':
                        (bool,),
                },
                'attribute_map': {
                    'merchant_order_no': 'merchantOrderNo',
                    'use_customer_culture': 'useCustomerCulture',
                },
                'location_map': {
                    'merchant_order_no': 'path',
                    'use_customer_culture': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/pdf',
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__order_packing_slip
        )

        def __order_update(
            self,
            **kwargs
        ):
            """Update Comment.  # noqa: E501

            Update the merchant comment for an order. Both the ChannelEngine order id as the<br />merchant order number can be used for updating a comment.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.order_update(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                merchant_order_comment_update_request (MerchantOrderCommentUpdateRequest): [optional]
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
                ApiResponse
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

        self.order_update = _Endpoint(
            settings={
                'response_type': (ApiResponse,),
                'auth': [
                    'apiKey'
                ],
                'endpoint_path': '/v2/orders/comment',
                'operation_id': 'order_update',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'merchant_order_comment_update_request',
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
                    'merchant_order_comment_update_request':
                        (MerchantOrderCommentUpdateRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'merchant_order_comment_update_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json-patch+json',
                    'application/json',
                    'application/*+json'
                ]
            },
            api_client=api_client,
            callable=__order_update
        )
