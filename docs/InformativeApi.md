# cryptoapis.InformativeApi

All URIs are relative to *https://rest.cryptoapis.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_transaction_request_details**](InformativeApi.md#get_transaction_request_details) | **GET** /wallet-as-a-service/transactionRequests/{transactionRequestId} | Get Transaction Request Details
[**get_wallet_asset_details**](InformativeApi.md#get_wallet_asset_details) | **GET** /wallet-as-a-service/wallets/{walletId}/{blockchain}/{network} | Get Wallet Asset Details
[**get_wallet_transaction_details_by_transaction_id**](InformativeApi.md#get_wallet_transaction_details_by_transaction_id) | **GET** /wallet-as-a-service/wallets/{blockchain}/{network}/transactions/{transactionId} | Get Wallet Transaction Details By Transaction ID
[**list_deposit_addresses**](InformativeApi.md#list_deposit_addresses) | **GET** /wallet-as-a-service/wallets/{walletId}/{blockchain}/{network}/addresses | List Deposit Addresses
[**list_supported_tokens**](InformativeApi.md#list_supported_tokens) | **GET** /wallet-as-a-service/info/{blockchain}/{network}/supported-tokens | List Supported Tokens
[**list_wallet_transactions**](InformativeApi.md#list_wallet_transactions) | **GET** /wallet-as-a-service/wallets/{walletId}/{blockchain}/{network}/transactions | List Wallet Transactions


# **get_transaction_request_details**
> GetTransactionRequestDetailsR get_transaction_request_details(transaction_request_id)

Get Transaction Request Details

Through this endpoint customers can obtain details on transaction request.    {note}This regards **transaction requests**, which is not to be confused with **transactions**. Transaction requests may not be approved due to any reason, hence a transaction may not occur.{/note}

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import informative_api
from cryptoapis.model.inline_response429 import InlineResponse429
from cryptoapis.model.inline_response422 import InlineResponse422
from cryptoapis.model.inline_response409 import InlineResponse409
from cryptoapis.model.inline_response40041 import InlineResponse40041
from cryptoapis.model.inline_response402 import InlineResponse402
from cryptoapis.model.inline_response500 import InlineResponse500
from cryptoapis.model.inline_response40141 import InlineResponse40141
from cryptoapis.model.inline_response415 import InlineResponse415
from cryptoapis.model.get_transaction_request_details_r import GetTransactionRequestDetailsR
from cryptoapis.model.inline_response40341 import InlineResponse40341
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
    api_instance = informative_api.InformativeApi(api_client)
    transaction_request_id = "6115126693397c0006f78eb4" # str | Represents the unique ID of the transaction request.
    context = "context_example" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Transaction Request Details
        api_response = api_instance.get_transaction_request_details(transaction_request_id)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling InformativeApi->get_transaction_request_details: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Transaction Request Details
        api_response = api_instance.get_transaction_request_details(transaction_request_id, context=context)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling InformativeApi->get_transaction_request_details: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_request_id** | **str**| Represents the unique ID of the transaction request. |
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]

### Return type

[**GetTransactionRequestDetailsR**](GetTransactionRequestDetailsR.md)

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

# **get_wallet_asset_details**
> GetWalletAssetDetailsR get_wallet_asset_details(blockchain, network, wallet_id)

Get Wallet Asset Details

Through this endpoint customers can obtain details about a specific Wallet/Vault.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import informative_api
from cryptoapis.model.inline_response40035 import InlineResponse40035
from cryptoapis.model.inline_response429 import InlineResponse429
from cryptoapis.model.inline_response422 import InlineResponse422
from cryptoapis.model.inline_response40135 import InlineResponse40135
from cryptoapis.model.inline_response409 import InlineResponse409
from cryptoapis.model.inline_response402 import InlineResponse402
from cryptoapis.model.inline_response4041 import InlineResponse4041
from cryptoapis.model.inline_response500 import InlineResponse500
from cryptoapis.model.inline_response415 import InlineResponse415
from cryptoapis.model.inline_response40335 import InlineResponse40335
from cryptoapis.model.get_wallet_asset_details_r import GetWalletAssetDetailsR
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
    api_instance = informative_api.InformativeApi(api_client)
    blockchain = "bitcoin" # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    network = "testnet" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    wallet_id = "60c9d9921c38030006675ff6" # str | Defines the unique ID of the Wallet.
    context = "context_example" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Wallet Asset Details
        api_response = api_instance.get_wallet_asset_details(blockchain, network, wallet_id)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling InformativeApi->get_wallet_asset_details: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Wallet Asset Details
        api_response = api_instance.get_wallet_asset_details(blockchain, network, wallet_id, context=context)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling InformativeApi->get_wallet_asset_details: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. |
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. |
 **wallet_id** | **str**| Defines the unique ID of the Wallet. |
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]

### Return type

[**GetWalletAssetDetailsR**](GetWalletAssetDetailsR.md)

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
**404** | The specified resource has not been found. |  -  |
**409** | The data provided seems to be invalid. |  -  |
**415** | The selected Media Type is unavailable. The Content-Type header should be &#39;application/json&#39;. |  -  |
**422** | Your request body for POST requests must have a structure of { data: { item: [...properties] } } |  -  |
**429** | The request limit has been reached. There can be maximum {requests} requests per {seconds} second(s) made. Please contact our team via email if you need more or upgrade your plan. |  -  |
**500** | An unexpected server error has occurred, we are working to fix this. Please try again later and in case it occurs again please report it to our team via email. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wallet_transaction_details_by_transaction_id**
> GetWalletTransactionDetailsByTransactionIDR get_wallet_transaction_details_by_transaction_id(blockchain, network, transaction_id)

Get Wallet Transaction Details By Transaction ID

Through this endpoint users can obtain Wallet transaction information by providing a `transactionId`. Customers can receive information only for a transaction that has been made from their own wallet.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import informative_api
from cryptoapis.model.inline_response429 import InlineResponse429
from cryptoapis.model.inline_response40146 import InlineResponse40146
from cryptoapis.model.inline_response422 import InlineResponse422
from cryptoapis.model.inline_response409 import InlineResponse409
from cryptoapis.model.inline_response402 import InlineResponse402
from cryptoapis.model.inline_response4041 import InlineResponse4041
from cryptoapis.model.inline_response500 import InlineResponse500
from cryptoapis.model.inline_response415 import InlineResponse415
from cryptoapis.model.inline_response40346 import InlineResponse40346
from cryptoapis.model.get_wallet_transaction_details_by_transaction_idr import GetWalletTransactionDetailsByTransactionIDR
from cryptoapis.model.inline_response40046 import InlineResponse40046
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
    api_instance = informative_api.InformativeApi(api_client)
    blockchain = "bitcoin" # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    network = "testnet" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    transaction_id = "3e081861494aed897e589cdeab5d9e628d985e571ed1c19896d1aa698cce9d80" # str | Represents the unique identifier of a transaction, i.e. it could be `transactionId` in UTXO-based protocols like Bitcoin, and transaction `hash` in Ethereum blockchain.
    context = "context_example" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Wallet Transaction Details By Transaction ID
        api_response = api_instance.get_wallet_transaction_details_by_transaction_id(blockchain, network, transaction_id)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling InformativeApi->get_wallet_transaction_details_by_transaction_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Wallet Transaction Details By Transaction ID
        api_response = api_instance.get_wallet_transaction_details_by_transaction_id(blockchain, network, transaction_id, context=context)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling InformativeApi->get_wallet_transaction_details_by_transaction_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. |
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. |
 **transaction_id** | **str**| Represents the unique identifier of a transaction, i.e. it could be &#x60;transactionId&#x60; in UTXO-based protocols like Bitcoin, and transaction &#x60;hash&#x60; in Ethereum blockchain. |
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]

### Return type

[**GetWalletTransactionDetailsByTransactionIDR**](GetWalletTransactionDetailsByTransactionIDR.md)

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
**404** | The specified resource has not been found. |  -  |
**409** | The data provided seems to be invalid. |  -  |
**415** | The selected Media Type is unavailable. The Content-Type header should be &#39;application/json&#39;. |  -  |
**422** | Your request body for POST requests must have a structure of { data: { item: [...properties] } } |  -  |
**429** | The request limit has been reached. There can be maximum {requests} requests per {seconds} second(s) made. Please contact our team via email if you need more or upgrade your plan. |  -  |
**500** | An unexpected server error has occurred, we are working to fix this. Please try again later and in case it occurs again please report it to our team via email. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_deposit_addresses**
> ListDepositAddressesR list_deposit_addresses(blockchain, network, wallet_id)

List Deposit Addresses

Through this endpoint customers can pull a list of Deposit/Receiving Addresses they have already generated.    {note}Please note that listing data from the same type will apply pagination on the results.{/note}

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import informative_api
from cryptoapis.model.inline_response429 import InlineResponse429
from cryptoapis.model.list_deposit_addresses_r import ListDepositAddressesR
from cryptoapis.model.inline_response422 import InlineResponse422
from cryptoapis.model.inline_response409 import InlineResponse409
from cryptoapis.model.inline_response402 import InlineResponse402
from cryptoapis.model.inline_response4041 import InlineResponse4041
from cryptoapis.model.inline_response500 import InlineResponse500
from cryptoapis.model.inline_response415 import InlineResponse415
from cryptoapis.model.inline_response4037 import InlineResponse4037
from cryptoapis.model.inline_response4017 import InlineResponse4017
from cryptoapis.model.inline_response4007 import InlineResponse4007
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
    api_instance = informative_api.InformativeApi(api_client)
    blockchain = "bitcoin" # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    network = "testnet" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    wallet_id = "60c9d9921c38030006675ff6" # str | Represents the unique ID of the specific Wallet.
    context = "context_example" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List Deposit Addresses
        api_response = api_instance.list_deposit_addresses(blockchain, network, wallet_id)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling InformativeApi->list_deposit_addresses: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Deposit Addresses
        api_response = api_instance.list_deposit_addresses(blockchain, network, wallet_id, context=context)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling InformativeApi->list_deposit_addresses: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. |
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. |
 **wallet_id** | **str**| Represents the unique ID of the specific Wallet. |
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]

### Return type

[**ListDepositAddressesR**](ListDepositAddressesR.md)

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
**404** | The specified resource has not been found. |  -  |
**409** | The data provided seems to be invalid. |  -  |
**415** | The selected Media Type is unavailable. The Content-Type header should be &#39;application/json&#39;. |  -  |
**422** | Your request body for POST requests must have a structure of { data: { item: [...properties] } } |  -  |
**429** | The request limit has been reached. There can be maximum {requests} requests per {seconds} second(s) made. Please contact our team via email if you need more or upgrade your plan. |  -  |
**500** | An unexpected server error has occurred, we are working to fix this. Please try again later and in case it occurs again please report it to our team via email. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_supported_tokens**
> ListSupportedTokensR list_supported_tokens(blockchain, network)

List Supported Tokens

Through this endpoint customers can obtain information on multiple tokens at once.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import informative_api
from cryptoapis.model.inline_response429 import InlineResponse429
from cryptoapis.model.inline_response40034 import InlineResponse40034
from cryptoapis.model.inline_response422 import InlineResponse422
from cryptoapis.model.inline_response409 import InlineResponse409
from cryptoapis.model.inline_response40134 import InlineResponse40134
from cryptoapis.model.inline_response402 import InlineResponse402
from cryptoapis.model.list_supported_tokens_r import ListSupportedTokensR
from cryptoapis.model.inline_response500 import InlineResponse500
from cryptoapis.model.inline_response415 import InlineResponse415
from cryptoapis.model.inline_response40334 import InlineResponse40334
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
    api_instance = informative_api.InformativeApi(api_client)
    blockchain = "ethereum" # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    network = "ropsten" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    context = "context_example" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    limit = 50 # int | Defines how many items should be returned in the response per page basis. (optional) if omitted the server will use the default value of 50
    offset = 10 # int | The starting index of the response items, i.e. where the response should start listing the returned items. (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    try:
        # List Supported Tokens
        api_response = api_instance.list_supported_tokens(blockchain, network)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling InformativeApi->list_supported_tokens: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Supported Tokens
        api_response = api_instance.list_supported_tokens(blockchain, network, context=context, limit=limit, offset=offset)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling InformativeApi->list_supported_tokens: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. |
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. |
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]
 **limit** | **int**| Defines how many items should be returned in the response per page basis. | [optional] if omitted the server will use the default value of 50
 **offset** | **int**| The starting index of the response items, i.e. where the response should start listing the returned items. | [optional] if omitted the server will use the default value of 0

