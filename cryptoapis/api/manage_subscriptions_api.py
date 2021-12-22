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
from cryptoapis.model.activate_blockchain_event_subscription_r import ActivateBlockchainEventSubscriptionR
from cryptoapis.model.activate_blockchain_event_subscription_rb import ActivateBlockchainEventSubscriptionRB
from cryptoapis.model.delete_blockchain_event_subscription_r import DeleteBlockchainEventSubscriptionR
from cryptoapis.model.inline_response40066 import InlineResponse40066
from cryptoapis.model.inline_response40067 import InlineResponse40067
from cryptoapis.model.inline_response40068 import InlineResponse40068
from cryptoapis.model.inline_response40166 import InlineResponse40166
from cryptoapis.model.inline_response40167 import InlineResponse40167
from cryptoapis.model.inline_response40168 import InlineResponse40168
from cryptoapis.model.inline_response402 import InlineResponse402
from cryptoapis.model.inline_response40366 import InlineResponse40366
from cryptoapis.model.inline_response40367 import InlineResponse40367
from cryptoapis.model.inline_response40368 import InlineResponse40368
from cryptoapis.model.inline_response4041 import InlineResponse4041
from cryptoapis.model.inline_response409 import InlineResponse409
from cryptoapis.model.inline_response415 import InlineResponse415
from cryptoapis.model.inline_response422 import InlineResponse422
from cryptoapis.model.inline_response429 import InlineResponse429
from cryptoapis.model.inline_response500 import InlineResponse500
from cryptoapis.model.list_blockchain_events_subscriptions_r import ListBlockchainEventsSubscriptionsR


class ManageSubscriptionsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.activate_blockchain_event_subscription_endpoint = _Endpoint(
            settings={
                'response_type': (ActivateBlockchainEventSubscriptionR,),
                'auth': [
                    'ApiKey'
                ],
                'endpoint_path': '/blockchain-events/subscriptions/{referenceId}/activate',
                'operation_id': 'activate_blockchain_event_subscription',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'reference_id',
                    'context',
                    'activate_blockchain_event_subscription_rb',
                ],
                'required': [
                    'reference_id',
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
                    'reference_id':
                        (str,),
                    'context':
                        (str,),
                    'activate_blockchain_event_subscription_rb':
                        (ActivateBlockchainEventSubscriptionRB,),
                },
                'attribute_map': {
                    'reference_id': 'referenceId',
                    'context': 'context',
                },
                'location_map': {
                    'reference_id': 'path',
                    'context': 'query',
                    'activate_blockchain_event_subscription_rb': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.delete_blockchain_event_subscription_endpoint = _Endpoint(
            settings={
                'response_type': (DeleteBlockchainEventSubscriptionR,),
                'auth': [
                    'ApiKey'
                ],
                'endpoint_path': '/blockchain-events/{blockchain}/{network}/subscriptions/{referenceId}',
                'operation_id': 'delete_blockchain_event_subscription',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'blockchain',
                    'network',
                    'reference_id',
                    'context',
                ],
                'required': [
                    'blockchain',
                    'network',
                    'reference_id',
                ],
                'nullable': [
                ],
                'enum': [
                    'blockchain',
                    'network',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('blockchain',): {

                        "BITCOIN": "bitcoin",
                        "BITCOIN-CASH": "bitcoin-cash",
                        "LITECOIN": "litecoin",
                        "DOGECOIN": "dogecoin",
                        "DASH": "dash",
                        "ETHEREUM": "ethereum",
                        "ETHEREUM-CLASSIC": "ethereum-classic",
                        "XRP": "xrp",
                        "ZILLIQA": "zilliqa",
                        "BINANCE-SMART-CHAIN": "binance-smart-chain",
                        "ZCASH": "zcash",
                        "BITCOIN-SATOSHI-VISION": "bitcoin-satoshi-vision"
                    },
                    ('network',): {

                        "MAINNET": "mainnet",
                        "TESTNET": "testnet",
                        "ROPSTEN": "ropsten",
                        "MORDOR": "mordor"
                    },
                },
                'openapi_types': {
                    'blockchain':
                        (str,),
                    'network':
                        (str,),
                    'reference_id':
                        (str,),
                    'context':
                        (str,),
                },
                'attribute_map': {
                    'blockchain': 'blockchain',
                    'network': 'network',
                    'reference_id': 'referenceId',
                    'context': 'context',
                },
                'location_map': {
                    'blockchain': 'path',
                    'network': 'path',
                    'reference_id': 'path',
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
        self.list_blockchain_events_subscriptions_endpoint = _Endpoint(
            settings={
                'response_type': (ListBlockchainEventsSubscriptionsR,),
                'auth': [
                    'ApiKey'
                ],
                'endpoint_path': '/blockchain-events/{blockchain}/{network}/subscriptions',
                'operation_id': 'list_blockchain_events_subscriptions',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'blockchain',
                    'network',
                    'context',
                    'limit',
                    'offset',
                ],
                'required': [
                    'blockchain',
                    'network',
                ],
                'nullable': [
                ],
                'enum': [
                    'blockchain',
                    'network',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('blockchain',): {

                        "BITCOIN": "bitcoin",
                        "BITCOIN-CASH": "bitcoin-cash",
                        "LITECOIN": "litecoin",
                        "DOGECOIN": "dogecoin",
                        "DASH": "dash",
                        "ETHEREUM": "ethereum",
                        "ETHEREUM-CLASSIC": "ethereum-classic",
                        "XRP": "xrp",
                        "ZILLIQA": "zilliqa",
                        "BINANCE-SMART-CHAIN": "binance-smart-chain",
                        "ZCASH": "zcash"
                    },
                    ('network',): {

                        "MAINNET": "mainnet",
                        "TESTNET": "testnet",
                        "ROPSTEN": "ropsten",
                        "MORDOR": "mordor"
                    },
                },
                'openapi_types': {
                    'blockchain':
                        (str,),
                    'network':
                        (str,),
                    'context':
                        (str,),
                    'limit':
                        (int,),
                    'offset':
                        (int,),
                },
                'attribute_map': {
                    'blockchain': 'blockchain',
                    'network': 'network',
                    'context': 'context',
                    'limit': 'limit',
                    'offset': 'offset',
                },
                'location_map': {
                    'blockchain': 'path',
                    'network': 'path',
                    'context': 'query',
                    'limit': 'query',
                    'offset': 'query',
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

    def activate_blockchain_event_subscription(
        self,
        reference_id,
        **kwargs
    ):
        """Activate Blockchain Event Subscription  # noqa: E501

        Through this endpoint customers can reactivate an event subscription (callback) which has been deactivated by the system. Deactivations could happen due to various reasons, most often \"maximum retry attempts reached\".  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.activate_blockchain_event_subscription(reference_id, async_req=True)
        >>> result = thread.get()

        Args:
            reference_id (str): Represents a unique ID used to reference the specific callback subscription.

        Keyword Args:
            context (str): In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user.. [optional]
            activate_blockchain_event_subscription_rb (ActivateBlockchainEventSubscriptionRB): [optional]
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
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            ActivateBlockchainEventSubscriptionR
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
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['reference_id'] = \
            reference_id
        return self.activate_blockchain_event_subscription_endpoint.call_with_http_info(**kwargs)

    def delete_blockchain_event_subscription(
        self,
        blockchain,
        network,
        reference_id,
        **kwargs
    ):
        """Delete Blockchain Event Subscription  # noqa: E501

        Through this endpoint the customer can delete blockchain event subscriptions they have by attributes `referenceId` and `network`.    Currently Crypto APIs 2.0 offers certain Blockchain event endpoints which allow the user to subscribe for one/a few/all and receive callback notifications when the specific event occurs.    {note}To have an operational callback subscription, you need to first verify a domain for the Callback URL. Please see more information on Callbacks [here](https://developers.cryptoapis.io/technical-documentation/general-information/callbacks#callback-url).{/note}    {warning}Crypto APIs will notify the user **only when** the event occurs. There are cases when the specific event doesn't happen at all, or takes a long time to do so. A callback notification **will not** be sent if the event does not or cannot occur, or will take long time to occur.{/warning}  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_blockchain_event_subscription(blockchain, network, reference_id, async_req=True)
        >>> result = thread.get()

        Args:
            blockchain (str): Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
            network (str): Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
            reference_id (str): Represents a unique ID used to reference the specific callback subscription.

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
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            DeleteBlockchainEventSubscriptionR
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
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['blockchain'] = \
            blockchain
        kwargs['network'] = \
            network
        kwargs['reference_id'] = \
            reference_id
        return self.delete_blockchain_event_subscription_endpoint.call_with_http_info(**kwargs)

    def list_blockchain_events_subscriptions(
        self,
        blockchain,
        network,
        **kwargs
    ):
        """List Blockchain Events Subscriptions  # noqa: E501

        Through this endpoint the customer can obtain a list of their callback subscriptions for the available Blockchain events.    Currently Crypto APIs 2.0 offers certain Blockchain event endpoints which allow the user to subscribe for one/a few/all and receive callback notifications when the specific event occurs.    {note}To have an operational callback subscription, you need to first verify a domain for the Callback URL. Please see more information on Callbacks [here](https://developers.cryptoapis.io/technical-documentation/general-information/callbacks#callback-url).{/note}  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_blockchain_events_subscriptions(blockchain, network, async_req=True)
        >>> result = thread.get()

        Args:
            blockchain (str): Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
            network (str): Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.

        Keyword Args:
            context (str): In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user.. [optional]
            limit (int): Defines how many items should be returned in the response per page basis.. [optional] if omitted the server will use the default value of 50
            offset (int): The starting index of the response items, i.e. where the response should start listing the returned items.. [optional] if omitted the server will use the default value of 0
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
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            ListBlockchainEventsSubscriptionsR
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
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['blockchain'] = \
            blockchain
        kwargs['network'] = \
            network
        return self.list_blockchain_events_subscriptions_endpoint.call_with_http_info(**kwargs)

