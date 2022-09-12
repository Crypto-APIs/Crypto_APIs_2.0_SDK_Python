# cryptoapis.CreateSubscriptionsForApi

All URIs are relative to *https://rest.cryptoapis.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**block_height_reached**](CreateSubscriptionsForApi.md#block_height_reached) | **POST** /blockchain-events/{blockchain}/{network}/subscriptions/block-height-reached | Block Height Reached
[**mined_transaction**](CreateSubscriptionsForApi.md#mined_transaction) | **POST** /blockchain-events/{blockchain}/{network}/subscriptions/transaction-mined | Mined transaction
[**new_block**](CreateSubscriptionsForApi.md#new_block) | **POST** /blockchain-events/{blockchain}/{network}/subscriptions/block-mined | New Block
[**new_confirmed_coins_transactions**](CreateSubscriptionsForApi.md#new_confirmed_coins_transactions) | **POST** /blockchain-events/{blockchain}/{network}/subscriptions/address-coins-transactions-confirmed | New confirmed coins transactions
[**new_confirmed_coins_transactions_and_each_confirmation**](CreateSubscriptionsForApi.md#new_confirmed_coins_transactions_and_each_confirmation) | **POST** /blockchain-events/{blockchain}/{network}/subscriptions/address-coins-transactions-confirmed-each-confirmation | New confirmed coins transactions and each confirmation
[**new_confirmed_coins_transactions_for_specific_amount**](CreateSubscriptionsForApi.md#new_confirmed_coins_transactions_for_specific_amount) | **POST** /blockchain-events/{blockchain}/{network}/subscriptions/coins-transactions-for-specific-amount | New Confirmed Coins Transactions For Specific Amount
[**new_confirmed_internal_transactions**](CreateSubscriptionsForApi.md#new_confirmed_internal_transactions) | **POST** /blockchain-events/{blockchain}/{network}/subscriptions/address-internal-transactions-confirmed | New confirmed internal transactions
[**new_confirmed_internal_transactions_and_each_confirmation**](CreateSubscriptionsForApi.md#new_confirmed_internal_transactions_and_each_confirmation) | **POST** /blockchain-events/{blockchain}/{network}/subscriptions/address-internal-transactions-confirmed-each-confirmation | New confirmed internal transactions and each confirmation
[**new_confirmed_internal_transactions_for_specific_amount**](CreateSubscriptionsForApi.md#new_confirmed_internal_transactions_for_specific_amount) | **POST** /blockchain-events/{blockchain}/{network}/subscriptions/internal-transactions-for-specific-amount | New Confirmed Internal Transactions For Specific Amount
[**new_confirmed_token_transactions_for_specific_amount**](CreateSubscriptionsForApi.md#new_confirmed_token_transactions_for_specific_amount) | **POST** /blockchain-events/{blockchain}/{network}/subscriptions/tokens-transfers-for-specific-amount | New Confirmed Token Transactions For Specific Amount
[**new_confirmed_tokens_transactions**](CreateSubscriptionsForApi.md#new_confirmed_tokens_transactions) | **POST** /blockchain-events/{blockchain}/{network}/subscriptions/address-tokens-transactions-confirmed | New confirmed tokens transactions
[**new_confirmed_tokens_transactions_and_each_confirmation**](CreateSubscriptionsForApi.md#new_confirmed_tokens_transactions_and_each_confirmation) | **POST** /blockchain-events/{blockchain}/{network}/subscriptions/address-tokens-transactions-confirmed-each-confirmation | New confirmed tokens transactions and each confirmation
[**new_unconfirmed_coins_transactions**](CreateSubscriptionsForApi.md#new_unconfirmed_coins_transactions) | **POST** /blockchain-events/{blockchain}/{network}/subscriptions/address-coins-transactions-unconfirmed | New unconfirmed coins transactions
[**new_unconfirmed_tokens_transactions**](CreateSubscriptionsForApi.md#new_unconfirmed_tokens_transactions) | **POST** /blockchain-events/{blockchain}/{network}/subscriptions/address-tokens-transactions-unconfirmed | New unconfirmed tokens transactions


# **block_height_reached**
> BlockHeightReachedR block_height_reached(blockchain, network)

Block Height Reached

Through this endpoint customers can create callback subscriptions for a specific block height that hasn't been reached yet. In this case the event is when the specified block height in the request body is reached in a said blockchain. By creating this subscription the user will be notified by Crypto APIs 2.0 when that event occurs.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import create_subscriptions_for_api
from cryptoapis.model.convert_bitcoin_cash_address429_response import ConvertBitcoinCashAddress429Response
from cryptoapis.model.convert_bitcoin_cash_address500_response import ConvertBitcoinCashAddress500Response
from cryptoapis.model.block_height_reached403_response import BlockHeightReached403Response
from cryptoapis.model.convert_bitcoin_cash_address422_response import ConvertBitcoinCashAddress422Response
from cryptoapis.model.block_height_reached_r import BlockHeightReachedR
from cryptoapis.model.block_height_reached401_response import BlockHeightReached401Response
from cryptoapis.model.block_height_reached400_response import BlockHeightReached400Response
from cryptoapis.model.block_height_reached_rb import BlockHeightReachedRB
from cryptoapis.model.convert_bitcoin_cash_address402_response import ConvertBitcoinCashAddress402Response
from cryptoapis.model.block_height_reached409_response import BlockHeightReached409Response
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
    api_instance = create_subscriptions_for_api.CreateSubscriptionsForApi(api_client)
    blockchain = "bitcoin" # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    network = "testnet" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    context = "yourExampleString" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    block_height_reached_rb = BlockHeightReachedRB(
        context="yourExampleString",
        data=BlockHeightReachedRBData(
            item=BlockHeightReachedRBDataItem(
                allow_duplicates=True,
                block_height_reached=667900,
                callback_secret_key="yourSecretKey",
                callback_url="https://example.com",
            ),
        ),
    ) # BlockHeightReachedRB |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Block Height Reached
        api_response = api_instance.block_height_reached(blockchain, network)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling CreateSubscriptionsForApi->block_height_reached: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Block Height Reached
        api_response = api_instance.block_height_reached(blockchain, network, context=context, block_height_reached_rb=block_height_reached_rb)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling CreateSubscriptionsForApi->block_height_reached: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. |
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. |
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]
 **block_height_reached_rb** | [**BlockHeightReachedRB**](BlockHeightReachedRB.md)|  | [optional]

### Return type

[**BlockHeightReachedR**](BlockHeightReachedR.md)

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

# **mined_transaction**
> MinedTransactionR mined_transaction(blockchain, network)

Mined transaction

Through this endpoint customers can create callback subscriptions for a specific event. In this case the event is when a specific transaction is mined. By creating this subscription the user will be notified by Crypto APIs 2.0 when that event occurs. The information is returned per specified `transactionId`.    A transaction is mined when it is included in a new block in the blockchain.    {note}To have an operational callback subscription, you need to first verify a domain for the Callback URL. Please see more information on Callbacks [here](https://developers.cryptoapis.io/technical-documentation/general-information/callbacks#callback-url).{/note}    {warning}Crypto APIs will notify the user **only when** the event occurs. There are cases when the specific event doesn't happen at all, or takes a long time to do so. A callback notification **will not** be sent if the event does not or cannot occur, or will take long time to occur.{/warning}

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import create_subscriptions_for_api
from cryptoapis.model.convert_bitcoin_cash_address429_response import ConvertBitcoinCashAddress429Response
from cryptoapis.model.convert_bitcoin_cash_address500_response import ConvertBitcoinCashAddress500Response
from cryptoapis.model.mined_transaction401_response import MinedTransaction401Response
from cryptoapis.model.convert_bitcoin_cash_address422_response import ConvertBitcoinCashAddress422Response
from cryptoapis.model.mined_transaction400_response import MinedTransaction400Response
from cryptoapis.model.mined_transaction409_response import MinedTransaction409Response
from cryptoapis.model.mined_transaction_rb import MinedTransactionRB
from cryptoapis.model.mined_transaction_r import MinedTransactionR
from cryptoapis.model.mined_transaction403_response import MinedTransaction403Response
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
    api_instance = create_subscriptions_for_api.CreateSubscriptionsForApi(api_client)
    blockchain = "bitcoin" # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    network = "testnet" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    context = "yourExampleString" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    mined_transaction_rb = MinedTransactionRB(
        context="yourExampleString",
        data=MinedTransactionRBData(
            item=MinedTransactionRBDataItem(
                allow_duplicates=False,
                callback_secret_key="yourSecretKey",
                callback_url="https://example.com",
                transaction_id="df2690ff97e72c1f8b0f2102a8cb5c1d0fa8fb8754d543c9bc0edc4d4bc34bfc",
            ),
        ),
    ) # MinedTransactionRB |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Mined transaction
        api_response = api_instance.mined_transaction(blockchain, network)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling CreateSubscriptionsForApi->mined_transaction: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Mined transaction
        api_response = api_instance.mined_transaction(blockchain, network, context=context, mined_transaction_rb=mined_transaction_rb)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling CreateSubscriptionsForApi->mined_transaction: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. |
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. |
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]
 **mined_transaction_rb** | [**MinedTransactionRB**](MinedTransactionRB.md)|  | [optional]

### Return type

[**MinedTransactionR**](MinedTransactionR.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request has been successful. |  -  |
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

# **new_block**
> NewBlockR new_block(blockchain, network)

New Block

Through this endpoint customers can create callback subscriptions for a specific event. In this case the event is when a new block is mined in the specific blockchain. By creating this subscription the user will be notified by Crypto APIs 2.0 when that event occurs. The information is returned per specified address.    A new block is mined when it is added to the chain once a consensus is reached by the majority of the miners, which is when the block gets validated and added to the blockchain.    {note}To have an operational callback subscription, you need to first verify a domain for the Callback URL. Please see more information on Callbacks [here](https://developers.cryptoapis.io/technical-documentation/general-information/callbacks#callback-url).{/note}    {warning}Crypto APIs will notify the user **only when** the event occurs. There are cases when the specific event doesn't happen at all, or takes a long time to do so. A callback notification **will not** be sent if the event does not or cannot occur, or will take long time to occur.{/warning}

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import create_subscriptions_for_api
from cryptoapis.model.convert_bitcoin_cash_address429_response import ConvertBitcoinCashAddress429Response
from cryptoapis.model.convert_bitcoin_cash_address500_response import ConvertBitcoinCashAddress500Response
from cryptoapis.model.convert_bitcoin_cash_address422_response import ConvertBitcoinCashAddress422Response
from cryptoapis.model.new_block401_response import NewBlock401Response
from cryptoapis.model.new_block409_response import NewBlock409Response
from cryptoapis.model.new_block400_response import NewBlock400Response
from cryptoapis.model.new_block_rb import NewBlockRB
from cryptoapis.model.new_block403_response import NewBlock403Response
from cryptoapis.model.convert_bitcoin_cash_address402_response import ConvertBitcoinCashAddress402Response
from cryptoapis.model.new_block_r import NewBlockR
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
    api_instance = create_subscriptions_for_api.CreateSubscriptionsForApi(api_client)
    blockchain = "bitcoin" # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    network = "testnet" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    context = "yourExampleString" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    new_block_rb = NewBlockRB(
        context="yourExampleString",
        data=NewBlockRBData(
            item=NewBlockRBDataItem(
                allow_duplicates=True,
                callback_secret_key="yourSecretKey",
                callback_url="https://example.com",
            ),
        ),
    ) # NewBlockRB |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # New Block
        api_response = api_instance.new_block(blockchain, network)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling CreateSubscriptionsForApi->new_block: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # New Block
        api_response = api_instance.new_block(blockchain, network, context=context, new_block_rb=new_block_rb)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling CreateSubscriptionsForApi->new_block: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. |
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. |
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]
 **new_block_rb** | [**NewBlockRB**](NewBlockRB.md)|  | [optional]

### Return type

[**NewBlockR**](NewBlockR.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request has been successful. |  -  |
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

# **new_confirmed_coins_transactions**
> NewConfirmedCoinsTransactionsR new_confirmed_coins_transactions(blockchain, network)

New confirmed coins transactions

Through this endpoint customers can create callback subscriptions for a specific event. In this case the event is when there are new incoming or outgoing confirmed transactions for coins from/to the customer's address. By creating this subscription the user will be notified by Crypto APIs 2.0 when that event occurs. The information is returned per specified address.     Being confirmed means that the transactions are verified by miners and added to the next block.    {note}For UTXO-based protocols like Bitcoin a transaction could have multiple inputs and outputs which means the address could in as both sender and recipient. [Here](https://developers.cryptoapis.io/technical-documentation/general-information/callbacks#callback-data-returned-for-utxo-based-transactions) is how we inform you on that.{/note}    {note}To have an operational callback subscription, you need to first verify a domain for the Callback URL. Please see more information on Callbacks [here](https://developers.cryptoapis.io/technical-documentation/general-information/callbacks#callback-url).{/note}    {warning}Crypto APIs will notify the user **only when** the event occurs. There are cases when the specific event doesn't happen at all, or takes a long time to do so. A callback notification **will not** be sent if the event does not or cannot occur, or will take long time to occur.{/warning}

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import create_subscriptions_for_api
from cryptoapis.model.convert_bitcoin_cash_address429_response import ConvertBitcoinCashAddress429Response
from cryptoapis.model.convert_bitcoin_cash_address500_response import ConvertBitcoinCashAddress500Response
from cryptoapis.model.new_confirmed_coins_transactions403_response import NewConfirmedCoinsTransactions403Response
from cryptoapis.model.convert_bitcoin_cash_address422_response import ConvertBitcoinCashAddress422Response
from cryptoapis.model.new_confirmed_coins_transactions_rb import NewConfirmedCoinsTransactionsRB
from cryptoapis.model.new_confirmed_coins_transactions_r import NewConfirmedCoinsTransactionsR
from cryptoapis.model.new_confirmed_coins_transactions409_response import NewConfirmedCoinsTransactions409Response
from cryptoapis.model.new_confirmed_coins_transactions400_response import NewConfirmedCoinsTransactions400Response
from cryptoapis.model.convert_bitcoin_cash_address402_response import ConvertBitcoinCashAddress402Response
from cryptoapis.model.new_confirmed_coins_transactions401_response import NewConfirmedCoinsTransactions401Response
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
    api_instance = create_subscriptions_for_api.CreateSubscriptionsForApi(api_client)
    blockchain = "bitcoin" # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    network = "testnet" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    context = "yourExampleString" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    new_confirmed_coins_transactions_rb = NewConfirmedCoinsTransactionsRB(
        context="yourExampleString",
        data=NewConfirmedCoinsTransactionsRBData(
            item=NewConfirmedCoinsTransactionsRBDataItem(
                address="mho4jHBcrNCncKt38trJahXakuaBnS7LK5",
                allow_duplicates=True,
                callback_secret_key="yourSecretKey",
                callback_url="https://example.com",
                receive_callback_on=3,
            ),
        ),
    ) # NewConfirmedCoinsTransactionsRB |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # New confirmed coins transactions
        api_response = api_instance.new_confirmed_coins_transactions(blockchain, network)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling CreateSubscriptionsForApi->new_confirmed_coins_transactions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # New confirmed coins transactions
        api_response = api_instance.new_confirmed_coins_transactions(blockchain, network, context=context, new_confirmed_coins_transactions_rb=new_confirmed_coins_transactions_rb)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling CreateSubscriptionsForApi->new_confirmed_coins_transactions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. |
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. |
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]
 **new_confirmed_coins_transactions_rb** | [**NewConfirmedCoinsTransactionsRB**](NewConfirmedCoinsTransactionsRB.md)|  | [optional]

### Return type

[**NewConfirmedCoinsTransactionsR**](NewConfirmedCoinsTransactionsR.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request has been successful. |  -  |
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

# **new_confirmed_coins_transactions_and_each_confirmation**
> NewConfirmedCoinsTransactionsAndEachConfirmationR new_confirmed_coins_transactions_and_each_confirmation(blockchain, network)

New confirmed coins transactions and each confirmation

Through this endpoint customers can create callback subscriptions for a specific event. In this case the event is when there are new incoming or outgoing confirmed transactions for coins from/to the customer's address with also a response at each confirmation the transaction has received until the specified confirmations limit is reached. By creating this subscription the user will be notified by Crypto APIs 2.0 when that event occurs. The information is returned per specified address.     Being confirmed means that the transactions are verified by miners and added to the next block. This endpoint refers to **coins transactions only, not tokens**.    {note}For UTXO-based protocols like Bitcoin a transaction could have multiple inputs and outputs which means the address could in as both sender and recipient. [Here](https://developers.cryptoapis.io/technical-documentation/general-information/callbacks#callback-data-returned-for-utxo-based-transactions) is how we inform you on that.{/note}    {note}To have an operational callback subscription, you need to first verify a domain for the Callback URL. Please see more information on Callbacks [here](https://developers.cryptoapis.io/technical-documentation/general-information/callbacks#callback-url).{/note}    {warning}Crypto APIs will notify the user **only when** the event occurs. There are cases when the specific event doesn't happen at all, or takes a long time to do so. A callback notification **will not** be sent if the event does not or cannot occur, or will take long time to occur.{/warning}

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import create_subscriptions_for_api
from cryptoapis.model.convert_bitcoin_cash_address429_response import ConvertBitcoinCashAddress429Response
from cryptoapis.model.convert_bitcoin_cash_address500_response import ConvertBitcoinCashAddress500Response
from cryptoapis.model.new_confirmed_coins_transactions_and_each_confirmation_r import NewConfirmedCoinsTransactionsAndEachConfirmationR
from cryptoapis.model.new_confirmed_coins_transactions_and_each_confirmation_rb import NewConfirmedCoinsTransactionsAndEachConfirmationRB
from cryptoapis.model.convert_bitcoin_cash_address422_response import ConvertBitcoinCashAddress422Response
from cryptoapis.model.new_confirmed_coins_transactions_and_each_confirmation400_response import NewConfirmedCoinsTransactionsAndEachConfirmation400Response
from cryptoapis.model.new_confirmed_coins_transactions_and_each_confirmation401_response import NewConfirmedCoinsTransactionsAndEachConfirmation401Response
from cryptoapis.model.new_confirmed_coins_transactions_and_each_confirmation403_response import NewConfirmedCoinsTransactionsAndEachConfirmation403Response
from cryptoapis.model.convert_bitcoin_cash_address402_response import ConvertBitcoinCashAddress402Response
from cryptoapis.model.new_confirmed_coins_transactions_and_each_confirmation409_response import NewConfirmedCoinsTransactionsAndEachConfirmation409Response
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
    api_instance = create_subscriptions_for_api.CreateSubscriptionsForApi(api_client)
    blockchain = "bitcoin" # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    network = "testnet" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    context = "yourExampleString" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    new_confirmed_coins_transactions_and_each_confirmation_rb = NewConfirmedCoinsTransactionsAndEachConfirmationRB(
        context="yourExampleString",
        data=NewConfirmedCoinsTransactionsAndEachConfirmationRBData(
            item=NewConfirmedCoinsTransactionsAndEachConfirmationRBDataItem(
                address="mho4jHBcrNCncKt38trJahXakuaBnS7LK5",
                allow_duplicates=True,
                callback_secret_key="yourSecretKey",
                callback_url="https://example.com",
                confirmations_count=3,
            ),
        ),
    ) # NewConfirmedCoinsTransactionsAndEachConfirmationRB |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # New confirmed coins transactions and each confirmation
        api_response = api_instance.new_confirmed_coins_transactions_and_each_confirmation(blockchain, network)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling CreateSubscriptionsForApi->new_confirmed_coins_transactions_and_each_confirmation: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # New confirmed coins transactions and each confirmation
        api_response = api_instance.new_confirmed_coins_transactions_and_each_confirmation(blockchain, network, context=context, new_confirmed_coins_transactions_and_each_confirmation_rb=new_confirmed_coins_transactions_and_each_confirmation_rb)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling CreateSubscriptionsForApi->new_confirmed_coins_transactions_and_each_confirmation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. |
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. |
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]
 **new_confirmed_coins_transactions_and_each_confirmation_rb** | [**NewConfirmedCoinsTransactionsAndEachConfirmationRB**](NewConfirmedCoinsTransactionsAndEachConfirmationRB.md)|  | [optional]

### Return type

[**NewConfirmedCoinsTransactionsAndEachConfirmationR**](NewConfirmedCoinsTransactionsAndEachConfirmationR.md)

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

# **new_confirmed_coins_transactions_for_specific_amount**
> NewConfirmedCoinsTransactionsForSpecificAmountR new_confirmed_coins_transactions_for_specific_amount(blockchain, network)

New Confirmed Coins Transactions For Specific Amount

Through this endpoint customers can create callback subscriptions for a specific event and \"amountHigherThan\" value. In this case the event is when there are new incoming or outgoing confirmed coins transactions for the specified blockchain and the amount is equal or higher than the value specified.  By creating this subscription the user will be notified by Crypto APIs 2.0 when that event occurs  filtered for the specified amount. The information is returned per specified address.    Being confirmed means that the transactions are verified by miners and added to the next block.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import create_subscriptions_for_api
from cryptoapis.model.convert_bitcoin_cash_address429_response import ConvertBitcoinCashAddress429Response
from cryptoapis.model.convert_bitcoin_cash_address500_response import ConvertBitcoinCashAddress500Response
from cryptoapis.model.new_confirmed_coins_transactions_for_specific_amount409_response import NewConfirmedCoinsTransactionsForSpecificAmount409Response
from cryptoapis.model.new_confirmed_coins_transactions_for_specific_amount_rb import NewConfirmedCoinsTransactionsForSpecificAmountRB
from cryptoapis.model.convert_bitcoin_cash_address422_response import ConvertBitcoinCashAddress422Response
from cryptoapis.model.new_confirmed_coins_transactions_for_specific_amount403_response import NewConfirmedCoinsTransactionsForSpecificAmount403Response
from cryptoapis.model.new_confirmed_coins_transactions_for_specific_amount400_response import NewConfirmedCoinsTransactionsForSpecificAmount400Response
from cryptoapis.model.new_confirmed_coins_transactions_for_specific_amount_r import NewConfirmedCoinsTransactionsForSpecificAmountR
from cryptoapis.model.convert_bitcoin_cash_address402_response import ConvertBitcoinCashAddress402Response
from cryptoapis.model.new_confirmed_coins_transactions_for_specific_amount401_response import NewConfirmedCoinsTransactionsForSpecificAmount401Response
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
    api_instance = create_subscriptions_for_api.CreateSubscriptionsForApi(api_client)
    blockchain = "bitcoin" # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    network = "testnet" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    context = "yourExampleString" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    new_confirmed_coins_transactions_for_specific_amount_rb = NewConfirmedCoinsTransactionsForSpecificAmountRB(
        context="yourExampleString",
        data=NewConfirmedCoinsTransactionsForSpecificAmountRBData(
            item=NewConfirmedCoinsTransactionsForSpecificAmountRBDataItem(
                allow_duplicates=True,
                amount_higher_than=2,
                callback_secret_key="yourSecretKey",
                callback_url="https://example.com",
            ),
        ),
    ) # NewConfirmedCoinsTransactionsForSpecificAmountRB |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # New Confirmed Coins Transactions For Specific Amount
        api_response = api_instance.new_confirmed_coins_transactions_for_specific_amount(blockchain, network)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling CreateSubscriptionsForApi->new_confirmed_coins_transactions_for_specific_amount: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # New Confirmed Coins Transactions For Specific Amount
        api_response = api_instance.new_confirmed_coins_transactions_for_specific_amount(blockchain, network, context=context, new_confirmed_coins_transactions_for_specific_amount_rb=new_confirmed_coins_transactions_for_specific_amount_rb)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling CreateSubscriptionsForApi->new_confirmed_coins_transactions_for_specific_amount: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. |
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. |
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]
 **new_confirmed_coins_transactions_for_specific_amount_rb** | [**NewConfirmedCoinsTransactionsForSpecificAmountRB**](NewConfirmedCoinsTransactionsForSpecificAmountRB.md)|  | [optional]

### Return type

[**NewConfirmedCoinsTransactionsForSpecificAmountR**](NewConfirmedCoinsTransactionsForSpecificAmountR.md)

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

# **new_confirmed_internal_transactions**
> NewConfirmedInternalTransactionsR new_confirmed_internal_transactions(blockchain, network)

New confirmed internal transactions

Through this endpoint customers can create callback subscriptions for a specific event. In this case the event is when there are new confirmed internal transactions. By creating this subscription the user will be notified by Crypto APIs 2.0 when that event occurs.    Being confirmed means that the transactions are verified by miners and added to the next block.    {note}To have an operational callback subscription, you need to first verify a domain for the Callback URL. Please see more information on Callbacks [here](https://developers.cryptoapis.io/technical-documentation/general-information/callbacks#callback-url).{/note}    {warning}Crypto APIs will notify the user **only when** the event occurs. There are cases when the specific event doesn't happen at all, or takes a long time to do so. A callback notification **will not** be sent if the event does not or cannot occur, or will take long time to occur.{/warning}

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import create_subscriptions_for_api
from cryptoapis.model.convert_bitcoin_cash_address429_response import ConvertBitcoinCashAddress429Response
from cryptoapis.model.convert_bitcoin_cash_address500_response import ConvertBitcoinCashAddress500Response
from cryptoapis.model.convert_bitcoin_cash_address422_response import ConvertBitcoinCashAddress422Response
from cryptoapis.model.new_confirmed_internal_transactions401_response import NewConfirmedInternalTransactions401Response
from cryptoapis.model.new_confirmed_internal_transactions403_response import NewConfirmedInternalTransactions403Response
from cryptoapis.model.new_confirmed_internal_transactions409_response import NewConfirmedInternalTransactions409Response
from cryptoapis.model.new_confirmed_internal_transactions400_response import NewConfirmedInternalTransactions400Response
from cryptoapis.model.new_confirmed_internal_transactions_r import NewConfirmedInternalTransactionsR
from cryptoapis.model.convert_bitcoin_cash_address402_response import ConvertBitcoinCashAddress402Response
from cryptoapis.model.new_confirmed_internal_transactions_rb import NewConfirmedInternalTransactionsRB
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
    api_instance = create_subscriptions_for_api.CreateSubscriptionsForApi(api_client)
    blockchain = "ethereum-classic" # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    network = "mordor" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    context = "yourExampleString" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    new_confirmed_internal_transactions_rb = NewConfirmedInternalTransactionsRB(
        context="yourExampleString",
        data=NewConfirmedInternalTransactionsRBData(
            item=NewConfirmedInternalTransactionsRBDataItem(
                address="0xbcc817f057950b0df41206c5d7125e6225cae18e",
                allow_duplicates=True,
                callback_secret_key="yourSecretKey",
                callback_url="https://example.com",
                receive_callback_on=3,
            ),
        ),
    ) # NewConfirmedInternalTransactionsRB |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # New confirmed internal transactions
        api_response = api_instance.new_confirmed_internal_transactions(blockchain, network)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling CreateSubscriptionsForApi->new_confirmed_internal_transactions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # New confirmed internal transactions
        api_response = api_instance.new_confirmed_internal_transactions(blockchain, network, context=context, new_confirmed_internal_transactions_rb=new_confirmed_internal_transactions_rb)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling CreateSubscriptionsForApi->new_confirmed_internal_transactions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. |
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. |
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]
 **new_confirmed_internal_transactions_rb** | [**NewConfirmedInternalTransactionsRB**](NewConfirmedInternalTransactionsRB.md)|  | [optional]

### Return type

[**NewConfirmedInternalTransactionsR**](NewConfirmedInternalTransactionsR.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request has been successful. |  -  |
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

# **new_confirmed_internal_transactions_and_each_confirmation**
> NewConfirmedInternalTransactionsAndEachConfirmationR new_confirmed_internal_transactions_and_each_confirmation(blockchain, network)

New confirmed internal transactions and each confirmation

Through this endpoint customers can create callback subscriptions for a specific event. In this case the event is when there are new confirmed internal transactions. Includes also a response at each confirmation the transaction receives until the specified confirmations limit is reached. By creating this subscription the user will be notified by Crypto APIs 2.0 when that event occurs.     Being confirmed means that the transactions are verified by miners and added to the next block.    {note}To have an operational callback subscription, you need to first verify a domain for the Callback URL. Please see more information on Callbacks [here](https://developers.cryptoapis.io/technical-documentation/general-information/callbacks#callback-url).{/note}    {warning}Crypto APIs will notify the user **only when** the event occurs. There are cases when the specific event doesn't happen at all, or takes a long time to do so. A callback notification **will not** be sent if the event does not or cannot occur, or will take long time to occur.{/warning}

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import create_subscriptions_for_api
from cryptoapis.model.convert_bitcoin_cash_address429_response import ConvertBitcoinCashAddress429Response
from cryptoapis.model.convert_bitcoin_cash_address500_response import ConvertBitcoinCashAddress500Response
from cryptoapis.model.new_confirmed_internal_transactions_and_each_confirmation409_response import NewConfirmedInternalTransactionsAndEachConfirmation409Response
from cryptoapis.model.new_confirmed_internal_transactions_and_each_confirmation_r import NewConfirmedInternalTransactionsAndEachConfirmationR
from cryptoapis.model.convert_bitcoin_cash_address422_response import ConvertBitcoinCashAddress422Response
from cryptoapis.model.new_confirmed_internal_transactions_and_each_confirmation401_response import NewConfirmedInternalTransactionsAndEachConfirmation401Response
from cryptoapis.model.new_confirmed_internal_transactions_and_each_confirmation403_response import NewConfirmedInternalTransactionsAndEachConfirmation403Response
from cryptoapis.model.new_confirmed_internal_transactions_and_each_confirmation_rb import NewConfirmedInternalTransactionsAndEachConfirmationRB
from cryptoapis.model.new_confirmed_internal_transactions_and_each_confirmation400_response import NewConfirmedInternalTransactionsAndEachConfirmation400Response
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
    api_instance = create_subscriptions_for_api.CreateSubscriptionsForApi(api_client)
    blockchain = "ethereum-classic" # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    network = "mordor" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    context = "yourExampleString" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    new_confirmed_internal_transactions_and_each_confirmation_rb = NewConfirmedInternalTransactionsAndEachConfirmationRB(
        context="yourExampleString",
        data=NewConfirmedInternalTransactionsAndEachConfirmationRBData(
            item=NewConfirmedInternalTransactionsAndEachConfirmationRBDataItem(
                address="0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
                allow_duplicates=True,
                callback_secret_key="yourSecretString",
                callback_url="https://example.com",
                confirmations_count=3,
            ),
        ),
    ) # NewConfirmedInternalTransactionsAndEachConfirmationRB |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # New confirmed internal transactions and each confirmation
        api_response = api_instance.new_confirmed_internal_transactions_and_each_confirmation(blockchain, network)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling CreateSubscriptionsForApi->new_confirmed_internal_transactions_and_each_confirmation: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # New confirmed internal transactions and each confirmation
        api_response = api_instance.new_confirmed_internal_transactions_and_each_confirmation(blockchain, network, context=context, new_confirmed_internal_transactions_and_each_confirmation_rb=new_confirmed_internal_transactions_and_each_confirmation_rb)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling CreateSubscriptionsForApi->new_confirmed_internal_transactions_and_each_confirmation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. |
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. |
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]
 **new_confirmed_internal_transactions_and_each_confirmation_rb** | [**NewConfirmedInternalTransactionsAndEachConfirmationRB**](NewConfirmedInternalTransactionsAndEachConfirmationRB.md)|  | [optional]

### Return type

[**NewConfirmedInternalTransactionsAndEachConfirmationR**](NewConfirmedInternalTransactionsAndEachConfirmationR.md)

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

# **new_confirmed_internal_transactions_for_specific_amount**
> NewConfirmedInternalTransactionsForSpecificAmountR new_confirmed_internal_transactions_for_specific_amount(blockchain, network)

New Confirmed Internal Transactions For Specific Amount

Through this endpoint customers can create callback subscriptions for a specific event and \"amountHigherThan\" value. In this case the event is when there are new confirmed internal transactions and the amount is equal or higher than a value, specified by the customer. By creating this subscription the user will be notified by Crypto APIs 2.0 when that event occurs, filtered for the specified amount.  Being confirmed means that the transactions are verified by miners and added to the next block

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import create_subscriptions_for_api
from cryptoapis.model.convert_bitcoin_cash_address429_response import ConvertBitcoinCashAddress429Response
from cryptoapis.model.convert_bitcoin_cash_address500_response import ConvertBitcoinCashAddress500Response
from cryptoapis.model.new_confirmed_internal_transactions_for_specific_amount403_response import NewConfirmedInternalTransactionsForSpecificAmount403Response
from cryptoapis.model.convert_bitcoin_cash_address422_response import ConvertBitcoinCashAddress422Response
from cryptoapis.model.new_confirmed_internal_transactions_for_specific_amount400_response import NewConfirmedInternalTransactionsForSpecificAmount400Response
from cryptoapis.model.new_confirmed_internal_transactions_for_specific_amount_rb import NewConfirmedInternalTransactionsForSpecificAmountRB
from cryptoapis.model.new_confirmed_internal_transactions_for_specific_amount_r import NewConfirmedInternalTransactionsForSpecificAmountR
from cryptoapis.model.new_confirmed_internal_transactions_for_specific_amount401_response import NewConfirmedInternalTransactionsForSpecificAmount401Response
from cryptoapis.model.convert_bitcoin_cash_address402_response import ConvertBitcoinCashAddress402Response
from cryptoapis.model.new_confirmed_internal_transactions_for_specific_amount409_response import NewConfirmedInternalTransactionsForSpecificAmount409Response
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
    api_instance = create_subscriptions_for_api.CreateSubscriptionsForApi(api_client)
    blockchain = "ethereum" # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    network = "ropsten" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    context = "yourExampleString" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    new_confirmed_internal_transactions_for_specific_amount_rb = NewConfirmedInternalTransactionsForSpecificAmountRB(
        context="yourExampleString",
        data=NewConfirmedInternalTransactionsForSpecificAmountRBData(
            item=NewConfirmedInternalTransactionsForSpecificAmountRBDataItem(
                allow_duplicates=True,
                amount_higher_than=3,
                callback_secret_key="yourSecretKey",
                callback_url="https://example.com",
            ),
        ),
    ) # NewConfirmedInternalTransactionsForSpecificAmountRB |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # New Confirmed Internal Transactions For Specific Amount
        api_response = api_instance.new_confirmed_internal_transactions_for_specific_amount(blockchain, network)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling CreateSubscriptionsForApi->new_confirmed_internal_transactions_for_specific_amount: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # New Confirmed Internal Transactions For Specific Amount
        api_response = api_instance.new_confirmed_internal_transactions_for_specific_amount(blockchain, network, context=context, new_confirmed_internal_transactions_for_specific_amount_rb=new_confirmed_internal_transactions_for_specific_amount_rb)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling CreateSubscriptionsForApi->new_confirmed_internal_transactions_for_specific_amount: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. |
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. |
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]
 **new_confirmed_internal_transactions_for_specific_amount_rb** | [**NewConfirmedInternalTransactionsForSpecificAmountRB**](NewConfirmedInternalTransactionsForSpecificAmountRB.md)|  | [optional]

### Return type

[**NewConfirmedInternalTransactionsForSpecificAmountR**](NewConfirmedInternalTransactionsForSpecificAmountR.md)

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

# **new_confirmed_token_transactions_for_specific_amount**
> NewConfirmedTokenTransactionsForSpecificAmountR new_confirmed_token_transactions_for_specific_amount(blockchain, network)

New Confirmed Token Transactions For Specific Amount

Through this endpoint customers can create callback subscriptions for a specific event and \"amountHigherThan\" value. In this case the event is when there are new incoming or outgoing confirmed token transactions for the specified blockchain and the amount is equal or higher than the value specified. By creating this subscription the user will be notified by Crypto APIs 2.0 when that event occurs, filtered for the specified amount.  Being confirmed means that the transactions are verified by miners and added to the next block. This endpoint refers to tokens transactions only, not coins.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import create_subscriptions_for_api
from cryptoapis.model.convert_bitcoin_cash_address429_response import ConvertBitcoinCashAddress429Response
from cryptoapis.model.convert_bitcoin_cash_address500_response import ConvertBitcoinCashAddress500Response
from cryptoapis.model.convert_bitcoin_cash_address422_response import ConvertBitcoinCashAddress422Response
from cryptoapis.model.new_confirmed_token_transactions_for_specific_amount400_response import NewConfirmedTokenTransactionsForSpecificAmount400Response
from cryptoapis.model.new_confirmed_token_transactions_for_specific_amount_r import NewConfirmedTokenTransactionsForSpecificAmountR
from cryptoapis.model.new_confirmed_token_transactions_for_specific_amount403_response import NewConfirmedTokenTransactionsForSpecificAmount403Response
from cryptoapis.model.new_confirmed_token_transactions_for_specific_amount_rb import NewConfirmedTokenTransactionsForSpecificAmountRB
from cryptoapis.model.get_xrp_ripple_transaction_details_by_transaction_id404_response import GetXRPRippleTransactionDetailsByTransactionID404Response
from cryptoapis.model.new_confirmed_token_transactions_for_specific_amount409_response import NewConfirmedTokenTransactionsForSpecificAmount409Response
from cryptoapis.model.convert_bitcoin_cash_address402_response import ConvertBitcoinCashAddress402Response
from cryptoapis.model.new_confirmed_token_transactions_for_specific_amount401_response import NewConfirmedTokenTransactionsForSpecificAmount401Response
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
    api_instance = create_subscriptions_for_api.CreateSubscriptionsForApi(api_client)
    blockchain = "ethereum" # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    network = "ropsten" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    context = "yourExampleString" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    new_confirmed_token_transactions_for_specific_amount_rb = NewConfirmedTokenTransactionsForSpecificAmountRB(
        context="yourExampleString",
        data=NewConfirmedTokenTransactionsForSpecificAmountRBData(
            item=NewConfirmedTokenTransactionsForSpecificAmountRBDataItem(
                allow_duplicates=True,
                amount_higher_than=2,
                callback_secret_key="yourSecretKey",
                callback_url="https://example.com",
                contract_address="0x7495fede000c8a3b77eeae09cf70fa94cd2d53f5",
            ),
        ),
    ) # NewConfirmedTokenTransactionsForSpecificAmountRB |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # New Confirmed Token Transactions For Specific Amount
        api_response = api_instance.new_confirmed_token_transactions_for_specific_amount(blockchain, network)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling CreateSubscriptionsForApi->new_confirmed_token_transactions_for_specific_amount: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # New Confirmed Token Transactions For Specific Amount
        api_response = api_instance.new_confirmed_token_transactions_for_specific_amount(blockchain, network, context=context, new_confirmed_token_transactions_for_specific_amount_rb=new_confirmed_token_transactions_for_specific_amount_rb)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling CreateSubscriptionsForApi->new_confirmed_token_transactions_for_specific_amount: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. |
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. |
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]
 **new_confirmed_token_transactions_for_specific_amount_rb** | [**NewConfirmedTokenTransactionsForSpecificAmountRB**](NewConfirmedTokenTransactionsForSpecificAmountRB.md)|  | [optional]

### Return type

[**NewConfirmedTokenTransactionsForSpecificAmountR**](NewConfirmedTokenTransactionsForSpecificAmountR.md)

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
**404** | The specified resource has not been found. |  -  |
**409** | 409 |  -  |
**415** | The selected Media Type is unavailable. The Content-Type header should be &#39;application/json&#39;. |  -  |
**422** | Your request body for POST requests must have a structure of { data: { item: [...properties] } } |  -  |
**429** | The request limit has been reached. There can be maximum {requests} requests per {seconds} second(s) made. Please contact our team via email if you need more or upgrade your plan. |  -  |
**500** | An unexpected server error has occurred, we are working to fix this. Please try again later and in case it occurs again please report it to our team via email. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **new_confirmed_tokens_transactions**
> NewConfirmedTokensTransactionsR new_confirmed_tokens_transactions(blockchain, network)

New confirmed tokens transactions

Through this endpoint customers can create callback subscriptions for a specific event. In this case the event is when there are new incoming or outgoing confirmed transactions for tokens from/to the customer's address. By creating this subscription the user will be notified by Crypto APIs 2.0 when that event occurs. The information is returned per specified address.     Being confirmed means that the transactions are verified by miners and added to the next block. This endpoint refers to **tokens transactions only, not coins**.    {note}To have an operational callback subscription, you need to first verify a domain for the Callback URL. Please see more information on Callbacks [here](https://developers.cryptoapis.io/technical-documentation/general-information/callbacks#callback-url).{/note}    {warning}Crypto APIs will notify the user **only when** the event occurs. There are cases when the specific event doesn't happen at all, or takes a long time to do so. A callback notification **will not** be sent if the event does not or cannot occur, or will take long time to occur.{/warning}

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import create_subscriptions_for_api
from cryptoapis.model.convert_bitcoin_cash_address429_response import ConvertBitcoinCashAddress429Response
from cryptoapis.model.convert_bitcoin_cash_address500_response import ConvertBitcoinCashAddress500Response
from cryptoapis.model.convert_bitcoin_cash_address422_response import ConvertBitcoinCashAddress422Response
from cryptoapis.model.new_confirmed_tokens_transactions409_response import NewConfirmedTokensTransactions409Response
from cryptoapis.model.new_confirmed_tokens_transactions401_response import NewConfirmedTokensTransactions401Response
from cryptoapis.model.new_confirmed_tokens_transactions403_response import NewConfirmedTokensTransactions403Response
from cryptoapis.model.new_confirmed_tokens_transactions_rb import NewConfirmedTokensTransactionsRB
from cryptoapis.model.new_confirmed_tokens_transactions400_response import NewConfirmedTokensTransactions400Response
from cryptoapis.model.new_confirmed_tokens_transactions_r import NewConfirmedTokensTransactionsR
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
    api_instance = create_subscriptions_for_api.CreateSubscriptionsForApi(api_client)
    blockchain = "ethereum" # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    network = "ropsten" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    context = "yourExampleString" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    new_confirmed_tokens_transactions_rb = NewConfirmedTokensTransactionsRB(
        context="yourExampleString",
        data=NewConfirmedTokensTransactionsRBData(
            item=NewConfirmedTokensTransactionsRBDataItem(
                address="0xbf16582e53d6fd892f11de8a3e29e8c3b65d77c2",
                allow_duplicates=True,
                callback_secret_key="yourSecretKey",
                callback_url="https://example.com",
                receive_callback_on=3,
            ),
        ),
    ) # NewConfirmedTokensTransactionsRB |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # New confirmed tokens transactions
        api_response = api_instance.new_confirmed_tokens_transactions(blockchain, network)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling CreateSubscriptionsForApi->new_confirmed_tokens_transactions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # New confirmed tokens transactions
        api_response = api_instance.new_confirmed_tokens_transactions(blockchain, network, context=context, new_confirmed_tokens_transactions_rb=new_confirmed_tokens_transactions_rb)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling CreateSubscriptionsForApi->new_confirmed_tokens_transactions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. |
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. |
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]
 **new_confirmed_tokens_transactions_rb** | [**NewConfirmedTokensTransactionsRB**](NewConfirmedTokensTransactionsRB.md)|  | [optional]

