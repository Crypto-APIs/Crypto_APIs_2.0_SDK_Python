# cryptoapis.OmniLayerApi

All URIs are relative to *https://rest.cryptoapis.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_omni_transaction_details_by_transaction_id__txid**](OmniLayerApi.md#get_omni_transaction_details_by_transaction_id__txid) | **GET** /blockchain-data/{blockchain}/{network}/omni/transactions/{transactionId} | Get Omni Transaction Details By Transaction ID (Txid)
[**get_unconfirmed_omni_transaction_by_transaction_id__txid**](OmniLayerApi.md#get_unconfirmed_omni_transaction_by_transaction_id__txid) | **GET** /blockchain-data/{blockchain}/{network}/omni/transactions-unconfirmed/{transactionId} | Get Unconfirmed Omni Transaction By Transaction ID (Txid)
[**list_omni_tokens_by_address**](OmniLayerApi.md#list_omni_tokens_by_address) | **GET** /blockchain-data/{blockchain}/{network}/omni/addresses/{address} | List Omni Tokens By Address
[**list_omni_transactions_by_address**](OmniLayerApi.md#list_omni_transactions_by_address) | **GET** /blockchain-data/{blockchain}/{network}/omni/addresses/{address}/transactions | List Omni Transactions By Address
[**list_omni_transactions_by_block_hash**](OmniLayerApi.md#list_omni_transactions_by_block_hash) | **GET** /blockchain-data/{blockchain}/{network}/omni/blocks/hash/{blockHash}/transactions | List Omni Transactions By Block Hash
[**list_omni_transactions_by_block_height**](OmniLayerApi.md#list_omni_transactions_by_block_height) | **GET** /blockchain-data/{blockchain}/{network}/omni/blocks/height/{blockHeight}/transactions | List Omni Transactions By Block Height
[**list_unconfirmed_omni_transactions_by_address**](OmniLayerApi.md#list_unconfirmed_omni_transactions_by_address) | **GET** /blockchain-data/{blockchain}/{network}/omni/address-transactions-unconfirmed/{address} | List Unconfirmed Omni Transactions By Address
[**list_unconfirmed_omni_transactions_by_property_id**](OmniLayerApi.md#list_unconfirmed_omni_transactions_by_property_id) | **GET** /blockchain-data/{blockchain}/{network}/omni/properties/{propertyId}/transactions | List Unconfirmed Omni Transactions By Property ID


# **get_omni_transaction_details_by_transaction_id__txid**
> GetOmniTransactionDetailsByTransactionIDTxidR get_omni_transaction_details_by_transaction_id__txid(network, transaction_id)

Get Omni Transaction Details By Transaction ID (Txid)

Through this endpoint customers can obtain details about an Omni transaction by the transaction's unique identifier. The transaction can return information such as hash, height, time of creation in Unix timestamp, etc.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import omni_layer_api
from cryptoapis.model.get_omni_transaction_details_by_transaction_id_txid_r import GetOmniTransactionDetailsByTransactionIDTxidR
from cryptoapis.model.get_address_details402_response import GetAddressDetails402Response
from cryptoapis.model.get_transaction_details_by_transaction_id404_response import GetTransactionDetailsByTransactionID404Response
from cryptoapis.model.get_address_details500_response import GetAddressDetails500Response
from cryptoapis.model.get_address_details415_response import GetAddressDetails415Response
from cryptoapis.model.get_address_details422_response import GetAddressDetails422Response
from cryptoapis.model.get_address_details409_response import GetAddressDetails409Response
from cryptoapis.model.get_omni_transaction_details_by_transaction_id_txid401_response import GetOmniTransactionDetailsByTransactionIDTxid401Response
from cryptoapis.model.get_address_details429_response import GetAddressDetails429Response
from cryptoapis.model.get_omni_transaction_details_by_transaction_id_txid400_response import GetOmniTransactionDetailsByTransactionIDTxid400Response
from cryptoapis.model.get_omni_transaction_details_by_transaction_id_txid403_response import GetOmniTransactionDetailsByTransactionIDTxid403Response
from pprint import pprint
# Defining the host is optional and defaults to https://rest.cryptoapis.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cryptoapis.Configuration(
    host = "https://rest.cryptoapis.io/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with cryptoapis.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = omni_layer_api.OmniLayerApi(api_client)
    network = "testnet" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    transaction_id = "d237ff4a681617b767bf22c4e1e8f5115b95c8c168d6cf53bbdec68529f91ecb" # str | Represents the unique identifier of a transaction, i.e. it could be `transactionId` in UTXO-based protocols like Bitcoin, and transaction `hash` in Ethereum blockchain.
    context = "yourExampleString" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Omni Transaction Details By Transaction ID (Txid)
        api_response = api_instance.get_omni_transaction_details_by_transaction_id__txid(network, transaction_id)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling OmniLayerApi->get_omni_transaction_details_by_transaction_id__txid: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Omni Transaction Details By Transaction ID (Txid)
        api_response = api_instance.get_omni_transaction_details_by_transaction_id__txid(network, transaction_id, context=context)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling OmniLayerApi->get_omni_transaction_details_by_transaction_id__txid: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. |
 **transaction_id** | **str**| Represents the unique identifier of a transaction, i.e. it could be &#x60;transactionId&#x60; in UTXO-based protocols like Bitcoin, and transaction &#x60;hash&#x60; in Ethereum blockchain. |
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. | defaults to "bitcoin"
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]

### Return type

[**GetOmniTransactionDetailsByTransactionIDTxidR**](GetOmniTransactionDetailsByTransactionIDTxidR.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request has been successful. |  -  |
**400** | 400 |  -  |
**401** | 401 |  -  |
**402** | You have insufficient credits. Please upgrade your plan from your Dashboard or contact our team via email. |  -  |
**403** | 403 |  -  |
**404** | The specified transaction has not been found on the specific blockchain. |  -  |
**409** | The data provided seems to be invalid. |  -  |
**415** | The selected Media Type is unavailable. The Content-Type header should be &#39;application/json&#39;. |  -  |
**422** | Your request body for POST requests must have a structure of { data: { item: [...properties] } } |  -  |
**429** | The request limit has been reached. There can be maximum {requests} requests per {seconds} second(s) made. Please contact our team via email if you need more or upgrade your plan. |  -  |
**500** | An unexpected server error has occurred, we are working to fix this. Please try again later and in case it occurs again please report it to our team via email. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_unconfirmed_omni_transaction_by_transaction_id__txid**
> GetUnconfirmedOmniTransactionByTransactionIDTxidR get_unconfirmed_omni_transaction_by_transaction_id__txid(network, transaction_id)

Get Unconfirmed Omni Transaction By Transaction ID (Txid)

Through this endpoint customers can obtain information on unconfirmed Omni transactions by an attribute `transactionId`. The transaction can have information such as hash, height, time of creation in Unix timestamp, etc.    Unconfirmed transactions are usually put in the Mempool and await verification so that they can be added to a block.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import omni_layer_api
from cryptoapis.model.get_unconfirmed_omni_transaction_by_transaction_id_txid400_response import GetUnconfirmedOmniTransactionByTransactionIDTxid400Response
from cryptoapis.model.get_unconfirmed_omni_transaction_by_transaction_id_txid_r import GetUnconfirmedOmniTransactionByTransactionIDTxidR
from cryptoapis.model.get_unconfirmed_omni_transaction_by_transaction_id_txid401_response import GetUnconfirmedOmniTransactionByTransactionIDTxid401Response
from cryptoapis.model.get_address_details402_response import GetAddressDetails402Response
from cryptoapis.model.get_transaction_details_by_transaction_id404_response import GetTransactionDetailsByTransactionID404Response
from cryptoapis.model.get_address_details500_response import GetAddressDetails500Response
from cryptoapis.model.get_address_details415_response import GetAddressDetails415Response
from cryptoapis.model.get_address_details422_response import GetAddressDetails422Response
from cryptoapis.model.get_address_details409_response import GetAddressDetails409Response
from cryptoapis.model.get_address_details429_response import GetAddressDetails429Response
from cryptoapis.model.get_unconfirmed_omni_transaction_by_transaction_id_txid403_response import GetUnconfirmedOmniTransactionByTransactionIDTxid403Response
from pprint import pprint
# Defining the host is optional and defaults to https://rest.cryptoapis.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cryptoapis.Configuration(
    host = "https://rest.cryptoapis.io/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with cryptoapis.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = omni_layer_api.OmniLayerApi(api_client)
    network = "testnet" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    transaction_id = "92f17d3d16a1baf7de570a86179cc263cb9866c66778feec2dce111430f41c08" # str | Represents the unique identifier of a transaction, i.e. it could be `transactionId` in UTXO-based protocols like Bitcoin, and transaction `hash` in Ethereum blockchain.
    context = "yourExampleString" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Unconfirmed Omni Transaction By Transaction ID (Txid)
        api_response = api_instance.get_unconfirmed_omni_transaction_by_transaction_id__txid(network, transaction_id)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling OmniLayerApi->get_unconfirmed_omni_transaction_by_transaction_id__txid: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Unconfirmed Omni Transaction By Transaction ID (Txid)
        api_response = api_instance.get_unconfirmed_omni_transaction_by_transaction_id__txid(network, transaction_id, context=context)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling OmniLayerApi->get_unconfirmed_omni_transaction_by_transaction_id__txid: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. |
 **transaction_id** | **str**| Represents the unique identifier of a transaction, i.e. it could be &#x60;transactionId&#x60; in UTXO-based protocols like Bitcoin, and transaction &#x60;hash&#x60; in Ethereum blockchain. |
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. | defaults to "bitcoin"
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]

### Return type

[**GetUnconfirmedOmniTransactionByTransactionIDTxidR**](GetUnconfirmedOmniTransactionByTransactionIDTxidR.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request has been successful. |  -  |
**400** | 400 |  -  |
**401** | 401 |  -  |
**402** | You have insufficient credits. Please upgrade your plan from your Dashboard or contact our team via email. |  -  |
**403** | 403 |  -  |
**404** | The specified transaction has not been found on the specific blockchain. |  -  |
**409** | The data provided seems to be invalid. |  -  |
**415** | The selected Media Type is unavailable. The Content-Type header should be &#39;application/json&#39;. |  -  |
**422** | Your request body for POST requests must have a structure of { data: { item: [...properties] } } |  -  |
**429** | The request limit has been reached. There can be maximum {requests} requests per {seconds} second(s) made. Please contact our team via email if you need more or upgrade your plan. |  -  |
**500** | An unexpected server error has occurred, we are working to fix this. Please try again later and in case it occurs again please report it to our team via email. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_omni_tokens_by_address**
> ListOmniTokensByAddressR list_omni_tokens_by_address(network, address)

List Omni Tokens By Address

Through this endpoint the customer can receive basic information about a given Omni address based on confirmed/synced blocks only. In the case where there are any incoming or outgoing **unconfirmed** transactions for the specific address, they **will not** be counted or calculated here.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import omni_layer_api
from cryptoapis.model.list_omni_tokens_by_address401_response import ListOmniTokensByAddress401Response
from cryptoapis.model.list_omni_tokens_by_address400_response import ListOmniTokensByAddress400Response
from cryptoapis.model.get_address_details402_response import GetAddressDetails402Response
from cryptoapis.model.get_address_details500_response import GetAddressDetails500Response
from cryptoapis.model.get_address_details415_response import GetAddressDetails415Response
from cryptoapis.model.get_address_details422_response import GetAddressDetails422Response
from cryptoapis.model.list_omni_tokens_by_address_r import ListOmniTokensByAddressR
from cryptoapis.model.get_address_details409_response import GetAddressDetails409Response
from cryptoapis.model.get_address_details429_response import GetAddressDetails429Response
from cryptoapis.model.list_omni_tokens_by_address403_response import ListOmniTokensByAddress403Response
from pprint import pprint
# Defining the host is optional and defaults to https://rest.cryptoapis.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cryptoapis.Configuration(
    host = "https://rest.cryptoapis.io/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with cryptoapis.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = omni_layer_api.OmniLayerApi(api_client)
    network = "testnet" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    address = "mi7iSsKcvyFYNsiYdDZqJmH75RmoHomwmo" # str | Represents the public address, which is a compressed and shortened form of a public key.
    context = "yourExampleString" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List Omni Tokens By Address
        api_response = api_instance.list_omni_tokens_by_address(network, address)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling OmniLayerApi->list_omni_tokens_by_address: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Omni Tokens By Address
        api_response = api_instance.list_omni_tokens_by_address(network, address, context=context)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling OmniLayerApi->list_omni_tokens_by_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. |
 **address** | **str**| Represents the public address, which is a compressed and shortened form of a public key. |
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. | defaults to "bitcoin"
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]

### Return type

[**ListOmniTokensByAddressR**](ListOmniTokensByAddressR.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request has been successful. |  -  |
**400** | 400 |  -  |
**401** | 401 |  -  |
**402** | You have insufficient credits. Please upgrade your plan from your Dashboard or contact our team via email. |  -  |
**403** | 403 |  -  |
**409** | The data provided seems to be invalid. |  -  |
**415** | The selected Media Type is unavailable. The Content-Type header should be &#39;application/json&#39;. |  -  |
**422** | Your request body for POST requests must have a structure of { data: { item: [...properties] } } |  -  |
**429** | The request limit has been reached. There can be maximum {requests} requests per {seconds} second(s) made. Please contact our team via email if you need more or upgrade your plan. |  -  |
**500** | An unexpected server error has occurred, we are working to fix this. Please try again later and in case it occurs again please report it to our team via email. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_omni_transactions_by_address**
> ListOmniTransactionsByAddressR list_omni_transactions_by_address(network, address)

List Omni Transactions By Address

This endpoint will list Omni transactions by an attribute `address`. The transactions listed will detail additional information such as hash, height, time of creation in Unix timestamp, etc.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import omni_layer_api
from cryptoapis.model.list_omni_transactions_by_address403_response import ListOmniTransactionsByAddress403Response
from cryptoapis.model.get_address_details402_response import GetAddressDetails402Response
from cryptoapis.model.get_address_details500_response import GetAddressDetails500Response
from cryptoapis.model.get_address_details415_response import GetAddressDetails415Response
from cryptoapis.model.get_address_details422_response import GetAddressDetails422Response
from cryptoapis.model.get_address_details409_response import GetAddressDetails409Response
from cryptoapis.model.get_address_details429_response import GetAddressDetails429Response
from cryptoapis.model.list_omni_transactions_by_address_r import ListOmniTransactionsByAddressR
from cryptoapis.model.list_omni_transactions_by_address400_response import ListOmniTransactionsByAddress400Response
from cryptoapis.model.list_omni_transactions_by_address401_response import ListOmniTransactionsByAddress401Response
from pprint import pprint
# Defining the host is optional and defaults to https://rest.cryptoapis.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cryptoapis.Configuration(
    host = "https://rest.cryptoapis.io/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with cryptoapis.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = omni_layer_api.OmniLayerApi(api_client)
    network = "testnet" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    address = "mi7iSsKcvyFYNsiYdDZqJmH75RmoHomwmo" # str | Represents the public address, which is a compressed and shortened form of a public key.
    context = "yourExampleString" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    limit = 50 # int | Defines how many items should be returned in the response per page basis. (optional) if omitted the server will use the default value of 50
    offset = 0 # int | The starting index of the response items, i.e. where the response should start listing the returned items. (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    try:
        # List Omni Transactions By Address
        api_response = api_instance.list_omni_transactions_by_address(network, address)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling OmniLayerApi->list_omni_transactions_by_address: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Omni Transactions By Address
        api_response = api_instance.list_omni_transactions_by_address(network, address, context=context, limit=limit, offset=offset)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling OmniLayerApi->list_omni_transactions_by_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. |
 **address** | **str**| Represents the public address, which is a compressed and shortened form of a public key. |
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. | defaults to "bitcoin"
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]
 **limit** | **int**| Defines how many items should be returned in the response per page basis. | [optional] if omitted the server will use the default value of 50
 **offset** | **int**| The starting index of the response items, i.e. where the response should start listing the returned items. | [optional] if omitted the server will use the default value of 0

### Return type

[**ListOmniTransactionsByAddressR**](ListOmniTransactionsByAddressR.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request has been successful. |  -  |
**400** | 400 |  -  |
**401** | 401 |  -  |
**402** | You have insufficient credits. Please upgrade your plan from your Dashboard or contact our team via email. |  -  |
**403** | 403 |  -  |
**409** | The data provided seems to be invalid. |  -  |
**415** | The selected Media Type is unavailable. The Content-Type header should be &#39;application/json&#39;. |  -  |
**422** | Your request body for POST requests must have a structure of { data: { item: [...properties] } } |  -  |
**429** | The request limit has been reached. There can be maximum {requests} requests per {seconds} second(s) made. Please contact our team via email if you need more or upgrade your plan. |  -  |
**500** | An unexpected server error has occurred, we are working to fix this. Please try again later and in case it occurs again please report it to our team via email. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_omni_transactions_by_block_hash**
> ListOmniTransactionsByBlockHashR list_omni_transactions_by_block_hash(network, block_hash)

List Omni Transactions By Block Hash

This endpoint will list Omni transactions by an attribute `transactionHash`. The transactions listed will detail additional information such as addresses, height, time of creation in Unix timestamp, etc.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import omni_layer_api
from cryptoapis.model.list_omni_transactions_by_block_hash400_response import ListOmniTransactionsByBlockHash400Response
from cryptoapis.model.get_address_details402_response import GetAddressDetails402Response
from cryptoapis.model.get_address_details500_response import GetAddressDetails500Response
from cryptoapis.model.get_address_details415_response import GetAddressDetails415Response
from cryptoapis.model.get_address_details422_response import GetAddressDetails422Response
from cryptoapis.model.get_address_details409_response import GetAddressDetails409Response
from cryptoapis.model.get_address_details429_response import GetAddressDetails429Response
from cryptoapis.model.list_omni_transactions_by_block_hash401_response import ListOmniTransactionsByBlockHash401Response
from cryptoapis.model.list_omni_transactions_by_block_hash_r import ListOmniTransactionsByBlockHashR
from cryptoapis.model.list_omni_transactions_by_block_hash403_response import ListOmniTransactionsByBlockHash403Response
from pprint import pprint
# Defining the host is optional and defaults to https://rest.cryptoapis.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cryptoapis.Configuration(
    host = "https://rest.cryptoapis.io/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with cryptoapis.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = omni_layer_api.OmniLayerApi(api_client)
    network = "testnet" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    block_hash = "000000000000001f50c9d33d122562daa7fc9582df0b415e626216c37d015818" # str | Represents the hash of the block, which is its unique identifier. It represents a cryptographic digital fingerprint made by hashing the block header twice through the SHA256 algorithm.
    context = "yourExampleString" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    limit = 50 # int | Defines how many items should be returned in the response per page basis. (optional) if omitted the server will use the default value of 50
    offset = 0 # int | The starting index of the response items, i.e. where the response should start listing the returned items. (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    try:
        # List Omni Transactions By Block Hash
        api_response = api_instance.list_omni_transactions_by_block_hash(network, block_hash)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling OmniLayerApi->list_omni_transactions_by_block_hash: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Omni Transactions By Block Hash
        api_response = api_instance.list_omni_transactions_by_block_hash(network, block_hash, context=context, limit=limit, offset=offset)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling OmniLayerApi->list_omni_transactions_by_block_hash: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. |
 **block_hash** | **str**| Represents the hash of the block, which is its unique identifier. It represents a cryptographic digital fingerprint made by hashing the block header twice through the SHA256 algorithm. |
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. | defaults to "bitcoin"
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]
 **limit** | **int**| Defines how many items should be returned in the response per page basis. | [optional] if omitted the server will use the default value of 50
 **offset** | **int**| The starting index of the response items, i.e. where the response should start listing the returned items. | [optional] if omitted the server will use the default value of 0

### Return type

[**ListOmniTransactionsByBlockHashR**](ListOmniTransactionsByBlockHashR.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request has been successfull. |  -  |
**400** | 400 |  -  |
**401** | 401 |  -  |
**402** | You have insufficient credits. Please upgrade your plan from your Dashboard or contact our team via email. |  -  |
**403** | 403 |  -  |
**409** | The data provided seems to be invalid. |  -  |
**415** | The selected Media Type is unavailable. The Content-Type header should be &#39;application/json&#39;. |  -  |
**422** | Your request body for POST requests must have a structure of { data: { item: [...properties] } } |  -  |
**429** | The request limit has been reached. There can be maximum {requests} requests per {seconds} second(s) made. Please contact our team via email if you need more or upgrade your plan. |  -  |
**500** | An unexpected server error has occurred, we are working to fix this. Please try again later and in case it occurs again please report it to our team via email. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_omni_transactions_by_block_height**
> ListOmniTransactionsByBlockHeightR list_omni_transactions_by_block_height(network, block_height)

List Omni Transactions By Block Height

This endpoint will list Omni transactions by an attribute `blockHeight`. The transactions listed will detail additional information such as hash, addresses, time of creation in Unix timestamp, etc.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import omni_layer_api
from cryptoapis.model.get_address_details402_response import GetAddressDetails402Response
from cryptoapis.model.get_address_details500_response import GetAddressDetails500Response
from cryptoapis.model.get_address_details415_response import GetAddressDetails415Response
from cryptoapis.model.get_address_details422_response import GetAddressDetails422Response
from cryptoapis.model.list_omni_transactions_by_block_height400_response import ListOmniTransactionsByBlockHeight400Response
from cryptoapis.model.get_address_details409_response import GetAddressDetails409Response
from cryptoapis.model.get_address_details429_response import GetAddressDetails429Response
from cryptoapis.model.list_omni_transactions_by_block_height401_response import ListOmniTransactionsByBlockHeight401Response
from cryptoapis.model.list_omni_transactions_by_block_height403_response import ListOmniTransactionsByBlockHeight403Response
from cryptoapis.model.list_omni_transactions_by_block_height_r import ListOmniTransactionsByBlockHeightR
from pprint import pprint
# Defining the host is optional and defaults to https://rest.cryptoapis.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cryptoapis.Configuration(
    host = "https://rest.cryptoapis.io/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with cryptoapis.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = omni_layer_api.OmniLayerApi(api_client)
    network = "testnet" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    block_height = "1941222" # str | Represents the number of blocks in the blockchain preceding this specific block. Block numbers have no gaps. A blockchain usually starts with block 0 called the \"Genesis block\".
    context = "yourExampleString" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    limit = 50 # int | Defines how many items should be returned in the response per page basis. (optional) if omitted the server will use the default value of 50
    offset = 0 # int | The starting index of the response items, i.e. where the response should start listing the returned items. (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    try:
        # List Omni Transactions By Block Height
        api_response = api_instance.list_omni_transactions_by_block_height(network, block_height)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling OmniLayerApi->list_omni_transactions_by_block_height: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Omni Transactions By Block Height
        api_response = api_instance.list_omni_transactions_by_block_height(network, block_height, context=context, limit=limit, offset=offset)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling OmniLayerApi->list_omni_transactions_by_block_height: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. |
 **block_height** | **str**| Represents the number of blocks in the blockchain preceding this specific block. Block numbers have no gaps. A blockchain usually starts with block 0 called the \&quot;Genesis block\&quot;. |
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. | defaults to "bitcoin"
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]
 **limit** | **int**| Defines how many items should be returned in the response per page basis. | [optional] if omitted the server will use the default value of 50
 **offset** | **int**| The starting index of the response items, i.e. where the response should start listing the returned items. | [optional] if omitted the server will use the default value of 0

### Return type

[**ListOmniTransactionsByBlockHeightR**](ListOmniTransactionsByBlockHeightR.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request has been successful. |  -  |
**400** | 400 |  -  |
**401** | 401 |  -  |
**402** | You have insufficient credits. Please upgrade your plan from your Dashboard or contact our team via email. |  -  |
**403** | 403 |  -  |
**409** | The data provided seems to be invalid. |  -  |
**415** | The selected Media Type is unavailable. The Content-Type header should be &#39;application/json&#39;. |  -  |
**422** | Your request body for POST requests must have a structure of { data: { item: [...properties] } } |  -  |
**429** | The request limit has been reached. There can be maximum {requests} requests per {seconds} second(s) made. Please contact our team via email if you need more or upgrade your plan. |  -  |
**500** | An unexpected server error has occurred, we are working to fix this. Please try again later and in case it occurs again please report it to our team via email. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_unconfirmed_omni_transactions_by_address**
> ListUnconfirmedOmniTransactionsByAddressR list_unconfirmed_omni_transactions_by_address(network, address)

List Unconfirmed Omni Transactions By Address

This endpoint will list unconfirmed Omni transactions by an attribute `address`. The transactions listed will detail additional information such as hash, height, time of creation in Unix timestamp, etc.    Unconfirmed transactions are usually put in the Mempool and await verification so that they can be added to a block.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import omni_layer_api
from cryptoapis.model.list_unconfirmed_omni_transactions_by_address401_response import ListUnconfirmedOmniTransactionsByAddress401Response
from cryptoapis.model.get_address_details402_response import GetAddressDetails402Response
from cryptoapis.model.get_address_details500_response import GetAddressDetails500Response
from cryptoapis.model.get_address_details415_response import GetAddressDetails415Response
from cryptoapis.model.get_address_details422_response import GetAddressDetails422Response
from cryptoapis.model.list_unconfirmed_omni_transactions_by_address_r import ListUnconfirmedOmniTransactionsByAddressR
from cryptoapis.model.get_address_details409_response import GetAddressDetails409Response
from cryptoapis.model.get_address_details429_response import GetAddressDetails429Response
from cryptoapis.model.list_unconfirmed_omni_transactions_by_address403_response import ListUnconfirmedOmniTransactionsByAddress403Response
from cryptoapis.model.list_unconfirmed_omni_transactions_by_address400_response import ListUnconfirmedOmniTransactionsByAddress400Response
from pprint import pprint
# Defining the host is optional and defaults to https://rest.cryptoapis.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cryptoapis.Configuration(
    host = "https://rest.cryptoapis.io/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with cryptoapis.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = omni_layer_api.OmniLayerApi(api_client)
    network = "testnet" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    address = "mi7iSsKcvyFYNsiYdDZqJmH75RmoHomwmo" # str | Represents the public address, which is a compressed and shortened form of a public key.
    context = "yourExampleString" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    limit = 50 # int | Defines how many items should be returned in the response per page basis. (optional) if omitted the server will use the default value of 50
    offset = 0 # int | The starting index of the response items, i.e. where the response should start listing the returned items. (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    try:
        # List Unconfirmed Omni Transactions By Address
        api_response = api_instance.list_unconfirmed_omni_transactions_by_address(network, address)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling OmniLayerApi->list_unconfirmed_omni_transactions_by_address: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Unconfirmed Omni Transactions By Address
        api_response = api_instance.list_unconfirmed_omni_transactions_by_address(network, address, context=context, limit=limit, offset=offset)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling OmniLayerApi->list_unconfirmed_omni_transactions_by_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. |
 **address** | **str**| Represents the public address, which is a compressed and shortened form of a public key. |
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. | defaults to "bitcoin"
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]
 **limit** | **int**| Defines how many items should be returned in the response per page basis. | [optional] if omitted the server will use the default value of 50
 **offset** | **int**| The starting index of the response items, i.e. where the response should start listing the returned items. | [optional] if omitted the server will use the default value of 0

### Return type

[**ListUnconfirmedOmniTransactionsByAddressR**](ListUnconfirmedOmniTransactionsByAddressR.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request has been successful. |  -  |
**400** | 400 |  -  |
**401** | 401 |  -  |
**402** | You have insufficient credits. Please upgrade your plan from your Dashboard or contact our team via email. |  -  |
**403** | 403 |  -  |
**409** | The data provided seems to be invalid. |  -  |
**415** | The selected Media Type is unavailable. The Content-Type header should be &#39;application/json&#39;. |  -  |
**422** | Your request body for POST requests must have a structure of { data: { item: [...properties] } } |  -  |
**429** | The request limit has been reached. There can be maximum {requests} requests per {seconds} second(s) made. Please contact our team via email if you need more or upgrade your plan. |  -  |
**500** | An unexpected server error has occurred, we are working to fix this. Please try again later and in case it occurs again please report it to our team via email. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_unconfirmed_omni_transactions_by_property_id**
> ListUnconfirmedOmniTransactionsByPropertyIDR list_unconfirmed_omni_transactions_by_property_id(network, property_id)

List Unconfirmed Omni Transactions By Property ID

This endpoint will list unconfirmed Omni transactions by an attribute `propertyId`. The transactions listed will detail additional information such as hash, height, time of creation in Unix timestamp, etc.    Unconfirmed transactions are usually put in the Mempool and await verification so that they can be added to a block.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import omni_layer_api
from cryptoapis.model.get_address_details402_response import GetAddressDetails402Response
from cryptoapis.model.get_address_details500_response import GetAddressDetails500Response
from cryptoapis.model.list_unconfirmed_omni_transactions_by_property_id400_response import ListUnconfirmedOmniTransactionsByPropertyID400Response
from cryptoapis.model.get_address_details415_response import GetAddressDetails415Response
from cryptoapis.model.get_address_details422_response import GetAddressDetails422Response
from cryptoapis.model.list_unconfirmed_omni_transactions_by_property_id401_response import ListUnconfirmedOmniTransactionsByPropertyID401Response
from cryptoapis.model.list_unconfirmed_omni_transactions_by_property_id403_response import ListUnconfirmedOmniTransactionsByPropertyID403Response
from cryptoapis.model.get_address_details409_response import GetAddressDetails409Response
from cryptoapis.model.list_unconfirmed_omni_transactions_by_property_idr import ListUnconfirmedOmniTransactionsByPropertyIDR
from cryptoapis.model.get_address_details429_response import GetAddressDetails429Response
from pprint import pprint
# Defining the host is optional and defaults to https://rest.cryptoapis.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cryptoapis.Configuration(
    host = "https://rest.cryptoapis.io/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with cryptoapis.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = omni_layer_api.OmniLayerApi(api_client)
    network = "testnet" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    property_id = "2" # str | Represents the identifier of the tokens to send.
    context = "yourExampleString" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    limit = 50 # int | Defines how many items should be returned in the response per page basis. (optional) if omitted the server will use the default value of 50
    offset = 0 # int | The starting index of the response items, i.e. where the response should start listing the returned items. (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    try:
        # List Unconfirmed Omni Transactions By Property ID
        api_response = api_instance.list_unconfirmed_omni_transactions_by_property_id(network, property_id)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling OmniLayerApi->list_unconfirmed_omni_transactions_by_property_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Unconfirmed Omni Transactions By Property ID
        api_response = api_instance.list_unconfirmed_omni_transactions_by_property_id(network, property_id, context=context, limit=limit, offset=offset)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling OmniLayerApi->list_unconfirmed_omni_transactions_by_property_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. |
 **property_id** | **str**| Represents the identifier of the tokens to send. |
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. | defaults to "bitcoin"
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]
 **limit** | **int**| Defines how many items should be returned in the response per page basis. | [optional] if omitted the server will use the default value of 50
 **offset** | **int**| The starting index of the response items, i.e. where the response should start listing the returned items. | [optional] if omitted the server will use the default value of 0

### Return type

[**ListUnconfirmedOmniTransactionsByPropertyIDR**](ListUnconfirmedOmniTransactionsByPropertyIDR.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request has been successful. |  -  |
**400** | 400 |  -  |
**401** | 401 |  -  |
**402** | You have insufficient credits. Please upgrade your plan from your Dashboard or contact our team via email. |  -  |
**403** | 403 |  -  |
**409** | The data provided seems to be invalid. |  -  |
**415** | The selected Media Type is unavailable. The Content-Type header should be &#39;application/json&#39;. |  -  |
**422** | Your request body for POST requests must have a structure of { data: { item: [...properties] } } |  -  |
**429** | The request limit has been reached. There can be maximum {requests} requests per {seconds} second(s) made. Please contact our team via email if you need more or upgrade your plan. |  -  |
**500** | An unexpected server error has occurred, we are working to fix this. Please try again later and in case it occurs again please report it to our team via email. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

