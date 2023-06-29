# cryptoapis.HDWalletsApi

All URIs are relative to *https://rest.cryptoapis.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**derive_and_sync_new_change_addresses**](HDWalletsApi.md#derive_and_sync_new_change_addresses) | **POST** /blockchain-data/{blockchain}/{network}/hd/derive-sync-change | Derive And Sync New Change Addresses
[**derive_and_sync_new_receiving_addresses**](HDWalletsApi.md#derive_and_sync_new_receiving_addresses) | **POST** /blockchain-data/{blockchain}/{network}/hd/derive-and-sync | Derive And Sync New Receiving Addresses
[**get_hd_wallet__x_pub_y_pub_z_pub_assets**](HDWalletsApi.md#get_hd_wallet__x_pub_y_pub_z_pub_assets) | **GET** /blockchain-data/{blockchain}/{network}/hd/{extendedPublicKey}/assets | Get HD Wallet (xPub, yPub, zPub) Assets
[**get_hd_wallet__x_pub_y_pub_z_pub_details**](HDWalletsApi.md#get_hd_wallet__x_pub_y_pub_z_pub_details) | **GET** /blockchain-data/{blockchain}/{network}/hd/{extendedPublicKey}/details | Get HD Wallet (xPub, yPub, zPub) Details
[**list_hd_wallet__x_pub_y_pub_z_pub_transactions**](HDWalletsApi.md#list_hd_wallet__x_pub_y_pub_z_pub_transactions) | **GET** /blockchain-data/{blockchain}/{network}/hd/{extendedPublicKey}/transactions | List HD Wallet (xPub, yPub, zPub) Transactions
[**list_hd_wallet__x_pub_y_pub_z_pub_utxos**](HDWalletsApi.md#list_hd_wallet__x_pub_y_pub_z_pub_utxos) | **GET** /blockchain-data/{blockchain}/{network}/hd/{extendedPublicKey}/utxos | List HD Wallet (xPub, yPub, zPub) UTXOs
[**list_synced_addresses**](HDWalletsApi.md#list_synced_addresses) | **GET** /blockchain-data/{blockchain}/{network}/hd/{extendedPublicKey}/synced-addresses | List Synced Addresses
[**prepare_a_transaction_from_an_address_in_hd_wallet__x_pub_y_pub_z_pub**](HDWalletsApi.md#prepare_a_transaction_from_an_address_in_hd_wallet__x_pub_y_pub_z_pub) | **POST** /blockchain-data/{blockchain}/{network}/transactions/prepare-account-based-transaction | Prepare A Transaction From An Address In HD Wallet (xPub, yPub, zPub)
[**prepare_a_utxo_based_transaction_from_hd_wallet__x_pub_y_pub_z_pub**](HDWalletsApi.md#prepare_a_utxo_based_transaction_from_hd_wallet__x_pub_y_pub_z_pub) | **POST** /blockchain-data/{blockchain}/{network}/transactions/prepare-utxo-transaction | Prepare A UTXO-Based Transaction From HD Wallet (xPub, yPub, zPub)
[**sync_hd_wallet__x_pub_y_pub_z_pub**](HDWalletsApi.md#sync_hd_wallet__x_pub_y_pub_z_pub) | **POST** /blockchain-data/{blockchain}/{network}/hd/sync | Sync HD Wallet (xPub, yPub, zPub)
[**sync_new_hd_wallet__x_pub_y_pub_z_pub**](HDWalletsApi.md#sync_new_hd_wallet__x_pub_y_pub_z_pub) | **POST** /blockchain-data/{blockchain}/{network}/hd/sync-new | Sync New HD Wallet (xPub, yPub, zPub)


# **derive_and_sync_new_change_addresses**
> DeriveAndSyncNewChangeAddressesR derive_and_sync_new_change_addresses(blockchain, network, context=context, derive_and_sync_new_change_addresses_rb=derive_and_sync_new_change_addresses_rb)

Derive And Sync New Change Addresses

Through this endpoint users can derive 100 change addresses, starting from the last index we have data for, which are then added to the xPub, subscribed for syncing, and start recording data. If no data is available, it will start from index 0. We use type P2WPKH.

### Example

* Api Key Authentication (ApiKey):
```python
import time
import os
import cryptoapis
from cryptoapis.models.derive_and_sync_new_change_addresses_r import DeriveAndSyncNewChangeAddressesR
from cryptoapis.models.derive_and_sync_new_change_addresses_rb import DeriveAndSyncNewChangeAddressesRB
from cryptoapis.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.cryptoapis.io
# See configuration.py for a list of all supported configuration parameters.
configuration = cryptoapis.Configuration(
    host = "https://rest.cryptoapis.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with cryptoapis.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cryptoapis.HDWalletsApi(api_client)
    blockchain = 'bitcoin' # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    network = 'testnet' # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    context = 'yourExampleString' # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    derive_and_sync_new_change_addresses_rb = cryptoapis.DeriveAndSyncNewChangeAddressesRB() # DeriveAndSyncNewChangeAddressesRB |  (optional)

    try:
        # Derive And Sync New Change Addresses
        api_response = api_instance.derive_and_sync_new_change_addresses(blockchain, network, context=context, derive_and_sync_new_change_addresses_rb=derive_and_sync_new_change_addresses_rb)
        print("The response of HDWalletsApi->derive_and_sync_new_change_addresses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HDWalletsApi->derive_and_sync_new_change_addresses: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. | 
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. | 
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional] 
 **derive_and_sync_new_change_addresses_rb** | [**DeriveAndSyncNewChangeAddressesRB**](DeriveAndSyncNewChangeAddressesRB.md)|  | [optional] 

### Return type

[**DeriveAndSyncNewChangeAddressesR**](DeriveAndSyncNewChangeAddressesR.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfull Request |  -  |
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

# **derive_and_sync_new_receiving_addresses**
> DeriveAndSyncNewReceivingAddressesR derive_and_sync_new_receiving_addresses(blockchain, network, context=context, derive_and_sync_new_receiving_addresses_rb=derive_and_sync_new_receiving_addresses_rb)

Derive And Sync New Receiving Addresses

Through this endpoint users can derive 100 receiving addresses, starting from the last index we have data for, which are then added to the xPub, subscribed for syncing, and start recording data. If no data is available, it will start from index 0. We use type P2WPKH.

### Example

* Api Key Authentication (ApiKey):
```python
import time
import os
import cryptoapis
from cryptoapis.models.derive_and_sync_new_receiving_addresses_r import DeriveAndSyncNewReceivingAddressesR
from cryptoapis.models.derive_and_sync_new_receiving_addresses_rb import DeriveAndSyncNewReceivingAddressesRB
from cryptoapis.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.cryptoapis.io
# See configuration.py for a list of all supported configuration parameters.
configuration = cryptoapis.Configuration(
    host = "https://rest.cryptoapis.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with cryptoapis.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cryptoapis.HDWalletsApi(api_client)
    blockchain = 'bitcoin' # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    network = 'testnet' # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    context = 'yourExampleString' # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    derive_and_sync_new_receiving_addresses_rb = cryptoapis.DeriveAndSyncNewReceivingAddressesRB() # DeriveAndSyncNewReceivingAddressesRB |  (optional)

    try:
        # Derive And Sync New Receiving Addresses
        api_response = api_instance.derive_and_sync_new_receiving_addresses(blockchain, network, context=context, derive_and_sync_new_receiving_addresses_rb=derive_and_sync_new_receiving_addresses_rb)
        print("The response of HDWalletsApi->derive_and_sync_new_receiving_addresses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HDWalletsApi->derive_and_sync_new_receiving_addresses: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. | 
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. | 
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional] 
 **derive_and_sync_new_receiving_addresses_rb** | [**DeriveAndSyncNewReceivingAddressesRB**](DeriveAndSyncNewReceivingAddressesRB.md)|  | [optional] 

### Return type

[**DeriveAndSyncNewReceivingAddressesR**](DeriveAndSyncNewReceivingAddressesR.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfull Request |  -  |
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

# **get_hd_wallet__x_pub_y_pub_z_pub_assets**
> GetHDWalletXPubYPubZPubAssetsR get_hd_wallet__x_pub_y_pub_z_pub_assets(blockchain, extended_public_key, network, context=context, derivation=derivation)

Get HD Wallet (xPub, yPub, zPub) Assets

This endpoint will return details on assets we support for a specified from the customer extended public key (xPub). These could be cryptocurrencies, fungible or non-fungible (NFT) tokens. Each asset has a unique identifier - assetId, and a unique symbol in the form of a string, e.g. \"USDT\".

### Example

* Api Key Authentication (ApiKey):
```python
import time
import os
import cryptoapis
from cryptoapis.models.get_hd_wallet_x_pub_y_pub_z_pub_assets_r import GetHDWalletXPubYPubZPubAssetsR
from cryptoapis.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.cryptoapis.io
# See configuration.py for a list of all supported configuration parameters.
configuration = cryptoapis.Configuration(
    host = "https://rest.cryptoapis.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with cryptoapis.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cryptoapis.HDWalletsApi(api_client)
    blockchain = 'ethereum' # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    extended_public_key = 'xpub68SyZPMPpZUy9QB2fk2J28b5Rwd6jeWKind3K8oziZuVcL7wWZiXZNCPKuh42ejSpTLYngQ9Gbzj9a1Ap2QQmoFs2sMSbUvkEr8D3GW7MrR' # str | Defines the account extended publicly known key which is used to derive all child public keys.
    network = 'goerli' # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    context = 'yourExampleString' # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    derivation = 'account' # str | The way how the HD walled derives, for example when the type is ACCOUNT, it derives change and receive addresses while when the type is BIP32 it derives directly. (optional)

    try:
        # Get HD Wallet (xPub, yPub, zPub) Assets
        api_response = api_instance.get_hd_wallet__x_pub_y_pub_z_pub_assets(blockchain, extended_public_key, network, context=context, derivation=derivation)
        print("The response of HDWalletsApi->get_hd_wallet__x_pub_y_pub_z_pub_assets:\n")
        pprint(api_response)
    except Exception as e:
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
> GetHDWalletXPubYPubZPubDetailsR get_hd_wallet__x_pub_y_pub_z_pub_details(blockchain, extended_public_key, network, context=context, derivation=derivation)

Get HD Wallet (xPub, yPub, zPub) Details

HD wallet details is useful endpoint to get the most important data about HD wallet without the need to do a lot of calculations, once the HD Wallet is synced using Sync endpoint we keep it up to date and we calculate these details in advance.

### Example

* Api Key Authentication (ApiKey):
```python
import time
import os
import cryptoapis
from cryptoapis.models.get_hd_wallet_x_pub_y_pub_z_pub_details_r import GetHDWalletXPubYPubZPubDetailsR
from cryptoapis.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.cryptoapis.io
# See configuration.py for a list of all supported configuration parameters.
configuration = cryptoapis.Configuration(
    host = "https://rest.cryptoapis.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with cryptoapis.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cryptoapis.HDWalletsApi(api_client)
    blockchain = 'bitcoin' # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    extended_public_key = 'upub5Ei6bRNneqozk6smK7dvtXHC5PjUyEL4ynCfMKvjznLcXi9DQaikETzQjHvJC43XexMvQs64jxB1njMjCHpRZ4xQWAmv3ge9cVtjfsHmbvQ' # str | Defines the account extended publicly known key which is used to derive all child public keys.
    network = 'testnet' # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    context = 'yourExampleString' # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    derivation = 'derivation_example' # str | The way how the HD walled derives, for example when the type is ACCOUNT, it derives change and receive addresses while when the type is BIP32 it derives directly. (optional)

    try:
        # Get HD Wallet (xPub, yPub, zPub) Details
        api_response = api_instance.get_hd_wallet__x_pub_y_pub_z_pub_details(blockchain, extended_public_key, network, context=context, derivation=derivation)
        print("The response of HDWalletsApi->get_hd_wallet__x_pub_y_pub_z_pub_details:\n")
        pprint(api_response)
    except Exception as e:
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
> ListHDWalletXPubYPubZPubTransactionsR list_hd_wallet__x_pub_y_pub_z_pub_transactions(blockchain, extended_public_key, network, context=context, derivation=derivation, limit=limit, offset=offset)

List HD Wallet (xPub, yPub, zPub) Transactions

This endpoint will list HD Wallet transactions.

### Example

* Api Key Authentication (ApiKey):
```python
import time
import os
import cryptoapis
from cryptoapis.models.list_hd_wallet_x_pub_y_pub_z_pub_transactions_r import ListHDWalletXPubYPubZPubTransactionsR
from cryptoapis.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.cryptoapis.io
# See configuration.py for a list of all supported configuration parameters.
configuration = cryptoapis.Configuration(
    host = "https://rest.cryptoapis.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with cryptoapis.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cryptoapis.HDWalletsApi(api_client)
    blockchain = 'bitcoin' # str | Represents the specific blockchain.
    extended_public_key = 'tpubD9GMECjiZHCaF9NHSMAeMbQMXnM7CviEJZsYBuztVwsUjPHWjxewWAUXWV2UExaAtoEvQGXDBmVWo6ZHGtj6TsH6Pop7D9DskQwGHA1gu1w' # str | Defines the master public key (xPub) of the account.
    network = 'testnet' # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    context = 'yourExampleString' # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    derivation = 'derivation_example' # str | The way how the HD walled derives, for example when the type is ACCOUNT, it derives change and receive addresses while when the type is BIP32 it derives directly. (optional)
    limit = 50 # int | Defines how many items should be returned in the response per page basis. (optional) (default to 50)
    offset = 0 # int | The starting index of the response items, i.e. where the response should start listing the returned items. (optional) (default to 0)

    try:
        # List HD Wallet (xPub, yPub, zPub) Transactions
        api_response = api_instance.list_hd_wallet__x_pub_y_pub_z_pub_transactions(blockchain, extended_public_key, network, context=context, derivation=derivation, limit=limit, offset=offset)
        print("The response of HDWalletsApi->list_hd_wallet__x_pub_y_pub_z_pub_transactions:\n")
        pprint(api_response)
    except Exception as e:
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
 **limit** | **int**| Defines how many items should be returned in the response per page basis. | [optional] [default to 50]
 **offset** | **int**| The starting index of the response items, i.e. where the response should start listing the returned items. | [optional] [default to 0]

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
> ListHDWalletXPubYPubZPubUTXOsR list_hd_wallet__x_pub_y_pub_z_pub_utxos(blockchain, extended_public_key, network, context=context, derivation=derivation, limit=limit, offset=offset)

List HD Wallet (xPub, yPub, zPub) UTXOs

Through this endpoint you can list HD wallet's UTXOs (Unspent Transaction Outputs) by providing extended public key of an already synced HD wallet.

### Example

* Api Key Authentication (ApiKey):
```python
import time
import os
import cryptoapis
from cryptoapis.models.list_hd_wallet_x_pub_y_pub_z_pub_utxos_r import ListHDWalletXPubYPubZPubUTXOsR
from cryptoapis.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.cryptoapis.io
# See configuration.py for a list of all supported configuration parameters.
configuration = cryptoapis.Configuration(
    host = "https://rest.cryptoapis.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with cryptoapis.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cryptoapis.HDWalletsApi(api_client)
    blockchain = 'bitcoin' # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    extended_public_key = 'tpubDDCs6jf3Tg8VTts6EBCNpibVanPQpSkmYRLAXVvuhcuC6ZcbYtEizqERj8D4TBukuvjNSjtjEbKYdtFuRG5WuisrirZG9m5L8wUvf4bHhgQ' # str | Defines the account extended publicly known key which is used to derive all child public keys.
    network = 'testnet' # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    context = 'yourExampleString' # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    derivation = 'account' # str | The way how the HD walled derives, for example when the type is ACCOUNT, it derives change and receive addresses while when the type is BIP32 it derives directly. (optional)
    limit = 50 # int | Defines how many items should be returned in the response per page basis. (optional) (default to 50)
    offset = 0 # int | The starting index of the response items, i.e. where the response should start listing the returned items. (optional) (default to 0)

    try:
        # List HD Wallet (xPub, yPub, zPub) UTXOs
        api_response = api_instance.list_hd_wallet__x_pub_y_pub_z_pub_utxos(blockchain, extended_public_key, network, context=context, derivation=derivation, limit=limit, offset=offset)
        print("The response of HDWalletsApi->list_hd_wallet__x_pub_y_pub_z_pub_utxos:\n")
        pprint(api_response)
    except Exception as e:
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
 **limit** | **int**| Defines how many items should be returned in the response per page basis. | [optional] [default to 50]
 **offset** | **int**| The starting index of the response items, i.e. where the response should start listing the returned items. | [optional] [default to 0]

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

# **list_synced_addresses**
> ListSyncedAddressesR list_synced_addresses(blockchain, extended_public_key, network, context=context, address_format=address_format, is_change_address=is_change_address, limit=limit, offset=offset)

List Synced Addresses

Through this endpoint users can list all addresses that Crypto APIs has synced for a specific xPub. This includes previous and current/new xPubs, what addresses we’ve synced for them, etc.

### Example

* Api Key Authentication (ApiKey):
```python
import time
import os
import cryptoapis
from cryptoapis.models.list_synced_addresses_r import ListSyncedAddressesR
from cryptoapis.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.cryptoapis.io
# See configuration.py for a list of all supported configuration parameters.
configuration = cryptoapis.Configuration(
    host = "https://rest.cryptoapis.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with cryptoapis.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cryptoapis.HDWalletsApi(api_client)
    blockchain = 'ethereum' # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    extended_public_key = 'tpubD9GMECjiZHCaF9NHSMAeMbQMXnM7CviEJZsYBuztVwsUjPHWjxewWAUXWV2UExaAtoEvQGXDBmVWo6ZHGtj6TsH6Pop7D9DskQwGHA1gu1w' # str | Defines the account extended publicly known key which is used to derive all child public keys.
    network = 'goerli' # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    context = 'yourExampleString' # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    address_format = 'standard' # str | Defines the address format value. (optional)
    is_change_address = True # bool | Defines if the address is change addres or not. (optional) (default to True)
    limit = 50 # int | Defines how many items should be returned in the response per page basis. (optional) (default to 50)
    offset = 0 # int | The starting index of the response items, i.e. where the response should start listing the returned items. (optional) (default to 0)

    try:
        # List Synced Addresses
        api_response = api_instance.list_synced_addresses(blockchain, extended_public_key, network, context=context, address_format=address_format, is_change_address=is_change_address, limit=limit, offset=offset)
        print("The response of HDWalletsApi->list_synced_addresses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HDWalletsApi->list_synced_addresses: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. | 
 **extended_public_key** | **str**| Defines the account extended publicly known key which is used to derive all child public keys. | 
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. | 
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional] 
 **address_format** | **str**| Defines the address format value. | [optional] 
 **is_change_address** | **bool**| Defines if the address is change addres or not. | [optional] [default to True]
 **limit** | **int**| Defines how many items should be returned in the response per page basis. | [optional] [default to 50]
 **offset** | **int**| The starting index of the response items, i.e. where the response should start listing the returned items. | [optional] [default to 0]

### Return type

[**ListSyncedAddressesR**](ListSyncedAddressesR.md)

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

# **prepare_a_transaction_from_an_address_in_hd_wallet__x_pub_y_pub_z_pub**
> PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubR prepare_a_transaction_from_an_address_in_hd_wallet__x_pub_y_pub_z_pub(blockchain, network, context=context, prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_rb=prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_rb)

Prepare A Transaction From An Address In HD Wallet (xPub, yPub, zPub)

Through this endpoint users can prepare a transaction for signing from a synced with Crypto APIs address from the specific xPub. This endpoint applies to all supported account-based blockchain protocols, e.g. Ethereum, BSC, etc.

### Example

* Api Key Authentication (ApiKey):
```python
import time
import os
import cryptoapis
from cryptoapis.models.prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_r import PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubR
from cryptoapis.models.prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_rb import PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRB
from cryptoapis.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.cryptoapis.io
# See configuration.py for a list of all supported configuration parameters.
configuration = cryptoapis.Configuration(
    host = "https://rest.cryptoapis.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with cryptoapis.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cryptoapis.HDWalletsApi(api_client)
    blockchain = 'ethereum' # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    network = 'goerli' # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"goerli\" are test networks.
    context = 'yourExampleString' # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_rb = cryptoapis.PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRB() # PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRB |  (optional)

    try:
        # Prepare A Transaction From An Address In HD Wallet (xPub, yPub, zPub)
        api_response = api_instance.prepare_a_transaction_from_an_address_in_hd_wallet__x_pub_y_pub_z_pub(blockchain, network, context=context, prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_rb=prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_rb)
        print("The response of HDWalletsApi->prepare_a_transaction_from_an_address_in_hd_wallet__x_pub_y_pub_z_pub:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HDWalletsApi->prepare_a_transaction_from_an_address_in_hd_wallet__x_pub_y_pub_z_pub: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. | 
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;goerli\&quot; are test networks. | 
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional] 
 **prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_rb** | [**PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRB**](PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRB.md)|  | [optional] 

### Return type

[**PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubR**](PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubR.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The resource has been successfully submitted. |  -  |
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

# **prepare_a_utxo_based_transaction_from_hd_wallet__x_pub_y_pub_z_pub**
> PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubR prepare_a_utxo_based_transaction_from_hd_wallet__x_pub_y_pub_z_pub(blockchain, network, context=context, prepare_autxo_based_transaction_from_hd_wallet_x_pub_y_pub_z_pub_rb=prepare_autxo_based_transaction_from_hd_wallet_x_pub_y_pub_z_pub_rb)

Prepare A UTXO-Based Transaction From HD Wallet (xPub, yPub, zPub)

Through the “Prepare a UTXO-based transaction from xPub” endpoint users can prepare a transaction for signing from all synced with Crypto APIs addresses for the specific xPub. This is based on the `selectionStrategy` and the addresses’ balances. In the case a user has an address not synced with Crypto APIs, it will not be included. This endpoint applies to all supported UTXO-based blockchain protocols, e.g. Bitcoin, Litecoin, etc.

### Example

* Api Key Authentication (ApiKey):
```python
import time
import os
import cryptoapis
from cryptoapis.models.prepare_autxo_based_transaction_from_hd_wallet_x_pub_y_pub_z_pub_r import PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubR
from cryptoapis.models.prepare_autxo_based_transaction_from_hd_wallet_x_pub_y_pub_z_pub_rb import PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRB
from cryptoapis.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.cryptoapis.io
# See configuration.py for a list of all supported configuration parameters.
configuration = cryptoapis.Configuration(
    host = "https://rest.cryptoapis.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with cryptoapis.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cryptoapis.HDWalletsApi(api_client)
    blockchain = 'bitcoin' # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    network = 'testnet' # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    context = 'yourExampleString' # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    prepare_autxo_based_transaction_from_hd_wallet_x_pub_y_pub_z_pub_rb = cryptoapis.PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRB() # PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRB |  (optional)

    try:
        # Prepare A UTXO-Based Transaction From HD Wallet (xPub, yPub, zPub)
        api_response = api_instance.prepare_a_utxo_based_transaction_from_hd_wallet__x_pub_y_pub_z_pub(blockchain, network, context=context, prepare_autxo_based_transaction_from_hd_wallet_x_pub_y_pub_z_pub_rb=prepare_autxo_based_transaction_from_hd_wallet_x_pub_y_pub_z_pub_rb)
        print("The response of HDWalletsApi->prepare_a_utxo_based_transaction_from_hd_wallet__x_pub_y_pub_z_pub:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HDWalletsApi->prepare_a_utxo_based_transaction_from_hd_wallet__x_pub_y_pub_z_pub: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. | 
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. | 
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional] 
 **prepare_autxo_based_transaction_from_hd_wallet_x_pub_y_pub_z_pub_rb** | [**PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRB**](PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRB.md)|  | [optional] 

### Return type

[**PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubR**](PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubR.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The resource has been successfully submitted. |  -  |
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

# **sync_hd_wallet__x_pub_y_pub_z_pub**
> SyncHDWalletXPubYPubZPubR sync_hd_wallet__x_pub_y_pub_z_pub(blockchain, network, context=context, sync_hd_wallet_x_pub_y_pub_z_pub_rb=sync_hd_wallet_x_pub_y_pub_z_pub_rb)

Sync HD Wallet (xPub, yPub, zPub)

HD wallets usually have a lot of addresses and transactions, getting the data on demand is a heavy operation. That's why we have created this feature, to be able to get HD wallet details or transactions this HD wallet must be synced first. In addition to the initial sync we keep updating the synced HD wallets all the time.

### Example

* Api Key Authentication (ApiKey):
```python
import time
import os
import cryptoapis
from cryptoapis.models.sync_hd_wallet_x_pub_y_pub_z_pub_r import SyncHDWalletXPubYPubZPubR
from cryptoapis.models.sync_hd_wallet_x_pub_y_pub_z_pub_rb import SyncHDWalletXPubYPubZPubRB
from cryptoapis.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.cryptoapis.io
# See configuration.py for a list of all supported configuration parameters.
configuration = cryptoapis.Configuration(
    host = "https://rest.cryptoapis.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with cryptoapis.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cryptoapis.HDWalletsApi(api_client)
    blockchain = 'bitcoin' # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    network = 'testnet' # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    context = 'yourExampleString' # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    sync_hd_wallet_x_pub_y_pub_z_pub_rb = cryptoapis.SyncHDWalletXPubYPubZPubRB() # SyncHDWalletXPubYPubZPubRB |  (optional)

    try:
        # Sync HD Wallet (xPub, yPub, zPub)
        api_response = api_instance.sync_hd_wallet__x_pub_y_pub_z_pub(blockchain, network, context=context, sync_hd_wallet_x_pub_y_pub_z_pub_rb=sync_hd_wallet_x_pub_y_pub_z_pub_rb)
        print("The response of HDWalletsApi->sync_hd_wallet__x_pub_y_pub_z_pub:\n")
        pprint(api_response)
    except Exception as e:
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

# **sync_new_hd_wallet__x_pub_y_pub_z_pub**
> SyncNewHDWalletXPubYPubZPubR sync_new_hd_wallet__x_pub_y_pub_z_pub(blockchain, network, context=context, sync_new_hd_wallet_x_pub_y_pub_z_pub_rb=sync_new_hd_wallet_x_pub_y_pub_z_pub_rb)

Sync New HD Wallet (xPub, yPub, zPub)

Through this endpoint users can add a brand new xPub to the Crypto APIs system to be ready for deriving. Unlike our other similar endpoint “Sync HD Wallet (xPub, yPub, zPub)”, this endpoint does not create new addresses nor syncs old data.

### Example

* Api Key Authentication (ApiKey):
```python
import time
import os
import cryptoapis
from cryptoapis.models.sync_new_hd_wallet_x_pub_y_pub_z_pub_r import SyncNewHDWalletXPubYPubZPubR
from cryptoapis.models.sync_new_hd_wallet_x_pub_y_pub_z_pub_rb import SyncNewHDWalletXPubYPubZPubRB
from cryptoapis.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.cryptoapis.io
# See configuration.py for a list of all supported configuration parameters.
configuration = cryptoapis.Configuration(
    host = "https://rest.cryptoapis.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with cryptoapis.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cryptoapis.HDWalletsApi(api_client)
    blockchain = 'bitcoin' # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    network = 'testnet' # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    context = 'yourExampleString' # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    sync_new_hd_wallet_x_pub_y_pub_z_pub_rb = cryptoapis.SyncNewHDWalletXPubYPubZPubRB() # SyncNewHDWalletXPubYPubZPubRB |  (optional)

    try:
        # Sync New HD Wallet (xPub, yPub, zPub)
        api_response = api_instance.sync_new_hd_wallet__x_pub_y_pub_z_pub(blockchain, network, context=context, sync_new_hd_wallet_x_pub_y_pub_z_pub_rb=sync_new_hd_wallet_x_pub_y_pub_z_pub_rb)
        print("The response of HDWalletsApi->sync_new_hd_wallet__x_pub_y_pub_z_pub:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HDWalletsApi->sync_new_hd_wallet__x_pub_y_pub_z_pub: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. | 
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. | 
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional] 
 **sync_new_hd_wallet_x_pub_y_pub_z_pub_rb** | [**SyncNewHDWalletXPubYPubZPubRB**](SyncNewHDWalletXPubYPubZPubRB.md)|  | [optional] 

### Return type

[**SyncNewHDWalletXPubYPubZPubR**](SyncNewHDWalletXPubYPubZPubR.md)

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

