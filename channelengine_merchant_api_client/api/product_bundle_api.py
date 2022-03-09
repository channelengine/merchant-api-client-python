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
from channelengine_merchant_api_client.model.collection_of_merchant_product_bundle_response import CollectionOfMerchantProductBundleResponse


class ProductBundleApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __product_bundle_get_by_filter(
            self,
            **kwargs
        ):
            """Get product bundles.  # noqa: E501

            You can get the full product information on bundles from the regular /products endpoint.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.product_bundle_get_by_filter(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                search (str): Search product(s) by Name, MerchantProductNo, Ean or Brand<br />This search is applied to the result after applying the other filters.. [optional]
                ean_list ([str]): Search products by submitting a list of EAN's.. [optional]
                merchant_product_no_list ([str]): Search products by submitting a list of MerchantProductNo's.. [optional]
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
                CollectionOfMerchantProductBundleResponse
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

        self.product_bundle_get_by_filter = _Endpoint(
            settings={
                'response_type': (CollectionOfMerchantProductBundleResponse,),
                'auth': [
                    'apiKey'
                ],
                'endpoint_path': '/v2/productbundles',
                'operation_id': 'product_bundle_get_by_filter',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'search',
                    'ean_list',
                    'merchant_product_no_list',
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
                    'search':
                        (str,),
                    'ean_list':
                        ([str],),
                    'merchant_product_no_list':
                        ([str],),
                    'page':
                        (int,),
                },
                'attribute_map': {
                    'search': 'search',
                    'ean_list': 'eanList',
                    'merchant_product_no_list': 'merchantProductNoList',
                    'page': 'page',
                },
                'location_map': {
                    'search': 'query',
                    'ean_list': 'query',
                    'merchant_product_no_list': 'query',
                    'page': 'query',
                },
                'collection_format_map': {
                    'ean_list': 'multi',
                    'merchant_product_no_list': 'multi',
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__product_bundle_get_by_filter
        )
