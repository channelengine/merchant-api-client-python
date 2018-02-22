# coding: utf-8

"""
    ChannelEngine Merchant API

    ChannelEngine API for merchants  # noqa: E501

    OpenAPI spec version: 2.5.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from channelengine_merchant_api_client.api_client import ApiClient


class ReturnApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def return_declare_for_merchant(self, model, **kwargs):  # noqa: E501
        """Create Return  # noqa: E501

        Mark (part of) an order as returned by the customer.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.return_declare_for_merchant(model, async=True)
        >>> result = thread.get()

        :param async bool
        :param MerchantReturnRequest model:  (required)
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.return_declare_for_merchant_with_http_info(model, **kwargs)  # noqa: E501
        else:
            (data) = self.return_declare_for_merchant_with_http_info(model, **kwargs)  # noqa: E501
            return data

    def return_declare_for_merchant_with_http_info(self, model, **kwargs):  # noqa: E501
        """Create Return  # noqa: E501

        Mark (part of) an order as returned by the customer.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.return_declare_for_merchant_with_http_info(model, async=True)
        >>> result = thread.get()

        :param async bool
        :param MerchantReturnRequest model:  (required)
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['model']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method return_declare_for_merchant" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'model' is set
        if ('model' not in params or
                params['model'] is None):
            raise ValueError("Missing the required parameter `model` when calling `return_declare_for_merchant`")  # noqa: E501

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
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json', 'application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apikey']  # noqa: E501

        return self.api_client.call_api(
            '/v2/returns/merchant', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def return_get_declared_by_channel(self, created_since, **kwargs):  # noqa: E501
        """Get Returns  # noqa: E501

        Get all returns created by the channel. This call is supposed  to be used by merchants. Channels should use the 'GET /v2/returns/channel'  call.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.return_get_declared_by_channel(created_since, async=True)
        >>> result = thread.get()

        :param async bool
        :param datetime created_since:  (required)
        :return: CollectionOfMerchantReturnResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.return_get_declared_by_channel_with_http_info(created_since, **kwargs)  # noqa: E501
        else:
            (data) = self.return_get_declared_by_channel_with_http_info(created_since, **kwargs)  # noqa: E501
            return data

    def return_get_declared_by_channel_with_http_info(self, created_since, **kwargs):  # noqa: E501
        """Get Returns  # noqa: E501

        Get all returns created by the channel. This call is supposed  to be used by merchants. Channels should use the 'GET /v2/returns/channel'  call.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.return_get_declared_by_channel_with_http_info(created_since, async=True)
        >>> result = thread.get()

        :param async bool
        :param datetime created_since:  (required)
        :return: CollectionOfMerchantReturnResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['created_since']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method return_get_declared_by_channel" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'created_since' is set
        if ('created_since' not in params or
                params['created_since'] is None):
            raise ValueError("Missing the required parameter `created_since` when calling `return_get_declared_by_channel`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'created_since' in params:
            query_params.append(('createdSince', params['created_since']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apikey']  # noqa: E501

        return self.api_client.call_api(
            '/v2/returns/merchant', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CollectionOfMerchantReturnResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
