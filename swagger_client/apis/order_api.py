# coding: utf-8

"""
    ChannelEngine API V2

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.4.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..api_client import ApiClient


class OrderApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def order_acknowledge(self, model, **kwargs):
        """
        Merchant: Acknowledge Order
        For merchants.    Acknowledge an order. By acknowledging the order the merchant can confirm that  the order has been imported. When acknowledging an order the merchant has to supply  references that uniquely identify the order and the order lines. These references  will be used in the other API calls.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.order_acknowledge(model, async=True)
        >>> result = thread.get()

        :param async bool
        :param OrderAcknowledgement model: Relations between the id's returned by ChannelEngine and the references which the merchant uses (required)
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.order_acknowledge_with_http_info(model, **kwargs)
        else:
            (data) = self.order_acknowledge_with_http_info(model, **kwargs)
            return data

    def order_acknowledge_with_http_info(self, model, **kwargs):
        """
        Merchant: Acknowledge Order
        For merchants.    Acknowledge an order. By acknowledging the order the merchant can confirm that  the order has been imported. When acknowledging an order the merchant has to supply  references that uniquely identify the order and the order lines. These references  will be used in the other API calls.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.order_acknowledge_with_http_info(model, async=True)
        >>> result = thread.get()

        :param async bool
        :param OrderAcknowledgement model: Relations between the id's returned by ChannelEngine and the references which the merchant uses (required)
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['model']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method order_acknowledge" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'model' is set
        if ('model' not in params) or (params['model'] is None):
            raise ValueError("Missing the required parameter `model` when calling `order_acknowledge`")


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'model' in params:
            body_params = params['model']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'text/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json', 'text/json', 'application/xml', 'text/xml', 'application/x-www-form-urlencoded'])

        # Authentication setting
        auth_settings = ['apikey']

        return self.api_client.call_api('/v2/orders/acknowledge', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ApiResponse',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def order_create(self, model, **kwargs):
        """
        Channel: Create Order
        For channels.    Create a new order in ChannelEngine.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.order_create(model, async=True)
        >>> result = thread.get()

        :param async bool
        :param ChannelOrderRequest model:  (required)
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.order_create_with_http_info(model, **kwargs)
        else:
            (data) = self.order_create_with_http_info(model, **kwargs)
            return data

    def order_create_with_http_info(self, model, **kwargs):
        """
        Channel: Create Order
        For channels.    Create a new order in ChannelEngine.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.order_create_with_http_info(model, async=True)
        >>> result = thread.get()

        :param async bool
        :param ChannelOrderRequest model:  (required)
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['model']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method order_create" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'model' is set
        if ('model' not in params) or (params['model'] is None):
            raise ValueError("Missing the required parameter `model` when calling `order_create`")


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'model' in params:
            body_params = params['model']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'text/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json', 'text/json', 'application/x-www-form-urlencoded'])

        # Authentication setting
        auth_settings = ['apikey']

        return self.api_client.call_api('/v2/orders', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ApiResponse',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def order_get_by_filter(self, **kwargs):
        """
        Merchant: Get Orders By Filter
        For merchants.                Fetch orders based on the provided OrderFilter
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.order_get_by_filter(async=True)
        >>> result = thread.get()

        :param async bool
        :param list[str] filter_statuses:
        :param list[str] filter_merchant_order_nos:
        :param bool filter_exclude_marketplace_fulfilled_orders_and_lines:
        :param str filter_fulfillment_type: Filter orders on fulfillment type. This will include all orders lines, even if they are partially fulfilled by the marketplace.  To exclude orders and lines that are fulfilled by the marketplace from the response, set ExcludeMarketplaceFulfilledOrdersAndLines to true.
        :param int filter_page:
        :return: CollectionOfMerchantOrderResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.order_get_by_filter_with_http_info(**kwargs)
        else:
            (data) = self.order_get_by_filter_with_http_info(**kwargs)
            return data

    def order_get_by_filter_with_http_info(self, **kwargs):
        """
        Merchant: Get Orders By Filter
        For merchants.                Fetch orders based on the provided OrderFilter
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.order_get_by_filter_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param list[str] filter_statuses:
        :param list[str] filter_merchant_order_nos:
        :param bool filter_exclude_marketplace_fulfilled_orders_and_lines:
        :param str filter_fulfillment_type: Filter orders on fulfillment type. This will include all orders lines, even if they are partially fulfilled by the marketplace.  To exclude orders and lines that are fulfilled by the marketplace from the response, set ExcludeMarketplaceFulfilledOrdersAndLines to true.
        :param int filter_page:
        :return: CollectionOfMerchantOrderResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['filter_statuses', 'filter_merchant_order_nos', 'filter_exclude_marketplace_fulfilled_orders_and_lines', 'filter_fulfillment_type', 'filter_page']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method order_get_by_filter" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'filter_statuses' in params:
            query_params.append(('filter.statuses', params['filter_statuses']))
            collection_formats['filter.statuses'] = 'multi'
        if 'filter_merchant_order_nos' in params:
            query_params.append(('filter.merchantOrderNos', params['filter_merchant_order_nos']))
            collection_formats['filter.merchantOrderNos'] = 'multi'
        if 'filter_exclude_marketplace_fulfilled_orders_and_lines' in params:
            query_params.append(('filter.excludeMarketplaceFulfilledOrdersAndLines', params['filter_exclude_marketplace_fulfilled_orders_and_lines']))
        if 'filter_fulfillment_type' in params:
            query_params.append(('filter.fulfillmentType', params['filter_fulfillment_type']))
        if 'filter_page' in params:
            query_params.append(('filter.page', params['filter_page']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'text/json'])

        # Authentication setting
        auth_settings = ['apikey']

        return self.api_client.call_api('/v2/orders', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='CollectionOfMerchantOrderResponse',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def order_get_new(self, **kwargs):
        """
        Merchant: Get New Orders
        For merchants.                Fetch newly placed orders (order with status NEW).
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.order_get_new(async=True)
        >>> result = thread.get()

        :param async bool
        :return: CollectionOfMerchantOrderResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.order_get_new_with_http_info(**kwargs)
        else:
            (data) = self.order_get_new_with_http_info(**kwargs)
            return data

    def order_get_new_with_http_info(self, **kwargs):
        """
        Merchant: Get New Orders
        For merchants.                Fetch newly placed orders (order with status NEW).
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.order_get_new_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :return: CollectionOfMerchantOrderResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method order_get_new" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'text/json'])

        # Authentication setting
        auth_settings = ['apikey']

        return self.api_client.call_api('/v2/orders/new', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='CollectionOfMerchantOrderResponse',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def order_invoice(self, merchant_order_no, **kwargs):
        """
        Merchant: Download Invoice
        For merchants.    Generates the ChannelEngine VAT invoice for this order in PDF
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.order_invoice(merchant_order_no, async=True)
        >>> result = thread.get()

        :param async bool
        :param str merchant_order_no: The unique order reference as used by the merchant (required)
        :param bool use_customer_culture: Generate the invoice in the billing address' country's language
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.order_invoice_with_http_info(merchant_order_no, **kwargs)
        else:
            (data) = self.order_invoice_with_http_info(merchant_order_no, **kwargs)
            return data

    def order_invoice_with_http_info(self, merchant_order_no, **kwargs):
        """
        Merchant: Download Invoice
        For merchants.    Generates the ChannelEngine VAT invoice for this order in PDF
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.order_invoice_with_http_info(merchant_order_no, async=True)
        >>> result = thread.get()

        :param async bool
        :param str merchant_order_no: The unique order reference as used by the merchant (required)
        :param bool use_customer_culture: Generate the invoice in the billing address' country's language
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['merchant_order_no', 'use_customer_culture']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method order_invoice" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'merchant_order_no' is set
        if ('merchant_order_no' not in params) or (params['merchant_order_no'] is None):
            raise ValueError("Missing the required parameter `merchant_order_no` when calling `order_invoice`")


        collection_formats = {}

        path_params = {}
        if 'merchant_order_no' in params:
            path_params['merchantOrderNo'] = params['merchant_order_no']

        query_params = []
        if 'use_customer_culture' in params:
            query_params.append(('useCustomerCulture', params['use_customer_culture']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/pdf'])

        # Authentication setting
        auth_settings = ['apikey']

        return self.api_client.call_api('/v2/orders/{merchantOrderNo}/invoice', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='file',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def order_packing_slip(self, merchant_order_no, **kwargs):
        """
        Merchant: Download Packing Slip
        For merchants.    Generates the ChannelEngine packing slip for this order in PDF
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.order_packing_slip(merchant_order_no, async=True)
        >>> result = thread.get()

        :param async bool
        :param str merchant_order_no: The unique order reference as used by the merchant (required)
        :param bool use_customer_culture: Generate the invoice in the billing address' country's language
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.order_packing_slip_with_http_info(merchant_order_no, **kwargs)
        else:
            (data) = self.order_packing_slip_with_http_info(merchant_order_no, **kwargs)
            return data

    def order_packing_slip_with_http_info(self, merchant_order_no, **kwargs):
        """
        Merchant: Download Packing Slip
        For merchants.    Generates the ChannelEngine packing slip for this order in PDF
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.order_packing_slip_with_http_info(merchant_order_no, async=True)
        >>> result = thread.get()

        :param async bool
        :param str merchant_order_no: The unique order reference as used by the merchant (required)
        :param bool use_customer_culture: Generate the invoice in the billing address' country's language
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['merchant_order_no', 'use_customer_culture']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method order_packing_slip" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'merchant_order_no' is set
        if ('merchant_order_no' not in params) or (params['merchant_order_no'] is None):
            raise ValueError("Missing the required parameter `merchant_order_no` when calling `order_packing_slip`")


        collection_formats = {}

        path_params = {}
        if 'merchant_order_no' in params:
            path_params['merchantOrderNo'] = params['merchant_order_no']

        query_params = []
        if 'use_customer_culture' in params:
            query_params.append(('useCustomerCulture', params['use_customer_culture']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/pdf'])

        # Authentication setting
        auth_settings = ['apikey']

        return self.api_client.call_api('/v2/orders/{merchantOrderNo}/packingslip', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='file',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