### Return type

[**NewConfirmedTokensTransactionsR**](NewConfirmedTokensTransactionsR.md)

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

# **new_confirmed_tokens_transactions_and_each_confirmation**
> NewConfirmedTokensTransactionsAndEachConfirmationR new_confirmed_tokens_transactions_and_each_confirmation(blockchain, network)

New confirmed tokens transactions and each confirmation

Through this endpoint customers can create callback subscriptions for a specific event. In this case the event is when there are new incoming or outgoing confirmed transactions for tokens from/to the customer's address with also a response at each confirmation the transaction has received until the specified confirmations limit is reached. By creating this subscription the user will be notified by Crypto APIs 2.0 when that event occurs. The information is returned per specified address.     Being confirmed means that the transactions are verified by miners and added to the next block. This endpoint refers to **tokens transactions only, not coins**.    {note}To have an operational callback subscription, you need to first verify a domain for the Callback URL. Please see more information on Callbacks [here](https://developers.cryptoapis.io/technical-documentation/general-information/callbacks#callback-url).{/note}    {warning}Crypto APIs will notify the user **only when** the event occurs. There are cases when the specific event doesn't happen at all, or takes a long time to do so. A callback notification **will not** be sent if the event does not or cannot occur, or will take long time to occur.{/warning}

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import create_subscriptions_for_api
from cryptoapis.model.convert_bitcoin_cash_address429_response import ConvertBitcoinCashAddress429Response
from cryptoapis.model.convert_bitcoin_cash_address500_response import ConvertBitcoinCashAddress500Response
from cryptoapis.model.convert_bitcoin_cash_address422_response import ConvertBitcoinCashAddress422Response
from cryptoapis.model.new_confirmed_tokens_transactions_and_each_confirmation_r import NewConfirmedTokensTransactionsAndEachConfirmationR
from cryptoapis.model.new_confirmed_tokens_transactions_and_each_confirmation400_response import NewConfirmedTokensTransactionsAndEachConfirmation400Response
from cryptoapis.model.new_confirmed_tokens_transactions_and_each_confirmation403_response import NewConfirmedTokensTransactionsAndEachConfirmation403Response
from cryptoapis.model.new_confirmed_tokens_transactions_and_each_confirmation409_response import NewConfirmedTokensTransactionsAndEachConfirmation409Response
from cryptoapis.model.new_confirmed_tokens_transactions_and_each_confirmation_rb import NewConfirmedTokensTransactionsAndEachConfirmationRB
from cryptoapis.model.new_confirmed_tokens_transactions_and_each_confirmation401_response import NewConfirmedTokensTransactionsAndEachConfirmation401Response
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
    api_instance = create_subscriptions_for_api.CreateSubscriptionsForApi(api_client)
    blockchain = "ethereum" # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    network = "ropsten" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    context = "yourExampleString" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    new_confirmed_tokens_transactions_and_each_confirmation_rb = NewConfirmedTokensTransactionsAndEachConfirmationRB(
        context="yourExampleString",
        data=NewConfirmedTokensTransactionsAndEachConfirmationRBData(
            item=NewConfirmedTokensTransactionsAndEachConfirmationRBDataItem(
                address="0x033ef6db9fbd0ee60e2931906b987fe0280471a0",
                allow_duplicates=True,
                callback_secret_key="yourSecretKey",
                callback_url="https://example.com",
                confirmations_count=3,
            ),
        ),
    ) # NewConfirmedTokensTransactionsAndEachConfirmationRB |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # New confirmed tokens transactions and each confirmation
        api_response = api_instance.new_confirmed_tokens_transactions_and_each_confirmation(blockchain, network)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling CreateSubscriptionsForApi->new_confirmed_tokens_transactions_and_each_confirmation: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # New confirmed tokens transactions and each confirmation
        api_response = api_instance.new_confirmed_tokens_transactions_and_each_confirmation(blockchain, network, context=context, new_confirmed_tokens_transactions_and_each_confirmation_rb=new_confirmed_tokens_transactions_and_each_confirmation_rb)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling CreateSubscriptionsForApi->new_confirmed_tokens_transactions_and_each_confirmation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. |
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. |
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]
 **new_confirmed_tokens_transactions_and_each_confirmation_rb** | [**NewConfirmedTokensTransactionsAndEachConfirmationRB**](NewConfirmedTokensTransactionsAndEachConfirmationRB.md)|  | [optional]

