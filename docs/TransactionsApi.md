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
> CreateCoinsTransactionFromAddressForWholeAmountR create_coins_transaction_from_address_for_whole_amount(address, blockchain, network, wallet_id, context=context, create_coins_transaction_from_address_for_whole_amount_rb=create_coins_transaction_from_address_for_whole_amount_rb)

Create Coins Transaction From Address For Whole Amount

Through this endpoint customers can create a new transaction from address for **coins** specifically, which will transfer over the entire available amount.

### Example

* Api Key Authentication (ApiKey):
```python
import time
import os
import cryptoapis
from cryptoapis.models.create_coins_transaction_from_address_for_whole_amount_r import CreateCoinsTransactionFromAddressForWholeAmountR
from cryptoapis.models.create_coins_transaction_from_address_for_whole_amount_rb import CreateCoinsTransactionFromAddressForWholeAmountRB
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
    api_instance = cryptoapis.TransactionsApi(api_client)
    address = '0x0902a667d6a3f287835e0a4593cae4167384abc6' # str | Defines the source address.
    blockchain = 'ethereum' # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    network = 'goerli' # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"goerli\" are test networks.
    wallet_id = '629df9dbae857c00073de9c8' # str | Represents the sender's specific and unique Wallet ID of the sender.
    context = 'yourExampleString' # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    create_coins_transaction_from_address_for_whole_amount_rb = cryptoapis.CreateCoinsTransactionFromAddressForWholeAmountRB() # CreateCoinsTransactionFromAddressForWholeAmountRB |  (optional)

    try:
        # Create Coins Transaction From Address For Whole Amount
        api_response = api_instance.create_coins_transaction_from_address_for_whole_amount(address, blockchain, network, wallet_id, context=context, create_coins_transaction_from_address_for_whole_amount_rb=create_coins_transaction_from_address_for_whole_amount_rb)
        print("The response of TransactionsApi->create_coins_transaction_from_address_for_whole_amount:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->create_coins_transaction_from_address_for_whole_amount: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Defines the source address. | 
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. | 
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;goerli\&quot; are test networks. | 
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
> CreateCoinsTransactionRequestFromAddressR create_coins_transaction_request_from_address(address, blockchain, network, wallet_id, context=context, create_coins_transaction_request_from_address_rb=create_coins_transaction_request_from_address_rb)

Create Coins Transaction Request from Address

Through this endpoint users can create a new single transaction request from one address to another.

### Example

* Api Key Authentication (ApiKey):
```python
import time
import os
import cryptoapis
from cryptoapis.models.create_coins_transaction_request_from_address_r import CreateCoinsTransactionRequestFromAddressR
from cryptoapis.models.create_coins_transaction_request_from_address_rb import CreateCoinsTransactionRequestFromAddressRB
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
    api_instance = cryptoapis.TransactionsApi(api_client)
    address = '0x0902a667d6a3f287835e0a4593cae4167384abc6' # str | Defines the specific source address for the transaction. For XRP we also support the X-address format.
    blockchain = 'ethereum' # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    network = 'goerli' # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"goerli\" are test networks.
    wallet_id = '629df9dbae857c00073de9c8' # str | Represents the sender's specific and unique Wallet ID of the sender.
    context = 'yourExampleString' # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    create_coins_transaction_request_from_address_rb = cryptoapis.CreateCoinsTransactionRequestFromAddressRB() # CreateCoinsTransactionRequestFromAddressRB |  (optional)

    try:
        # Create Coins Transaction Request from Address
        api_response = api_instance.create_coins_transaction_request_from_address(address, blockchain, network, wallet_id, context=context, create_coins_transaction_request_from_address_rb=create_coins_transaction_request_from_address_rb)
        print("The response of TransactionsApi->create_coins_transaction_request_from_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->create_coins_transaction_request_from_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Defines the specific source address for the transaction. For XRP we also support the X-address format. | 
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. | 
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;goerli\&quot; are test networks. | 
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
> CreateCoinsTransactionRequestFromWalletR create_coins_transaction_request_from_wallet(blockchain, network, wallet_id, context=context, create_coins_transaction_request_from_wallet_rb=create_coins_transaction_request_from_wallet_rb)

Create Coins Transaction Request from Wallet

Through this endpoint users can create a new transaction request from the entire Wallet instead from just a specific address. This endpoint can generate transactions from multiple to multiple addresses.    {warning}This is available **only** for UTXO-based protocols such as Bitcoin, Bitcoin Cash, Litecoin, etc. It **is not** available for Account-based protocols like Ethereum.{/warning}

### Example

* Api Key Authentication (ApiKey):
```python
import time
import os
import cryptoapis
from cryptoapis.models.create_coins_transaction_request_from_wallet_r import CreateCoinsTransactionRequestFromWalletR
from cryptoapis.models.create_coins_transaction_request_from_wallet_rb import CreateCoinsTransactionRequestFromWalletRB
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
    api_instance = cryptoapis.TransactionsApi(api_client)
    blockchain = 'bitcoin' # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    network = 'testnet' # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"goerli\" are test networks. (default to 'testnet')
    wallet_id = '609e221675d04500068718dc' # str | Represents the sender's specific and unique Wallet ID of the sender.
    context = 'yourExampleString' # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    create_coins_transaction_request_from_wallet_rb = cryptoapis.CreateCoinsTransactionRequestFromWalletRB() # CreateCoinsTransactionRequestFromWalletRB |  (optional)

    try:
        # Create Coins Transaction Request from Wallet
        api_response = api_instance.create_coins_transaction_request_from_wallet(blockchain, network, wallet_id, context=context, create_coins_transaction_request_from_wallet_rb=create_coins_transaction_request_from_wallet_rb)
        print("The response of TransactionsApi->create_coins_transaction_request_from_wallet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->create_coins_transaction_request_from_wallet: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. | 
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;goerli\&quot; are test networks. | [default to &#39;testnet&#39;]
 **wallet_id** | **str**| Represents the sender&#39;s specific and unique Wallet ID of the sender. | 
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
> CreateFungibleTokenTransactionRequestFromAddressWithoutFeePriorityR create_fungible_token_transaction_request_from_address_without_fee_priority(blockchain, network, sender_address, wallet_id, context=context, create_fungible_token_transaction_request_from_address_without_fee_priority_rb=create_fungible_token_transaction_request_from_address_without_fee_priority_rb)

Create Fungible Token Transaction Request From Address Without Fee Priority

Through this endpoint customers can make a single feeless token transaction on the Tron blockchain protocol. TRX transactions burn certain resources called Bandwidth and Energy. Each account has 1500 bandwidth free for use every 24 hours and more can be obtained by staking TRX. The unit price of Energy is 280 SUN and of bandwidth - 1000 SUN. If the resources are insufficient, TRX will be burned to pay for them.

### Example

* Api Key Authentication (ApiKey):
```python
import time
import os
import cryptoapis
from cryptoapis.models.create_fungible_token_transaction_request_from_address_without_fee_priority_r import CreateFungibleTokenTransactionRequestFromAddressWithoutFeePriorityR
from cryptoapis.models.create_fungible_token_transaction_request_from_address_without_fee_priority_rb import CreateFungibleTokenTransactionRequestFromAddressWithoutFeePriorityRB
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
    api_instance = cryptoapis.TransactionsApi(api_client)
    blockchain = 'tron' # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    network = 'nile' # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"goerli\" are test networks.
    sender_address = 'TX8VXpdEoNNrKeEuNTfbEXfa9eZivcyUwD' # str | Defines the specific source address for the transaction.
    wallet_id = '62b9b5c3b97f4b0008092714' # str | Defines the unique ID of the Wallet.
    context = 'yourExampleString' # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    create_fungible_token_transaction_request_from_address_without_fee_priority_rb = cryptoapis.CreateFungibleTokenTransactionRequestFromAddressWithoutFeePriorityRB() # CreateFungibleTokenTransactionRequestFromAddressWithoutFeePriorityRB |  (optional)

    try:
        # Create Fungible Token Transaction Request From Address Without Fee Priority
        api_response = api_instance.create_fungible_token_transaction_request_from_address_without_fee_priority(blockchain, network, sender_address, wallet_id, context=context, create_fungible_token_transaction_request_from_address_without_fee_priority_rb=create_fungible_token_transaction_request_from_address_without_fee_priority_rb)
        print("The response of TransactionsApi->create_fungible_token_transaction_request_from_address_without_fee_priority:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->create_fungible_token_transaction_request_from_address_without_fee_priority: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. | 
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;goerli\&quot; are test networks. | 
 **sender_address** | **str**| Defines the specific source address for the transaction. | 
 **wallet_id** | **str**| Defines the unique ID of the Wallet. | 
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
> CreateFungibleTokensTransactionRequestFromAddressR create_fungible_tokens_transaction_request_from_address(blockchain, network, sender_address, wallet_id, context=context, create_fungible_tokens_transaction_request_from_address_rb=create_fungible_tokens_transaction_request_from_address_rb)

Create Fungible Tokens Transaction Request from Address

Through this endpoint users can make a single token transaction.    {note}To have an operational callback subscription, you need to first verify a domain for the Callback URL. Please see more information on Callbacks [here](https://developers.cryptoapis.io/technical-documentation/general-information/callbacks#callback-url).{/note}    {warning}Crypto APIs will notify the user **only when** the event occurs. There are cases when the specific event doesn't happen at all, or takes a long time to do so. A callback notification **will not** be sent if the event does not or cannot occur, or will take long time to occur.{/warning}

### Example

* Api Key Authentication (ApiKey):
```python
import time
import os
import cryptoapis
from cryptoapis.models.create_fungible_tokens_transaction_request_from_address_r import CreateFungibleTokensTransactionRequestFromAddressR
from cryptoapis.models.create_fungible_tokens_transaction_request_from_address_rb import CreateFungibleTokensTransactionRequestFromAddressRB
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
    api_instance = cryptoapis.TransactionsApi(api_client)
    blockchain = 'ethereum' # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    network = 'goerli' # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"goerli\" are test networks.
    sender_address = '0x0902a667d6a3f287835e0a4593cae4167384abc6' # str | Defines the specific source address for the transaction.
    wallet_id = '609e221675d04500068718dc' # str | Defines the unique ID of the Wallet.
    context = 'yourExampleString' # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    create_fungible_tokens_transaction_request_from_address_rb = cryptoapis.CreateFungibleTokensTransactionRequestFromAddressRB() # CreateFungibleTokensTransactionRequestFromAddressRB |  (optional)

    try:
        # Create Fungible Tokens Transaction Request from Address
        api_response = api_instance.create_fungible_tokens_transaction_request_from_address(blockchain, network, sender_address, wallet_id, context=context, create_fungible_tokens_transaction_request_from_address_rb=create_fungible_tokens_transaction_request_from_address_rb)
        print("The response of TransactionsApi->create_fungible_tokens_transaction_request_from_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->create_fungible_tokens_transaction_request_from_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. | 
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;goerli\&quot; are test networks. | 
 **sender_address** | **str**| Defines the specific source address for the transaction. | 
 **wallet_id** | **str**| Defines the unique ID of the Wallet. | 
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
> CreateSingleTransactionRequestFromAddressWithoutFeePriorityR create_single_transaction_request_from_address_without_fee_priority(address, blockchain, network, wallet_id, context=context, create_single_transaction_request_from_address_without_fee_priority_rb=create_single_transaction_request_from_address_without_fee_priority_rb)

Create Single Transaction Request From Address Without Fee Priority

Through this endpoint users can create a new single transaction request from one address to another. The difference between this endpoint and \"Create Coins Transaction Request from Address\"  is that for Tron blockchain there is no Fee Priority that defines how fast a transaction can be mined.

### Example

* Api Key Authentication (ApiKey):
```python
import time
import os
import cryptoapis
from cryptoapis.models.create_single_transaction_request_from_address_without_fee_priority_r import CreateSingleTransactionRequestFromAddressWithoutFeePriorityR
from cryptoapis.models.create_single_transaction_request_from_address_without_fee_priority_rb import CreateSingleTransactionRequestFromAddressWithoutFeePriorityRB
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
    api_instance = cryptoapis.TransactionsApi(api_client)
    address = 'TX8VXpdEoNNrKeEuNTfbEXfa9eZivcyUwD' # str | Defines the specific source address for the transaction.
    blockchain = 'tron' # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    network = 'nile' # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"goerli\" are test networks.
    wallet_id = '62b9b5c3b97f4b0008092714' # str | Represents the sender's specific and unique Wallet ID of the sender.
    context = 'yourExampleString' # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    create_single_transaction_request_from_address_without_fee_priority_rb = cryptoapis.CreateSingleTransactionRequestFromAddressWithoutFeePriorityRB() # CreateSingleTransactionRequestFromAddressWithoutFeePriorityRB |  (optional)

    try:
        # Create Single Transaction Request From Address Without Fee Priority
        api_response = api_instance.create_single_transaction_request_from_address_without_fee_priority(address, blockchain, network, wallet_id, context=context, create_single_transaction_request_from_address_without_fee_priority_rb=create_single_transaction_request_from_address_without_fee_priority_rb)
        print("The response of TransactionsApi->create_single_transaction_request_from_address_without_fee_priority:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->create_single_transaction_request_from_address_without_fee_priority: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Defines the specific source address for the transaction. | 
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. | 
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;goerli\&quot; are test networks. | 
 **wallet_id** | **str**| Represents the sender&#39;s specific and unique Wallet ID of the sender. | 
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

