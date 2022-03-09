"""
    ChannelEngine Merchant API

    ChannelEngine API for merchants  # noqa: E501

    The version of the OpenAPI document: 2.9.12
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
    from channelengine_merchant_api_client.model.merchant_shipment_line_request import MerchantShipmentLineRequest
    from channelengine_merchant_api_client.model.merchant_shipment_package_dimensions_request import MerchantShipmentPackageDimensionsRequest
    from channelengine_merchant_api_client.model.merchant_shipment_package_weight_request import MerchantShipmentPackageWeightRequest
    globals()['MerchantShipmentLineRequest'] = MerchantShipmentLineRequest
    globals()['MerchantShipmentPackageDimensionsRequest'] = MerchantShipmentPackageDimensionsRequest
    globals()['MerchantShipmentPackageWeightRequest'] = MerchantShipmentPackageWeightRequest


class MerchantChannelLabelShipmentRequest(ModelNormal):
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
        ('merchant_shipment_no',): {
            'max_length': 250,
            'min_length': 0,
        },
        ('merchant_order_no',): {
            'max_length': 50,
            'min_length': 0,
        },
        ('lines',): {
            'min_items': 1,
        },
        ('shipped_from_country_code',): {
            'max_length': 3,
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
            'dimensions': (MerchantShipmentPackageDimensionsRequest,),  # noqa: E501
            'weight': (MerchantShipmentPackageWeightRequest,),  # noqa: E501
            'channel_method_code': (str,),  # noqa: E501
            'merchant_shipment_no': (str,),  # noqa: E501
            'merchant_order_no': (str,),  # noqa: E501
            'lines': ([MerchantShipmentLineRequest],),  # noqa: E501
            'shipped_from_country_code': (str, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'dimensions': 'Dimensions',  # noqa: E501
        'weight': 'Weight',  # noqa: E501
        'channel_method_code': 'ChannelMethodCode',  # noqa: E501
        'merchant_shipment_no': 'MerchantShipmentNo',  # noqa: E501
        'merchant_order_no': 'MerchantOrderNo',  # noqa: E501
        'lines': 'Lines',  # noqa: E501
        'shipped_from_country_code': 'ShippedFromCountryCode',  # noqa: E501
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
    def __init__(self, dimensions, weight, channel_method_code, merchant_shipment_no, merchant_order_no, lines, *args, **kwargs):  # noqa: E501
        """MerchantChannelLabelShipmentRequest - a model defined in OpenAPI

        Args:
            dimensions (MerchantShipmentPackageDimensionsRequest):
            weight (MerchantShipmentPackageWeightRequest):
            channel_method_code (str):
            merchant_shipment_no (str): The unique shipment reference used by the Merchant.
            merchant_order_no (str): The unique order reference used by the Merchant.
            lines ([MerchantShipmentLineRequest]):

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
            shipped_from_country_code (str, none_type): The code of the country from where the package is being shipped.. [optional]  # noqa: E501
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

        self.dimensions = dimensions
        self.weight = weight
        self.channel_method_code = channel_method_code
        self.merchant_shipment_no = merchant_shipment_no
        self.merchant_order_no = merchant_order_no
        self.lines = lines
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
