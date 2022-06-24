# cryptoapis.HDWalletsApi

All URIs are relative to *https://rest.cryptoapis.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_hd_wallet__x_pub_y_pub_z_pub_assets**](HDWalletsApi.md#get_hd_wallet__x_pub_y_pub_z_pub_assets) | **GET** /blockchain-data/{blockchain}/{network}/hd/{extendedPublicKey}/assets | Get HD Wallet (xPub, yPub, zPub) Assets
[**get_hd_wallet__x_pub_y_pub_z_pub_details**](HDWalletsApi.md#get_hd_wallet__x_pub_y_pub_z_pub_details) | **GET** /blockchain-data/{blockchain}/{network}/hd/{extendedPublicKey}/details | Get HD Wallet (xPub, yPub, zPub) Details
[**list_hd_wallet__x_pub_y_pub_z_pub_transactions**](HDWalletsApi.md#list_hd_wallet__x_pub_y_pub_z_pub_transactions) | **GET** /blockchain-data/{blockchain}/{network}/hd/{extendedPublicKey}/transactions | List HD Wallet (xPub, yPub, zPub) Transactions
[**list_hd_wallet__x_pub_y_pub_z_pub_utxos**](HDWalletsApi.md#list_hd_wallet__x_pub_y_pub_z_pub_utxos) | **GET** /blockchain-data/{blockchain}/{network}/hd/{extendedPublicKey}/utxos | List HD Wallet (xPub, yPub, zPub) UTXOs
[**sync_hd_wallet__x_pub_y_pub_z_pub**](HDWalletsApi.md#sync_hd_wallet__x_pub_y_pub_z_pub) | **POST** /blockchain-data/{blockchain}/{network}/hd/sync | Sync HD Wallet (xPub, yPub, zPub)


# **get_hd_wallet__x_pub_y_pub_z_pub_assets**
> GetHDWalletXPubYPubZPubAssetsR get_hd_wallet__x_pub_y_pub_z_pub_assets(blockchain, extended_public_key, network)

Get HD Wallet (xPub, yPub, zPub) Assets

This endpoint will return details on assets we support for a specified from the customer extended public key (xPub). These could be cryptocurrencies, fungible or non-fungible (NFT) tokens. Each asset has a unique identifier - assetId, and a unique symbol in the form of a string, e.g. \"USDT\".

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import hd_wallets_api
from cryptoapis.model.get_address_details402_response import GetAddressDetails402Response
from cryptoapis.model.get_hd_wallet_x_pub_y_pub_z_pub_assets400_response import GetHDWalletXPubYPubZPubAssets400Response
from cryptoapis.model.get_address_details500_response import GetAddressDetails500Response
from cryptoapis.model.get_address_details415_response import GetAddressDetails415Response
from cryptoapis.model.get_address_details409_response import GetAddressDetails409Response
from cryptoapis.model.get_hd_wallet_x_pub_y_pub_z_pub_assets403_response import GetHDWalletXPubYPubZPubAssets403Response
from cryptoapis.model.get_address_details429_response import GetAddressDetails429Response
from cryptoapis.model.get_hd_wallet_x_pub_y_pub_z_pub_assets_r import GetHDWalletXPubYPubZPubAssetsR
from cryptoapis.model.get_hd_wallet_x_pub_y_pub_z_pub_assets422_response import GetHDWalletXPubYPubZPubAssets422Response
from cryptoapis.model.get_hd_wallet_x_pub_y_pub_z_pub_assets401_response import GetHDWalletXPubYPubZPubAssets401Response
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
    api_instance = hd_wallets_api.HDWalletsApi(api_client)
    blockchain = "ethereum" # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    extended_public_key = "xpub68SyZPMPpZUy9QB2fk2J28b5Rwd6jeWKind3K8oziZuVcL7wWZiXZNCPKuh42ejSpTLYngQ9Gbzj9a1Ap2QQmoFs2sMSbUvkEr8D3GW7MrR" # str | Defines the account extended publicly known key which is used to derive all child public keys.
    network = "ropsten" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    context = "yourExampleString" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    derivation = "account" # str | The way how the HD walled derives, for example when the type is ACCOUNT, it derives change and receive addresses while when the type is BIP32 it derives directly. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get HD Wallet (xPub, yPub, zPub) Assets
        api_response = api_instance.get_hd_wallet__x_pub_y_pub_z_pub_assets(blockchain, extended_public_key, network)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling HDWalletsApi->get_hd_wallet__x_pub_y_pub_z_pub_assets: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get HD Wallet (xPub, yPub, zPub) Assets
        api_response = api_instance.get_hd_wallet__x_pub_y_pub_z_pub_assets(blockchain, extended_public_key, network, context=context, derivation=derivation)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling HDWalletsApi->get_hd_wallet__x_pub_y_pub_z_pub_assets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. |
 **extended_public_key** | **str**| Defines the account extended publicly known key which is used to derive all child public keys. |
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. |
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]
 **derivation** | **str**| The way how the HD walled derives, for example when the type is ACCOUNT, it derives change and receive addresses while when the type is BIP32 it derives directly. | [optional]

### Return type

[**GetHDWalletXPubYPubZPubAssetsR**](GetHDWalletXPubYPubZPubAssetsR.md)

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
**422** | 422 |  -  |
**429** | The request limit has been reached. There can be maximum {requests} requests per {seconds} second(s) made. Please contact our team via email if you need more or upgrade your plan. |  -  |
**500** | An unexpected server error has occurred, we are working to fix this. Please try again later and in case it occurs again please report it to our team via email. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hd_wallet__x_pub_y_pub_z_pub_details**
> GetHDWalletXPubYPubZPubDetailsR get_hd_wallet__x_pub_y_pub_z_pub_details(blockchain, extended_public_key, network)

Get HD Wallet (xPub, yPub, zPub) Details

HD wallet details is useful endpoint to get the most important data about HD wallet without the need to do a lot of calculations, once the HD Wallet is synced using Sync endpoint we keep it up to date and we calculate these details in advance.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import hd_wallets_api
from cryptoapis.model.get_hd_wallet_x_pub_y_pub_z_pub_details422_response import GetHDWalletXPubYPubZPubDetails422Response
from cryptoapis.model.get_hd_wallet_x_pub_y_pub_z_pub_details400_response import GetHDWalletXPubYPubZPubDetails400Response
from cryptoapis.model.get_address_details402_response import GetAddressDetails402Response
from cryptoapis.model.get_address_details500_response import GetAddressDetails500Response
from cryptoapis.model.get_address_details415_response import GetAddressDetails415Response
from cryptoapis.model.get_hd_wallet_x_pub_y_pub_z_pub_details403_response import GetHDWalletXPubYPubZPubDetails403Response
from cryptoapis.model.get_address_details409_response import GetAddressDetails409Response
from cryptoapis.model.get_address_details429_response import GetAddressDetails429Response
from cryptoapis.model.get_hd_wallet_x_pub_y_pub_z_pub_details_r import GetHDWalletXPubYPubZPubDetailsR
from cryptoapis.model.get_hd_wallet_x_pub_y_pub_z_pub_details401_response import GetHDWalletXPubYPubZPubDetails401Response
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
    api_instance = hd_wallets_api.HDWalletsApi(api_client)
    blockchain = "bitcoin" # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    extended_public_key = "upub5Ei6bRNneqozk6smK7dvtXHC5PjUyEL4ynCfMKvjznLcXi9DQaikETzQjHvJC43XexMvQs64jxB1njMjCHpRZ4xQWAmv3ge9cVtjfsHmbvQ" # str | Defines the account extended publicly known key which is used to derive all child public keys.
    network = "testnet" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    context = "yourExampleString" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    derivation = "account" # str | The way how the HD walled derives, for example when the type is ACCOUNT, it derives change and receive addresses while when the type is BIP32 it derives directly. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get HD Wallet (xPub, yPub, zPub) Details
        api_response = api_instance.get_hd_wallet__x_pub_y_pub_z_pub_details(blockchain, extended_public_key, network)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling HDWalletsApi->get_hd_wallet__x_pub_y_pub_z_pub_details: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get HD Wallet (xPub, yPub, zPub) Details
        api_response = api_instance.get_hd_wallet__x_pub_y_pub_z_pub_details(blockchain, extended_public_key, network, context=context, derivation=derivation)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling HDWalletsApi->get_hd_wallet__x_pub_y_pub_z_pub_details: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. |
 **extended_public_key** | **str**| Defines the account extended publicly known key which is used to derive all child public keys. |
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. |
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]
 **derivation** | **str**| The way how the HD walled derives, for example when the type is ACCOUNT, it derives change and receive addresses while when the type is BIP32 it derives directly. | [optional]

### Return type

[**GetHDWalletXPubYPubZPubDetailsR**](GetHDWalletXPubYPubZPubDetailsR.md)

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
**422** | 422 |  -  |
**429** | The request limit has been reached. There can be maximum {requests} requests per {seconds} second(s) made. Please contact our team via email if you need more or upgrade your plan. |  -  |
**500** | An unexpected server error has occurred, we are working to fix this. Please try again later and in case it occurs again please report it to our team via email. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_hd_wallet__x_pub_y_pub_z_pub_transactions**
> ListHDWalletXPubYPubZPubTransactionsR list_hd_wallet__x_pub_y_pub_z_pub_transactions(blockchain, extended_public_key, network)

List HD Wallet (xPub, yPub, zPub) Transactions

This endpoint will list HD Wallet transactions.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import hd_wallets_api
from cryptoapis.model.list_hd_wallet_x_pub_y_pub_z_pub_transactions401_response import ListHDWalletXPubYPubZPubTransactions401Response
from cryptoapis.model.get_address_details402_response import GetAddressDetails402Response
from cryptoapis.model.list_hd_wallet_x_pub_y_pub_z_pub_transactions_r import ListHDWalletXPubYPubZPubTransactionsR
from cryptoapis.model.list_hd_wallet_x_pub_y_pub_z_pub_transactions400_response import ListHDWalletXPubYPubZPubTransactions400Response
from cryptoapis.model.get_address_details500_response import GetAddressDetails500Response
from cryptoapis.model.get_address_details415_response import GetAddressDetails415Response
from cryptoapis.model.list_hd_wallet_x_pub_y_pub_z_pub_transactions403_response import ListHDWalletXPubYPubZPubTransactions403Response
from cryptoapis.model.get_address_details409_response import GetAddressDetails409Response
from cryptoapis.model.get_address_details429_response import GetAddressDetails429Response
from cryptoapis.model.list_hd_wallet_x_pub_y_pub_z_pub_transactions422_response import ListHDWalletXPubYPubZPubTransactions422Response
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
    api_instance = hd_wallets_api.HDWalletsApi(api_client)
    blockchain = "bitcoin" # str | Represents the specific blockchain.
    extended_public_key = "tpubD9GMECjiZHCaF9NHSMAeMbQMXnM7CviEJZsYBuztVwsUjPHWjxewWAUXWV2UExaAtoEvQGXDBmVWo6ZHGtj6TsH6Pop7D9DskQwGHA1gu1w" # str | Defines the master public key (xPub) of the account.
    network = "testnet" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    context = "yourExampleString" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    derivation = "account" # str | The way how the HD walled derives, for example when the type is ACCOUNT, it derives change and receive addresses while when the type is BIP32 it derives directly. (optional)
    limit = 50 # int | Defines how many items should be returned in the response per page basis. (optional) if omitted the server will use the default value of 50
    offset = 0 # int | The starting index of the response items, i.e. where the response should start listing the returned items. (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    try:
        # List HD Wallet (xPub, yPub, zPub) Transactions
        api_response = api_instance.list_hd_wallet__x_pub_y_pub_z_pub_transactions(blockchain, extended_public_key, network)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling HDWalletsApi->list_hd_wallet__x_pub_y_pub_z_pub_transactions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List HD Wallet (xPub, yPub, zPub) Transactions
        api_response = api_instance.list_hd_wallet__x_pub_y_pub_z_pub_transactions(blockchain, extended_public_key, network, context=context, derivation=derivation, limit=limit, offset=offset)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling HDWalletsApi->list_hd_wallet__x_pub_y_pub_z_pub_transactions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain** | **str**| Represents the specific blockchain. |
 **extended_public_key** | **str**| Defines the master public key (xPub) of the account. |
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. |
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]
 **derivation** | **str**| The way how the HD walled derives, for example when the type is ACCOUNT, it derives change and receive addresses while when the type is BIP32 it derives directly. | [optional]
 **limit** | **int**| Defines how many items should be returned in the response per page basis. | [optional] if omitted the server will use the default value of 50
 **offset** | **int**| The starting index of the response items, i.e. where the response should start listing the returned items. | [optional] if omitted the server will use the default value of 0

### Return type

[**ListHDWalletXPubYPubZPubTransactionsR**](ListHDWalletXPubYPubZPubTransactionsR.md)

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
**422** | 422 |  -  |
**429** | The request limit has been reached. There can be maximum {requests} requests per {seconds} second(s) made. Please contact our team via email if you need more or upgrade your plan. |  -  |
**500** | An unexpected server error has occurred, we are working to fix this. Please try again later and in case it occurs again please report it to our team via email. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_hd_wallet__x_pub_y_pub_z_pub_utxos**
> ListHDWalletXPubYPubZPubUTXOsR list_hd_wallet__x_pub_y_pub_z_pub_utxos(blockchain, extended_public_key, network)

List HD Wallet (xPub, yPub, zPub) UTXOs

Through this endpoint you can list HD wallet's UTXOs (Unspent Transaction Outputs) by providing extended public key of an already synced HD wallet.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import hd_wallets_api
from cryptoapis.model.list_hd_wallet_x_pub_y_pub_z_pub_utxos_r import ListHDWalletXPubYPubZPubUTXOsR
from cryptoapis.model.get_address_details402_response import GetAddressDetails402Response
from cryptoapis.model.get_address_details500_response import GetAddressDetails500Response
from cryptoapis.model.get_address_details415_response import GetAddressDetails415Response
from cryptoapis.model.get_address_details409_response import GetAddressDetails409Response
from cryptoapis.model.get_address_details429_response import GetAddressDetails429Response
from cryptoapis.model.list_hd_wallet_x_pub_y_pub_z_pub_utxos400_response import ListHDWalletXPubYPubZPubUTXOs400Response
from cryptoapis.model.list_hd_wallet_x_pub_y_pub_z_pub_utxos401_response import ListHDWalletXPubYPubZPubUTXOs401Response
from cryptoapis.model.list_hd_wallet_x_pub_y_pub_z_pub_utxos422_response import ListHDWalletXPubYPubZPubUTXOs422Response
from cryptoapis.model.list_hd_wallet_x_pub_y_pub_z_pub_utxos403_response import ListHDWalletXPubYPubZPubUTXOs403Response
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
    api_instance = hd_wallets_api.HDWalletsApi(api_client)
    blockchain = "bitcoin" # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    extended_public_key = "tpubDDCs6jf3Tg8VTts6EBCNpibVanPQpSkmYRLAXVvuhcuC6ZcbYtEizqERj8D4TBukuvjNSjtjEbKYdtFuRG5WuisrirZG9m5L8wUvf4bHhgQ" # str | Defines the account extended publicly known key which is used to derive all child public keys.
    network = "testnet" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    context = "yourExampleString" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    derivation = "account" # str | The way how the HD walled derives, for example when the type is ACCOUNT, it derives change and receive addresses while when the type is BIP32 it derives directly. (optional)
    limit = 50 # int | Defines how many items should be returned in the response per page basis. (optional) if omitted the server will use the default value of 50
    offset = 0 # int | The starting index of the response items, i.e. where the response should start listing the returned items. (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    try:
        # List HD Wallet (xPub, yPub, zPub) UTXOs
        api_response = api_instance.list_hd_wallet__x_pub_y_pub_z_pub_utxos(blockchain, extended_public_key, network)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling HDWalletsApi->list_hd_wallet__x_pub_y_pub_z_pub_utxos: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List HD Wallet (xPub, yPub, zPub) UTXOs
        api_response = api_instance.list_hd_wallet__x_pub_y_pub_z_pub_utxos(blockchain, extended_public_key, network, context=context, derivation=derivation, limit=limit, offset=offset)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling HDWalletsApi->list_hd_wallet__x_pub_y_pub_z_pub_utxos: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. |
 **extended_public_key** | **str**| Defines the account extended publicly known key which is used to derive all child public keys. |
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. |
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]
 **derivation** | **str**| The way how the HD walled derives, for example when the type is ACCOUNT, it derives change and receive addresses while when the type is BIP32 it derives directly. | [optional]
 **limit** | **int**| Defines how many items should be returned in the response per page basis. | [optional] if omitted the server will use the default value of 50
 **offset** | **int**| The starting index of the response items, i.e. where the response should start listing the returned items. | [optional] if omitted the server will use the default value of 0

