# coding: utf-8

"""
    ChannelEngine API V2

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.1.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.apis.shipment_api import ShipmentApi


class TestShipmentApi(unittest.TestCase):
    """ ShipmentApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.shipment_api.ShipmentApi()

    def tearDown(self):
        pass

    def test_shipment_create(self):
        """
        Test case for shipment_create

        Merchant: Create Shipment
        """
        pass

    def test_shipment_index(self):
        """
        Test case for shipment_index

        Channel: Get Shipments
        """
        pass

    def test_shipment_update(self):
        """
        Test case for shipment_update

        Merchant: Update Shipment
        """
        pass


if __name__ == '__main__':
    unittest.main()
