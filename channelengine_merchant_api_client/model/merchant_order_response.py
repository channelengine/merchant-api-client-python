"""
    ChannelEngine Merchant API

    ChannelEngine API for merchants  # noqa: E501

    The version of the OpenAPI document: 2.9.10
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

def lazy_import():
    from channelengine_merchant_api_client.model.merchant_address_response import MerchantAddressResponse
    from channelengine_merchant_api_client.model.merchant_order_line_response import MerchantOrderLineResponse
    from channelengine_merchant_api_client.model.order_status_view import OrderStatusView
    from channelengine_merchant_api_client.model.order_support import OrderSupport
    globals()['MerchantAddressResponse'] = MerchantAddressResponse
    globals()['MerchantOrderLineResponse'] = MerchantOrderLineResponse
    globals()['OrderStatusView'] = OrderStatusView
    globals()['OrderSupport'] = OrderSupport


class MerchantOrderResponse(ModelNormal):
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
        ('email',): {
            'max_length': 250,
            'min_length': 0,
        },
        ('shipping_costs_incl_vat',): {
            'inclusive_minimum': 0,
        },
        ('currency_code',): {
            'max_length': 3,
        },
        ('phone',): {
            'max_length': 50,
            'min_length': 0,
        },
        ('company_registration_no',): {
            'max_length': 50,
            'min_length': 0,
        },
        ('vat_no',): {
            'max_length': 50,
            'min_length': 0,
        },
        ('payment_method',): {
            'max_length': 50,
            'min_length': 0,
        },
        ('payment_reference_no',): {
            'max_length': 250,
            'min_length': 0,
        },
        ('channel_customer_no',): {
            'max_length': 50,
            'min_length': 0,
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
            'email': (str,),  # noqa: E501
            'shipping_costs_incl_vat': (float,),  # noqa: E501
            'currency_code': (str,),  # noqa: E501
            'order_date': (datetime,),  # noqa: E501
            'id': (int,),  # noqa: E501
            'channel_name': (str, none_type,),  # noqa: E501
            'channel_id': (int, none_type,),  # noqa: E501
            'global_channel_name': (str, none_type,),  # noqa: E501
            'global_channel_id': (int, none_type,),  # noqa: E501
            'channel_order_support': (OrderSupport,),  # noqa: E501
            'channel_order_no': (str, none_type,),  # noqa: E501
            'status': (OrderStatusView,),  # noqa: E501
            'is_business_order': (bool,),  # noqa: E501
            'created_at': (datetime, none_type,),  # noqa: E501
            'updated_at': (datetime, none_type,),  # noqa: E501
            'merchant_comment': (str, none_type,),  # noqa: E501
            'billing_address': (MerchantAddressResponse,),  # noqa: E501
            'shipping_address': (MerchantAddressResponse,),  # noqa: E501
            'sub_total_incl_vat': (float, none_type,),  # noqa: E501
            'sub_total_vat': (float, none_type,),  # noqa: E501
            'shipping_costs_vat': (float, none_type,),  # noqa: E501
            'total_incl_vat': (float,),  # noqa: E501
            'total_vat': (float, none_type,),  # noqa: E501
            'original_sub_total_incl_vat': (float, none_type,),  # noqa: E501
            'original_sub_total_vat': (float, none_type,),  # noqa: E501
            'original_shipping_costs_incl_vat': (float, none_type,),  # noqa: E501
            'original_shipping_costs_vat': (float, none_type,),  # noqa: E501
            'original_total_incl_vat': (float, none_type,),  # noqa: E501
            'original_total_vat': (float, none_type,),  # noqa: E501
            'lines': ([MerchantOrderLineResponse], none_type,),  # noqa: E501
            'phone': (str, none_type,),  # noqa: E501
            'company_registration_no': (str, none_type,),  # noqa: E501
            'vat_no': (str, none_type,),  # noqa: E501
            'payment_method': (str, none_type,),  # noqa: E501
            'payment_reference_no': (str, none_type,),  # noqa: E501
            'channel_customer_no': (str, none_type,),  # noqa: E501
            'extra_data': ({str: (str,)}, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'email': 'Email',  # noqa: E501
        'shipping_costs_incl_vat': 'ShippingCostsInclVat',  # noqa: E501
        'currency_code': 'CurrencyCode',  # noqa: E501
        'order_date': 'OrderDate',  # noqa: E501
        'id': 'Id',  # noqa: E501
        'channel_name': 'ChannelName',  # noqa: E501
        'channel_id': 'ChannelId',  # noqa: E501
        'global_channel_name': 'GlobalChannelName',  # noqa: E501
        'global_channel_id': 'GlobalChannelId',  # noqa: E501
        'channel_order_support': 'ChannelOrderSupport',  # noqa: E501
        'channel_order_no': 'ChannelOrderNo',  # noqa: E501
        'status': 'Status',  # noqa: E501
        'is_business_order': 'IsBusinessOrder',  # noqa: E501
        'created_at': 'CreatedAt',  # noqa: E501
        'updated_at': 'UpdatedAt',  # noqa: E501
        'merchant_comment': 'MerchantComment',  # noqa: E501
        'billing_address': 'BillingAddress',  # noqa: E501
        'shipping_address': 'ShippingAddress',  # noqa: E501
        'sub_total_incl_vat': 'SubTotalInclVat',  # noqa: E501
        'sub_total_vat': 'SubTotalVat',  # noqa: E501
        'shipping_costs_vat': 'ShippingCostsVat',  # noqa: E501
        'total_incl_vat': 'TotalInclVat',  # noqa: E501
        'total_vat': 'TotalVat',  # noqa: E501
        'original_sub_total_incl_vat': 'OriginalSubTotalInclVat',  # noqa: E501
        'original_sub_total_vat': 'OriginalSubTotalVat',  # noqa: E501
        'original_shipping_costs_incl_vat': 'OriginalShippingCostsInclVat',  # noqa: E501
        'original_shipping_costs_vat': 'OriginalShippingCostsVat',  # noqa: E501
        'original_total_incl_vat': 'OriginalTotalInclVat',  # noqa: E501
        'original_total_vat': 'OriginalTotalVat',  # noqa: E501
        'lines': 'Lines',  # noqa: E501
        'phone': 'Phone',  # noqa: E501
        'company_registration_no': 'CompanyRegistrationNo',  # noqa: E501
        'vat_no': 'VatNo',  # noqa: E501
        'payment_method': 'PaymentMethod',  # noqa: E501
        'payment_reference_no': 'PaymentReferenceNo',  # noqa: E501
        'channel_customer_no': 'ChannelCustomerNo',  # noqa: E501
        'extra_data': 'ExtraData',  # noqa: E501
    }

    _composed_schemas = {}

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, email, shipping_costs_incl_vat, currency_code, order_date, *args, **kwargs):  # noqa: E501
        """MerchantOrderResponse - a model defined in OpenAPI

        Args:
            email (str): The customer's email.
            shipping_costs_incl_vat (float): The shipping fee including VAT  (in the shop's base currency calculated using the exchange rate at the time of ordering).
            currency_code (str): The currency code for the amounts of the order.
            order_date (datetime): The date the order was created at the channel.

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
            id (int): The unique identifier used by ChannelEngine. This identifier does  not have to be saved. It should only be used in a call to acknowledge the order.. [optional]  # noqa: E501
            channel_name (str, none_type): The name of the channel for this specific environment/account.. [optional]  # noqa: E501
            channel_id (int, none_type): The unique ID of the channel for this specific environment/account.. [optional]  # noqa: E501
            global_channel_name (str, none_type): The name of the channel across all of ChannelEngine.. [optional]  # noqa: E501
            global_channel_id (int, none_type): The unique ID of the channel across all of ChannelEngine.. [optional]  # noqa: E501
            channel_order_support (OrderSupport): [optional]  # noqa: E501
            channel_order_no (str, none_type): The order reference used by the channel.  This number is not guaranteed to be unique accross all orders,  because different channels can use the same order number format.. [optional]  # noqa: E501
            status (OrderStatusView): [optional]  # noqa: E501
            is_business_order (bool): Indicating whether the order is a business order.. [optional]  # noqa: E501
            created_at (datetime, none_type): The date the order was created in ChannelEngine.. [optional]  # noqa: E501
            updated_at (datetime, none_type): The date the order was last updated in ChannelEngine.. [optional]  # noqa: E501
            merchant_comment (str, none_type): The optional comment a merchant can add to an order.. [optional]  # noqa: E501
            billing_address (MerchantAddressResponse): [optional]  # noqa: E501
            shipping_address (MerchantAddressResponse): [optional]  # noqa: E501
            sub_total_incl_vat (float, none_type): The total value of the order lines including VAT  (in the shop's base currency calculated using the exchange rate at the time of ordering).. [optional]  # noqa: E501
            sub_total_vat (float, none_type): The total amount of VAT charged over the order lines  (in the shop's base currency calculated using the exchange rate at the time of ordering).. [optional]  # noqa: E501
            shipping_costs_vat (float, none_type): The total amount of VAT charged over the shipping fee  (in the shop's base currency calculated using the exchange rate at the time of ordering).. [optional]  # noqa: E501
            total_incl_vat (float): The total value of the order including VAT  (in the shop's base currency calculated using the exchange rate at the time of ordering).. [optional]  # noqa: E501
            total_vat (float, none_type): The total amount of VAT charged over the total value of te order  (in the shop's base currency calculated using the exchange rate at the time of ordering).. [optional]  # noqa: E501
            original_sub_total_incl_vat (float, none_type): The total value of the order lines including VAT  (in the currency in which the order was paid for, see CurrencyCode).. [optional]  # noqa: E501
            original_sub_total_vat (float, none_type): The total amount of VAT charged over the order lines  (in the currency in which the order was paid for, see CurrencyCode).. [optional]  # noqa: E501
            original_shipping_costs_incl_vat (float, none_type): The shipping fee including VAT  (in the currency in which the order was paid for, see CurrencyCode).. [optional]  # noqa: E501
            original_shipping_costs_vat (float, none_type): The total amount of VAT charged over the shipping fee  (in the currency in which the order was paid for, see CurrencyCode).. [optional]  # noqa: E501
            original_total_incl_vat (float, none_type): The total value of the order including VAT  (in the currency in which the order was paid for, see CurrencyCode).. [optional]  # noqa: E501
            original_total_vat (float, none_type): The total amount of VAT charged over the total value of te order  (in the currency in which the order was paid for, see CurrencyCode).. [optional]  # noqa: E501
            lines ([MerchantOrderLineResponse], none_type): [optional]  # noqa: E501
            phone (str, none_type): The customer's telephone number.. [optional]  # noqa: E501
            company_registration_no (str, none_type): Optional. A company's chamber of commerce number.. [optional]  # noqa: E501
            vat_no (str, none_type): Optional. A company's VAT number.. [optional]  # noqa: E501
            payment_method (str, none_type): The payment method used on the order.. [optional]  # noqa: E501
            payment_reference_no (str, none_type): Reference or transaction id for the payment. [optional]  # noqa: E501
            channel_customer_no (str, none_type): The unique customer reference used by the channel.. [optional]  # noqa: E501
            extra_data ({str: (str,)}, none_type): Extra data on the order.. [optional]  # noqa: E501
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

        self.email = email
        self.shipping_costs_incl_vat = shipping_costs_incl_vat
        self.currency_code = currency_code
        self.order_date = order_date
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
