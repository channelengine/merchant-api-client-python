"""
    ChannelEngine Merchant API

    ChannelEngine API for merchants  # noqa: E501

    The version of the OpenAPI document: 2.9.11
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
from channelengine_merchant_api_client.model.collection_of_merchant_offer_get_stock_response import CollectionOfMerchantOfferGetStockResponse
from channelengine_merchant_api_client.model.merchant_stock_price_update_request import MerchantStockPriceUpdateRequest
from channelengine_merchant_api_client.model.single_of_dictionary_of_string_and_list_of_string import SingleOfDictionaryOfStringAndListOfString


class OfferApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __offer_get_stock(
            self,
            skus,
            stock_location_ids,
            **kwargs
        ):
            """Get stock for products.  # noqa: E501

            Get stock of products at stock location(s).  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.offer_get_stock(skus, stock_location_ids, async_req=True)
            >>> result = thread.get()

            Args:
                skus ([str]): List of your products' sku's.
                stock_location_ids ([int]): The ChannelEngine id of the stock location(s).

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
                CollectionOfMerchantOfferGetStockResponse
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
            kwargs['skus'] = \
                skus
            kwargs['stock_location_ids'] = \
                stock_location_ids
            return self.call_with_http_info(**kwargs)

        self.offer_get_stock = _Endpoint(
            settings={
                'response_type': (CollectionOfMerchantOfferGetStockResponse,),
                'auth': [
                    'apiKey'
                ],
                'endpoint_path': '/v2/offer/stock',
                'operation_id': 'offer_get_stock',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'skus',
                    'stock_location_ids',
                ],
                'required': [
                    'skus',
                    'stock_location_ids',
                ],
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
                    'skus':
                        ([str],),
                    'stock_location_ids':
                        ([int],),
                },
                'attribute_map': {
                    'skus': 'skus',
                    'stock_location_ids': 'stockLocationIds',
                },
                'location_map': {
                    'skus': 'query',
                    'stock_location_ids': 'query',
                },
                'collection_format_map': {
                    'skus': 'multi',
                    'stock_location_ids': 'multi',
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__offer_get_stock
        )

        def __offer_stock_price_update(
            self,
            merchant_stock_price_update_request,
            **kwargs
        ):
            """Update stock and/or price.  # noqa: E501

            Update stock and/or price of product(s).  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.offer_stock_price_update(merchant_stock_price_update_request, async_req=True)
            >>> result = thread.get()

            Args:
                merchant_stock_price_update_request ([MerchantStockPriceUpdateRequest]): References to the products that should be updated, and the new values<br />for the stock or price fields. It is possible to supply only one of the two fields<br />or both.

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
                SingleOfDictionaryOfStringAndListOfString
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
            kwargs['merchant_stock_price_update_request'] = \
                merchant_stock_price_update_request
            return self.call_with_http_info(**kwargs)

        self.offer_stock_price_update = _Endpoint(
            settings={
                'response_type': (SingleOfDictionaryOfStringAndListOfString,),
                'auth': [
                    'apiKey'
                ],
                'endpoint_path': '/v2/offer',
                'operation_id': 'offer_stock_price_update',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'merchant_stock_price_update_request',
                ],
                'required': [
                    'merchant_stock_price_update_request',
                ],
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
                    'merchant_stock_price_update_request':
                        ([MerchantStockPriceUpdateRequest],),
                },
                'attribute_map': {
                },
                'location_map': {
                    'merchant_stock_price_update_request': 'body',
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
            callable=__offer_stock_price_update
        )
