# coding: utf-8

"""
    ChannelEngine API V2

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.4.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..api_client import ApiClient


class ShipmentApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def shipment_create(self, model, **kwargs):
        """
        Merchant: Create Shipment
        For merchants.    Mark (part of) an order as shipped.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.shipment_create(model, async=True)
        >>> result = thread.get()

        :param async bool
        :param MerchantShipmentRequest model:  (required)
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.shipment_create_with_http_info(model, **kwargs)
        else:
            (data) = self.shipment_create_with_http_info(model, **kwargs)
            return data

    def shipment_create_with_http_info(self, model, **kwargs):
        """
        Merchant: Create Shipment
        For merchants.    Mark (part of) an order as shipped.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.shipment_create_with_http_info(model, async=True)
        >>> result = thread.get()

        :param async bool
        :param MerchantShipmentRequest model:  (required)
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
                    " to method shipment_create" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'model' is set
        if ('model' not in params) or (params['model'] is None):
            raise ValueError("Missing the required parameter `model` when calling `shipment_create`")


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

        return self.api_client.call_api('/v2/shipments', 'POST',
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

    def shipment_index(self, created_since, **kwargs):
        """
        Channel: Get Shipments
        For channels.    Gets all shipments created since the supplied date.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.shipment_index(created_since, async=True)
        >>> result = thread.get()

        :param async bool
        :param datetime created_since:  (required)
        :return: CollectionOfChannelShipmentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.shipment_index_with_http_info(created_since, **kwargs)
        else:
            (data) = self.shipment_index_with_http_info(created_since, **kwargs)
            return data

    def shipment_index_with_http_info(self, created_since, **kwargs):
        """
        Channel: Get Shipments
        For channels.    Gets all shipments created since the supplied date.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.shipment_index_with_http_info(created_since, async=True)
        >>> result = thread.get()

        :param async bool
        :param datetime created_since:  (required)
        :return: CollectionOfChannelShipmentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['created_since']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method shipment_index" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'created_since' is set
        if ('created_since' not in params) or (params['created_since'] is None):
            raise ValueError("Missing the required parameter `created_since` when calling `shipment_index`")


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'created_since' in params:
            query_params.append(('createdSince', params['created_since']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'text/json'])

        # Authentication setting
        auth_settings = ['apikey']

        return self.api_client.call_api('/v2/shipments', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='CollectionOfChannelShipmentResponse',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def shipment_update(self, merchant_shipment_no, model, **kwargs):
        """
        Merchant: Update Shipment
        For merchants.    Update an existing shipment with tracking information
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.shipment_update(merchant_shipment_no, model, async=True)
        >>> result = thread.get()

        :param async bool
        :param str merchant_shipment_no: The merchant's shipment reference (required)
        :param MerchantShipmentTrackingRequest model: The updated tracking information (required)
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.shipment_update_with_http_info(merchant_shipment_no, model, **kwargs)
        else:
            (data) = self.shipment_update_with_http_info(merchant_shipment_no, model, **kwargs)
            return data

    def shipment_update_with_http_info(self, merchant_shipment_no, model, **kwargs):
        """
        Merchant: Update Shipment
        For merchants.    Update an existing shipment with tracking information
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.shipment_update_with_http_info(merchant_shipment_no, model, async=True)
        >>> result = thread.get()

        :param async bool
        :param str merchant_shipment_no: The merchant's shipment reference (required)
        :param MerchantShipmentTrackingRequest model: The updated tracking information (required)
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['merchant_shipment_no', 'model']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method shipment_update" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'merchant_shipment_no' is set
        if ('merchant_shipment_no' not in params) or (params['merchant_shipment_no'] is None):
            raise ValueError("Missing the required parameter `merchant_shipment_no` when calling `shipment_update`")
        # verify the required parameter 'model' is set
        if ('model' not in params) or (params['model'] is None):
            raise ValueError("Missing the required parameter `model` when calling `shipment_update`")


        collection_formats = {}

        path_params = {}
        if 'merchant_shipment_no' in params:
            path_params['merchantShipmentNo'] = params['merchant_shipment_no']

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

        return self.api_client.call_api('/v2/shipments/{merchantShipmentNo}', 'PUT',
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