### Return type

[**NewConfirmedTokensTransactionsAndEachConfirmationR**](NewConfirmedTokensTransactionsAndEachConfirmationR.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request has been successful. |  -  |
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

# **new_unconfirmed_coins_transactions**
> NewUnconfirmedCoinsTransactionsR new_unconfirmed_coins_transactions(blockchain, network)

New unconfirmed coins transactions

Through this endpoint customers can create callback subscriptions for a specific event. In this case the event is when there are new unconfirmed coins transactions for the user. By creating this subscription the user will be notified by Crypto APIs 2.0 when that event occurs. The information is returned per specified address.    Unconfirmed coins transactions remain in the mempool (memory pool) until they are confirmed by miners and added to the next block. Sometimes spikes in transaction activity can cause delays in confirmations.    {note}For UTXO-based protocols like Bitcoin a transaction could have multiple inputs and outputs which means the address could in as both sender and recipient. [Here](https://developers.cryptoapis.io/technical-documentation/general-information/callbacks#callback-data-returned-for-utxo-based-transactions) is how we inform you on that.{/note}    {warning}We cannot guarantee at 100% that webhooks for unconfirmed transactions will always be received. Some may **not get received** due to the possibility of some nodes not being updated with that information. This can occur in networks with low activity and/or not many nodes, e.g. Testnet networks and rarely Mainnets.{/warning}    {note}To have an operational callback subscription, you need to first verify a domain for the Callback URL. Please see more information on Callbacks [here](https://developers.cryptoapis.io/technical-documentation/general-information/callbacks#callback-url).{/note}    {note}It is also **important to note** that just because pending unconfirmed transactions are in the mempool, **doesn't necessarily** mean they will get confirmed.{/note}    {warning}Crypto APIs will notify the user **only when** the event occurs. There are cases when the specific event doesn't happen at all, or takes a long time to do so. A callback notification **will not** be sent if the event does not or cannot occur, or will take long time to occur.{/warning}

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import create_subscriptions_for_api
from cryptoapis.model.new_unconfirmed_coins_transactions_r import NewUnconfirmedCoinsTransactionsR
from cryptoapis.model.convert_bitcoin_cash_address429_response import ConvertBitcoinCashAddress429Response
from cryptoapis.model.convert_bitcoin_cash_address500_response import ConvertBitcoinCashAddress500Response
from cryptoapis.model.convert_bitcoin_cash_address422_response import ConvertBitcoinCashAddress422Response
from cryptoapis.model.new_unconfirmed_coins_transactions400_response import NewUnconfirmedCoinsTransactions400Response
from cryptoapis.model.new_unconfirmed_coins_transactions_rb import NewUnconfirmedCoinsTransactionsRB
from cryptoapis.model.new_unconfirmed_coins_transactions401_response import NewUnconfirmedCoinsTransactions401Response
from cryptoapis.model.new_unconfirmed_coins_transactions403_response import NewUnconfirmedCoinsTransactions403Response
from cryptoapis.model.convert_bitcoin_cash_address402_response import ConvertBitcoinCashAddress402Response
from cryptoapis.model.new_unconfirmed_coins_transactions409_response import NewUnconfirmedCoinsTransactions409Response
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
    api_instance = create_subscriptions_for_api.CreateSubscriptionsForApi(api_client)
    blockchain = "bitcoin" # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    network = "testnet" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    context = "yourExampleString" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    new_unconfirmed_coins_transactions_rb = NewUnconfirmedCoinsTransactionsRB(
        context="yourExampleString",
        data=NewUnconfirmedCoinsTransactionsRBData(
            item=NewUnconfirmedCoinsTransactionsRBDataItem(
                address="mho4jHBcrNCncKt38trJahXakuaBnS7LK5",
                allow_duplicates=True,
                callback_secret_key="yourSecretKey",
                callback_url="https://example.com",
            ),
        ),
    ) # NewUnconfirmedCoinsTransactionsRB |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # New unconfirmed coins transactions
        api_response = api_instance.new_unconfirmed_coins_transactions(blockchain, network)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling CreateSubscriptionsForApi->new_unconfirmed_coins_transactions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # New unconfirmed coins transactions
        api_response = api_instance.new_unconfirmed_coins_transactions(blockchain, network, context=context, new_unconfirmed_coins_transactions_rb=new_unconfirmed_coins_transactions_rb)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling CreateSubscriptionsForApi->new_unconfirmed_coins_transactions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. |
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. |
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]
 **new_unconfirmed_coins_transactions_rb** | [**NewUnconfirmedCoinsTransactionsRB**](NewUnconfirmedCoinsTransactionsRB.md)|  | [optional]

