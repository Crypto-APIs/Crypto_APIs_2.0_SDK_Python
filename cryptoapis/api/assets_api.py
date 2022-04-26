"""
    CryptoAPIs

    Crypto APIs 2.0 is a complex and innovative infrastructure layer that radically simplifies the development of any Blockchain and Crypto related applications. Organized around REST, Crypto APIs 2.0 can assist both novice Bitcoin/Ethereum enthusiasts and crypto experts with the development of their blockchain applications. Crypto APIs 2.0 provides unified endpoints and data, raw data, automatic tokens and coins forwardings, callback functionalities, and much more.  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: developers@cryptoapis.io
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from cryptoapis.api_client import ApiClient, Endpoint as _Endpoint
from cryptoapis.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from cryptoapis.model.get_asset_details_by_asset_idr import GetAssetDetailsByAssetIDR
from cryptoapis.model.get_asset_details_by_asset_symbol_r import GetAssetDetailsByAssetSymbolR
from cryptoapis.model.inline_response400108 import InlineResponse400108
from cryptoapis.model.inline_response400109 import InlineResponse400109
from cryptoapis.model.inline_response400110 import InlineResponse400110
from cryptoapis.model.inline_response401108 import InlineResponse401108
from cryptoapis.model.inline_response401109 import InlineResponse401109
from cryptoapis.model.inline_response401110 import InlineResponse401110
from cryptoapis.model.inline_response402 import InlineResponse402
from cryptoapis.model.inline_response403108 import InlineResponse403108
from cryptoapis.model.inline_response403109 import InlineResponse403109
from cryptoapis.model.inline_response403110 import InlineResponse403110
from cryptoapis.model.inline_response409 import InlineResponse409
from cryptoapis.model.inline_response415 import InlineResponse415
from cryptoapis.model.inline_response422 import InlineResponse422
from cryptoapis.model.inline_response429 import InlineResponse429
from cryptoapis.model.inline_response500 import InlineResponse500
from cryptoapis.model.list_assets_details_r import ListAssetsDetailsR


class AssetsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.get_asset_details_by_asset_id_endpoint = _Endpoint(
            settings={
                'response_type': (GetAssetDetailsByAssetIDR,),
                'auth': [
                    'ApiKey'
                ],
                'endpoint_path': '/market-data/assets/assetId/{assetId}',
                'operation_id': 'get_asset_details_by_asset_id',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'asset_id',
                    'context',
                ],
                'required': [
                    'asset_id',
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
                    'asset_id':
                        (str,),
                    'context':
                        (str,),
                },
                'attribute_map': {
                    'asset_id': 'assetId',
                    'context': 'context',
                },
                'location_map': {
                    'asset_id': 'path',
                    'context': 'query',
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
            api_client=api_client
        )
        self.get_asset_details_by_asset_symbol_endpoint = _Endpoint(
            settings={
                'response_type': (GetAssetDetailsByAssetSymbolR,),
                'auth': [
                    'ApiKey'
                ],
                'endpoint_path': '/market-data/assets/{assetSymbol}',
                'operation_id': 'get_asset_details_by_asset_symbol',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'asset_symbol',
                    'context',
                ],
                'required': [
                    'asset_symbol',
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
                    'asset_symbol':
                        (str,),
                    'context':
                        (str,),
                },
                'attribute_map': {
                    'asset_symbol': 'assetSymbol',
                    'context': 'context',
                },
                'location_map': {
                    'asset_symbol': 'path',
                    'context': 'query',
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
            api_client=api_client
        )
        self.list_assets_details_endpoint = _Endpoint(
            settings={
                'response_type': (ListAssetsDetailsR,),
                'auth': [
                    'ApiKey'
                ],
                'endpoint_path': '/market-data/assets/details',
                'operation_id': 'list_assets_details',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'context',
                    'asset_type',
                    'crypto_type',
                    'limit',
                    'offset',
                    'waas_enabled',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                    'asset_type',
                    'crypto_type',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('asset_type',): {

                        "FIAT": "fiat",
                        "CRYPTO": "crypto"
                    },
                    ('crypto_type',): {

                        "COIN": "coin",
                        "TOKEN": "token"
                    },
                },
                'openapi_types': {
                    'context':
                        (str,),
                    'asset_type':
                        (str,),
                    'crypto_type':
                        (str,),
                    'limit':
                        (int,),
                    'offset':
                        (int,),
                    'waas_enabled':
                        (bool,),
                },
                'attribute_map': {
                    'context': 'context',
                    'asset_type': 'assetType',
                    'crypto_type': 'cryptoType',
                    'limit': 'limit',
                    'offset': 'offset',
                    'waas_enabled': 'waasEnabled',
                },
                'location_map': {
                    'context': 'query',
                    'asset_type': 'query',
                    'crypto_type': 'query',
                    'limit': 'query',
                    'offset': 'query',
                    'waas_enabled': 'query',
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
            api_client=api_client
        )

    def get_asset_details_by_asset_id(
        self,
        asset_id,
        **kwargs
    ):
        """Get Asset Details By Asset ID  # noqa: E501

        Through this endpoint users can obtain information on assets by `assetId`.    The details returned could include information on the latest rate and rate fluctuation of different periods of time - 24 hours, a week, one hour, the encoding of the logo, and more.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_asset_details_by_asset_id(asset_id, async_req=True)
        >>> result = thread.get()

        Args:
            asset_id (str): Defines the unique ID of the specific asset.

        Keyword Args:
            context (str): In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            GetAssetDetailsByAssetIDR
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
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['asset_id'] = \
            asset_id
        return self.get_asset_details_by_asset_id_endpoint.call_with_http_info(**kwargs)

    def get_asset_details_by_asset_symbol(
        self,
        asset_symbol,
        **kwargs
    ):
        """Get Asset Details By Asset Symbol  # noqa: E501

        Through this endpoint users can obtain information on assets by asset symbol.    The details returned could include information on the latest rate and rate fluctuation of different periods of time - 24 hours, a week, one hour, the encoding of the logo, and more.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_asset_details_by_asset_symbol(asset_symbol, async_req=True)
        >>> result = thread.get()

        Args:
            asset_symbol (str): Specifies the asset's unique symbol in the Crypto APIs listings.

        Keyword Args:
            context (str): In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            GetAssetDetailsByAssetSymbolR
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
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['asset_symbol'] = \
            asset_symbol
        return self.get_asset_details_by_asset_symbol_endpoint.call_with_http_info(**kwargs)

    def list_assets_details(
        self,
        **kwargs
    ):
        """List Assets Details  # noqa: E501

        This endpoint will return a list of details on assets. These could be cryptocurrencies or FIAT assets that we support. Each asset has a unique identifier - `assetId` and a unique symbol in the form of a string, e.g. \"BTC\".    The details returned could include information on the latest rate and rate fluctuation of different periods of time - 24 hours, a week, one hour, the encoding of the logo, and more.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_assets_details(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            context (str): In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user.. [optional]
            asset_type (str): Defines the type of the supported asset. This could be either \"crypto\" or \"fiat\".. [optional]
            crypto_type (str): Subtype of the crypto assets. Could be COIN or TOKEN. [optional]
            limit (int): Defines how many items should be returned in the response per page basis.. [optional] if omitted the server will use the default value of 50
            offset (int): The starting index of the response items, i.e. where the response should start listing the returned items.. [optional] if omitted the server will use the default value of 0
            waas_enabled (bool): Show only if WaaS is/not enabled. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            ListAssetsDetailsR
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
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.list_assets_details_endpoint.call_with_http_info(**kwargs)

