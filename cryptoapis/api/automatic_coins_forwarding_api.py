# coding: utf-8

"""
    CryptoAPIs

    Crypto APIs is a complex and innovative infrastructure layer that radically simplifies the development of any Blockchain and Crypto related applications. Organized around REST, Crypto APIs can assist both novice Bitcoin/Ethereum enthusiasts and crypto experts with the development of their blockchain applications. Crypto APIs provides unified endpoints and data, raw data, automatic tokens and coins forwardings, callback functionalities, and much more.  # noqa: E501

    The version of the OpenAPI document: 2021-03-20
    Contact: developers@cryptoapis.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError
from typing_extensions import Annotated

from pydantic import Field, StrictInt, StrictStr

from typing import Optional

from cryptoapis.models.create_automatic_coins_forwarding_r import CreateAutomaticCoinsForwardingR
from cryptoapis.models.create_automatic_coins_forwarding_rb import CreateAutomaticCoinsForwardingRB
from cryptoapis.models.delete_automatic_coins_forwarding_r import DeleteAutomaticCoinsForwardingR
from cryptoapis.models.list_coins_forwarding_automations_r import ListCoinsForwardingAutomationsR

from cryptoapis.api_client import ApiClient
from cryptoapis.api_response import ApiResponse
from cryptoapis.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class AutomaticCoinsForwardingApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def create_automatic_coins_forwarding(self, blockchain : Annotated[StrictStr, Field(..., description="Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.")], network : Annotated[StrictStr, Field(..., description="Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.")], context : Annotated[Optional[StrictStr], Field(description="In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user.")] = None, create_automatic_coins_forwarding_rb : Optional[CreateAutomaticCoinsForwardingRB] = None, **kwargs) -> CreateAutomaticCoinsForwardingR:  # noqa: E501
        """Create Automatic Coins Forwarding  # noqa: E501

        Through this endpoint customers can set up an automatic forwarding function specifically for coins (**not** tokens). They can have a `toAddress` which is essentially the main address and the destination for the automatic coins forwarding.     There is also a `minimumTransferAmount` which only when reached will then trigger the forwarding. Through this the customer can save from fees.    Moreover, `feePriority` can be also set,  which defines how quickly to move the coins once they are received. The higher priority, the larger the fee will be. It can be \"SLOW\", \"STANDARD\" or \"FAST\".    The response of this endpoint contains an attribute `fromAddress` which can be used as a deposit address. Any funds received by this address will be automatically forwarded to `toAddress` based on what the customer has set for the automation.    For this automatic forwarding the customer can set a callback subscription.    {warning}The subscription will work for all incoming transactions until it is deleted. There is no need to do that for every transaction.{/warning}    {note}This endpoint generates a new `fromAddress` each time.{/note}  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_automatic_coins_forwarding(blockchain, network, context, create_automatic_coins_forwarding_rb, async_req=True)
        >>> result = thread.get()

        :param blockchain: Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. (required)
        :type blockchain: str
        :param network: Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks. (required)
        :type network: str
        :param context: In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user.
        :type context: str
        :param create_automatic_coins_forwarding_rb:
        :type create_automatic_coins_forwarding_rb: CreateAutomaticCoinsForwardingRB
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: CreateAutomaticCoinsForwardingR
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the create_automatic_coins_forwarding_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.create_automatic_coins_forwarding_with_http_info(blockchain, network, context, create_automatic_coins_forwarding_rb, **kwargs)  # noqa: E501

    @validate_arguments
    def create_automatic_coins_forwarding_with_http_info(self, blockchain : Annotated[StrictStr, Field(..., description="Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.")], network : Annotated[StrictStr, Field(..., description="Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.")], context : Annotated[Optional[StrictStr], Field(description="In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user.")] = None, create_automatic_coins_forwarding_rb : Optional[CreateAutomaticCoinsForwardingRB] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Create Automatic Coins Forwarding  # noqa: E501

        Through this endpoint customers can set up an automatic forwarding function specifically for coins (**not** tokens). They can have a `toAddress` which is essentially the main address and the destination for the automatic coins forwarding.     There is also a `minimumTransferAmount` which only when reached will then trigger the forwarding. Through this the customer can save from fees.    Moreover, `feePriority` can be also set,  which defines how quickly to move the coins once they are received. The higher priority, the larger the fee will be. It can be \"SLOW\", \"STANDARD\" or \"FAST\".    The response of this endpoint contains an attribute `fromAddress` which can be used as a deposit address. Any funds received by this address will be automatically forwarded to `toAddress` based on what the customer has set for the automation.    For this automatic forwarding the customer can set a callback subscription.    {warning}The subscription will work for all incoming transactions until it is deleted. There is no need to do that for every transaction.{/warning}    {note}This endpoint generates a new `fromAddress` each time.{/note}  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_automatic_coins_forwarding_with_http_info(blockchain, network, context, create_automatic_coins_forwarding_rb, async_req=True)
        >>> result = thread.get()

        :param blockchain: Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. (required)
        :type blockchain: str
        :param network: Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks. (required)
        :type network: str
        :param context: In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user.
        :type context: str
        :param create_automatic_coins_forwarding_rb:
        :type create_automatic_coins_forwarding_rb: CreateAutomaticCoinsForwardingRB
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(CreateAutomaticCoinsForwardingR, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'blockchain',
            'network',
            'context',
            'create_automatic_coins_forwarding_rb'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_automatic_coins_forwarding" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['blockchain']:
            _path_params['blockchain'] = _params['blockchain']

        if _params['network']:
            _path_params['network'] = _params['network']


        # process the query parameters
        _query_params = []
        if _params.get('context') is not None:  # noqa: E501
            _query_params.append(('context', _params['context']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['create_automatic_coins_forwarding_rb'] is not None:
            _body_params = _params['create_automatic_coins_forwarding_rb']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['ApiKey']  # noqa: E501

        _response_types_map = {
            '201': "CreateAutomaticCoinsForwardingR",
            '400': "object",
            '401': "object",
            '402': "object",
            '403': "object",
            '404': "object",
            '409': "object",
            '415': "object",
            '422': "object",
            '429': "object",
            '500': "object",
        }

        return self.api_client.call_api(
            '/blockchain-automations/{blockchain}/{network}/coins-forwarding/automations', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def delete_automatic_coins_forwarding(self, blockchain : Annotated[StrictStr, Field(..., description="Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.")], network : Annotated[StrictStr, Field(..., description="Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.")], reference_id : Annotated[StrictStr, Field(..., description="Represents a unique ID used to reference the specific callback subscription.")], context : Annotated[Optional[StrictStr], Field(description="In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user.")] = None, **kwargs) -> DeleteAutomaticCoinsForwardingR:  # noqa: E501
        """Delete Automatic Coins Forwarding  # noqa: E501

        Through this endpoint customers can delete a forwarding function they have set for **coins** (**not** tokens).    By setting a `fromAddress` and a `toAddress`, and specifying the amount, coins can be transferred between addresses.     A `feePriority` will be returned which represents the fee priority of the automation whether it is \"SLOW\", \"STANDARD\" OR \"FAST\".    {warning}The subscription will work for all incoming transactions until it is deleted. There is no need to do that for every transaction.{/warning}  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_automatic_coins_forwarding(blockchain, network, reference_id, context, async_req=True)
        >>> result = thread.get()

        :param blockchain: Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. (required)
        :type blockchain: str
        :param network: Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks. (required)
        :type network: str
        :param reference_id: Represents a unique ID used to reference the specific callback subscription. (required)
        :type reference_id: str
        :param context: In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user.
        :type context: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: DeleteAutomaticCoinsForwardingR
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the delete_automatic_coins_forwarding_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.delete_automatic_coins_forwarding_with_http_info(blockchain, network, reference_id, context, **kwargs)  # noqa: E501

    @validate_arguments
    def delete_automatic_coins_forwarding_with_http_info(self, blockchain : Annotated[StrictStr, Field(..., description="Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.")], network : Annotated[StrictStr, Field(..., description="Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.")], reference_id : Annotated[StrictStr, Field(..., description="Represents a unique ID used to reference the specific callback subscription.")], context : Annotated[Optional[StrictStr], Field(description="In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user.")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Delete Automatic Coins Forwarding  # noqa: E501

        Through this endpoint customers can delete a forwarding function they have set for **coins** (**not** tokens).    By setting a `fromAddress` and a `toAddress`, and specifying the amount, coins can be transferred between addresses.     A `feePriority` will be returned which represents the fee priority of the automation whether it is \"SLOW\", \"STANDARD\" OR \"FAST\".    {warning}The subscription will work for all incoming transactions until it is deleted. There is no need to do that for every transaction.{/warning}  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_automatic_coins_forwarding_with_http_info(blockchain, network, reference_id, context, async_req=True)
        >>> result = thread.get()

        :param blockchain: Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. (required)
        :type blockchain: str
        :param network: Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks. (required)
        :type network: str
        :param reference_id: Represents a unique ID used to reference the specific callback subscription. (required)
        :type reference_id: str
        :param context: In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user.
        :type context: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(DeleteAutomaticCoinsForwardingR, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'blockchain',
            'network',
            'reference_id',
            'context'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_automatic_coins_forwarding" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['blockchain']:
            _path_params['blockchain'] = _params['blockchain']

        if _params['network']:
            _path_params['network'] = _params['network']

        if _params['reference_id']:
            _path_params['referenceId'] = _params['reference_id']


        # process the query parameters
        _query_params = []
        if _params.get('context') is not None:  # noqa: E501
            _query_params.append(('context', _params['context']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['ApiKey']  # noqa: E501

        _response_types_map = {
            '200': "DeleteAutomaticCoinsForwardingR",
            '400': "DeleteAutomaticCoinsForwarding400Response",
            '401': "DeleteAutomaticCoinsForwarding401Response",
            '402': "ConvertBitcoinCashAddress402Response",
            '403': "DeleteAutomaticCoinsForwarding403Response",
            '404': "GetXRPRippleTransactionDetailsByTransactionID404Response",
            '409': "ConvertBitcoinCashAddress409Response",
            '415': "ConvertBitcoinCashAddress415Response",
            '422': "ConvertBitcoinCashAddress422Response",
            '429': "ConvertBitcoinCashAddress429Response",
            '500': "ConvertBitcoinCashAddress500Response",
        }

        return self.api_client.call_api(
            '/blockchain-automations/{blockchain}/{network}/coins-forwarding/automations/{referenceId}', 'DELETE',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def list_coins_forwarding_automations(self, blockchain : Annotated[StrictStr, Field(..., description="Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.")], network : Annotated[StrictStr, Field(..., description="Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.")], context : Annotated[Optional[StrictStr], Field(description="In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user.")] = None, limit : Annotated[Optional[StrictInt], Field(description="Defines how many items should be returned in the response per page basis.")] = None, offset : Annotated[Optional[StrictInt], Field(description="The starting index of the response items, i.e. where the response should start listing the returned items.")] = None, **kwargs) -> ListCoinsForwardingAutomationsR:  # noqa: E501
        """List Coins Forwarding Automations  # noqa: E501

        Through this endpoint customers can list all of their **coins** forwarding automations (**not** tokens).    Customers can set up automatic forwarding functions for coins by setting a `fromAddress` and a `toAddress`, and specifying the amount that can be transferred between addresses.     A `feePriority` will be returned which represents the fee priority of the automation whether it is \"SLOW\", \"STANDARD\" OR \"FAST\".    {warning}The subscription will work for all transactions until it is deleted. There is no need to do that for every transaction.{/warning}  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_coins_forwarding_automations(blockchain, network, context, limit, offset, async_req=True)
        >>> result = thread.get()

        :param blockchain: Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. (required)
        :type blockchain: str
        :param network: Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks. (required)
        :type network: str
        :param context: In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user.
        :type context: str
        :param limit: Defines how many items should be returned in the response per page basis.
        :type limit: int
        :param offset: The starting index of the response items, i.e. where the response should start listing the returned items.
        :type offset: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ListCoinsForwardingAutomationsR
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the list_coins_forwarding_automations_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.list_coins_forwarding_automations_with_http_info(blockchain, network, context, limit, offset, **kwargs)  # noqa: E501

    @validate_arguments
    def list_coins_forwarding_automations_with_http_info(self, blockchain : Annotated[StrictStr, Field(..., description="Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.")], network : Annotated[StrictStr, Field(..., description="Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.")], context : Annotated[Optional[StrictStr], Field(description="In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user.")] = None, limit : Annotated[Optional[StrictInt], Field(description="Defines how many items should be returned in the response per page basis.")] = None, offset : Annotated[Optional[StrictInt], Field(description="The starting index of the response items, i.e. where the response should start listing the returned items.")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """List Coins Forwarding Automations  # noqa: E501

        Through this endpoint customers can list all of their **coins** forwarding automations (**not** tokens).    Customers can set up automatic forwarding functions for coins by setting a `fromAddress` and a `toAddress`, and specifying the amount that can be transferred between addresses.     A `feePriority` will be returned which represents the fee priority of the automation whether it is \"SLOW\", \"STANDARD\" OR \"FAST\".    {warning}The subscription will work for all transactions until it is deleted. There is no need to do that for every transaction.{/warning}  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_coins_forwarding_automations_with_http_info(blockchain, network, context, limit, offset, async_req=True)
        >>> result = thread.get()

        :param blockchain: Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. (required)
        :type blockchain: str
        :param network: Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks. (required)
        :type network: str
        :param context: In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user.
        :type context: str
        :param limit: Defines how many items should be returned in the response per page basis.
        :type limit: int
        :param offset: The starting index of the response items, i.e. where the response should start listing the returned items.
        :type offset: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ListCoinsForwardingAutomationsR, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'blockchain',
            'network',
            'context',
            'limit',
            'offset'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_coins_forwarding_automations" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['blockchain']:
            _path_params['blockchain'] = _params['blockchain']

        if _params['network']:
            _path_params['network'] = _params['network']


        # process the query parameters
        _query_params = []
        if _params.get('context') is not None:  # noqa: E501
            _query_params.append(('context', _params['context']))

        if _params.get('limit') is not None:  # noqa: E501
            _query_params.append(('limit', _params['limit']))

        if _params.get('offset') is not None:  # noqa: E501
            _query_params.append(('offset', _params['offset']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['ApiKey']  # noqa: E501

        _response_types_map = {
            '200': "ListCoinsForwardingAutomationsR",
            '400': "ListCoinsForwardingAutomations400Response",
            '401': "ListCoinsForwardingAutomations401Response",
            '402': "ConvertBitcoinCashAddress402Response",
            '403': "ListCoinsForwardingAutomations403Response",
            '404': "GetXRPRippleTransactionDetailsByTransactionID404Response",
            '409': "ConvertBitcoinCashAddress409Response",
            '415': "ConvertBitcoinCashAddress415Response",
            '422': "ConvertBitcoinCashAddress422Response",
            '429': "ConvertBitcoinCashAddress429Response",
            '500': "ConvertBitcoinCashAddress500Response",
        }

        return self.api_client.call_api(
            '/blockchain-automations/{blockchain}/{network}/coins-forwarding/automations', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