### Return type

[**NewUnconfirmedCoinsTransactionsR**](NewUnconfirmedCoinsTransactionsR.md)

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

# **new_unconfirmed_tokens_transactions**
> NewUnconfirmedTokensTransactionsR new_unconfirmed_tokens_transactions(blockchain, network)

New unconfirmed tokens transactions

Through this endpoint customers can create callback subscriptions for a specific event. In this case the event is when there are new unconfirmed tokens transactions for the user. By creating this subscription the user will be notified by Crypto APIs 2.0 when that event occurs. The information is returned per specified address.    Unconfirmed tokens transactions remain in the mempool (memory pool) until they are confirmed by miners and added to the next block. Sometimes spikes in transaction activity can cause delays in confirmations.    {warning}We cannot guarantee at 100% that webhooks for unconfirmed transactions will always be received. Some may **not get received** due to the possibility of some nodes not being updated with that information. This can occur in networks with low activity and/or not many nodes, e.g. Testnet networks and rarely Mainnets.{/warning}    {note}To have an operational callback subscription, you need to first verify a domain for the Callback URL. Please see more information on Callbacks [here](https://developers.cryptoapis.io/technical-documentation/general-information/callbacks#callback-url).{/note}    {note}It is also **important to note** that just because pending unconfirmed transactions are in the mempool, **doesn't necessarily** mean they will get confirmed.{/note}    {warning}Crypto APIs will notify the user **only when** the event occurs. There are cases when the specific event doesn't happen at all, or takes a long time to do so. A callback notification **will not** be sent if the event does not or cannot occur, or will take long time to occur.{/warning}

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import create_subscriptions_for_api
from cryptoapis.model.convert_bitcoin_cash_address429_response import ConvertBitcoinCashAddress429Response
from cryptoapis.model.convert_bitcoin_cash_address500_response import ConvertBitcoinCashAddress500Response
from cryptoapis.model.convert_bitcoin_cash_address422_response import ConvertBitcoinCashAddress422Response
from cryptoapis.model.new_unconfirmed_tokens_transactions_r import NewUnconfirmedTokensTransactionsR
from cryptoapis.model.new_unconfirmed_tokens_transactions409_response import NewUnconfirmedTokensTransactions409Response
from cryptoapis.model.new_unconfirmed_tokens_transactions400_response import NewUnconfirmedTokensTransactions400Response
from cryptoapis.model.new_unconfirmed_tokens_transactions401_response import NewUnconfirmedTokensTransactions401Response
from cryptoapis.model.new_unconfirmed_tokens_transactions403_response import NewUnconfirmedTokensTransactions403Response
from cryptoapis.model.convert_bitcoin_cash_address402_response import ConvertBitcoinCashAddress402Response
from cryptoapis.model.new_unconfirmed_tokens_transactions_rb import NewUnconfirmedTokensTransactionsRB
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
    api_instance = create_subscriptions_for_api.CreateSubscriptionsForApi(api_client)
    blockchain = "ethereum" # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    network = "ropsten" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    context = "yourExampleString" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    new_unconfirmed_tokens_transactions_rb = NewUnconfirmedTokensTransactionsRB(
        context="yourExampleString",
        data=NewUnconfirmedTokensTransactionsRBData(
            item=NewUnconfirmedTokensTransactionsRBDataItem(
                address="0x033ef6db9fbd0ee60e2931906b987fe0280471a0",
                allow_duplicates=True,
                callback_secret_key="yourSecretKey",
                callback_url="https://example.com",
            ),
        ),
    ) # NewUnconfirmedTokensTransactionsRB |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # New unconfirmed tokens transactions
        api_response = api_instance.new_unconfirmed_tokens_transactions(blockchain, network)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling CreateSubscriptionsForApi->new_unconfirmed_tokens_transactions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # New unconfirmed tokens transactions
        api_response = api_instance.new_unconfirmed_tokens_transactions(blockchain, network, context=context, new_unconfirmed_tokens_transactions_rb=new_unconfirmed_tokens_transactions_rb)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling CreateSubscriptionsForApi->new_unconfirmed_tokens_transactions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. |
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. |
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]
 **new_unconfirmed_tokens_transactions_rb** | [**NewUnconfirmedTokensTransactionsRB**](NewUnconfirmedTokensTransactionsRB.md)|  | [optional]

### Return type

[**NewUnconfirmedTokensTransactionsR**](NewUnconfirmedTokensTransactionsR.md)

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

