# cryptoapis.CreateSubscriptionsForApi

All URIs are relative to *https://rest.cryptoapis.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mined_transaction**](CreateSubscriptionsForApi.md#mined_transaction) | **POST** /blockchain-events/{blockchain}/{network}/subscriptions/transaction-mined | Mined transaction
[**new_block**](CreateSubscriptionsForApi.md#new_block) | **POST** /blockchain-events/{blockchain}/{network}/subscriptions/block-mined | New Block
[**new_confirmed_coins_transactions**](CreateSubscriptionsForApi.md#new_confirmed_coins_transactions) | **POST** /blockchain-events/{blockchain}/{network}/subscriptions/address-coins-transactions-confirmed | New confirmed coins transactions
[**new_confirmed_coins_transactions_and_each_confirmation**](CreateSubscriptionsForApi.md#new_confirmed_coins_transactions_and_each_confirmation) | **POST** /blockchain-events/{blockchain}/{network}/subscriptions/address-coins-transactions-confirmed-each-confirmation | New confirmed coins transactions and each confirmation
[**new_confirmed_tokens_transactions**](CreateSubscriptionsForApi.md#new_confirmed_tokens_transactions) | **POST** /blockchain-events/{blockchain}/{network}/subscriptions/address-tokens-transactions-confirmed | New confirmed tokens transactions
[**new_confirmed_tokens_transactions_and_each_confirmation**](CreateSubscriptionsForApi.md#new_confirmed_tokens_transactions_and_each_confirmation) | **POST** /blockchain-events/{blockchain}/{network}/subscriptions/address-tokens-transactions-confirmed-each-confirmation | New confirmed tokens transactions and each confirmation
[**new_unconfirmed_coins_transactions**](CreateSubscriptionsForApi.md#new_unconfirmed_coins_transactions) | **POST** /blockchain-events/{blockchain}/{network}/subscriptions/address-coins-transactions-unconfirmed | New unconfirmed coins transactions
[**new_unconfirmed_tokens_transactions**](CreateSubscriptionsForApi.md#new_unconfirmed_tokens_transactions) | **POST** /blockchain-events/{blockchain}/{network}/subscriptions/address-tokens-transactions-unconfirmed | New unconfirmed tokens transactions


# **mined_transaction**
> MinedTransactionResponse mined_transaction(blockchain, network)

Mined transaction

Through this endpoint customers can create callback subscriptions for a specific event. In this case the event is when a specific transaction is mined. By creating this subscription the user will be notified by Crypto APIs 2.0 when that event occurs. The information is returned per specified `transactionId`.    A transaction is mined when it is included in a new block in the blockchain.    {note}To have an operational callback subscription, you need to first verify a domain for the Callback URL. Please see more information on Callbacks [here](https://developers.cryptoapis.io/technical-documentation/general-information/callbacks#callback-url).{/note}    {warning}Crypto APIs will notify the user **only when** the event occurs. There are cases when the specific event doesn't happen at all, or takes a long time to do so. A callback notification **will not** be sent if the event does not or cannot occur, or will take long time to occur.{/warning}

### Example

* Api Key Authentication (ApiKey):
```python
import time
import cryptoapis
from cryptoapis.api import create_subscriptions_for_api
from cryptoapis.model.mined_transaction_response import MinedTransactionResponse
from cryptoapis.model.blockchain_events_callbacks_limit_reached import BlockchainEventsCallbacksLimitReached
from cryptoapis.model.insufficient_credits import InsufficientCredits
from cryptoapis.model.mined_transaction_request_body import MinedTransactionRequestBody
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
    mined_transaction_request_body = MinedTransactionRequestBody(
        context="context_example",
        data=MinedTransactionRequestBodyData(
            item=MinedTransactionRequestBodyDataItem(
                allow_duplicates=False,
                callback_secret_key="yourSecretKey",
                callback_url="http://example.com",
                transaction_id="df2690ff97e72c1f8b0f2102a8cb5c1d0fa8fb8754d543c9bc0edc4d4bc34bfc",
            ),
        ),
    ) # MinedTransactionRequestBody |  (optional)

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
        api_response = api_instance.mined_transaction(blockchain, network, context=context, mined_transaction_request_body=mined_transaction_request_body)
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
 **mined_transaction_request_body** | [**MinedTransactionRequestBody**](MinedTransactionRequestBody.md)|  | [optional]

### Return type

[**MinedTransactionResponse**](MinedTransactionResponse.md)

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
> NewBlockResponse new_block(blockchain, network)

New Block

Through this endpoint customers can create callback subscriptions for a specific event. In this case the event is when a new block is mined in the specific blockchain. By creating this subscription the user will be notified by Crypto APIs 2.0 when that event occurs. The information is returned per specified address.    A new block is mined when it is added to the chain once a consensus is reached by the majority of the miners, which is when the block gets validated and added to the blockchain.    {note}To have an operational callback subscription, you need to first verify a domain for the Callback URL. Please see more information on Callbacks [here](https://developers.cryptoapis.io/technical-documentation/general-information/callbacks#callback-url).{/note}    {warning}Crypto APIs will notify the user **only when** the event occurs. There are cases when the specific event doesn't happen at all, or takes a long time to do so. A callback notification **will not** be sent if the event does not or cannot occur, or will take long time to occur.{/warning}

### Example

* Api Key Authentication (ApiKey):
```python
import time
import cryptoapis
from cryptoapis.api import create_subscriptions_for_api
from cryptoapis.model.new_block_request_body import NewBlockRequestBody
from cryptoapis.model.blockchain_events_callbacks_limit_reached import BlockchainEventsCallbacksLimitReached
from cryptoapis.model.insufficient_credits import InsufficientCredits
from cryptoapis.model.already_exists import AlreadyExists
from cryptoapis.model.invalid_api_key import InvalidApiKey
from cryptoapis.model.new_block_response import NewBlockResponse
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
    new_block_request_body = NewBlockRequestBody(
        context="context_example",
        data=NewBlockRequestBodyData(
            item=NewBlockRequestBodyDataItem(
                allow_duplicates=True,
                callback_secret_key="yourSecretKey",
                callback_url="http://example.com",
            ),
        ),
    ) # NewBlockRequestBody |  (optional)

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
        api_response = api_instance.new_block(blockchain, network, context=context, new_block_request_body=new_block_request_body)
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
 **new_block_request_body** | [**NewBlockRequestBody**](NewBlockRequestBody.md)|  | [optional]

### Return type

[**NewBlockResponse**](NewBlockResponse.md)

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
> NewConfirmedCoinsTransactionsResponse new_confirmed_coins_transactions(blockchain, network)

New confirmed coins transactions

Through this endpoint customers can create callback subscriptions for a specific event. In this case the event is when there are new incoming or outgoing confirmed transactions for coins from/to the customer's address. By creating this subscription the user will be notified by Crypto APIs 2.0 when that event occurs. The information is returned per specified address.     Being confirmed means that the transactions are verified by miners and added to the next block.    {note}To have an operational callback subscription, you need to first verify a domain for the Callback URL. Please see more information on Callbacks [here](https://developers.cryptoapis.io/technical-documentation/general-information/callbacks#callback-url).{/note}    {warning}Crypto APIs will notify the user **only when** the event occurs. There are cases when the specific event doesn't happen at all, or takes a long time to do so. A callback notification **will not** be sent if the event does not or cannot occur, or will take long time to occur.{/warning}

### Example

* Api Key Authentication (ApiKey):
```python
import time
import cryptoapis
from cryptoapis.api import create_subscriptions_for_api
from cryptoapis.model.new_confirmed_coins_transactions_response import NewConfirmedCoinsTransactionsResponse
from cryptoapis.model.blockchain_events_callbacks_limit_reached import BlockchainEventsCallbacksLimitReached
from cryptoapis.model.insufficient_credits import InsufficientCredits
from cryptoapis.model.new_confirmed_coins_transactions_request_body import NewConfirmedCoinsTransactionsRequestBody
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
    new_confirmed_coins_transactions_request_body = NewConfirmedCoinsTransactionsRequestBody(
        context="context_example",
        data=NewConfirmedCoinsTransactionsRequestBodyData(
            item=NewConfirmedCoinsTransactionsRequestBodyDataItem(
                address="mho4jHBcrNCncKt38trJahXakuaBnS7LK5",
                allow_duplicates=True,
                callback_secret_key="yourSecretKey",
                callback_url="http://example.com",
            ),
        ),
    ) # NewConfirmedCoinsTransactionsRequestBody |  (optional)

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
        api_response = api_instance.new_confirmed_coins_transactions(blockchain, network, context=context, new_confirmed_coins_transactions_request_body=new_confirmed_coins_transactions_request_body)
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
 **new_confirmed_coins_transactions_request_body** | [**NewConfirmedCoinsTransactionsRequestBody**](NewConfirmedCoinsTransactionsRequestBody.md)|  | [optional]

### Return type

[**NewConfirmedCoinsTransactionsResponse**](NewConfirmedCoinsTransactionsResponse.md)

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
> NewConfirmedCoinsTransactionsAndEachConfirmationResponse new_confirmed_coins_transactions_and_each_confirmation(blockchain, network)

New confirmed coins transactions and each confirmation

Through this endpoint customers can create callback subscriptions for a specific event. In this case the event is when there are new incoming or outgoing confirmed transactions for coins from/to the customer's address with also a response at each confirmation the transaction has received until the specified confirmations limit is reached. By creating this subscription the user will be notified by Crypto APIs 2.0 when that event occurs. The information is returned per specified address.     Being confirmed means that the transactions are verified by miners and added to the next block. This endpoint refers to **coins transactions only, not tokens**.    {note}To have an operational callback subscription, you need to first verify a domain for the Callback URL. Please see more information on Callbacks [here](https://developers.cryptoapis.io/technical-documentation/general-information/callbacks#callback-url).{/note}    {warning}Crypto APIs will notify the user **only when** the event occurs. There are cases when the specific event doesn't happen at all, or takes a long time to do so. A callback notification **will not** be sent if the event does not or cannot occur, or will take long time to occur.{/warning}

### Example

* Api Key Authentication (ApiKey):
```python
import time
import cryptoapis
from cryptoapis.api import create_subscriptions_for_api
from cryptoapis.model.new_confirmed_coins_transactions_and_each_confirmation_response import NewConfirmedCoinsTransactionsAndEachConfirmationResponse
from cryptoapis.model.new_confirmed_coins_transactions_and_each_confirmation_request_body import NewConfirmedCoinsTransactionsAndEachConfirmationRequestBody
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
    new_confirmed_coins_transactions_and_each_confirmation_request_body = NewConfirmedCoinsTransactionsAndEachConfirmationRequestBody(
        context="context_example",
        data=NewConfirmedCoinsTransactionsAndEachConfirmationRequestBodyData(
            item=NewConfirmedCoinsTransactionsAndEachConfirmationRequestBodyDataItem(
                address="mho4jHBcrNCncKt38trJahXakuaBnS7LK5",
                allow_duplicates=True,
                callback_secret_key="yourSecretKey",
                callback_url="http://example.com",
                confirmations_count=3,
            ),
        ),
    ) # NewConfirmedCoinsTransactionsAndEachConfirmationRequestBody |  (optional)

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
        api_response = api_instance.new_confirmed_coins_transactions_and_each_confirmation(blockchain, network, context=context, new_confirmed_coins_transactions_and_each_confirmation_request_body=new_confirmed_coins_transactions_and_each_confirmation_request_body)
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
 **new_confirmed_coins_transactions_and_each_confirmation_request_body** | [**NewConfirmedCoinsTransactionsAndEachConfirmationRequestBody**](NewConfirmedCoinsTransactionsAndEachConfirmationRequestBody.md)|  | [optional]

### Return type

[**NewConfirmedCoinsTransactionsAndEachConfirmationResponse**](NewConfirmedCoinsTransactionsAndEachConfirmationResponse.md)

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
> NewConfirmedTokensTransactionsResponse new_confirmed_tokens_transactions(blockchain, network)

New confirmed tokens transactions

Through this endpoint customers can create callback subscriptions for a specific event. In this case the event is when there are new incoming or outgoing confirmed transactions for tokens from/to the customer's address. By creating this subscription the user will be notified by Crypto APIs 2.0 when that event occurs. The information is returned per specified address.     Being confirmed means that the transactions are verified by miners and added to the next block. This endpoint refers to **tokens transactions only, not coins**.    {note}To have an operational callback subscription, you need to first verify a domain for the Callback URL. Please see more information on Callbacks [here](https://developers.cryptoapis.io/technical-documentation/general-information/callbacks#callback-url).{/note}    {warning}Crypto APIs will notify the user **only when** the event occurs. There are cases when the specific event doesn't happen at all, or takes a long time to do so. A callback notification **will not** be sent if the event does not or cannot occur, or will take long time to occur.{/warning}

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
from cryptoapis.model.new_confirmed_tokens_transactions_request_body import NewConfirmedTokensTransactionsRequestBody
from cryptoapis.model.invalid_pagination import InvalidPagination
from cryptoapis.model.new_confirmed_tokens_transactions_response import NewConfirmedTokensTransactionsResponse
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
    new_confirmed_tokens_transactions_request_body = NewConfirmedTokensTransactionsRequestBody(
        context="context_example",
        data=NewUnconfirmedTokensTransactionsRequestBodyData(
            item=NewUnconfirmedTokensTransactionsRequestBodyDataItem(
                address="mho4jHBcrNCncKt38trJahXakuaBnS7LK5",
                allow_duplicates=True,
                callback_secret_key="yourSecretKey",
                callback_url="http://example.com",
            ),
        ),
    ) # NewConfirmedTokensTransactionsRequestBody |  (optional)

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
        api_response = api_instance.new_confirmed_tokens_transactions(blockchain, network, context=context, new_confirmed_tokens_transactions_request_body=new_confirmed_tokens_transactions_request_body)
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
 **new_confirmed_tokens_transactions_request_body** | [**NewConfirmedTokensTransactionsRequestBody**](NewConfirmedTokensTransactionsRequestBody.md)|  | [optional]

### Return type

[**NewConfirmedTokensTransactionsResponse**](NewConfirmedTokensTransactionsResponse.md)

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
> NewConfirmedTokensTransactionsAndEachConfirmationResponse new_confirmed_tokens_transactions_and_each_confirmation(blockchain, network)

New confirmed tokens transactions and each confirmation

Through this endpoint customers can create callback subscriptions for a specific event. In this case the event is when there are new incoming or outgoing confirmed transactions for tokens from/to the customer's address with also a response at each confirmation the transaction has received until the specified confirmations limit is reached. By creating this subscription the user will be notified by Crypto APIs 2.0 when that event occurs. The information is returned per specified address.     Being confirmed means that the transactions are verified by miners and added to the next block. This endpoint refers to **tokens transactions only, not coins**.    {note}To have an operational callback subscription, you need to first verify a domain for the Callback URL. Please see more information on Callbacks [here](https://developers.cryptoapis.io/technical-documentation/general-information/callbacks#callback-url).{/note}    {warning}Crypto APIs will notify the user **only when** the event occurs. There are cases when the specific event doesn't happen at all, or takes a long time to do so. A callback notification **will not** be sent if the event does not or cannot occur, or will take long time to occur.{/warning}

### Example

* Api Key Authentication (ApiKey):
```python
import time
import cryptoapis
from cryptoapis.api import create_subscriptions_for_api
from cryptoapis.model.new_confirmed_tokens_transactions_and_each_confirmation_response import NewConfirmedTokensTransactionsAndEachConfirmationResponse
from cryptoapis.model.blockchain_events_callbacks_limit_reached import BlockchainEventsCallbacksLimitReached
from cryptoapis.model.insufficient_credits import InsufficientCredits
from cryptoapis.model.already_exists import AlreadyExists
from cryptoapis.model.invalid_api_key import InvalidApiKey
from cryptoapis.model.invalid_request_body_structure import InvalidRequestBodyStructure
from cryptoapis.model.request_limit_reached import RequestLimitReached
from cryptoapis.model.invalid_pagination import InvalidPagination
from cryptoapis.model.unexpected_server_error import UnexpectedServerError
from cryptoapis.model.unsupported_media_type import UnsupportedMediaType
from cryptoapis.model.new_confirmed_tokens_transactions_and_each_confirmation_request_body import NewConfirmedTokensTransactionsAndEachConfirmationRequestBody
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
    new_confirmed_tokens_transactions_and_each_confirmation_request_body = NewConfirmedTokensTransactionsAndEachConfirmationRequestBody(
        context="context_example",
        data=NewConfirmedTokensTransactionsAndEachConfirmationRequestBodyData(
            item=NewConfirmedTokensTransactionsAndEachConfirmationRequestBodyDataItem(
                address="mho4jHBcrNCncKt38trJahXakuaBnS7LK5",
                allow_duplicates=True,
                callback_secret_key="yourSecretKey",
                callback_url="http://example.com",
                confirmations_count=3,
            ),
        ),
    ) # NewConfirmedTokensTransactionsAndEachConfirmationRequestBody |  (optional)

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
        api_response = api_instance.new_confirmed_tokens_transactions_and_each_confirmation(blockchain, network, context=context, new_confirmed_tokens_transactions_and_each_confirmation_request_body=new_confirmed_tokens_transactions_and_each_confirmation_request_body)
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
 **new_confirmed_tokens_transactions_and_each_confirmation_request_body** | [**NewConfirmedTokensTransactionsAndEachConfirmationRequestBody**](NewConfirmedTokensTransactionsAndEachConfirmationRequestBody.md)|  | [optional]

### Return type

[**NewConfirmedTokensTransactionsAndEachConfirmationResponse**](NewConfirmedTokensTransactionsAndEachConfirmationResponse.md)

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
> NewUnconfirmedCoinsTransactionsResponse new_unconfirmed_coins_transactions(blockchain, network)

New unconfirmed coins transactions

Through this endpoint customers can create callback subscriptions for a specific event. In this case the event is when there are new unconfirmed coins transactions for the user. By creating this subscription the user will be notified by Crypto APIs 2.0 when that event occurs. The information is returned per specified address.    Unconfirmed coins transactions remain in the mempool (memory pool) until they are confirmed by miners and added to the next block. Sometimes spikes in transaction activity can cause delays in confirmations.    {note}To have an operational callback subscription, you need to first verify a domain for the Callback URL. Please see more information on Callbacks [here](https://developers.cryptoapis.io/technical-documentation/general-information/callbacks#callback-url).{/note}    {note}It is also **important to note** that just because pending unconfirmed transactions are in the mempool, **doesn't necessarily** mean they will get confirmed.{/note}    {warning}Crypto APIs will notify the user **only when** the event occurs. There are cases when the specific event doesn't happen at all, or takes a long time to do so. A callback notification **will not** be sent if the event does not or cannot occur, or will take long time to occur.{/warning}

### Example

* Api Key Authentication (ApiKey):
```python
import time
import cryptoapis
from cryptoapis.api import create_subscriptions_for_api
from cryptoapis.model.new_unconfirmed_coins_transactions_request_body import NewUnconfirmedCoinsTransactionsRequestBody
from cryptoapis.model.blockchain_events_callbacks_limit_reached import BlockchainEventsCallbacksLimitReached
from cryptoapis.model.insufficient_credits import InsufficientCredits
from cryptoapis.model.already_exists import AlreadyExists
from cryptoapis.model.invalid_api_key import InvalidApiKey
from cryptoapis.model.new_unconfirmed_coins_transactions_response import NewUnconfirmedCoinsTransactionsResponse
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
    new_unconfirmed_coins_transactions_request_body = NewUnconfirmedCoinsTransactionsRequestBody(
        context="context_example",
        data=NewUnconfirmedCoinsTransactionsRequestBodyData(
            item=NewUnconfirmedCoinsTransactionsRequestBodyDataItem(
                address="mho4jHBcrNCncKt38trJahXakuaBnS7LK5",
                allow_duplicates=True,
                callback_secret_key="yourSecretKey",
                callback_url="http://example.com",
            ),
        ),
    ) # NewUnconfirmedCoinsTransactionsRequestBody |  (optional)

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
        api_response = api_instance.new_unconfirmed_coins_transactions(blockchain, network, context=context, new_unconfirmed_coins_transactions_request_body=new_unconfirmed_coins_transactions_request_body)
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
 **new_unconfirmed_coins_transactions_request_body** | [**NewUnconfirmedCoinsTransactionsRequestBody**](NewUnconfirmedCoinsTransactionsRequestBody.md)|  | [optional]

### Return type

[**NewUnconfirmedCoinsTransactionsResponse**](NewUnconfirmedCoinsTransactionsResponse.md)

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
> NewUnconfirmedTokensTransactionsResponse new_unconfirmed_tokens_transactions(blockchain, network)

New unconfirmed tokens transactions

Through this endpoint customers can create callback subscriptions for a specific event. In this case the event is when there are new unconfirmed tokens transactions for the user. By creating this subscription the user will be notified by Crypto APIs 2.0 when that event occurs. The information is returned per specified address.    Unconfirmed tokens transactions remain in the mempool (memory pool) until they are confirmed by miners and added to the next block. Sometimes spikes in transaction activity can cause delays in confirmations.    {note}To have an operational callback subscription, you need to first verify a domain for the Callback URL. Please see more information on Callbacks [here](https://developers.cryptoapis.io/technical-documentation/general-information/callbacks#callback-url).{/note}    {note}It is also **important to note** that just because pending unconfirmed transactions are in the mempool, **doesn't necessarily** mean they will get confirmed.{/note}    {warning}Crypto APIs will notify the user **only when** the event occurs. There are cases when the specific event doesn't happen at all, or takes a long time to do so. A callback notification **will not** be sent if the event does not or cannot occur, or will take long time to occur.{/warning}

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
from cryptoapis.model.new_unconfirmed_tokens_transactions_response import NewUnconfirmedTokensTransactionsResponse
from cryptoapis.model.invalid_pagination import InvalidPagination
from cryptoapis.model.new_unconfirmed_tokens_transactions_request_body import NewUnconfirmedTokensTransactionsRequestBody
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
    new_unconfirmed_tokens_transactions_request_body = NewUnconfirmedTokensTransactionsRequestBody(
        context="context_example",
        data=NewUnconfirmedTokensTransactionsRequestBodyData(
            item=NewUnconfirmedTokensTransactionsRequestBodyDataItem(
                address="mho4jHBcrNCncKt38trJahXakuaBnS7LK5",
                allow_duplicates=True,
                callback_secret_key="yourSecretKey",
                callback_url="http://example.com",
            ),
        ),
    ) # NewUnconfirmedTokensTransactionsRequestBody |  (optional)

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
        api_response = api_instance.new_unconfirmed_tokens_transactions(blockchain, network, context=context, new_unconfirmed_tokens_transactions_request_body=new_unconfirmed_tokens_transactions_request_body)
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
 **new_unconfirmed_tokens_transactions_request_body** | [**NewUnconfirmedTokensTransactionsRequestBody**](NewUnconfirmedTokensTransactionsRequestBody.md)|  | [optional]

### Return type

[**NewUnconfirmedTokensTransactionsResponse**](NewUnconfirmedTokensTransactionsResponse.md)

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

