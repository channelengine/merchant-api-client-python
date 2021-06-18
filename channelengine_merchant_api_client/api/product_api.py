"""
    ChannelEngine Merchant API

    ChannelEngine API for merchants  # noqa: E501

    The version of the OpenAPI document: 2.9.7
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
from channelengine_merchant_api_client.model.collection_of_merchant_product_response import CollectionOfMerchantProductResponse
from channelengine_merchant_api_client.model.merchant_product_request import MerchantProductRequest
from channelengine_merchant_api_client.model.operation import Operation
from channelengine_merchant_api_client.model.patch_merchant_product_dto import PatchMerchantProductDto
from channelengine_merchant_api_client.model.single_of_merchant_product_response import SingleOfMerchantProductResponse
from channelengine_merchant_api_client.model.single_of_product_creation_result import SingleOfProductCreationResult


class ProductApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __product_bulk_delete(
            self,
            **kwargs
        ):
            """Delete multiple Products.  # noqa: E501

            Delete the products based on the merchant references.<br />Note that we do not really delete a products, as the products<br />might still be referenced by orders etc. Therefore, the references<br />used for these products cannot be reused. We do however deactivate the products<br />which means that they will not be sent to channels.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.product_bulk_delete(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                request_body ([str], none_type): [optional]
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

        self.product_bulk_delete = _Endpoint(
            settings={
                'response_type': (ApiResponse,),
                'auth': [
                    'apiKey'
                ],
                'endpoint_path': '/v2/products/bulkdelete',
                'operation_id': 'product_bulk_delete',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'request_body',
                ],
                'required': [],
                'nullable': [
                    'request_body',
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
                    'request_body':
                        ([str], none_type,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'request_body': 'body',
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
            callable=__product_bulk_delete
        )

        def __product_bulk_patch(
            self,
            **kwargs
        ):
            """Bulk Patch Products  # noqa: E501

            This endpoint allows you to update multiple fields on a multiple products.<br />Products sent in a request can only be updated for the fields listed in object 'PropertiesToUpdate'. <br />In other words, you specify which products you want to update and which fields should be updated for all products.<br /><br />Sample request:<br /><br /> PATCH /v2/products<br /> {<br /> \"PropertiesToUpdate\": [<br /> \"name\",<br /> \"description\"<br /> ],<br /> \"MerchantProductRequestModels\": [<br /> {<br /> \"MerchantProductNo\": \"testMerchantProductNo\",<br /> \"Name\": \"testName\",<br /> \"Description\": \"testDescription\",<br /> },<br /> {<br /> \"MerchantProductNo\": \"testMerchantProductNo2\",<br /> \"Name\": \"testName3\",<br /> \"Description\": \"testDescription1\",<br /> }<br /> ]<br /> }  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.product_bulk_patch(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                patch_merchant_product_dto (PatchMerchantProductDto): 1) PropertiesToUpdate: Fields to update<br />2) MerchantProductRequestModels: Products to be updated. [optional]
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
                SingleOfProductCreationResult
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

        self.product_bulk_patch = _Endpoint(
            settings={
                'response_type': (SingleOfProductCreationResult,),
                'auth': [
                    'apiKey'
                ],
                'endpoint_path': '/v2/products',
                'operation_id': 'product_bulk_patch',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'patch_merchant_product_dto',
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
                    'patch_merchant_product_dto':
                        (PatchMerchantProductDto,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'patch_merchant_product_dto': 'body',
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
            callable=__product_bulk_patch
        )

        def __product_create(
            self,
            **kwargs
        ):
            """Upsert Products.  # noqa: E501

            Upsert (update or create) products. The parent serves as the 'base' product of the children.<br />For example, the children could be different sizes or colors of the parent product.<br />For channels where every size and color are different products this does not make any difference<br />(the children will just be sent separately, while ignoring the parent).<br />But there are channels where the parent and the children need to be sent together, for example<br />when there is one product with a list of sizes. In this case all the product information is retrieved<br />from the parent product while the size list is generated from the children.<br /> <br />Note that the parent itself is a 'blueprint' of the child products and we do our best to make sure it<br />does not end up on the marketplaces itself. Only the children can be purchased.<br /> <br />It's not possible to nest parent and children more than one level (A parent can have many children,<br />but any child cannot itself also have children).<br /> <br />The supplied MerchantProductNo needs to be unique.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.product_create(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                merchant_product_request ([MerchantProductRequest], none_type): [optional]
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
                SingleOfProductCreationResult
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

        self.product_create = _Endpoint(
            settings={
                'response_type': (SingleOfProductCreationResult,),
                'auth': [
                    'apiKey'
                ],
                'endpoint_path': '/v2/products',
                'operation_id': 'product_create',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'merchant_product_request',
                ],
                'required': [],
                'nullable': [
                    'merchant_product_request',
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
                    'merchant_product_request':
                        ([MerchantProductRequest], none_type,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'merchant_product_request': 'body',
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
            callable=__product_create
        )

        def __product_delete(
            self,
            merchant_product_no,
            **kwargs
        ):
            """Delete Product.  # noqa: E501

            Delete a product based on the merchant reference.<br />Note that we do not really delete a product, as the product<br />might still be referenced by orders etc. Therefore, the references<br />used for this product cannot be reused. We do however deactivate the product<br />which means that it will not be sent to channels.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.product_delete(merchant_product_no, async_req=True)
            >>> result = thread.get()

            Args:
                merchant_product_no (str, none_type):

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
            kwargs['merchant_product_no'] = \
                merchant_product_no
            return self.call_with_http_info(**kwargs)

        self.product_delete = _Endpoint(
            settings={
                'response_type': (ApiResponse,),
                'auth': [
                    'apiKey'
                ],
                'endpoint_path': '/v2/products/{merchantProductNo}',
                'operation_id': 'product_delete',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'merchant_product_no',
                ],
                'required': [
                    'merchant_product_no',
                ],
                'nullable': [
                    'merchant_product_no',
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
                    'merchant_product_no':
                        (str, none_type,),
                },
                'attribute_map': {
                    'merchant_product_no': 'merchantProductNo',
                },
                'location_map': {
                    'merchant_product_no': 'path',
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
            callable=__product_delete
        )

        def __product_get_by_filter(
            self,
            **kwargs
        ):
            """Get Products.  # noqa: E501

            Retrieve all products.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.product_get_by_filter(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                search (str, none_type): Search product(s) by Name, MerchantProductNo, Ean or Brand<br />This search is applied to the result after applying the other filters.. [optional]
                ean_list ([str], none_type): Search products by submitting a list of EAN's.. [optional]
                merchant_product_no_list ([str], none_type): Search products by submitting a list of MerchantProductNo's.. [optional]
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
                CollectionOfMerchantProductResponse
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

        self.product_get_by_filter = _Endpoint(
            settings={
                'response_type': (CollectionOfMerchantProductResponse,),
                'auth': [
                    'apiKey'
                ],
                'endpoint_path': '/v2/products',
                'operation_id': 'product_get_by_filter',
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
                    'search',
                    'ean_list',
                    'merchant_product_no_list',
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
                    'search':
                        (str, none_type,),
                    'ean_list':
                        ([str], none_type,),
                    'merchant_product_no_list':
                        ([str], none_type,),
                    'page':
                        (int, none_type,),
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
            callable=__product_get_by_filter
        )

        def __product_get_by_merchant_product_no(
            self,
            merchant_product_no,
            **kwargs
        ):
            """Get Product.  # noqa: E501

            Retrieve a product based on the merchant reference.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.product_get_by_merchant_product_no(merchant_product_no, async_req=True)
            >>> result = thread.get()

            Args:
                merchant_product_no (str, none_type):

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
                SingleOfMerchantProductResponse
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
            kwargs['merchant_product_no'] = \
                merchant_product_no
            return self.call_with_http_info(**kwargs)

        self.product_get_by_merchant_product_no = _Endpoint(
            settings={
                'response_type': (SingleOfMerchantProductResponse,),
                'auth': [
                    'apiKey'
                ],
                'endpoint_path': '/v2/products/{merchantProductNo}',
                'operation_id': 'product_get_by_merchant_product_no',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'merchant_product_no',
                ],
                'required': [
                    'merchant_product_no',
                ],
                'nullable': [
                    'merchant_product_no',
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
                    'merchant_product_no':
                        (str, none_type,),
                },
                'attribute_map': {
                    'merchant_product_no': 'merchantProductNo',
                },
                'location_map': {
                    'merchant_product_no': 'path',
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
            callable=__product_get_by_merchant_product_no
        )

        def __product_patch(
            self,
            merchant_product_no,
            **kwargs
        ):
            """Patch product  # noqa: E501

            Patch products. This endpoint allows you to update single fields on a product using patch operations,<br />without having to supply the other product information.<br /><br />The format of this endpoint is a JsonPatchDocument. Examples of how this format works can be found here:<br />http://jsonpatch.com/<br /> <br />It's not possible to nest parent and children more than one level (A parent can have many children,<br />but any child cannot itself also have children).<br /> <br />The supplied MerchantProductNo needs to be unique.<br /><br /><br />Sample request:<br /> <br /> PATCH /v2/products/{merchantProductNo}<br /> {<br /> \"value\": \"Value\",<br /> \"path\": \"Name\",<br /> \"op\": \"replace\"<br /> }  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.product_patch(merchant_product_no, async_req=True)
            >>> result = thread.get()

            Args:
                merchant_product_no (str, none_type): The MerchantProductNo of the product you wish to patch

            Keyword Args:
                operation ([Operation], none_type): The JsonPatchDocument providing the operations you wish to perform on the product. <br /> Value contains the value you wish to set on the property you're updating (used with operations \"add\" and \"replace\").<br /> Path contains the path to the property you're updating (e.g. Description). Every property in the model used for creation an updating can be used.<br /> Op contains the operation you wish to perform (\"add\",\"replace\",\"remove\").<br /> From is only used when using the \"move\" operation. It refers to the source path of the value to be moved.. [optional]
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
                SingleOfProductCreationResult
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
            kwargs['merchant_product_no'] = \
                merchant_product_no
            return self.call_with_http_info(**kwargs)

        self.product_patch = _Endpoint(
            settings={
                'response_type': (SingleOfProductCreationResult,),
                'auth': [
                    'apiKey'
                ],
                'endpoint_path': '/v2/products/{merchantProductNo}',
                'operation_id': 'product_patch',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'merchant_product_no',
                    'operation',
                ],
                'required': [
                    'merchant_product_no',
                ],
                'nullable': [
                    'merchant_product_no',
                    'operation',
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
                    'merchant_product_no':
                        (str, none_type,),
                    'operation':
                        ([Operation], none_type,),
                },
                'attribute_map': {
                    'merchant_product_no': 'merchantProductNo',
                },
                'location_map': {
                    'merchant_product_no': 'path',
                    'operation': 'body',
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
            callable=__product_patch
        )
