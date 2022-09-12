# cryptoapis.TransactionsApi

All URIs are relative to *https://rest.cryptoapis.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_coins_transaction_from_address_for_whole_amount**](TransactionsApi.md#create_coins_transaction_from_address_for_whole_amount) | **POST** /wallet-as-a-service/wallets/{walletId}/{blockchain}/{network}/addresses/{address}/all-transaction-requests | Create Coins Transaction From Address For Whole Amount
[**create_coins_transaction_request_from_address**](TransactionsApi.md#create_coins_transaction_request_from_address) | **POST** /wallet-as-a-service/wallets/{walletId}/{blockchain}/{network}/addresses/{address}/transaction-requests | Create Coins Transaction Request from Address
[**create_coins_transaction_request_from_wallet**](TransactionsApi.md#create_coins_transaction_request_from_wallet) | **POST** /wallet-as-a-service/wallets/{walletId}/{blockchain}/{network}/transaction-requests | Create Coins Transaction Request from Wallet
[**create_fungible_token_transaction_request_from_address_without_fee_priority**](TransactionsApi.md#create_fungible_token_transaction_request_from_address_without_fee_priority) | **POST** /wallet-as-a-service/wallets/{walletId}/{blockchain}/{network}/addresses/{senderAddress}/feeless-token-transaction-requests | Create Fungible Token Transaction Request From Address Without Fee Priority
[**create_fungible_tokens_transaction_request_from_address**](TransactionsApi.md#create_fungible_tokens_transaction_request_from_address) | **POST** /wallet-as-a-service/wallets/{walletId}/{blockchain}/{network}/addresses/{senderAddress}/token-transaction-requests | Create Fungible Tokens Transaction Request from Address
[**create_single_transaction_request_from_address_without_fee_priority**](TransactionsApi.md#create_single_transaction_request_from_address_without_fee_priority) | **POST** /wallet-as-a-service/wallets/{walletId}/{blockchain}/{network}/addresses/{address}/feeless-transaction-requests | Create Single Transaction Request From Address Without Fee Priority


# **create_coins_transaction_from_address_for_whole_amount**
> CreateCoinsTransactionFromAddressForWholeAmountR create_coins_transaction_from_address_for_whole_amount(address, blockchain, network, wallet_id)

Create Coins Transaction From Address For Whole Amount

Through this endpoint customers can create a new transaction from address for **coins** specifically, which will transfer over the entire available amount.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import transactions_api
from cryptoapis.model.convert_bitcoin_cash_address429_response import ConvertBitcoinCashAddress429Response
from cryptoapis.model.convert_bitcoin_cash_address500_response import ConvertBitcoinCashAddress500Response
from cryptoapis.model.convert_bitcoin_cash_address422_response import ConvertBitcoinCashAddress422Response
from cryptoapis.model.create_coins_transaction_from_address_for_whole_amount400_response import CreateCoinsTransactionFromAddressForWholeAmount400Response
from cryptoapis.model.create_coins_transaction_from_address_for_whole_amount403_response import CreateCoinsTransactionFromAddressForWholeAmount403Response
from cryptoapis.model.create_coins_transaction_from_address_for_whole_amount401_response import CreateCoinsTransactionFromAddressForWholeAmount401Response
from cryptoapis.model.create_coins_transaction_from_address_for_whole_amount_r import CreateCoinsTransactionFromAddressForWholeAmountR
from cryptoapis.model.create_coins_transaction_from_address_for_whole_amount_rb import CreateCoinsTransactionFromAddressForWholeAmountRB
from cryptoapis.model.convert_bitcoin_cash_address402_response import ConvertBitcoinCashAddress402Response
from cryptoapis.model.create_coins_transaction_from_address_for_whole_amount409_response import CreateCoinsTransactionFromAddressForWholeAmount409Response
from cryptoapis.model.convert_bitcoin_cash_address415_response import ConvertBitcoinCashAddress415Response
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
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with cryptoapis.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = transactions_api.TransactionsApi(api_client)
    address = "0x6f61e3c2fbb8c8be698bd0907ba6c04b62800fe5" # str | Defines the source address.
    blockchain = "ethereum" # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    network = "ropsten" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    wallet_id = "609e221675d04500068718dc" # str | Represents the sender's specific and unique Wallet ID of the sender.
    context = "yourExampleString" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    create_coins_transaction_from_address_for_whole_amount_rb = CreateCoinsTransactionFromAddressForWholeAmountRB(
        context="yourExampleString",
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
        api_response = api_instance.create_coins_transaction_from_address_for_whole_amount(address, blockchain, network, wallet_id)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling TransactionsApi->create_coins_transaction_from_address_for_whole_amount: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Coins Transaction From Address For Whole Amount
        api_response = api_instance.create_coins_transaction_from_address_for_whole_amount(address, blockchain, network, wallet_id, context=context, create_coins_transaction_from_address_for_whole_amount_rb=create_coins_transaction_from_address_for_whole_amount_rb)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling TransactionsApi->create_coins_transaction_from_address_for_whole_amount: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Defines the source address. |
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. |
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. |
 **wallet_id** | **str**| Represents the sender&#39;s specific and unique Wallet ID of the sender. |
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
**400** | 400 |  -  |
**401** | 401 |  -  |
**402** | You have insufficient credits. Please upgrade your plan from your Dashboard or contact our team via email. |  -  |
**403** | 403 |  -  |
**409** | 409 |  -  |
**415** | The selected Media Type is unavailable. The Content-Type header should be &#39;application/json&#39;. |  -  |
**422** | Your request body for POST requests must have a structure of { data: { item: [...properties] } } |  -  |
**429** | The request limit has been reached. There can be maximum {requests} requests per {seconds} second(s) made. Please contact our team via email if you need more or upgrade your plan. |  -  |
**500** | An unexpected server error has occurred, we are working to fix this. Please try again later and in case it occurs again please report it to our team via email. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_coins_transaction_request_from_address**
> CreateCoinsTransactionRequestFromAddressR create_coins_transaction_request_from_address(address, blockchain, network, wallet_id)

Create Coins Transaction Request from Address

Through this endpoint users can create a new single transaction request from one address to another.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import transactions_api
from cryptoapis.model.convert_bitcoin_cash_address429_response import ConvertBitcoinCashAddress429Response
from cryptoapis.model.convert_bitcoin_cash_address500_response import ConvertBitcoinCashAddress500Response
from cryptoapis.model.create_coins_transaction_request_from_address_r import CreateCoinsTransactionRequestFromAddressR
from cryptoapis.model.convert_bitcoin_cash_address422_response import ConvertBitcoinCashAddress422Response
from cryptoapis.model.create_coins_transaction_request_from_address400_response import CreateCoinsTransactionRequestFromAddress400Response
from cryptoapis.model.create_coins_transaction_request_from_address409_response import CreateCoinsTransactionRequestFromAddress409Response
from cryptoapis.model.create_coins_transaction_request_from_address403_response import CreateCoinsTransactionRequestFromAddress403Response
from cryptoapis.model.create_coins_transaction_request_from_address401_response import CreateCoinsTransactionRequestFromAddress401Response
from cryptoapis.model.convert_bitcoin_cash_address402_response import ConvertBitcoinCashAddress402Response
from cryptoapis.model.create_coins_transaction_request_from_address_rb import CreateCoinsTransactionRequestFromAddressRB
from cryptoapis.model.convert_bitcoin_cash_address415_response import ConvertBitcoinCashAddress415Response
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
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with cryptoapis.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = transactions_api.TransactionsApi(api_client)
    address = "0x6f61e3c2fbb8c8be698bd0907ba6c04b62800fe5" # str | Defines the specific source address for the transaction. For XRP we also support the X-address format.
    blockchain = "ethereum" # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    network = "ropsten" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    wallet_id = "609e221675d04500068718dc" # str | Represents the sender's specific and unique Wallet ID of the sender.
    context = "yourExampleString" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    create_coins_transaction_request_from_address_rb = CreateCoinsTransactionRequestFromAddressRB(
        context="yourExampleString",
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
        api_response = api_instance.create_coins_transaction_request_from_address(address, blockchain, network, wallet_id)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling TransactionsApi->create_coins_transaction_request_from_address: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Coins Transaction Request from Address
        api_response = api_instance.create_coins_transaction_request_from_address(address, blockchain, network, wallet_id, context=context, create_coins_transaction_request_from_address_rb=create_coins_transaction_request_from_address_rb)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling TransactionsApi->create_coins_transaction_request_from_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Defines the specific source address for the transaction. For XRP we also support the X-address format. |
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. |
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. |
 **wallet_id** | **str**| Represents the sender&#39;s specific and unique Wallet ID of the sender. |
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
**400** | 400 |  -  |
**401** | 401 |  -  |
**402** | You have insufficient credits. Please upgrade your plan from your Dashboard or contact our team via email. |  -  |
**403** | 403 |  -  |
**409** | 409 |  -  |
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
from cryptoapis.model.convert_bitcoin_cash_address429_response import ConvertBitcoinCashAddress429Response
from cryptoapis.model.convert_bitcoin_cash_address500_response import ConvertBitcoinCashAddress500Response
from cryptoapis.model.create_coins_transaction_request_from_wallet400_response import CreateCoinsTransactionRequestFromWallet400Response
from cryptoapis.model.convert_bitcoin_cash_address422_response import ConvertBitcoinCashAddress422Response
from cryptoapis.model.create_coins_transaction_request_from_wallet_rb import CreateCoinsTransactionRequestFromWalletRB
from cryptoapis.model.create_coins_transaction_request_from_wallet401_response import CreateCoinsTransactionRequestFromWallet401Response
from cryptoapis.model.create_coins_transaction_request_from_wallet_r import CreateCoinsTransactionRequestFromWalletR
from cryptoapis.model.create_coins_transaction_request_from_wallet409_response import CreateCoinsTransactionRequestFromWallet409Response
from cryptoapis.model.create_coins_transaction_request_from_wallet403_response import CreateCoinsTransactionRequestFromWallet403Response
from cryptoapis.model.convert_bitcoin_cash_address402_response import ConvertBitcoinCashAddress402Response
from cryptoapis.model.convert_bitcoin_cash_address415_response import ConvertBitcoinCashAddress415Response
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
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with cryptoapis.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = transactions_api.TransactionsApi(api_client)
    blockchain = "bitcoin" # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    wallet_id = "609e221675d04500068718dc" # str | Represents the sender's specific and unique Wallet ID of the sender.
    context = "yourExampleString" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    create_coins_transaction_request_from_wallet_rb = CreateCoinsTransactionRequestFromWalletRB(
        context="yourExampleString",
        data=CreateCoinsTransactionRequestFromWalletRBData(
            item=CreateCoinsTransactionRequestFromWalletRBDataItem(
                callback_secret_key="yourSecretKey",
                callback_url="https://example.com",
                fee_priority="standard",
                note="yourAdditionalInformationhere",
                prepare_strategy="minimize-dust",
                recipients=[
                    CreateCoinsTransactionRequestFromWalletRBDataItemRecipientsInner(
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
**400** | 400 |  -  |
**401** | 401 |  -  |
**402** | You have insufficient credits. Please upgrade your plan from your Dashboard or contact our team via email. |  -  |
**403** | 403 |  -  |
**409** | 409 |  -  |
**415** | The selected Media Type is unavailable. The Content-Type header should be &#39;application/json&#39;. |  -  |
**422** | Your request body for POST requests must have a structure of { data: { item: [...properties] } } |  -  |
**429** | The request limit has been reached. There can be maximum {requests} requests per {seconds} second(s) made. Please contact our team via email if you need more or upgrade your plan. |  -  |
**500** | An unexpected server error has occurred, we are working to fix this. Please try again later and in case it occurs again please report it to our team via email. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_fungible_token_transaction_request_from_address_without_fee_priority**
> CreateFungibleTokenTransactionRequestFromAddressWithoutFeePriorityR create_fungible_token_transaction_request_from_address_without_fee_priority(network, sender_address, wallet_id)

Create Fungible Token Transaction Request From Address Without Fee Priority

Through this endpoint customers can make a single feeless token transaction on the Tron blockchain protocol. TRX transactions burn certain resources called Bandwidth and Energy. Each account has 1500 bandwidth free for use every 24 hours and more can be obtained by staking TRX. The unit price of Energy is 280 SUN and of bandwidth - 1000 SUN. If the resources are insufficient, TRX will be burned to pay for them.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import transactions_api
from cryptoapis.model.convert_bitcoin_cash_address429_response import ConvertBitcoinCashAddress429Response
from cryptoapis.model.convert_bitcoin_cash_address500_response import ConvertBitcoinCashAddress500Response
from cryptoapis.model.convert_bitcoin_cash_address422_response import ConvertBitcoinCashAddress422Response
from cryptoapis.model.create_fungible_token_transaction_request_from_address_without_fee_priority409_response import CreateFungibleTokenTransactionRequestFromAddressWithoutFeePriority409Response
from cryptoapis.model.create_fungible_token_transaction_request_from_address_without_fee_priority403_response import CreateFungibleTokenTransactionRequestFromAddressWithoutFeePriority403Response
from cryptoapis.model.create_fungible_token_transaction_request_from_address_without_fee_priority401_response import CreateFungibleTokenTransactionRequestFromAddressWithoutFeePriority401Response
from cryptoapis.model.convert_bitcoin_cash_address402_response import ConvertBitcoinCashAddress402Response
from cryptoapis.model.create_fungible_token_transaction_request_from_address_without_fee_priority_r import CreateFungibleTokenTransactionRequestFromAddressWithoutFeePriorityR
from cryptoapis.model.create_fungible_token_transaction_request_from_address_without_fee_priority_rb import CreateFungibleTokenTransactionRequestFromAddressWithoutFeePriorityRB
from cryptoapis.model.create_fungible_token_transaction_request_from_address_without_fee_priority400_response import CreateFungibleTokenTransactionRequestFromAddressWithoutFeePriority400Response
from cryptoapis.model.convert_bitcoin_cash_address415_response import ConvertBitcoinCashAddress415Response
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
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with cryptoapis.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = transactions_api.TransactionsApi(api_client)
    network = "nile" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    sender_address = "TX8VXpdEoNNrKeEuNTfbEXfa9eZivcyUwD" # str | Defines the specific source address for the transaction.
    wallet_id = "62b9b5c3b97f4b0008092714" # str | Defines the unique ID of the Wallet.
    context = "yourExampleString" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    create_fungible_token_transaction_request_from_address_without_fee_priority_rb = CreateFungibleTokenTransactionRequestFromAddressWithoutFeePriorityRB(
        context="yourExampleString",
        data=CreateFungibleTokenTransactionRequestFromAddressWithoutFeePriorityRBData(
            item=CreateFungibleTokenTransactionRequestFromAddressWithoutFeePriorityRBDataItem(
                amount="0.25684",
                callback_secret_key="yourSecretString",
                callback_url="https://example.com",
                fee_limit="1000000000",
                note="yourAdditionalInformationhere",
                recipient_address="TMVeigwYyuXJVHER4oA2yQzsFFSN2JfXkt",
                token_identifier="TF17BgPaZYbz8oxbjhriubPDsA7ArKoLX3",
            ),
        ),
    ) # CreateFungibleTokenTransactionRequestFromAddressWithoutFeePriorityRB |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create Fungible Token Transaction Request From Address Without Fee Priority
        api_response = api_instance.create_fungible_token_transaction_request_from_address_without_fee_priority(network, sender_address, wallet_id)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling TransactionsApi->create_fungible_token_transaction_request_from_address_without_fee_priority: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Fungible Token Transaction Request From Address Without Fee Priority
        api_response = api_instance.create_fungible_token_transaction_request_from_address_without_fee_priority(network, sender_address, wallet_id, context=context, create_fungible_token_transaction_request_from_address_without_fee_priority_rb=create_fungible_token_transaction_request_from_address_without_fee_priority_rb)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling TransactionsApi->create_fungible_token_transaction_request_from_address_without_fee_priority: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. |
 **sender_address** | **str**| Defines the specific source address for the transaction. |
 **wallet_id** | **str**| Defines the unique ID of the Wallet. |
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. | defaults to "tron"
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]
 **create_fungible_token_transaction_request_from_address_without_fee_priority_rb** | [**CreateFungibleTokenTransactionRequestFromAddressWithoutFeePriorityRB**](CreateFungibleTokenTransactionRequestFromAddressWithoutFeePriorityRB.md)|  | [optional]

### Return type

[**CreateFungibleTokenTransactionRequestFromAddressWithoutFeePriorityR**](CreateFungibleTokenTransactionRequestFromAddressWithoutFeePriorityR.md)

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
**422** | Your request body for POST requests must have a structure of { data: { item: [...properties] } } |  -  |
**429** | The request limit has been reached. There can be maximum {requests} requests per {seconds} second(s) made. Please contact our team via email if you need more or upgrade your plan. |  -  |
**500** | An unexpected server error has occurred, we are working to fix this. Please try again later and in case it occurs again please report it to our team via email. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_fungible_tokens_transaction_request_from_address**
> CreateFungibleTokensTransactionRequestFromAddressR create_fungible_tokens_transaction_request_from_address(sender_address, wallet_id)

Create Fungible Tokens Transaction Request from Address

Through this endpoint users can make a single token transaction.    {note}To have an operational callback subscription, you need to first verify a domain for the Callback URL. Please see more information on Callbacks [here](https://developers.cryptoapis.io/technical-documentation/general-information/callbacks#callback-url).{/note}    {warning}Crypto APIs will notify the user **only when** the event occurs. There are cases when the specific event doesn't happen at all, or takes a long time to do so. A callback notification **will not** be sent if the event does not or cannot occur, or will take long time to occur.{/warning}

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import transactions_api
from cryptoapis.model.convert_bitcoin_cash_address429_response import ConvertBitcoinCashAddress429Response
from cryptoapis.model.convert_bitcoin_cash_address500_response import ConvertBitcoinCashAddress500Response
from cryptoapis.model.create_fungible_tokens_transaction_request_from_address_r import CreateFungibleTokensTransactionRequestFromAddressR
from cryptoapis.model.create_fungible_tokens_transaction_request_from_address403_response import CreateFungibleTokensTransactionRequestFromAddress403Response
from cryptoapis.model.convert_bitcoin_cash_address422_response import ConvertBitcoinCashAddress422Response
from cryptoapis.model.create_fungible_tokens_transaction_request_from_address400_response import CreateFungibleTokensTransactionRequestFromAddress400Response
from cryptoapis.model.create_fungible_tokens_transaction_request_from_address401_response import CreateFungibleTokensTransactionRequestFromAddress401Response
from cryptoapis.model.create_fungible_tokens_transaction_request_from_address409_response import CreateFungibleTokensTransactionRequestFromAddress409Response
from cryptoapis.model.convert_bitcoin_cash_address402_response import ConvertBitcoinCashAddress402Response
from cryptoapis.model.create_fungible_tokens_transaction_request_from_address_rb import CreateFungibleTokensTransactionRequestFromAddressRB
from cryptoapis.model.convert_bitcoin_cash_address415_response import ConvertBitcoinCashAddress415Response
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
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with cryptoapis.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = transactions_api.TransactionsApi(api_client)
    sender_address = "0x6f61e3c2fbb8c8be698bd0907ba6c04b62800fe5" # str | Defines the specific source address for the transaction.
    wallet_id = "609e221675d04500068718dc" # str | Defines the unique ID of the Wallet.
    context = "yourExampleString" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    create_fungible_tokens_transaction_request_from_address_rb = CreateFungibleTokensTransactionRequestFromAddressRB(
        context="yourExampleString",
        data=CreateFungibleTokensTransactionRequestFromAddressRBData(
            item=CreateFungibleTokensTransactionRequestFromAddressRBDataItem(
                amount="0.2",
                callback_secret_key="yourSecretString",
                callback_url="https://example.com",
                fee_priority="standard",
                note="yourAdditionalInformationhere",
                recipient_address="0xc065b539490f81b6c297c37b1925c3be2f190732",
                token_identifier="0xdac17f958d2ee523a2206206994597c13d831ec7",
            ),
        ),
    ) # CreateFungibleTokensTransactionRequestFromAddressRB |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create Fungible Tokens Transaction Request from Address
        api_response = api_instance.create_fungible_tokens_transaction_request_from_address(sender_address, wallet_id)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling TransactionsApi->create_fungible_tokens_transaction_request_from_address: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Fungible Tokens Transaction Request from Address
        api_response = api_instance.create_fungible_tokens_transaction_request_from_address(sender_address, wallet_id, context=context, create_fungible_tokens_transaction_request_from_address_rb=create_fungible_tokens_transaction_request_from_address_rb)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling TransactionsApi->create_fungible_tokens_transaction_request_from_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sender_address** | **str**| Defines the specific source address for the transaction. |
 **wallet_id** | **str**| Defines the unique ID of the Wallet. |
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. | defaults to "ethereum"
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. | defaults to "mainnet"
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]
 **create_fungible_tokens_transaction_request_from_address_rb** | [**CreateFungibleTokensTransactionRequestFromAddressRB**](CreateFungibleTokensTransactionRequestFromAddressRB.md)|  | [optional]

### Return type

[**CreateFungibleTokensTransactionRequestFromAddressR**](CreateFungibleTokensTransactionRequestFromAddressR.md)

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
**422** | Your request body for POST requests must have a structure of { data: { item: [...properties] } } |  -  |
**429** | The request limit has been reached. There can be maximum {requests} requests per {seconds} second(s) made. Please contact our team via email if you need more or upgrade your plan. |  -  |
**500** | An unexpected server error has occurred, we are working to fix this. Please try again later and in case it occurs again please report it to our team via email. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_single_transaction_request_from_address_without_fee_priority**
> CreateSingleTransactionRequestFromAddressWithoutFeePriorityR create_single_transaction_request_from_address_without_fee_priority(address, network, wallet_id)

Create Single Transaction Request From Address Without Fee Priority

Through this endpoint users can create a new single transaction request from one address to another. The difference between this endpoint and \"Create Coins Transaction Request from Address\"  is that for Tron blockchain there is no Fee Priority that defines how fast a transaction can be mined.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import transactions_api
from cryptoapis.model.convert_bitcoin_cash_address429_response import ConvertBitcoinCashAddress429Response
from cryptoapis.model.convert_bitcoin_cash_address500_response import ConvertBitcoinCashAddress500Response
from cryptoapis.model.create_single_transaction_request_from_address_without_fee_priority409_response import CreateSingleTransactionRequestFromAddressWithoutFeePriority409Response
from cryptoapis.model.convert_bitcoin_cash_address422_response import ConvertBitcoinCashAddress422Response
from cryptoapis.model.create_single_transaction_request_from_address_without_fee_priority403_response import CreateSingleTransactionRequestFromAddressWithoutFeePriority403Response
from cryptoapis.model.create_single_transaction_request_from_address_without_fee_priority400_response import CreateSingleTransactionRequestFromAddressWithoutFeePriority400Response
from cryptoapis.model.create_single_transaction_request_from_address_without_fee_priority401_response import CreateSingleTransactionRequestFromAddressWithoutFeePriority401Response
from cryptoapis.model.create_single_transaction_request_from_address_without_fee_priority_rb import CreateSingleTransactionRequestFromAddressWithoutFeePriorityRB
from cryptoapis.model.create_single_transaction_request_from_address_without_fee_priority_r import CreateSingleTransactionRequestFromAddressWithoutFeePriorityR
from cryptoapis.model.convert_bitcoin_cash_address402_response import ConvertBitcoinCashAddress402Response
from cryptoapis.model.convert_bitcoin_cash_address415_response import ConvertBitcoinCashAddress415Response
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
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with cryptoapis.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = transactions_api.TransactionsApi(api_client)
    address = "TX8VXpdEoNNrKeEuNTfbEXfa9eZivcyUwD" # str | Defines the specific source address for the transaction.
    network = "nile" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    wallet_id = "62b9b5c3b97f4b0008092714" # str | Represents the sender's specific and unique Wallet ID of the sender.
    context = "yourExampleString" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    create_single_transaction_request_from_address_without_fee_priority_rb = CreateSingleTransactionRequestFromAddressWithoutFeePriorityRB(
        context="yourExampleString",
        data=CreateSingleTransactionRequestFromAddressWithoutFeePriorityRBData(
            item=CreateSingleTransactionRequestFromAddressWithoutFeePriorityRBDataItem(
                amount="0.0006",
                callback_secret_key="yourSecretKey",
                callback_url="https://example.com",
                note="yourAdditionalInformationhere",
                recipient_address="TMVeigwYyuXJVHER4oA2yQzsFFSN2JfXkt",
            ),
        ),
    ) # CreateSingleTransactionRequestFromAddressWithoutFeePriorityRB |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create Single Transaction Request From Address Without Fee Priority
        api_response = api_instance.create_single_transaction_request_from_address_without_fee_priority(address, network, wallet_id)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling TransactionsApi->create_single_transaction_request_from_address_without_fee_priority: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Single Transaction Request From Address Without Fee Priority
        api_response = api_instance.create_single_transaction_request_from_address_without_fee_priority(address, network, wallet_id, context=context, create_single_transaction_request_from_address_without_fee_priority_rb=create_single_transaction_request_from_address_without_fee_priority_rb)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling TransactionsApi->create_single_transaction_request_from_address_without_fee_priority: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Defines the specific source address for the transaction. |
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. |
 **wallet_id** | **str**| Represents the sender&#39;s specific and unique Wallet ID of the sender. |
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. | defaults to "tron"
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]
 **create_single_transaction_request_from_address_without_fee_priority_rb** | [**CreateSingleTransactionRequestFromAddressWithoutFeePriorityRB**](CreateSingleTransactionRequestFromAddressWithoutFeePriorityRB.md)|  | [optional]

### Return type

[**CreateSingleTransactionRequestFromAddressWithoutFeePriorityR**](CreateSingleTransactionRequestFromAddressWithoutFeePriorityR.md)

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
**422** | Your request body for POST requests must have a structure of { data: { item: [...properties] } } |  -  |
**429** | The request limit has been reached. There can be maximum {requests} requests per {seconds} second(s) made. Please contact our team via email if you need more or upgrade your plan. |  -  |
**500** | An unexpected server error has occurred, we are working to fix this. Please try again later and in case it occurs again please report it to our team via email. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

