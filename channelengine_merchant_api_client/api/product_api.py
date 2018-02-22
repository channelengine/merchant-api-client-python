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


class ProductApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def product_create(self, products, **kwargs):  # noqa: E501
        """Upsert Products  # noqa: E501

        Upsert (update or create) products. The parent serves as the 'base' product of the children.  For example, the children could be different sizes or colors of the parent product.  For channels where every size and color are different products this does not make any difference  (the children will just be sent separately, while ignoring the parent).  But there are channels where the parent and the children need to be sent together, for example  when there is one product with a list of sizes. In this case all the product information is retrieved  from the parent product while the size list is generated from the children.    Note that the parent itself is a 'blueprint' of the child products and we do our best to make sure it  does not end up on the marketplaces itself. Only the children can be purchased.    It's not possible to nest parent and children more than one level (A parent can have many children,  but any child cannot itself also have children).    The supplied MerchantProductNo needs to be unique.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.product_create(products, async=True)
        >>> result = thread.get()

        :param async bool
        :param list[MerchantProductRequest] products:  (required)
        :return: SingleOfProductCreationResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.product_create_with_http_info(products, **kwargs)  # noqa: E501
        else:
            (data) = self.product_create_with_http_info(products, **kwargs)  # noqa: E501
            return data

    def product_create_with_http_info(self, products, **kwargs):  # noqa: E501
        """Upsert Products  # noqa: E501

        Upsert (update or create) products. The parent serves as the 'base' product of the children.  For example, the children could be different sizes or colors of the parent product.  For channels where every size and color are different products this does not make any difference  (the children will just be sent separately, while ignoring the parent).  But there are channels where the parent and the children need to be sent together, for example  when there is one product with a list of sizes. In this case all the product information is retrieved  from the parent product while the size list is generated from the children.    Note that the parent itself is a 'blueprint' of the child products and we do our best to make sure it  does not end up on the marketplaces itself. Only the children can be purchased.    It's not possible to nest parent and children more than one level (A parent can have many children,  but any child cannot itself also have children).    The supplied MerchantProductNo needs to be unique.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.product_create_with_http_info(products, async=True)
        >>> result = thread.get()

        :param async bool
        :param list[MerchantProductRequest] products:  (required)
        :return: SingleOfProductCreationResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['products']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method product_create" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'products' is set
        if ('products' not in params or
                params['products'] is None):
            raise ValueError("Missing the required parameter `products` when calling `product_create`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'products' in params:
            body_params = params['products']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json', 'application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apikey']  # noqa: E501

        return self.api_client.call_api(
            '/v2/products', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SingleOfProductCreationResult',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def product_delete(self, merchant_product_no, **kwargs):  # noqa: E501
        """Delete Product  # noqa: E501

        Delete a product based on the merchant reference.  Note that we do not really delete a product, as the product  might still be referenced by orders etc. Therefore, the references  used for this product cannot be reused. We do however deactivate the product  which means that it will not be sent to channels.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.product_delete(merchant_product_no, async=True)
        >>> result = thread.get()

        :param async bool
        :param str merchant_product_no:  (required)
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.product_delete_with_http_info(merchant_product_no, **kwargs)  # noqa: E501
        else:
            (data) = self.product_delete_with_http_info(merchant_product_no, **kwargs)  # noqa: E501
            return data

    def product_delete_with_http_info(self, merchant_product_no, **kwargs):  # noqa: E501
        """Delete Product  # noqa: E501

        Delete a product based on the merchant reference.  Note that we do not really delete a product, as the product  might still be referenced by orders etc. Therefore, the references  used for this product cannot be reused. We do however deactivate the product  which means that it will not be sent to channels.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.product_delete_with_http_info(merchant_product_no, async=True)
        >>> result = thread.get()

        :param async bool
        :param str merchant_product_no:  (required)
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['merchant_product_no']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method product_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'merchant_product_no' is set
        if ('merchant_product_no' not in params or
                params['merchant_product_no'] is None):
            raise ValueError("Missing the required parameter `merchant_product_no` when calling `product_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'merchant_product_no' in params:
            path_params['merchantProductNo'] = params['merchant_product_no']  # noqa: E501

        query_params = []

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
            '/v2/products/{merchantProductNo}', 'DELETE',
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

    def product_get_by_merchant_product_no(self, merchant_product_no, **kwargs):  # noqa: E501
        """Get Product  # noqa: E501

        Retrieve a product based on the merchant reference.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.product_get_by_merchant_product_no(merchant_product_no, async=True)
        >>> result = thread.get()

        :param async bool
        :param str merchant_product_no:  (required)
        :return: SingleOfMerchantProductResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.product_get_by_merchant_product_no_with_http_info(merchant_product_no, **kwargs)  # noqa: E501
        else:
            (data) = self.product_get_by_merchant_product_no_with_http_info(merchant_product_no, **kwargs)  # noqa: E501
            return data

    def product_get_by_merchant_product_no_with_http_info(self, merchant_product_no, **kwargs):  # noqa: E501
        """Get Product  # noqa: E501

        Retrieve a product based on the merchant reference.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.product_get_by_merchant_product_no_with_http_info(merchant_product_no, async=True)
        >>> result = thread.get()

        :param async bool
        :param str merchant_product_no:  (required)
        :return: SingleOfMerchantProductResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['merchant_product_no']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method product_get_by_merchant_product_no" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'merchant_product_no' is set
        if ('merchant_product_no' not in params or
                params['merchant_product_no'] is None):
            raise ValueError("Missing the required parameter `merchant_product_no` when calling `product_get_by_merchant_product_no`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'merchant_product_no' in params:
            path_params['merchantProductNo'] = params['merchant_product_no']  # noqa: E501

        query_params = []

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
            '/v2/products/{merchantProductNo}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SingleOfMerchantProductResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)