### Return type

[**ListHDWalletXPubYPubZPubUTXOsR**](ListHDWalletXPubYPubZPubUTXOsR.md)

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
**422** | 422 |  -  |
**429** | The request limit has been reached. There can be maximum {requests} requests per {seconds} second(s) made. Please contact our team via email if you need more or upgrade your plan. |  -  |
**500** | An unexpected server error has occurred, we are working to fix this. Please try again later and in case it occurs again please report it to our team via email. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sync_hd_wallet__x_pub_y_pub_z_pub**
> SyncHDWalletXPubYPubZPubR sync_hd_wallet__x_pub_y_pub_z_pub(blockchain, network)

Sync HD Wallet (xPub, yPub, zPub)

HD wallets usually have a lot of addresses and transactions, getting the data on demand is a heavy operation. That's why we have created this feature, to be able to get HD wallet details or transactions this HD wallet must be synced first. In addition to the initial sync we keep updating the synced HD wallets all the time.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import hd_wallets_api
from cryptoapis.model.sync_hd_wallet_x_pub_y_pub_z_pub_r import SyncHDWalletXPubYPubZPubR
from cryptoapis.model.sync_hd_wallet_x_pub_y_pub_z_pub401_response import SyncHDWalletXPubYPubZPub401Response
from cryptoapis.model.get_address_details402_response import GetAddressDetails402Response
from cryptoapis.model.sync_hd_wallet_x_pub_y_pub_z_pub_rb import SyncHDWalletXPubYPubZPubRB
from cryptoapis.model.get_address_details500_response import GetAddressDetails500Response
from cryptoapis.model.get_address_details415_response import GetAddressDetails415Response
from cryptoapis.model.sync_hd_wallet_x_pub_y_pub_z_pub422_response import SyncHDWalletXPubYPubZPub422Response
from cryptoapis.model.sync_hd_wallet_x_pub_y_pub_z_pub409_response import SyncHDWalletXPubYPubZPub409Response
from cryptoapis.model.get_address_details429_response import GetAddressDetails429Response
from cryptoapis.model.sync_hd_wallet_x_pub_y_pub_z_pub403_response import SyncHDWalletXPubYPubZPub403Response
from cryptoapis.model.sync_hd_wallet_x_pub_y_pub_z_pub400_response import SyncHDWalletXPubYPubZPub400Response
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
    api_instance = hd_wallets_api.HDWalletsApi(api_client)
    blockchain = "bitcoin" # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    network = "testnet" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    context = "yourExampleString" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    sync_hd_wallet_x_pub_y_pub_z_pub_rb = SyncHDWalletXPubYPubZPubRB(
        context="yourExampleString",
        data=SyncHDWalletXPubYPubZPubRBData(
            item=SyncHDWalletXPubYPubZPubRBDataItem(
                extended_public_key="upub5Ei6bRNneqozk6smK7dvtXHC5PjUyEL4ynCfMKvjznLcXi9DQaikETzQjHvJC43XexMvQs64jxB1njMjCHpRZ4xQWAmv3ge9cVtjfsHmbvQ",
            ),
        ),
    ) # SyncHDWalletXPubYPubZPubRB |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Sync HD Wallet (xPub, yPub, zPub)
        api_response = api_instance.sync_hd_wallet__x_pub_y_pub_z_pub(blockchain, network)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling HDWalletsApi->sync_hd_wallet__x_pub_y_pub_z_pub: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Sync HD Wallet (xPub, yPub, zPub)
        api_response = api_instance.sync_hd_wallet__x_pub_y_pub_z_pub(blockchain, network, context=context, sync_hd_wallet_x_pub_y_pub_z_pub_rb=sync_hd_wallet_x_pub_y_pub_z_pub_rb)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling HDWalletsApi->sync_hd_wallet__x_pub_y_pub_z_pub: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. |
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. |
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]
 **sync_hd_wallet_x_pub_y_pub_z_pub_rb** | [**SyncHDWalletXPubYPubZPubRB**](SyncHDWalletXPubYPubZPubRB.md)|  | [optional]

### Return type

[**SyncHDWalletXPubYPubZPubR**](SyncHDWalletXPubYPubZPubR.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The resource has been successfully created. |  -  |
**400** | 400 |  -  |
**401** | 401 |  -  |
**402** | You have insufficient credits. Please upgrade your plan from your Dashboard or contact our team via email. |  -  |
**403** | 403 |  -  |
**409** | 409 |  -  |
**415** | The selected Media Type is unavailable. The Content-Type header should be &#39;application/json&#39;. |  -  |
**422** | 422 |  -  |
**429** | The request limit has been reached. There can be maximum {requests} requests per {seconds} second(s) made. Please contact our team via email if you need more or upgrade your plan. |  -  |
**500** | An unexpected server error has occurred, we are working to fix this. Please try again later and in case it occurs again please report it to our team via email. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

