# coding: utf-8

"""
    ChannelEngine API V2

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.4.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class EntitiesAddressModels(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'gender': 'str',
        'company_name': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'street_name': 'str',
        'house_nr': 'str',
        'house_nr_addition': 'str',
        'zip_code': 'str',
        'city': 'str',
        'region': 'str',
        'country_iso': 'str',
        'original': 'str'
    }

    attribute_map = {
        'gender': 'Gender',
        'company_name': 'CompanyName',
        'first_name': 'FirstName',
        'last_name': 'LastName',
        'street_name': 'StreetName',
        'house_nr': 'HouseNr',
        'house_nr_addition': 'HouseNrAddition',
        'zip_code': 'ZipCode',
        'city': 'City',
        'region': 'Region',
        'country_iso': 'CountryIso',
        'original': 'Original'
    }

    def __init__(self, gender=None, company_name=None, first_name=None, last_name=None, street_name=None, house_nr=None, house_nr_addition=None, zip_code=None, city=None, region=None, country_iso=None, original=None):
        """
        EntitiesAddressModels - a model defined in Swagger
        """

        self._gender = None
        self._company_name = None
        self._first_name = None
        self._last_name = None
        self._street_name = None
        self._house_nr = None
        self._house_nr_addition = None
        self._zip_code = None
        self._city = None
        self._region = None
        self._country_iso = None
        self._original = None
        self.discriminator = None

        if gender is not None:
          self.gender = gender
        if company_name is not None:
          self.company_name = company_name
        if first_name is not None:
          self.first_name = first_name
        if last_name is not None:
          self.last_name = last_name
        if street_name is not None:
          self.street_name = street_name
        if house_nr is not None:
          self.house_nr = house_nr
        if house_nr_addition is not None:
          self.house_nr_addition = house_nr_addition
        if zip_code is not None:
          self.zip_code = zip_code
        if city is not None:
          self.city = city
        if region is not None:
          self.region = region
        if country_iso is not None:
          self.country_iso = country_iso
        if original is not None:
          self.original = original

    @property
    def gender(self):
        """
        Gets the gender of this EntitiesAddressModels.

        :return: The gender of this EntitiesAddressModels.
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        """
        Sets the gender of this EntitiesAddressModels.

        :param gender: The gender of this EntitiesAddressModels.
        :type: str
        """
        allowed_values = ["MALE", "FEMALE", "NOT_APPLICABLE"]
        if gender not in allowed_values:
            raise ValueError(
                "Invalid value for `gender` ({0}), must be one of {1}"
                .format(gender, allowed_values)
            )

        self._gender = gender

    @property
    def company_name(self):
        """
        Gets the company_name of this EntitiesAddressModels.

        :return: The company_name of this EntitiesAddressModels.
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """
        Sets the company_name of this EntitiesAddressModels.

        :param company_name: The company_name of this EntitiesAddressModels.
        :type: str
        """

        self._company_name = company_name

    @property
    def first_name(self):
        """
        Gets the first_name of this EntitiesAddressModels.

        :return: The first_name of this EntitiesAddressModels.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """
        Sets the first_name of this EntitiesAddressModels.

        :param first_name: The first_name of this EntitiesAddressModels.
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """
        Gets the last_name of this EntitiesAddressModels.

        :return: The last_name of this EntitiesAddressModels.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """
        Sets the last_name of this EntitiesAddressModels.

        :param last_name: The last_name of this EntitiesAddressModels.
        :type: str
        """

        self._last_name = last_name

    @property
    def street_name(self):
        """
        Gets the street_name of this EntitiesAddressModels.

        :return: The street_name of this EntitiesAddressModels.
        :rtype: str
        """
        return self._street_name

    @street_name.setter
    def street_name(self, street_name):
        """
        Sets the street_name of this EntitiesAddressModels.

        :param street_name: The street_name of this EntitiesAddressModels.
        :type: str
        """

        self._street_name = street_name

    @property
    def house_nr(self):
        """
        Gets the house_nr of this EntitiesAddressModels.

        :return: The house_nr of this EntitiesAddressModels.
        :rtype: str
        """
        return self._house_nr

    @house_nr.setter
    def house_nr(self, house_nr):
        """
        Sets the house_nr of this EntitiesAddressModels.

        :param house_nr: The house_nr of this EntitiesAddressModels.
        :type: str
        """
        if house_nr is not None and len(house_nr) > 50:
            raise ValueError("Invalid value for `house_nr`, length must be less than or equal to `50`")
        if house_nr is not None and len(house_nr) < 0:
            raise ValueError("Invalid value for `house_nr`, length must be greater than or equal to `0`")

        self._house_nr = house_nr

    @property
    def house_nr_addition(self):
        """
        Gets the house_nr_addition of this EntitiesAddressModels.

        :return: The house_nr_addition of this EntitiesAddressModels.
        :rtype: str
        """
        return self._house_nr_addition

    @house_nr_addition.setter
    def house_nr_addition(self, house_nr_addition):
        """
        Sets the house_nr_addition of this EntitiesAddressModels.

        :param house_nr_addition: The house_nr_addition of this EntitiesAddressModels.
        :type: str
        """
        if house_nr_addition is not None and len(house_nr_addition) > 50:
            raise ValueError("Invalid value for `house_nr_addition`, length must be less than or equal to `50`")
        if house_nr_addition is not None and len(house_nr_addition) < 0:
            raise ValueError("Invalid value for `house_nr_addition`, length must be greater than or equal to `0`")

        self._house_nr_addition = house_nr_addition

    @property
    def zip_code(self):
        """
        Gets the zip_code of this EntitiesAddressModels.

        :return: The zip_code of this EntitiesAddressModels.
        :rtype: str
        """
        return self._zip_code

    @zip_code.setter
    def zip_code(self, zip_code):
        """
        Sets the zip_code of this EntitiesAddressModels.

        :param zip_code: The zip_code of this EntitiesAddressModels.
        :type: str
        """

        self._zip_code = zip_code

    @property
    def city(self):
        """
        Gets the city of this EntitiesAddressModels.

        :return: The city of this EntitiesAddressModels.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """
        Sets the city of this EntitiesAddressModels.

        :param city: The city of this EntitiesAddressModels.
        :type: str
        """

        self._city = city

    @property
    def region(self):
        """
        Gets the region of this EntitiesAddressModels.

        :return: The region of this EntitiesAddressModels.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """
        Sets the region of this EntitiesAddressModels.

        :param region: The region of this EntitiesAddressModels.
        :type: str
        """
        if region is not None and len(region) > 50:
            raise ValueError("Invalid value for `region`, length must be less than or equal to `50`")
        if region is not None and len(region) < 0:
            raise ValueError("Invalid value for `region`, length must be greater than or equal to `0`")

        self._region = region

    @property
    def country_iso(self):
        """
        Gets the country_iso of this EntitiesAddressModels.

        :return: The country_iso of this EntitiesAddressModels.
        :rtype: str
        """
        return self._country_iso

    @country_iso.setter
    def country_iso(self, country_iso):
        """
        Sets the country_iso of this EntitiesAddressModels.

        :param country_iso: The country_iso of this EntitiesAddressModels.
        :type: str
        """
        if country_iso is not None and len(country_iso) > 2:
            raise ValueError("Invalid value for `country_iso`, length must be less than or equal to `2`")
        if country_iso is not None and len(country_iso) < 0:
            raise ValueError("Invalid value for `country_iso`, length must be greater than or equal to `0`")

        self._country_iso = country_iso

    @property
    def original(self):
        """
        Gets the original of this EntitiesAddressModels.

        :return: The original of this EntitiesAddressModels.
        :rtype: str
        """
        return self._original

    @original.setter
    def original(self, original):
        """
        Sets the original of this EntitiesAddressModels.

        :param original: The original of this EntitiesAddressModels.
        :type: str
        """
        if original is not None and len(original) > 256:
            raise ValueError("Invalid value for `original`, length must be less than or equal to `256`")
        if original is not None and len(original) < 0:
            raise ValueError("Invalid value for `original`, length must be greater than or equal to `0`")

        self._original = original

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, EntitiesAddressModels):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
