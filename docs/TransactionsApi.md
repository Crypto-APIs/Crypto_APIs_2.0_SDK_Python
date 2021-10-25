# cryptoapis.TransactionsApi

All URIs are relative to *https://rest.cryptoapis.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_coins_transaction_from_address_for_whole_amount**](TransactionsApi.md#create_coins_transaction_from_address_for_whole_amount) | **POST** /wallet-as-a-service/wallets/{walletId}/{blockchain}/{network}/addresses/{address}/all-transaction-requests | Create Coins Transaction From Address For Whole Amount
[**create_coins_transaction_request_from_address**](TransactionsApi.md#create_coins_transaction_request_from_address) | **POST** /wallet-as-a-service/wallets/{walletId}/{blockchain}/{network}/addresses/{address}/transaction-requests | Create Coins Transaction Request from Address
[**create_coins_transaction_request_from_wallet**](TransactionsApi.md#create_coins_transaction_request_from_wallet) | **POST** /wallet-as-a-service/wallets/{walletId}/{blockchain}/{network}/transaction-requests | Create Coins Transaction Request from Wallet
[**create_tokens_transaction_request_from_address**](TransactionsApi.md#create_tokens_transaction_request_from_address) | **POST** /wallet-as-a-service/wallets/{walletId}/{blockchain}/{network}/addresses/{senderAddress}/token-transaction-requests | Create Tokens Transaction Request from Address


# **create_coins_transaction_from_address_for_whole_amount**
> CreateCoinsTransactionFromAddressForWholeAmountR create_coins_transaction_from_address_for_whole_amount(address, network, wallet_id)

Create Coins Transaction From Address For Whole Amount

Through this endpoint customers can create a new transaction from address for **coins** specifically, which will transfer over the entire available amount.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import transactions_api
from cryptoapis.model.wallet_as_a_service_address_balance_not_enough import WalletAsAServiceAddressBalanceNotEnough
from cryptoapis.model.insufficient_credits import InsufficientCredits
from cryptoapis.model.invalid_api_key import InvalidApiKey
from cryptoapis.model.invalid_request_body_structure import InvalidRequestBodyStructure
from cryptoapis.model.request_limit_reached import RequestLimitReached
from cryptoapis.model.invalid_pagination import InvalidPagination
from cryptoapis.model.create_coins_transaction_from_address_for_whole_amount_r import CreateCoinsTransactionFromAddressForWholeAmountR
from cryptoapis.model.create_coins_transaction_from_address_for_whole_amount_rb import CreateCoinsTransactionFromAddressForWholeAmountRB
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
    api_instance = transactions_api.TransactionsApi(api_client)
    address = "0x6f61e3c2fbb8c8be698bd0907ba6c04b62800fe5" # str | Defines the source address.
    network = "ropsten" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    wallet_id = "609e221675d04500068718dc" # str | Represents the sender's specific and unique Wallet ID of the sender.
    context = "context_example" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    create_coins_transaction_from_address_for_whole_amount_rb = CreateCoinsTransactionFromAddressForWholeAmountRB(
        context="context_example",
        data=CreateCoinsTransactionFromAddressForWholeAmountRBData(
            item=CreateCoinsTransactionFromAddressForWholeAmountRBDataItem(
                callback_secret_key="yourSecretString",
                callback_url="https://example.com",
                fee_priority="standard",
                note="yourAdditionalInformationhere",
                recipient_address="0xc065b539490f81b6c297c37b1925c3be2f190732",
            ),
        ),
    ) # CreateCoinsTransactionFromAddressForWholeAmountRB |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create Coins Transaction From Address For Whole Amount
        api_response = api_instance.create_coins_transaction_from_address_for_whole_amount(address, network, wallet_id)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling TransactionsApi->create_coins_transaction_from_address_for_whole_amount: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Coins Transaction From Address For Whole Amount
        api_response = api_instance.create_coins_transaction_from_address_for_whole_amount(address, network, wallet_id, context=context, create_coins_transaction_from_address_for_whole_amount_rb=create_coins_transaction_from_address_for_whole_amount_rb)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling TransactionsApi->create_coins_transaction_from_address_for_whole_amount: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Defines the source address. |
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. |
 **wallet_id** | **str**| Represents the sender&#39;s specific and unique Wallet ID of the sender. |
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. | defaults to "ethereum"
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]
 **create_coins_transaction_from_address_for_whole_amount_rb** | [**CreateCoinsTransactionFromAddressForWholeAmountRB**](CreateCoinsTransactionFromAddressForWholeAmountRB.md)|  | [optional]

### Return type

[**CreateCoinsTransactionFromAddressForWholeAmountR**](CreateCoinsTransactionFromAddressForWholeAmountR.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The resource has been successfully created. |  -  |
**400** | The pagination attributes that have been used are invalid. Please check the Documentation to see details on pagination. |  -  |
**401** | The provided API key is invalid. Please, generate a new one from your Dashboard. |  -  |
**402** | You have insufficient credits. Please upgrade your plan from your Dashboard or contact our team via email. |  -  |
**403** | Mainnets access is not available for your current subscription plan, please upgrade your plan to be able to use it. |  -  |
**409** | Your address balance is insufficient to complete the action. Please, deposit funds to your address and try again. |  -  |
**415** | The selected Media Type is unavailable. The Content-Type header should be &#39;application/json&#39;. |  -  |
**422** | Your request body for POST requests must have a structure of { data: { item: [...properties] } } |  -  |
**429** | The request limit has been reached. There can be maximum {requests} requests per {seconds} second(s) made. Please contact our team via email if you need more or upgrade your plan. |  -  |
**500** | An unexpected server error has occurred, we are working to fix this. Please try again later and in case it occurs again please report it to our team via email. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_coins_transaction_request_from_address**
> CreateCoinsTransactionRequestFromAddressR create_coins_transaction_request_from_address(address, network, wallet_id)

Create Coins Transaction Request from Address

Through this endpoint users can create a new single transaction request from one address to another.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import transactions_api
from cryptoapis.model.create_coins_transaction_request_from_address_r import CreateCoinsTransactionRequestFromAddressR
from cryptoapis.model.wallet_as_a_service_address_balance_not_enough import WalletAsAServiceAddressBalanceNotEnough
from cryptoapis.model.insufficient_credits import InsufficientCredits
from cryptoapis.model.invalid_api_key import InvalidApiKey
from cryptoapis.model.invalid_request_body_structure import InvalidRequestBodyStructure
from cryptoapis.model.request_limit_reached import RequestLimitReached
from cryptoapis.model.invalid_pagination import InvalidPagination
from cryptoapis.model.feature_mainnets_not_allowed_for_plan import FeatureMainnetsNotAllowedForPlan
from cryptoapis.model.create_coins_transaction_request_from_address_rb import CreateCoinsTransactionRequestFromAddressRB
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
    api_instance = transactions_api.TransactionsApi(api_client)
    address = "0x6f61e3c2fbb8c8be698bd0907ba6c04b62800fe5" # str | Defines the specific source address for the transaction.
    network = "ropsten" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    wallet_id = "609e221675d04500068718dc" # str | Represents the sender's specific and unique Wallet ID of the sender.
    context = "context_example" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    create_coins_transaction_request_from_address_rb = CreateCoinsTransactionRequestFromAddressRB(
        context="context_example",
        data=CreateCoinsTransactionRequestFromAddressRBData(
            item=CreateCoinsTransactionRequestFromAddressRBDataItem(
                amount="0.2",
                callback_secret_key="yourSecretString",
                callback_url="https://example.com",
                fee_priority="slow",
                note="yourAdditionalInformationhere",
                recipient_address="0xc065b539490f81b6c297c37b1925c3be2f190732",
            ),
        ),
    ) # CreateCoinsTransactionRequestFromAddressRB |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create Coins Transaction Request from Address
        api_response = api_instance.create_coins_transaction_request_from_address(address, network, wallet_id)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling TransactionsApi->create_coins_transaction_request_from_address: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Coins Transaction Request from Address
        api_response = api_instance.create_coins_transaction_request_from_address(address, network, wallet_id, context=context, create_coins_transaction_request_from_address_rb=create_coins_transaction_request_from_address_rb)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling TransactionsApi->create_coins_transaction_request_from_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Defines the specific source address for the transaction. |
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. |
 **wallet_id** | **str**| Represents the sender&#39;s specific and unique Wallet ID of the sender. |
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. | defaults to "ethereum"
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]
 **create_coins_transaction_request_from_address_rb** | [**CreateCoinsTransactionRequestFromAddressRB**](CreateCoinsTransactionRequestFromAddressRB.md)|  | [optional]

### Return type

[**CreateCoinsTransactionRequestFromAddressR**](CreateCoinsTransactionRequestFromAddressR.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The resource has been successfully created. |  -  |
**400** | The pagination attributes that have been used are invalid. Please check the Documentation to see details on pagination. |  -  |
**401** | The provided API key is invalid. Please, generate a new one from your Dashboard. |  -  |
**402** | You have insufficient credits. Please upgrade your plan from your Dashboard or contact our team via email. |  -  |
**403** | Mainnets access is not available for your current subscription plan, please upgrade your plan to be able to use it. |  -  |
**409** | Your address balance is insufficient to complete the action. Please, deposit funds to your address and try again. |  -  |
**415** | The selected Media Type is unavailable. The Content-Type header should be &#39;application/json&#39;. |  -  |
**422** | Your request body for POST requests must have a structure of { data: { item: [...properties] } } |  -  |
**429** | The request limit has been reached. There can be maximum {requests} requests per {seconds} second(s) made. Please contact our team via email if you need more or upgrade your plan. |  -  |
**500** | An unexpected server error has occurred, we are working to fix this. Please try again later and in case it occurs again please report it to our team via email. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_coins_transaction_request_from_wallet**
> CreateCoinsTransactionRequestFromWalletR create_coins_transaction_request_from_wallet(blockchain, wallet_id)

Create Coins Transaction Request from Wallet

Through this endpoint users can create a new transaction request from the entire Wallet instead from just a specific address. This endpoint can generate transactions from multiple to multiple addresses.    {warning}This is available **only** for UTXO-based protocols such as Bitcoin, Bitcoin Cash, Litecoin, etc. It **is not** available for Account-based protocols like Ethereum.{/warning}

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import transactions_api
from cryptoapis.model.create_coins_transaction_request_from_wallet_rb import CreateCoinsTransactionRequestFromWalletRB
from cryptoapis.model.wallet_as_a_service_no_deposit_addresses_found import WalletAsAServiceNoDepositAddressesFound
from cryptoapis.model.insufficient_credits import InsufficientCredits
from cryptoapis.model.invalid_api_key import InvalidApiKey
from cryptoapis.model.invalid_request_body_structure import InvalidRequestBodyStructure
from cryptoapis.model.request_limit_reached import RequestLimitReached
from cryptoapis.model.invalid_pagination import InvalidPagination
from cryptoapis.model.create_coins_transaction_request_from_wallet_r import CreateCoinsTransactionRequestFromWalletR
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
    api_instance = transactions_api.TransactionsApi(api_client)
    blockchain = "bitcoin" # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    wallet_id = "609e221675d04500068718dc" # str | Represents the sender's specific and unique Wallet ID of the sender.
    context = "context_example" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    create_coins_transaction_request_from_wallet_rb = CreateCoinsTransactionRequestFromWalletRB(
        context="context_example",
        data=CreateCoinsTransactionRequestFromWalletRBData(
            item=CreateCoinsTransactionRequestFromWalletRBDataItem(
                callback_secret_key="yourSecretKey",
                callback_url="https://example.com",
                fee_priority="standard",
                note="yourAdditionalInformationhere",
                prepare_strategy="minimize-dust",
                recipients=[
                    CreateCoinsTransactionRequestFromWalletRBDataItemRecipients(
                        address="2MtzNEqm2D9jcbPJ5mW7Z3AUNwqt3afZH66",
                        amount="0.125",
                    ),
                ],
            ),
        ),
    ) # CreateCoinsTransactionRequestFromWalletRB |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create Coins Transaction Request from Wallet
        api_response = api_instance.create_coins_transaction_request_from_wallet(blockchain, wallet_id)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling TransactionsApi->create_coins_transaction_request_from_wallet: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Coins Transaction Request from Wallet
        api_response = api_instance.create_coins_transaction_request_from_wallet(blockchain, wallet_id, context=context, create_coins_transaction_request_from_wallet_rb=create_coins_transaction_request_from_wallet_rb)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling TransactionsApi->create_coins_transaction_request_from_wallet: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. |
 **wallet_id** | **str**| Represents the sender&#39;s specific and unique Wallet ID of the sender. |
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. | defaults to "testnet"
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]
 **create_coins_transaction_request_from_wallet_rb** | [**CreateCoinsTransactionRequestFromWalletRB**](CreateCoinsTransactionRequestFromWalletRB.md)|  | [optional]

### Return type

[**CreateCoinsTransactionRequestFromWalletR**](CreateCoinsTransactionRequestFromWalletR.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The resource has been successfully created. |  -  |
**400** | The pagination attributes that have been used are invalid. Please check the Documentation to see details on pagination. |  -  |
**401** | The provided API key is invalid. Please, generate a new one from your Dashboard. |  -  |
**402** | You have insufficient credits. Please upgrade your plan from your Dashboard or contact our team via email. |  -  |
**403** | Mainnets access is not available for your current subscription plan, please upgrade your plan to be able to use it. |  -  |
**409** | Please first create a deposit address for the specific blockchain and network, in order to be able to make transactions. |  -  |
**415** | The selected Media Type is unavailable. The Content-Type header should be &#39;application/json&#39;. |  -  |
**422** | Your request body for POST requests must have a structure of { data: { item: [...properties] } } |  -  |
**429** | The request limit has been reached. There can be maximum {requests} requests per {seconds} second(s) made. Please contact our team via email if you need more or upgrade your plan. |  -  |
**500** | An unexpected server error has occurred, we are working to fix this. Please try again later and in case it occurs again please report it to our team via email. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_tokens_transaction_request_from_address**
> CreateTokensTransactionRequestFromAddressR create_tokens_transaction_request_from_address(sender_address, wallet_id)

Create Tokens Transaction Request from Address

Through this endpoint users can make a single token transaction.    {warning}This applies only to **fungible** tokens, **not** NFTs (non-fungible tokens).{/warning}    {note}To have an operational callback subscription, you need to first verify a domain for the Callback URL. Please see more information on Callbacks [here](https://developers.cryptoapis.io/technical-documentation/general-information/callbacks#callback-url).{/note}    {warning}Crypto APIs will notify the user **only when** the event occurs. There are cases when the specific event doesn't happen at all, or takes a long time to do so. A callback notification **will not** be sent if the event does not or cannot occur, or will take long time to occur.{/warning}

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import transactions_api
from cryptoapis.model.wallet_as_a_service_token_not_supported import WalletAsAServiceTokenNotSupported
from cryptoapis.model.insufficient_credits import InsufficientCredits
from cryptoapis.model.create_tokens_transaction_request_from_address_r import CreateTokensTransactionRequestFromAddressR
from cryptoapis.model.invalid_api_key import InvalidApiKey
from cryptoapis.model.invalid_request_body_structure import InvalidRequestBodyStructure
from cryptoapis.model.request_limit_reached import RequestLimitReached
from cryptoapis.model.invalid_pagination import InvalidPagination
from cryptoapis.model.create_tokens_transaction_request_from_address_rb import CreateTokensTransactionRequestFromAddressRB
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
    api_instance = transactions_api.TransactionsApi(api_client)
    sender_address = "0x6f61e3c2fbb8c8be698bd0907ba6c04b62800fe5" # str | Defines the specific source address for the transaction.
    wallet_id = "609e221675d04500068718dc" # str | Defines the unique ID of the Wallet.
    context = "context_example" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    create_tokens_transaction_request_from_address_rb = CreateTokensTransactionRequestFromAddressRB(
        context="context_example",
        data=CreateTokensTransactionRequestFromAddressRBData(
            item=CreateTokensTransactionRequestFromAddressRBDataItem(
                amount="0.2",
                callback_secret_key="yourSecretString",
                callback_url="https://example.com",
                fee_priority="standard",
                note="yourAdditionalInformationhere",
                recipient_address="0xc065b539490f81b6c297c37b1925c3be2f190732",
                token_identifier="0xdac17f958d2ee523a2206206994597c13d831ec7",
            ),
        ),
    ) # CreateTokensTransactionRequestFromAddressRB |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create Tokens Transaction Request from Address
        api_response = api_instance.create_tokens_transaction_request_from_address(sender_address, wallet_id)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling TransactionsApi->create_tokens_transaction_request_from_address: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Tokens Transaction Request from Address
        api_response = api_instance.create_tokens_transaction_request_from_address(sender_address, wallet_id, context=context, create_tokens_transaction_request_from_address_rb=create_tokens_transaction_request_from_address_rb)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling TransactionsApi->create_tokens_transaction_request_from_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sender_address** | **str**| Defines the specific source address for the transaction. |
 **wallet_id** | **str**| Defines the unique ID of the Wallet. |
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. | defaults to "ethereum"
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. | defaults to "mainnet"
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]
 **create_tokens_transaction_request_from_address_rb** | [**CreateTokensTransactionRequestFromAddressRB**](CreateTokensTransactionRequestFromAddressRB.md)|  | [optional]

### Return type

[**CreateTokensTransactionRequestFromAddressR**](CreateTokensTransactionRequestFromAddressR.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The resource has been successfully created. |  -  |
**400** | The pagination attributes that have been used are invalid. Please check the Documentation to see details on pagination. |  -  |
**401** | The provided API key is invalid. Please, generate a new one from your Dashboard. |  -  |
**402** | You have insufficient credits. Please upgrade your plan from your Dashboard or contact our team via email. |  -  |
**403** | Mainnets access is not available for your current subscription plan, please upgrade your plan to be able to use it. |  -  |
**409** | The token is not supported for this blockchain and network. To be supported, please contact our team. |  -  |
**415** | The selected Media Type is unavailable. The Content-Type header should be &#39;application/json&#39;. |  -  |
**422** | Your request body for POST requests must have a structure of { data: { item: [...properties] } } |  -  |
**429** | The request limit has been reached. There can be maximum {requests} requests per {seconds} second(s) made. Please contact our team via email if you need more or upgrade your plan. |  -  |
**500** | An unexpected server error has occurred, we are working to fix this. Please try again later and in case it occurs again please report it to our team via email. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