### Return type

[**ListSupportedTokensR**](ListSupportedTokensR.md)

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

# **list_wallet_transactions**
> ListWalletTransactionsR list_wallet_transactions(blockchain, network, wallet_id)

List Wallet Transactions

Through this endpoint customers can list Transactions from and to their Wallet. The data returned will include `transactionId`, `direction` of the transaction - incoming or outgoing, `amount` and more.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import informative_api
from cryptoapis.model.inline_response40045 import InlineResponse40045
from cryptoapis.model.inline_response429 import InlineResponse429
from cryptoapis.model.inline_response422 import InlineResponse422
from cryptoapis.model.list_wallet_transactions_r import ListWalletTransactionsR
from cryptoapis.model.inline_response40145 import InlineResponse40145
from cryptoapis.model.inline_response409 import InlineResponse409
from cryptoapis.model.inline_response402 import InlineResponse402
from cryptoapis.model.inline_response4041 import InlineResponse4041
from cryptoapis.model.inline_response500 import InlineResponse500
from cryptoapis.model.inline_response415 import InlineResponse415
from cryptoapis.model.inline_response40345 import InlineResponse40345
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
    api_instance = informative_api.InformativeApi(api_client)
    blockchain = "ethereum" # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    network = "ropsten" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    wallet_id = "60c9d9921c38030006675ff6" # str | Represents the unique ID of the specific Wallet.
    context = "context_example" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    limit = 50 # int | Defines how many items should be returned in the response per page basis. (optional) if omitted the server will use the default value of 50
    offset = 0 # int | The starting index of the response items, i.e. where the response should start listing the returned items. (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    try:
        # List Wallet Transactions
        api_response = api_instance.list_wallet_transactions(blockchain, network, wallet_id)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling InformativeApi->list_wallet_transactions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Wallet Transactions
        api_response = api_instance.list_wallet_transactions(blockchain, network, wallet_id, context=context, limit=limit, offset=offset)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling InformativeApi->list_wallet_transactions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. |
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. |
 **wallet_id** | **str**| Represents the unique ID of the specific Wallet. |
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]
 **limit** | **int**| Defines how many items should be returned in the response per page basis. | [optional] if omitted the server will use the default value of 50
 **offset** | **int**| The starting index of the response items, i.e. where the response should start listing the returned items. | [optional] if omitted the server will use the default value of 0

### Return type

[**ListWalletTransactionsR**](ListWalletTransactionsR.md)

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
**404** | The specified resource has not been found. |  -  |
**409** | The data provided seems to be invalid. |  -  |
**415** | The selected Media Type is unavailable. The Content-Type header should be &#39;application/json&#39;. |  -  |
**422** | Your request body for POST requests must have a structure of { data: { item: [...properties] } } |  -  |
**429** | The request limit has been reached. There can be maximum {requests} requests per {seconds} second(s) made. Please contact our team via email if you need more or upgrade your plan. |  -  |
**500** | An unexpected server error has occurred, we are working to fix this. Please try again later and in case it occurs again please report it to our team via email. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

