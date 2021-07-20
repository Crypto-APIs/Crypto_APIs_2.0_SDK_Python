# cryptoapis.UTXOBasedApi

All URIs are relative to *https://rest.cryptoapis.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_hd_wallet__x_pub_y_pub_z_pub_details**](UTXOBasedApi.md#get_hd_wallet__x_pub_y_pub_z_pub_details) | **GET** /blockchain-data/{blockchain}/{network}/hd/{extendedPublicKey}/details | Get HD Wallet (xPub, yPub, zPub) Details
[**list_hd_wallet__x_pub_y_pub_z_pub_transactions**](UTXOBasedApi.md#list_hd_wallet__x_pub_y_pub_z_pub_transactions) | **GET** /blockchain-data/{blockchain}/{network}/hd/{extendedPublicKey}/transactions | List HD Wallet (xPub, yPub, zPub) Transactions
[**sync_hd_wallet__x_pub_y_pub_z_pub**](UTXOBasedApi.md#sync_hd_wallet__x_pub_y_pub_z_pub) | **POST** /blockchain-data/{blockchain}/{network}/hd/sync | Sync HD Wallet (xPub, yPub, zPub)


# **get_hd_wallet__x_pub_y_pub_z_pub_details**
> GetHDWalletXPubYPubZPubDetailsR get_hd_wallet__x_pub_y_pub_z_pub_details(blockchain, extended_public_key, network)

Get HD Wallet (xPub, yPub, zPub) Details

HD wallet details is useful endpoint to get the most important data about HD wallet without the need to do a lot of calculations, once the HD Wallet is synced using Sync endpoint we keep it up to date and we calculate these details in advance.

### Example

* Api Key Authentication (ApiKey):
```python
import time
import cryptoapis
from cryptoapis.api import utxo_based_api
from cryptoapis.model.xpub_sync_in_progress import XpubSyncInProgress
from cryptoapis.model.insufficient_credits import InsufficientCredits
from cryptoapis.model.invalid_api_key import InvalidApiKey
from cryptoapis.model.invalid_data import InvalidData
from cryptoapis.model.request_limit_reached import RequestLimitReached
from cryptoapis.model.get_hd_wallet_x_pub_y_pub_z_pub_details_r import GetHDWalletXPubYPubZPubDetailsR
from cryptoapis.model.feature_mainnets_not_allowed_for_plan import FeatureMainnetsNotAllowedForPlan
from cryptoapis.model.xpub_not_synced import XpubNotSynced
from cryptoapis.model.unexpected_server_error import UnexpectedServerError
from cryptoapis.model.unsupported_media_type import UnsupportedMediaType
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
    api_instance = utxo_based_api.UTXOBasedApi(api_client)
    blockchain = "bitcoin" # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    extended_public_key = "upub5Ei6bRNneqozk6smK7dvtXHC5PjUyEL4ynCfMKvjznLcXi9DQaikETzQjHvJC43XexMvQs64jxB1njMjCHpRZ4xQWAmv3ge9cVtjfsHmbvQ" # str | Defines the account extended publicly known key which is used to derive all child public keys.
    network = "testnet" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\", \"rinkeby\" are test networks.
    context = "context_example" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    derivation = "account" # str | The way how the HD walled derives, for example when the type is ACCOUNT, it derives change and receive addresses while when the type is BIP32 it derives directly. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get HD Wallet (xPub, yPub, zPub) Details
        api_response = api_instance.get_hd_wallet__x_pub_y_pub_z_pub_details(blockchain, extended_public_key, network)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling UTXOBasedApi->get_hd_wallet__x_pub_y_pub_z_pub_details: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get HD Wallet (xPub, yPub, zPub) Details
        api_response = api_instance.get_hd_wallet__x_pub_y_pub_z_pub_details(blockchain, extended_public_key, network, context=context, derivation=derivation)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling UTXOBasedApi->get_hd_wallet__x_pub_y_pub_z_pub_details: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. |
 **extended_public_key** | **str**| Defines the account extended publicly known key which is used to derive all child public keys. |
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot;, \&quot;rinkeby\&quot; are test networks. |
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
**400** | This xPub is not yet synced, please first use endpoint “Sync HD (xPub, yPub, zPub) wallet” to synchronize it. |  -  |
**401** | The provided API key is invalid. Please, generate a new one from your Dashboard. |  -  |
**402** | You have insufficient credits. Please upgrade your plan from your Dashboard or contact our team via email. |  -  |
**403** | Mainnets access is not available for your current subscription plan, please upgrade your plan to be able to use it. |  -  |
**409** | The data provided seems to be invalid. |  -  |
**415** | The selected Media Type is unavailable. The Content-Type header should be &#39;application/json&#39;. |  -  |
**422** | Your wallet (xPub, yPub, zPub) is still syncing, it should take few seconds depending on how many transactions it has. |  -  |
**429** | The request limit has been reached. There can be maximum {requests} requests per {seconds} second(s) made. Please contact our team via email if you need more or upgrade your plan. |  -  |
**500** | An unexpected server error has occurred, we are working to fix this. Please try again later and in case it occurs again please report it to our team via email. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_hd_wallet__x_pub_y_pub_z_pub_transactions**
> ListHDWalletXPubYPubZPubTransactionsR list_hd_wallet__x_pub_y_pub_z_pub_transactions(blockchain, extended_public_key, network)

List HD Wallet (xPub, yPub, zPub) Transactions

This endpoint will list HD Wallet transactions.    {note}Please note that listing data from the same type will apply pagination on the results.{/note}

### Example

* Api Key Authentication (ApiKey):
```python
import time
import cryptoapis
from cryptoapis.api import utxo_based_api
from cryptoapis.model.list_hd_wallet_x_pub_y_pub_z_pub_transactions_r import ListHDWalletXPubYPubZPubTransactionsR
from cryptoapis.model.xpub_sync_in_progress import XpubSyncInProgress
from cryptoapis.model.insufficient_credits import InsufficientCredits
from cryptoapis.model.invalid_api_key import InvalidApiKey
from cryptoapis.model.invalid_data import InvalidData
from cryptoapis.model.request_limit_reached import RequestLimitReached
from cryptoapis.model.feature_mainnets_not_allowed_for_plan import FeatureMainnetsNotAllowedForPlan
from cryptoapis.model.xpub_not_synced import XpubNotSynced
from cryptoapis.model.unexpected_server_error import UnexpectedServerError
from cryptoapis.model.unsupported_media_type import UnsupportedMediaType
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
    api_instance = utxo_based_api.UTXOBasedApi(api_client)
    blockchain = "bitcoin" # str | Represents the specific blockchain.
    extended_public_key = "tpubD9GMECjiZHCaF9NHSMAeMbQMXnM7CviEJZsYBuztVwsUjPHWjxewWAUXWV2UExaAtoEvQGXDBmVWo6ZHGtj6TsH6Pop7D9DskQwGHA1gu1w" # str | Defines the master public key (xPub) of the account.
    network = "testnet" # str | Represents the specific network.
    context = "context_example" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    derivation = "account" # str | The way how the HD walled derives, for example when the type is ACCOUNT, it derives change and receive addresses while when the type is BIP32 it derives directly. (optional)
    limit = 50 # int | Defines how many items should be returned in the response per page basis. (optional) if omitted the server will use the default value of 50
    offset = 10 # int | The starting index of the response items, i.e. where the response should start listing the returned items. (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    try:
        # List HD Wallet (xPub, yPub, zPub) Transactions
        api_response = api_instance.list_hd_wallet__x_pub_y_pub_z_pub_transactions(blockchain, extended_public_key, network)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling UTXOBasedApi->list_hd_wallet__x_pub_y_pub_z_pub_transactions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List HD Wallet (xPub, yPub, zPub) Transactions
        api_response = api_instance.list_hd_wallet__x_pub_y_pub_z_pub_transactions(blockchain, extended_public_key, network, context=context, derivation=derivation, limit=limit, offset=offset)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling UTXOBasedApi->list_hd_wallet__x_pub_y_pub_z_pub_transactions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain** | **str**| Represents the specific blockchain. |
 **extended_public_key** | **str**| Defines the master public key (xPub) of the account. |
 **network** | **str**| Represents the specific network. |
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
**400** | This xPub is not yet synced, please first use endpoint “Sync HD (xPub, yPub, zPub) wallet” to synchronize it. |  -  |
**401** | The provided API key is invalid. Please, generate a new one from your Dashboard. |  -  |
**402** | You have insufficient credits. Please upgrade your plan from your Dashboard or contact our team via email. |  -  |
**403** | Mainnets access is not available for your current subscription plan, please upgrade your plan to be able to use it. |  -  |
**409** | The data provided seems to be invalid. |  -  |
**415** | The selected Media Type is unavailable. The Content-Type header should be &#39;application/json&#39;. |  -  |
**422** | Your wallet (xPub, yPub, zPub) is still syncing, it should take few seconds depending on how many transactions it has. |  -  |
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
from cryptoapis.api import utxo_based_api
from cryptoapis.model.sync_hd_wallet_x_pub_y_pub_z_pub_r import SyncHDWalletXPubYPubZPubR
from cryptoapis.model.invalid_xpub import InvalidXpub
from cryptoapis.model.sync_hd_wallet_x_pub_y_pub_z_pub_rb import SyncHDWalletXPubYPubZPubRB
from cryptoapis.model.xpub_sync_in_progress import XpubSyncInProgress
from cryptoapis.model.insufficient_credits import InsufficientCredits
from cryptoapis.model.already_exists import AlreadyExists
from cryptoapis.model.invalid_api_key import InvalidApiKey
from cryptoapis.model.request_limit_reached import RequestLimitReached
from cryptoapis.model.feature_mainnets_not_allowed_for_plan import FeatureMainnetsNotAllowedForPlan
from cryptoapis.model.unexpected_server_error import UnexpectedServerError
from cryptoapis.model.unsupported_media_type import UnsupportedMediaType
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
    api_instance = utxo_based_api.UTXOBasedApi(api_client)
    blockchain = "bitcoin" # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    network = "testnet" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\", \"rinkeby\" are test networks.
    context = "context_example" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    sync_hd_wallet_x_pub_y_pub_z_pub_rb = SyncHDWalletXPubYPubZPubRB(
        context="context_example",
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
        print("Exception when calling UTXOBasedApi->sync_hd_wallet__x_pub_y_pub_z_pub: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Sync HD Wallet (xPub, yPub, zPub)
        api_response = api_instance.sync_hd_wallet__x_pub_y_pub_z_pub(blockchain, network, context=context, sync_hd_wallet_x_pub_y_pub_z_pub_rb=sync_hd_wallet_x_pub_y_pub_z_pub_rb)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling UTXOBasedApi->sync_hd_wallet__x_pub_y_pub_z_pub: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. |
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot;, \&quot;rinkeby\&quot; are test networks. |
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
**400** | The provided Xpub is invalid. |  -  |
**401** | The provided API key is invalid. Please, generate a new one from your Dashboard. |  -  |
**402** | You have insufficient credits. Please upgrade your plan from your Dashboard or contact our team via email. |  -  |
**403** | Mainnets access is not available for your current subscription plan, please upgrade your plan to be able to use it. |  -  |
**409** | The specified resource already exists. |  -  |
**415** | The selected Media Type is unavailable. The Content-Type header should be &#39;application/json&#39;. |  -  |
**422** | Your wallet (xPub, yPub, zPub) is still syncing, it should take few seconds depending on how many transactions it has. |  -  |
**429** | The request limit has been reached. There can be maximum {requests} requests per {seconds} second(s) made. Please contact our team via email if you need more or upgrade your plan. |  -  |
**500** | An unexpected server error has occurred, we are working to fix this. Please try again later and in case it occurs again please report it to our team via email. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

