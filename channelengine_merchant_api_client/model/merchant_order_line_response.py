"""
    ChannelEngine Merchant API

    ChannelEngine API for merchants  # noqa: E501

    The version of the OpenAPI document: 2.11.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from channelengine_merchant_api_client.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)
from ..model_utils import OpenApiModel
from channelengine_merchant_api_client.exceptions import ApiAttributeError


def lazy_import():
    from channelengine_merchant_api_client.model.condition import Condition
    from channelengine_merchant_api_client.model.merchant_order_line_extra_data_response import MerchantOrderLineExtraDataResponse
    from channelengine_merchant_api_client.model.merchant_stock_location_response import MerchantStockLocationResponse
    from channelengine_merchant_api_client.model.order_status_view import OrderStatusView
    globals()['Condition'] = Condition
    globals()['MerchantOrderLineExtraDataResponse'] = MerchantOrderLineExtraDataResponse
    globals()['MerchantStockLocationResponse'] = MerchantStockLocationResponse
    globals()['OrderStatusView'] = OrderStatusView


class MerchantOrderLineResponse(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
        ('channel_product_no',): {
            'max_length': 60,
            'min_length': 0,
        },
        ('quantity',): {
            'inclusive_minimum': 0,
        },
        ('unit_price_incl_vat',): {
            'inclusive_minimum': 0,
        },
        ('merchant_product_no',): {
            'max_length': 50,
            'min_length': 0,
        },
        ('cancellation_requested_quantity',): {
            'inclusive_minimum': 0,
        },
        ('fee_fixed',): {
            'inclusive_minimum': 0,
        },
        ('fee_rate',): {
            'inclusive_minimum': 0,
        },
    }

    additional_properties_type = None

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'channel_product_no': (str,),  # noqa: E501
            'quantity': (int,),  # noqa: E501
            'unit_price_incl_vat': (float,),  # noqa: E501
            'status': (OrderStatusView,),  # noqa: E501
            'is_fulfillment_by_marketplace': (bool,),  # noqa: E501
            'gtin': (str, none_type,),  # noqa: E501
            'description': (str, none_type,),  # noqa: E501
            'stock_location': (MerchantStockLocationResponse,),  # noqa: E501
            'unit_vat': (float, none_type,),  # noqa: E501
            'line_total_incl_vat': (float, none_type,),  # noqa: E501
            'line_vat': (float, none_type,),  # noqa: E501
            'original_unit_price_incl_vat': (float, none_type,),  # noqa: E501
            'original_unit_vat': (float, none_type,),  # noqa: E501
            'original_line_total_incl_vat': (float, none_type,),  # noqa: E501
            'original_line_vat': (float, none_type,),  # noqa: E501
            'original_fee_fixed': (float,),  # noqa: E501
            'bundle_product_merchant_product_no': (str, none_type,),  # noqa: E501
            'juris_code': (str, none_type,),  # noqa: E501
            'juris_name': (str, none_type,),  # noqa: E501
            'vat_rate': (float,),  # noqa: E501
            'extra_data': ([MerchantOrderLineExtraDataResponse], none_type,),  # noqa: E501
            'merchant_product_no': (str, none_type,),  # noqa: E501
            'cancellation_requested_quantity': (int,),  # noqa: E501
            'fee_fixed': (float,),  # noqa: E501
            'fee_rate': (float,),  # noqa: E501
            'condition': (Condition,),  # noqa: E501
            'expected_delivery_date': (datetime, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'channel_product_no': 'ChannelProductNo',  # noqa: E501
        'quantity': 'Quantity',  # noqa: E501
        'unit_price_incl_vat': 'UnitPriceInclVat',  # noqa: E501
        'status': 'Status',  # noqa: E501
        'is_fulfillment_by_marketplace': 'IsFulfillmentByMarketplace',  # noqa: E501
        'gtin': 'Gtin',  # noqa: E501
        'description': 'Description',  # noqa: E501
        'stock_location': 'StockLocation',  # noqa: E501
        'unit_vat': 'UnitVat',  # noqa: E501
        'line_total_incl_vat': 'LineTotalInclVat',  # noqa: E501
        'line_vat': 'LineVat',  # noqa: E501
        'original_unit_price_incl_vat': 'OriginalUnitPriceInclVat',  # noqa: E501
        'original_unit_vat': 'OriginalUnitVat',  # noqa: E501
        'original_line_total_incl_vat': 'OriginalLineTotalInclVat',  # noqa: E501
        'original_line_vat': 'OriginalLineVat',  # noqa: E501
        'original_fee_fixed': 'OriginalFeeFixed',  # noqa: E501
        'bundle_product_merchant_product_no': 'BundleProductMerchantProductNo',  # noqa: E501
        'juris_code': 'JurisCode',  # noqa: E501
        'juris_name': 'JurisName',  # noqa: E501
        'vat_rate': 'VatRate',  # noqa: E501
        'extra_data': 'ExtraData',  # noqa: E501
        'merchant_product_no': 'MerchantProductNo',  # noqa: E501
        'cancellation_requested_quantity': 'CancellationRequestedQuantity',  # noqa: E501
        'fee_fixed': 'FeeFixed',  # noqa: E501
        'fee_rate': 'FeeRate',  # noqa: E501
        'condition': 'Condition',  # noqa: E501
        'expected_delivery_date': 'ExpectedDeliveryDate',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, channel_product_no, quantity, unit_price_incl_vat, *args, **kwargs):  # noqa: E501
        """MerchantOrderLineResponse - a model defined in OpenAPI

        Args:
            channel_product_no (str): The unique product reference used by the channel.
            quantity (int): The number of items of the product.
            unit_price_incl_vat (float): The value of a single unit of the ordered product including VAT  (in the shop's base currency calculated using the exchange rate at the time of ordering).

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            status (OrderStatusView): [optional]  # noqa: E501
            is_fulfillment_by_marketplace (bool): Is the order fulfilled by the marketplace (amazon: FBA, bol: LVB, etc.)?.. [optional]  # noqa: E501
            gtin (str, none_type): Either the GTIN (EAN, ISBN, UPC etc) provided by the channel, or the the GTIN belonging to the MerchantProductNo in ChannelEngine.. [optional]  # noqa: E501
            description (str, none_type): The product description (or title) provided by the channel.. [optional]  # noqa: E501
            stock_location (MerchantStockLocationResponse): [optional]  # noqa: E501
            unit_vat (float, none_type): The total amount of VAT charged over the value of a single unit of the ordered product  (in the shop's base currency calculated using the exchange rate at the time of ordering).. [optional]  # noqa: E501
            line_total_incl_vat (float, none_type): The total value of the order line (quantity * unit price) including VAT  (in the shop's base currency calculated using the exchange rate at the time of ordering).. [optional]  # noqa: E501
            line_vat (float, none_type): The total amount of VAT charged over the total value of the order line (quantity * unit price)  (in the shop's base currency calculated using the exchange rate at the time of ordering).. [optional]  # noqa: E501
            original_unit_price_incl_vat (float, none_type): The value of a single unit of the ordered product including VAT  (in the currency in which the order was paid for, see CurrencyCode).. [optional]  # noqa: E501
            original_unit_vat (float, none_type): The total amount of VAT charged over the value of a single unit of the ordered product  (in the currency in which the order was paid for, see CurrencyCode).. [optional]  # noqa: E501
            original_line_total_incl_vat (float, none_type): The total value of the order line (quantity * unit price) including VAT  (in the currency in which the order was paid for, see CurrencyCode).. [optional]  # noqa: E501
            original_line_vat (float, none_type): The total amount of VAT charged over the total value of the order line (quantity * unit price)  (in the currency in which the order was paid for, see CurrencyCode).. [optional]  # noqa: E501
            original_fee_fixed (float): A percentage fee that is charged by the Channel for this orderline.  This fee rate is based on the currency of client  This field is optional, send 0 if not applicable.. [optional]  # noqa: E501
            bundle_product_merchant_product_no (str, none_type): If the product is ordered part of a bundle, this field contains the MerchantProductNo of  the product bundle.. [optional]  # noqa: E501
            juris_code (str, none_type): State assigned code identifying the jurisdiction.. [optional]  # noqa: E501
            juris_name (str, none_type): Name of a tax jurisdiction.. [optional]  # noqa: E501
            vat_rate (float): VAT rate of the orderline.. [optional]  # noqa: E501
            extra_data ([MerchantOrderLineExtraDataResponse], none_type): [optional]  # noqa: E501
            merchant_product_no (str, none_type): The unique product reference used by the merchant.. [optional]  # noqa: E501
            cancellation_requested_quantity (int): The number of items for which cancellation was requested by the customer.  Some channels allow a customer to cancel an order until it has been shipped.  When an order has already been acknowledged in ChannelEngine, it can only be cancelled by creating a cancellation.  Use this field to check whether it is still possible to cancel the order. If this is the case, submit a cancellation to ChannelEngine.. [optional]  # noqa: E501
            fee_fixed (float): A fixed fee that is charged by the Channel for this orderline.  This fee rate is based on the currency of the Channel  This field is optional, send 0 if not applicable.. [optional]  # noqa: E501
            fee_rate (float): A percentage fee that is charged by the Channel for this orderline.  This field is optional, send 0 if not applicable.. [optional]  # noqa: E501
            condition (Condition): [optional]  # noqa: E501
            expected_delivery_date (datetime, none_type): Expected delivery date from channels, empty if channels not support this value. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.channel_product_no = channel_product_no
        self.quantity = quantity
        self.unit_price_incl_vat = unit_price_incl_vat
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, channel_product_no, quantity, unit_price_incl_vat, *args, **kwargs):  # noqa: E501
        """MerchantOrderLineResponse - a model defined in OpenAPI

        Args:
            channel_product_no (str): The unique product reference used by the channel.
            quantity (int): The number of items of the product.
            unit_price_incl_vat (float): The value of a single unit of the ordered product including VAT  (in the shop's base currency calculated using the exchange rate at the time of ordering).

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            status (OrderStatusView): [optional]  # noqa: E501
            is_fulfillment_by_marketplace (bool): Is the order fulfilled by the marketplace (amazon: FBA, bol: LVB, etc.)?.. [optional]  # noqa: E501
            gtin (str, none_type): Either the GTIN (EAN, ISBN, UPC etc) provided by the channel, or the the GTIN belonging to the MerchantProductNo in ChannelEngine.. [optional]  # noqa: E501
            description (str, none_type): The product description (or title) provided by the channel.. [optional]  # noqa: E501
            stock_location (MerchantStockLocationResponse): [optional]  # noqa: E501
            unit_vat (float, none_type): The total amount of VAT charged over the value of a single unit of the ordered product  (in the shop's base currency calculated using the exchange rate at the time of ordering).. [optional]  # noqa: E501
            line_total_incl_vat (float, none_type): The total value of the order line (quantity * unit price) including VAT  (in the shop's base currency calculated using the exchange rate at the time of ordering).. [optional]  # noqa: E501
            line_vat (float, none_type): The total amount of VAT charged over the total value of the order line (quantity * unit price)  (in the shop's base currency calculated using the exchange rate at the time of ordering).. [optional]  # noqa: E501
            original_unit_price_incl_vat (float, none_type): The value of a single unit of the ordered product including VAT  (in the currency in which the order was paid for, see CurrencyCode).. [optional]  # noqa: E501
            original_unit_vat (float, none_type): The total amount of VAT charged over the value of a single unit of the ordered product  (in the currency in which the order was paid for, see CurrencyCode).. [optional]  # noqa: E501
            original_line_total_incl_vat (float, none_type): The total value of the order line (quantity * unit price) including VAT  (in the currency in which the order was paid for, see CurrencyCode).. [optional]  # noqa: E501
            original_line_vat (float, none_type): The total amount of VAT charged over the total value of the order line (quantity * unit price)  (in the currency in which the order was paid for, see CurrencyCode).. [optional]  # noqa: E501
            original_fee_fixed (float): A percentage fee that is charged by the Channel for this orderline.  This fee rate is based on the currency of client  This field is optional, send 0 if not applicable.. [optional]  # noqa: E501
            bundle_product_merchant_product_no (str, none_type): If the product is ordered part of a bundle, this field contains the MerchantProductNo of  the product bundle.. [optional]  # noqa: E501
            juris_code (str, none_type): State assigned code identifying the jurisdiction.. [optional]  # noqa: E501
            juris_name (str, none_type): Name of a tax jurisdiction.. [optional]  # noqa: E501
            vat_rate (float): VAT rate of the orderline.. [optional]  # noqa: E501
            extra_data ([MerchantOrderLineExtraDataResponse], none_type): [optional]  # noqa: E501
            merchant_product_no (str, none_type): The unique product reference used by the merchant.. [optional]  # noqa: E501
            cancellation_requested_quantity (int): The number of items for which cancellation was requested by the customer.  Some channels allow a customer to cancel an order until it has been shipped.  When an order has already been acknowledged in ChannelEngine, it can only be cancelled by creating a cancellation.  Use this field to check whether it is still possible to cancel the order. If this is the case, submit a cancellation to ChannelEngine.. [optional]  # noqa: E501
            fee_fixed (float): A fixed fee that is charged by the Channel for this orderline.  This fee rate is based on the currency of the Channel  This field is optional, send 0 if not applicable.. [optional]  # noqa: E501
            fee_rate (float): A percentage fee that is charged by the Channel for this orderline.  This field is optional, send 0 if not applicable.. [optional]  # noqa: E501
            condition (Condition): [optional]  # noqa: E501
            expected_delivery_date (datetime, none_type): Expected delivery date from channels, empty if channels not support this value. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.channel_product_no = channel_product_no
        self.quantity = quantity
        self.unit_price_incl_vat = unit_price_incl_vat
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
