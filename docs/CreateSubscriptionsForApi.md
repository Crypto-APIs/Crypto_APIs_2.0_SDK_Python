# cryptoapis.CreateSubscriptionsForApi

All URIs are relative to *https://rest.cryptoapis.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mined_transaction**](CreateSubscriptionsForApi.md#mined_transaction) | **POST** /blockchain-events/{blockchain}/{network}/subscriptions/transaction-mined | Mined transaction
[**new_block**](CreateSubscriptionsForApi.md#new_block) | **POST** /blockchain-events/{blockchain}/{network}/subscriptions/block-mined | New Block
[**new_confirmed_coins_transactions**](CreateSubscriptionsForApi.md#new_confirmed_coins_transactions) | **POST** /blockchain-events/{blockchain}/{network}/subscriptions/address-coins-transactions-confirmed | New confirmed coins transactions
[**new_confirmed_coins_transactions_and_each_confirmation**](CreateSubscriptionsForApi.md#new_confirmed_coins_transactions_and_each_confirmation) | **POST** /blockchain-events/{blockchain}/{network}/subscriptions/address-coins-transactions-confirmed-each-confirmation | New confirmed coins transactions and each confirmation
[**new_confirmed_internal_transactions**](CreateSubscriptionsForApi.md#new_confirmed_internal_transactions) | **POST** /blockchain-events/{blockchain}/{network}/subscriptions/address-internal-transactions-confirmed | New confirmed internal transactions
[**new_confirmed_internal_transactions_and_each_confirmation**](CreateSubscriptionsForApi.md#new_confirmed_internal_transactions_and_each_confirmation) | **POST** /blockchain-events/{blockchain}/{network}/subscriptions/address-internal-transactions-confirmed-each-confirmation | New confirmed internal transactions and each confirmation
[**new_confirmed_tokens_transactions**](CreateSubscriptionsForApi.md#new_confirmed_tokens_transactions) | **POST** /blockchain-events/{blockchain}/{network}/subscriptions/address-tokens-transactions-confirmed | New confirmed tokens transactions
[**new_confirmed_tokens_transactions_and_each_confirmation**](CreateSubscriptionsForApi.md#new_confirmed_tokens_transactions_and_each_confirmation) | **POST** /blockchain-events/{blockchain}/{network}/subscriptions/address-tokens-transactions-confirmed-each-confirmation | New confirmed tokens transactions and each confirmation
[**new_unconfirmed_coins_transactions**](CreateSubscriptionsForApi.md#new_unconfirmed_coins_transactions) | **POST** /blockchain-events/{blockchain}/{network}/subscriptions/address-coins-transactions-unconfirmed | New unconfirmed coins transactions
[**new_unconfirmed_tokens_transactions**](CreateSubscriptionsForApi.md#new_unconfirmed_tokens_transactions) | **POST** /blockchain-events/{blockchain}/{network}/subscriptions/address-tokens-transactions-unconfirmed | New unconfirmed tokens transactions


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
from cryptoapis.model.blockchain_events_callbacks_limit_reached import BlockchainEventsCallbacksLimitReached
from cryptoapis.model.insufficient_credits import InsufficientCredits
from cryptoapis.model.already_exists import AlreadyExists
from cryptoapis.model.invalid_api_key import InvalidApiKey
from cryptoapis.model.invalid_request_body_structure import InvalidRequestBodyStructure
from cryptoapis.model.request_limit_reached import RequestLimitReached
from cryptoapis.model.mined_transaction_rb import MinedTransactionRB
from cryptoapis.model.invalid_pagination import InvalidPagination
from cryptoapis.model.mined_transaction_r import MinedTransactionR
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
    api_instance = create_subscriptions_for_api.CreateSubscriptionsForApi(api_client)
    blockchain = "bitcoin" # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    network = "testnet" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\", \"rinkeby\" are test networks.
    context = "context_example" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    mined_transaction_rb = MinedTransactionRB(
        context="context_example",
        data=MinedTransactionRBData(
            item=MinedTransactionRBDataItem(
                allow_duplicates=False,
                callback_secret_key="yourSecretKey",
                callback_url="http://example.com",
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
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot;, \&quot;rinkeby\&quot; are test networks. |
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
**400** | The pagination attributes that have been used are invalid. Please check the Documentation to see details on pagination. |  -  |
**401** | The provided API key is invalid. Please, generate a new one from your Dashboard. |  -  |
**402** | You have insufficient credits. Please upgrade your plan from your Dashboard or contact our team via email. |  -  |
**403** | You have reached the maximum number of active Blockchain Events subscriptions which is {callbacks_limit} now. Please upgrade your plan to be get higher number of active subscriptions. |  -  |
**409** | The specified resource already exists. |  -  |
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
from cryptoapis.model.blockchain_events_callbacks_limit_reached import BlockchainEventsCallbacksLimitReached
from cryptoapis.model.insufficient_credits import InsufficientCredits
from cryptoapis.model.already_exists import AlreadyExists
from cryptoapis.model.invalid_api_key import InvalidApiKey
from cryptoapis.model.invalid_request_body_structure import InvalidRequestBodyStructure
from cryptoapis.model.request_limit_reached import RequestLimitReached
from cryptoapis.model.new_block_rb import NewBlockRB
from cryptoapis.model.invalid_pagination import InvalidPagination
from cryptoapis.model.new_block_r import NewBlockR
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
    api_instance = create_subscriptions_for_api.CreateSubscriptionsForApi(api_client)
    blockchain = "bitcoin" # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    network = "testnet" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\", \"rinkeby\" are test networks.
    context = "context_example" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    new_block_rb = NewBlockRB(
        context="context_example",
        data=NewBlockRBData(
            item=NewBlockRBDataItem(
                allow_duplicates=True,
                callback_secret_key="yourSecretKey",
                callback_url="http://example.com",
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
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot;, \&quot;rinkeby\&quot; are test networks. |
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
**400** | The pagination attributes that have been used are invalid. Please check the Documentation to see details on pagination. |  -  |
**401** | The provided API key is invalid. Please, generate a new one from your Dashboard. |  -  |
**402** | You have insufficient credits. Please upgrade your plan from your Dashboard or contact our team via email. |  -  |
**403** | You have reached the maximum number of active Blockchain Events subscriptions which is {callbacks_limit} now. Please upgrade your plan to be get higher number of active subscriptions. |  -  |
**409** | The specified resource already exists. |  -  |
**415** | The selected Media Type is unavailable. The Content-Type header should be &#39;application/json&#39;. |  -  |
**422** | Your request body for POST requests must have a structure of { data: { item: [...properties] } } |  -  |
**429** | The request limit has been reached. There can be maximum {requests} requests per {seconds} second(s) made. Please contact our team via email if you need more or upgrade your plan. |  -  |
**500** | An unexpected server error has occurred, we are working to fix this. Please try again later and in case it occurs again please report it to our team via email. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **new_confirmed_coins_transactions**
> NewConfirmedCoinsTransactionsR new_confirmed_coins_transactions(blockchain, network)

New confirmed coins transactions

Through this endpoint customers can create callback subscriptions for a specific event. In this case the event is when there are new incoming or outgoing confirmed transactions for coins from/to the customer's address. By creating this subscription the user will be notified by Crypto APIs 2.0 when that event occurs. The information is returned per specified address.     Being confirmed means that the transactions are verified by miners and added to the next block.    {note}To have an operational callback subscription, you need to first verify a domain for the Callback URL. Please see more information on Callbacks [here](https://developers.cryptoapis.io/technical-documentation/general-information/callbacks#callback-url).{/note}    {warning}Crypto APIs will notify the user **only when** the event occurs. There are cases when the specific event doesn't happen at all, or takes a long time to do so. A callback notification **will not** be sent if the event does not or cannot occur, or will take long time to occur.{/warning}

### Example

* Api Key Authentication (ApiKey):
```python
import time
import cryptoapis
from cryptoapis.api import create_subscriptions_for_api
from cryptoapis.model.new_confirmed_coins_transactions_rb import NewConfirmedCoinsTransactionsRB
from cryptoapis.model.blockchain_events_callbacks_limit_reached import BlockchainEventsCallbacksLimitReached
from cryptoapis.model.insufficient_credits import InsufficientCredits
from cryptoapis.model.already_exists import AlreadyExists
from cryptoapis.model.invalid_api_key import InvalidApiKey
from cryptoapis.model.invalid_request_body_structure import InvalidRequestBodyStructure
from cryptoapis.model.request_limit_reached import RequestLimitReached
from cryptoapis.model.new_confirmed_coins_transactions_r import NewConfirmedCoinsTransactionsR
from cryptoapis.model.invalid_pagination import InvalidPagination
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
    api_instance = create_subscriptions_for_api.CreateSubscriptionsForApi(api_client)
    blockchain = "bitcoin" # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    network = "testnet" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\", \"rinkeby\" are test networks.
    context = "context_example" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    new_confirmed_coins_transactions_rb = NewConfirmedCoinsTransactionsRB(
        context="context_example",
        data=NewConfirmedCoinsTransactionsRBData(
            item=NewConfirmedCoinsTransactionsRBDataItem(
                address="mho4jHBcrNCncKt38trJahXakuaBnS7LK5",
                allow_duplicates=True,
                callback_secret_key="yourSecretKey",
                callback_url="http://example.com",
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
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot;, \&quot;rinkeby\&quot; are test networks. |
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
**400** | The pagination attributes that have been used are invalid. Please check the Documentation to see details on pagination. |  -  |
**401** | The provided API key is invalid. Please, generate a new one from your Dashboard. |  -  |
**402** | You have insufficient credits. Please upgrade your plan from your Dashboard or contact our team via email. |  -  |
**403** | You have reached the maximum number of active Blockchain Events subscriptions which is {callbacks_limit} now. Please upgrade your plan to be get higher number of active subscriptions. |  -  |
**409** | The specified resource already exists. |  -  |
**415** | The selected Media Type is unavailable. The Content-Type header should be &#39;application/json&#39;. |  -  |
**422** | Your request body for POST requests must have a structure of { data: { item: [...properties] } } |  -  |
**429** | The request limit has been reached. There can be maximum {requests} requests per {seconds} second(s) made. Please contact our team via email if you need more or upgrade your plan. |  -  |
**500** | An unexpected server error has occurred, we are working to fix this. Please try again later and in case it occurs again please report it to our team via email. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **new_confirmed_coins_transactions_and_each_confirmation**
> NewConfirmedCoinsTransactionsAndEachConfirmationR new_confirmed_coins_transactions_and_each_confirmation(blockchain, network)

New confirmed coins transactions and each confirmation

Through this endpoint customers can create callback subscriptions for a specific event. In this case the event is when there are new incoming or outgoing confirmed transactions for coins from/to the customer's address with also a response at each confirmation the transaction has received until the specified confirmations limit is reached. By creating this subscription the user will be notified by Crypto APIs 2.0 when that event occurs. The information is returned per specified address.     Being confirmed means that the transactions are verified by miners and added to the next block. This endpoint refers to **coins transactions only, not tokens**.    {note}To have an operational callback subscription, you need to first verify a domain for the Callback URL. Please see more information on Callbacks [here](https://developers.cryptoapis.io/technical-documentation/general-information/callbacks#callback-url).{/note}    {warning}Crypto APIs will notify the user **only when** the event occurs. There are cases when the specific event doesn't happen at all, or takes a long time to do so. A callback notification **will not** be sent if the event does not or cannot occur, or will take long time to occur.{/warning}

### Example

* Api Key Authentication (ApiKey):
```python
import time
import cryptoapis
from cryptoapis.api import create_subscriptions_for_api
from cryptoapis.model.new_confirmed_coins_transactions_and_each_confirmation_r import NewConfirmedCoinsTransactionsAndEachConfirmationR
from cryptoapis.model.new_confirmed_coins_transactions_and_each_confirmation_rb import NewConfirmedCoinsTransactionsAndEachConfirmationRB
from cryptoapis.model.blockchain_events_callbacks_limit_reached import BlockchainEventsCallbacksLimitReached
from cryptoapis.model.insufficient_credits import InsufficientCredits
from cryptoapis.model.already_exists import AlreadyExists
from cryptoapis.model.invalid_api_key import InvalidApiKey
from cryptoapis.model.invalid_request_body_structure import InvalidRequestBodyStructure
from cryptoapis.model.request_limit_reached import RequestLimitReached
from cryptoapis.model.invalid_pagination import InvalidPagination
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
    api_instance = create_subscriptions_for_api.CreateSubscriptionsForApi(api_client)
    blockchain = "bitcoin" # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    network = "testnet" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\", \"rinkeby\" are test networks.
    context = "context_example" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    new_confirmed_coins_transactions_and_each_confirmation_rb = NewConfirmedCoinsTransactionsAndEachConfirmationRB(
        context="context_example",
        data=NewConfirmedCoinsTransactionsAndEachConfirmationRBData(
            item=NewConfirmedCoinsTransactionsAndEachConfirmationRBDataItem(
                address="mho4jHBcrNCncKt38trJahXakuaBnS7LK5",
                allow_duplicates=True,
                callback_secret_key="yourSecretKey",
                callback_url="http://example.com",
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
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot;, \&quot;rinkeby\&quot; are test networks. |
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
**400** | The pagination attributes that have been used are invalid. Please check the Documentation to see details on pagination. |  -  |
**401** | The provided API key is invalid. Please, generate a new one from your Dashboard. |  -  |
**402** | You have insufficient credits. Please upgrade your plan from your Dashboard or contact our team via email. |  -  |
**403** | You have reached the maximum number of active Blockchain Events subscriptions which is {callbacks_limit} now. Please upgrade your plan to be get higher number of active subscriptions. |  -  |
**409** | The specified resource already exists. |  -  |
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
from cryptoapis.model.blockchain_events_callbacks_limit_reached import BlockchainEventsCallbacksLimitReached
from cryptoapis.model.insufficient_credits import InsufficientCredits
from cryptoapis.model.already_exists import AlreadyExists
from cryptoapis.model.invalid_api_key import InvalidApiKey
from cryptoapis.model.invalid_request_body_structure import InvalidRequestBodyStructure
from cryptoapis.model.request_limit_reached import RequestLimitReached
from cryptoapis.model.invalid_pagination import InvalidPagination
from cryptoapis.model.new_confirmed_internal_transactions_r import NewConfirmedInternalTransactionsR
from cryptoapis.model.unexpected_server_error import UnexpectedServerError
from cryptoapis.model.new_confirmed_internal_transactions_rb import NewConfirmedInternalTransactionsRB
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
    api_instance = create_subscriptions_for_api.CreateSubscriptionsForApi(api_client)
    blockchain = "ethereum" # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    network = "mainnet" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\", \"rinkeby\" are test networks.
    context = "context_example" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    new_confirmed_internal_transactions_rb = NewConfirmedInternalTransactionsRB(
        context="context_example",
        data=NewConfirmedInternalTransactionsRBData(
            item=NewConfirmedInternalTransactionsRBDataItem(
                address="0xbcc817f057950b0df41206c5d7125e6225cae18e",
                allow_duplicates=True,
                callback_secret_key="yourSecretKey",
                callback_url="http://example.com",
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
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot;, \&quot;rinkeby\&quot; are test networks. |
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
**400** | The pagination attributes that have been used are invalid. Please check the Documentation to see details on pagination. |  -  |
**401** | The provided API key is invalid. Please, generate a new one from your Dashboard. |  -  |
**402** | You have insufficient credits. Please upgrade your plan from your Dashboard or contact our team via email. |  -  |
**403** | You have reached the maximum number of active Blockchain Events subscriptions which is {callbacks_limit} now. Please upgrade your plan to be get higher number of active subscriptions. |  -  |
**409** | The specified resource already exists. |  -  |
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
from cryptoapis.model.new_confirmed_internal_transactions_and_each_confirmation_r import NewConfirmedInternalTransactionsAndEachConfirmationR
from cryptoapis.model.blockchain_events_callbacks_limit_reached import BlockchainEventsCallbacksLimitReached
from cryptoapis.model.insufficient_credits import InsufficientCredits
from cryptoapis.model.already_exists import AlreadyExists
from cryptoapis.model.invalid_api_key import InvalidApiKey
from cryptoapis.model.invalid_request_body_structure import InvalidRequestBodyStructure
from cryptoapis.model.request_limit_reached import RequestLimitReached
from cryptoapis.model.new_confirmed_internal_transactions_and_each_confirmation_rb import NewConfirmedInternalTransactionsAndEachConfirmationRB
from cryptoapis.model.invalid_pagination import InvalidPagination
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
    api_instance = create_subscriptions_for_api.CreateSubscriptionsForApi(api_client)
    blockchain = "ethereum" # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    network = "mainnet" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\", \"rinkeby\" are test networks.
    context = "context_example" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    new_confirmed_internal_transactions_and_each_confirmation_rb = NewConfirmedInternalTransactionsAndEachConfirmationRB(
        context="context_example",
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
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot;, \&quot;rinkeby\&quot; are test networks. |
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
**400** | The pagination attributes that have been used are invalid. Please check the Documentation to see details on pagination. |  -  |
**401** | The provided API key is invalid. Please, generate a new one from your Dashboard. |  -  |
**402** | You have insufficient credits. Please upgrade your plan from your Dashboard or contact our team via email. |  -  |
**403** | You have reached the maximum number of active Blockchain Events subscriptions which is {callbacks_limit} now. Please upgrade your plan to be get higher number of active subscriptions. |  -  |
**409** | The specified resource already exists. |  -  |
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
from cryptoapis.model.new_confirmed_tokens_transactions_rb import NewConfirmedTokensTransactionsRB
from cryptoapis.model.blockchain_events_callbacks_limit_reached import BlockchainEventsCallbacksLimitReached
from cryptoapis.model.insufficient_credits import InsufficientCredits
from cryptoapis.model.already_exists import AlreadyExists
from cryptoapis.model.invalid_api_key import InvalidApiKey
from cryptoapis.model.invalid_request_body_structure import InvalidRequestBodyStructure
from cryptoapis.model.request_limit_reached import RequestLimitReached
from cryptoapis.model.invalid_pagination import InvalidPagination
from cryptoapis.model.new_confirmed_tokens_transactions_r import NewConfirmedTokensTransactionsR
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
    api_instance = create_subscriptions_for_api.CreateSubscriptionsForApi(api_client)
    blockchain = "bitcoin" # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    network = "testnet" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\", \"rinkeby\" are test networks.
    context = "context_example" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    new_confirmed_tokens_transactions_rb = NewConfirmedTokensTransactionsRB(
        context="context_example",
        data=NewUnconfirmedTokensTransactionsRBData(
            item=NewUnconfirmedTokensTransactionsRBDataItem(
                address="mho4jHBcrNCncKt38trJahXakuaBnS7LK5",
                allow_duplicates=True,
                callback_secret_key="yourSecretKey",
                callback_url="http://example.com",
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
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot;, \&quot;rinkeby\&quot; are test networks. |
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
**400** | The pagination attributes that have been used are invalid. Please check the Documentation to see details on pagination. |  -  |
**401** | The provided API key is invalid. Please, generate a new one from your Dashboard. |  -  |
**402** | You have insufficient credits. Please upgrade your plan from your Dashboard or contact our team via email. |  -  |
**403** | You have reached the maximum number of active Blockchain Events subscriptions which is {callbacks_limit} now. Please upgrade your plan to be get higher number of active subscriptions. |  -  |
**409** | The specified resource already exists. |  -  |
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
from cryptoapis.model.new_confirmed_tokens_transactions_and_each_confirmation_r import NewConfirmedTokensTransactionsAndEachConfirmationR
from cryptoapis.model.blockchain_events_callbacks_limit_reached import BlockchainEventsCallbacksLimitReached
from cryptoapis.model.insufficient_credits import InsufficientCredits
from cryptoapis.model.already_exists import AlreadyExists
from cryptoapis.model.invalid_api_key import InvalidApiKey
from cryptoapis.model.invalid_request_body_structure import InvalidRequestBodyStructure
from cryptoapis.model.request_limit_reached import RequestLimitReached
from cryptoapis.model.invalid_pagination import InvalidPagination
from cryptoapis.model.new_confirmed_tokens_transactions_and_each_confirmation_rb import NewConfirmedTokensTransactionsAndEachConfirmationRB
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
    api_instance = create_subscriptions_for_api.CreateSubscriptionsForApi(api_client)
    blockchain = "bitcoin" # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    network = "testnet" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\", \"rinkeby\" are test networks.
    context = "context_example" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    new_confirmed_tokens_transactions_and_each_confirmation_rb = NewConfirmedTokensTransactionsAndEachConfirmationRB(
        context="context_example",
        data=NewConfirmedTokensTransactionsAndEachConfirmationRBData(
            item=NewConfirmedTokensTransactionsAndEachConfirmationRBDataItem(
                address="mho4jHBcrNCncKt38trJahXakuaBnS7LK5",
                allow_duplicates=True,
                callback_secret_key="yourSecretKey",
                callback_url="http://example.com",
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
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot;, \&quot;rinkeby\&quot; are test networks. |
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
**400** | The pagination attributes that have been used are invalid. Please check the Documentation to see details on pagination. |  -  |
**401** | The provided API key is invalid. Please, generate a new one from your Dashboard. |  -  |
**402** | You have insufficient credits. Please upgrade your plan from your Dashboard or contact our team via email. |  -  |
**403** | You have reached the maximum number of active Blockchain Events subscriptions which is {callbacks_limit} now. Please upgrade your plan to be get higher number of active subscriptions. |  -  |
**409** | The specified resource already exists. |  -  |
**415** | The selected Media Type is unavailable. The Content-Type header should be &#39;application/json&#39;. |  -  |
**422** | Your request body for POST requests must have a structure of { data: { item: [...properties] } } |  -  |
**429** | The request limit has been reached. There can be maximum {requests} requests per {seconds} second(s) made. Please contact our team via email if you need more or upgrade your plan. |  -  |
**500** | An unexpected server error has occurred, we are working to fix this. Please try again later and in case it occurs again please report it to our team via email. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **new_unconfirmed_coins_transactions**
> NewUnconfirmedCoinsTransactionsR new_unconfirmed_coins_transactions(blockchain, network)

New unconfirmed coins transactions

Through this endpoint customers can create callback subscriptions for a specific event. In this case the event is when there are new unconfirmed coins transactions for the user. By creating this subscription the user will be notified by Crypto APIs 2.0 when that event occurs. The information is returned per specified address.    Unconfirmed coins transactions remain in the mempool (memory pool) until they are confirmed by miners and added to the next block. Sometimes spikes in transaction activity can cause delays in confirmations.    {warning}We cannot guarantee at 100% that webhooks for unconfirmed transactions will always be received. Some may **not get received** due to the possibility of some nodes not being updated with that information. This can occur in networks with low activity and/or not many nodes, e.g. Testnet networks and rarely Mainnets.{/warning}    {note}To have an operational callback subscription, you need to first verify a domain for the Callback URL. Please see more information on Callbacks [here](https://developers.cryptoapis.io/technical-documentation/general-information/callbacks#callback-url).{/note}    {note}It is also **important to note** that just because pending unconfirmed transactions are in the mempool, **doesn't necessarily** mean they will get confirmed.{/note}    {warning}Crypto APIs will notify the user **only when** the event occurs. There are cases when the specific event doesn't happen at all, or takes a long time to do so. A callback notification **will not** be sent if the event does not or cannot occur, or will take long time to occur.{/warning}

### Example

* Api Key Authentication (ApiKey):
```python
import time
import cryptoapis
from cryptoapis.api import create_subscriptions_for_api
from cryptoapis.model.new_unconfirmed_coins_transactions_r import NewUnconfirmedCoinsTransactionsR
from cryptoapis.model.blockchain_events_callbacks_limit_reached import BlockchainEventsCallbacksLimitReached
from cryptoapis.model.insufficient_credits import InsufficientCredits
from cryptoapis.model.already_exists import AlreadyExists
from cryptoapis.model.invalid_api_key import InvalidApiKey
from cryptoapis.model.invalid_request_body_structure import InvalidRequestBodyStructure
from cryptoapis.model.request_limit_reached import RequestLimitReached
from cryptoapis.model.invalid_pagination import InvalidPagination
from cryptoapis.model.new_unconfirmed_coins_transactions_rb import NewUnconfirmedCoinsTransactionsRB
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
    api_instance = create_subscriptions_for_api.CreateSubscriptionsForApi(api_client)
    blockchain = "bitcoin" # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    network = "testnet" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\", \"rinkeby\" are test networks.
    context = "context_example" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    new_unconfirmed_coins_transactions_rb = NewUnconfirmedCoinsTransactionsRB(
        context="context_example",
        data=NewUnconfirmedCoinsTransactionsRBData(
            item=NewUnconfirmedCoinsTransactionsRBDataItem(
                address="mho4jHBcrNCncKt38trJahXakuaBnS7LK5",
                allow_duplicates=True,
                callback_secret_key="yourSecretKey",
                callback_url="http://example.com",
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
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot;, \&quot;rinkeby\&quot; are test networks. |
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
**400** | The pagination attributes that have been used are invalid. Please check the Documentation to see details on pagination. |  -  |
**401** | The provided API key is invalid. Please, generate a new one from your Dashboard. |  -  |
**402** | You have insufficient credits. Please upgrade your plan from your Dashboard or contact our team via email. |  -  |
**403** | You have reached the maximum number of active Blockchain Events subscriptions which is {callbacks_limit} now. Please upgrade your plan to be get higher number of active subscriptions. |  -  |
**409** | The specified resource already exists. |  -  |
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
from cryptoapis.model.new_unconfirmed_tokens_transactions_r import NewUnconfirmedTokensTransactionsR
from cryptoapis.model.blockchain_events_callbacks_limit_reached import BlockchainEventsCallbacksLimitReached
from cryptoapis.model.insufficient_credits import InsufficientCredits
from cryptoapis.model.already_exists import AlreadyExists
from cryptoapis.model.invalid_api_key import InvalidApiKey
from cryptoapis.model.invalid_request_body_structure import InvalidRequestBodyStructure
from cryptoapis.model.request_limit_reached import RequestLimitReached
from cryptoapis.model.invalid_pagination import InvalidPagination
from cryptoapis.model.unexpected_server_error import UnexpectedServerError
from cryptoapis.model.new_unconfirmed_tokens_transactions_rb import NewUnconfirmedTokensTransactionsRB
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
    api_instance = create_subscriptions_for_api.CreateSubscriptionsForApi(api_client)
    blockchain = "bitcoin" # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    network = "testnet" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\", \"rinkeby\" are test networks.
    context = "context_example" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    new_unconfirmed_tokens_transactions_rb = NewUnconfirmedTokensTransactionsRB(
        context="context_example",
        data=NewUnconfirmedTokensTransactionsRBData(
            item=NewUnconfirmedTokensTransactionsRBDataItem(
                address="mho4jHBcrNCncKt38trJahXakuaBnS7LK5",
                allow_duplicates=True,
                callback_secret_key="yourSecretKey",
                callback_url="http://example.com",
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
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot;, \&quot;rinkeby\&quot; are test networks. |
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
**400** | The pagination attributes that have been used are invalid. Please check the Documentation to see details on pagination. |  -  |
**401** | The provided API key is invalid. Please, generate a new one from your Dashboard. |  -  |
**402** | You have insufficient credits. Please upgrade your plan from your Dashboard or contact our team via email. |  -  |
**403** | You have reached the maximum number of active Blockchain Events subscriptions which is {callbacks_limit} now. Please upgrade your plan to be get higher number of active subscriptions. |  -  |
**409** | The specified resource already exists. |  -  |
**415** | The selected Media Type is unavailable. The Content-Type header should be &#39;application/json&#39;. |  -  |
**422** | Your request body for POST requests must have a structure of { data: { item: [...properties] } } |  -  |
**429** | The request limit has been reached. There can be maximum {requests} requests per {seconds} second(s) made. Please contact our team via email if you need more or upgrade your plan. |  -  |
**500** | An unexpected server error has occurred, we are working to fix this. Please try again later and in case it occurs again please report it to our team via email. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

