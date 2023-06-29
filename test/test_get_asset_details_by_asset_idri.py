# coding: utf-8

"""
    CryptoAPIs

    Crypto APIs is a complex and innovative infrastructure layer that radically simplifies the development of any Blockchain and Crypto related applications. Organized around REST, Crypto APIs can assist both novice Bitcoin/Ethereum enthusiasts and crypto experts with the development of their blockchain applications. Crypto APIs provides unified endpoints and data, raw data, automatic tokens and coins forwardings, callback functionalities, and much more.  # noqa: E501

    The version of the OpenAPI document: 2021-03-20
    Contact: developers@cryptoapis.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import cryptoapis
from cryptoapis.models.get_asset_details_by_asset_idri import GetAssetDetailsByAssetIDRI  # noqa: E501
from cryptoapis.rest import ApiException

class TestGetAssetDetailsByAssetIDRI(unittest.TestCase):
    """GetAssetDetailsByAssetIDRI unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetAssetDetailsByAssetIDRI
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetAssetDetailsByAssetIDRI`
        """
        model = cryptoapis.models.get_asset_details_by_asset_idri.GetAssetDetailsByAssetIDRI()  # noqa: E501
        if include_optional :
            return GetAssetDetailsByAssetIDRI(
                asset_id = '5b1ea92e584bf50020130615', 
                asset_logo = cryptoapis.models.get_asset_details_by_asset_idri_asset_logo.GetAssetDetailsByAssetIDRI_assetLogo(
                    encoding = 'base64', 
                    image_data = 'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIzMiIgaGVpZ2h0PSIzMiI+PGcgZmlsbD0ibm9uZSIgZmlsbC1ydWxlPSJldmVub2RkIj48Y2lyY2xlIGN4PSIxNiIgY3k9IjE2IiByPSIxNiIgZmlsbD0iI0Y3OTMxQSIvPjxwYXRoIGZpbGw9IiNGRkYiIGZpbGwtcnVsZT0ibm9uemVybyIgZD0iTTIzLjE4OSAxNC4wMmMuMzE0LTIuMDk2LTEuMjgzLTMuMjIzLTMuNDY1LTMuOTc1bC43MDgtMi44NC0xLjcyOC0uNDMtLjY5IDIuNzY1Yy0uNDU0LS4xMTQtLjkyLS4yMi0xLjM4NS0uMzI2bC42OTUtMi43ODNMMTUuNTk2IDZsLS43MDggMi44MzljLS4zNzYtLjA4Ni0uNzQ2LS4xNy0xLjEwNC0uMjZsLjAwMi0uMDA5LTIuMzg0LS41OTUtLjQ2IDEuODQ2czEuMjgzLjI5NCAxLjI1Ni4zMTJjLjcuMTc1LjgyNi42MzguODA1IDEuMDA2bC0uODA2IDMuMjM1Yy4wNDguMDEyLjExLjAzLjE4LjA1N2wtLjE4My0uMDQ1LTEuMTMgNC41MzJjLS4wODYuMjEyLS4zMDMuNTMxLS43OTMuNDEuMDE4LjAyNS0xLjI1Ni0uMzEzLTEuMjU2LS4zMTNsLS44NTggMS45NzggMi4yNS41NjFjLjQxOC4xMDUuODI4LjIxNSAxLjIzMS4zMThsLS43MTUgMi44NzIgMS43MjcuNDMuNzA4LTIuODRjLjQ3Mi4xMjcuOTMuMjQ1IDEuMzc4LjM1N2wtLjcwNiAyLjgyOCAxLjcyOC40My43MTUtMi44NjZjMi45NDguNTU4IDUuMTY0LjMzMyA2LjA5Ny0yLjMzMy43NTItMi4xNDYtLjAzNy0zLjM4NS0xLjU4OC00LjE5MiAxLjEzLS4yNiAxLjk4LTEuMDAzIDIuMjA3LTIuNTM4em0tMy45NSA1LjUzOGMtLjUzMyAyLjE0Ny00LjE0OC45ODYtNS4zMi42OTVsLjk1LTMuODA1YzEuMTcyLjI5MyA0LjkyOS44NzIgNC4zNyAzLjExem0uNTM1LTUuNTY5Yy0uNDg3IDEuOTUzLTMuNDk1Ljk2LTQuNDcuNzE3bC44Ni0zLjQ1Yy45NzUuMjQzIDQuMTE4LjY5NiAzLjYxIDIuNzMzeiIvPjwvZz48L3N2Zz4=', 
                    mime_type = 'image/svg+xml', ), 
                asset_name = 'Bitcoin', 
                asset_original_symbol = 'BTC', 
                asset_symbol = 'BTC', 
                asset_type = 'crypto', 
                latest_rate = cryptoapis.models.get_asset_details_by_asset_idri_latest_rate.GetAssetDetailsByAssetIDRI_latestRate(
                    amount = '61704.20995670996', 
                    calculation_timestamp = 1636107864, 
                    unit = 'USD', ), 
                slug = 'bitcoin', 
                specific_data = cryptoapis.models.get_asset_details_by_asset_idris.GetAssetDetailsByAssetIDRIS()
            )
        else :
            return GetAssetDetailsByAssetIDRI(
                asset_id = '5b1ea92e584bf50020130615',
                asset_logo = cryptoapis.models.get_asset_details_by_asset_idri_asset_logo.GetAssetDetailsByAssetIDRI_assetLogo(
                    encoding = 'base64', 
                    image_data = 'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIzMiIgaGVpZ2h0PSIzMiI+PGcgZmlsbD0ibm9uZSIgZmlsbC1ydWxlPSJldmVub2RkIj48Y2lyY2xlIGN4PSIxNiIgY3k9IjE2IiByPSIxNiIgZmlsbD0iI0Y3OTMxQSIvPjxwYXRoIGZpbGw9IiNGRkYiIGZpbGwtcnVsZT0ibm9uemVybyIgZD0iTTIzLjE4OSAxNC4wMmMuMzE0LTIuMDk2LTEuMjgzLTMuMjIzLTMuNDY1LTMuOTc1bC43MDgtMi44NC0xLjcyOC0uNDMtLjY5IDIuNzY1Yy0uNDU0LS4xMTQtLjkyLS4yMi0xLjM4NS0uMzI2bC42OTUtMi43ODNMMTUuNTk2IDZsLS43MDggMi44MzljLS4zNzYtLjA4Ni0uNzQ2LS4xNy0xLjEwNC0uMjZsLjAwMi0uMDA5LTIuMzg0LS41OTUtLjQ2IDEuODQ2czEuMjgzLjI5NCAxLjI1Ni4zMTJjLjcuMTc1LjgyNi42MzguODA1IDEuMDA2bC0uODA2IDMuMjM1Yy4wNDguMDEyLjExLjAzLjE4LjA1N2wtLjE4My0uMDQ1LTEuMTMgNC41MzJjLS4wODYuMjEyLS4zMDMuNTMxLS43OTMuNDEuMDE4LjAyNS0xLjI1Ni0uMzEzLTEuMjU2LS4zMTNsLS44NTggMS45NzggMi4yNS41NjFjLjQxOC4xMDUuODI4LjIxNSAxLjIzMS4zMThsLS43MTUgMi44NzIgMS43MjcuNDMuNzA4LTIuODRjLjQ3Mi4xMjcuOTMuMjQ1IDEuMzc4LjM1N2wtLjcwNiAyLjgyOCAxLjcyOC40My43MTUtMi44NjZjMi45NDguNTU4IDUuMTY0LjMzMyA2LjA5Ny0yLjMzMy43NTItMi4xNDYtLjAzNy0zLjM4NS0xLjU4OC00LjE5MiAxLjEzLS4yNiAxLjk4LTEuMDAzIDIuMjA3LTIuNTM4em0tMy45NSA1LjUzOGMtLjUzMyAyLjE0Ny00LjE0OC45ODYtNS4zMi42OTVsLjk1LTMuODA1YzEuMTcyLjI5MyA0LjkyOS44NzIgNC4zNyAzLjExem0uNTM1LTUuNTY5Yy0uNDg3IDEuOTUzLTMuNDk1Ljk2LTQuNDcuNzE3bC44Ni0zLjQ1Yy45NzUuMjQzIDQuMTE4LjY5NiAzLjYxIDIuNzMzeiIvPjwvZz48L3N2Zz4=', 
                    mime_type = 'image/svg+xml', ),
                asset_name = 'Bitcoin',
                asset_original_symbol = 'BTC',
                asset_symbol = 'BTC',
                asset_type = 'crypto',
                latest_rate = cryptoapis.models.get_asset_details_by_asset_idri_latest_rate.GetAssetDetailsByAssetIDRI_latestRate(
                    amount = '61704.20995670996', 
                    calculation_timestamp = 1636107864, 
                    unit = 'USD', ),
                specific_data = cryptoapis.models.get_asset_details_by_asset_idris.GetAssetDetailsByAssetIDRIS(),
        )
        """

    def testGetAssetDetailsByAssetIDRI(self):
        """Test GetAssetDetailsByAssetIDRI"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
