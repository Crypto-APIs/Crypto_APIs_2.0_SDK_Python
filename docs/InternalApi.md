# cryptoapis.InternalApi

All URIs are relative to *https://rest.cryptoapis.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_internal_transaction_by_transaction_hash_and_operation_id**](InternalApi.md#get_internal_transaction_by_transaction_hash_and_operation_id) | **GET** /blockchain-data/{blockchain}/{network}/transactions/{transactionHash}/internal/{operationId} | Get Internal Transaction by Transaction Hash and Operation Id
[**list_internal_transaction_details_by_transaction_hash**](InternalApi.md#list_internal_transaction_details_by_transaction_hash) | **GET** /blockchain-data/{blockchain}/{network}/transactions/{transactionHash}/internal | List Internal Transaction Details by Transaction Hash
[**list_internal_transactions_by_address**](InternalApi.md#list_internal_transactions_by_address) | **GET** /blockchain-data/{blockchain}/{network}/addresses/{address}/internal | List Internal Transactions By Address


# **get_internal_transaction_by_transaction_hash_and_operation_id**
> GetInternalTransactionByTransactionHashAndOperationIdR get_internal_transaction_by_transaction_hash_and_operation_id(blockchain, network, operation_id, transaction_hash)

Get Internal Transaction by Transaction Hash and Operation Id

Through this endpoint customers can obtain detailed information about a specific Internal Transaction by using the attributes `transactionHash`  (the parent transaction's Hash) and `operationId` (type trace address).    An internal transaction is the result of a smart contract being triggered by an EOA or a subsequent contract call.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import internal_api
from cryptoapis.model.get_internal_transaction_by_transaction_hash_and_operation_id400_response import GetInternalTransactionByTransactionHashAndOperationId400Response
from cryptoapis.model.get_address_details402_response import GetAddressDetails402Response
from cryptoapis.model.get_internal_transaction_by_transaction_hash_and_operation_id403_response import GetInternalTransactionByTransactionHashAndOperationId403Response
from cryptoapis.model.get_address_details500_response import GetAddressDetails500Response
from cryptoapis.model.get_address_details415_response import GetAddressDetails415Response
from cryptoapis.model.get_address_details422_response import GetAddressDetails422Response
from cryptoapis.model.get_internal_transaction_by_transaction_hash_and_operation_id401_response import GetInternalTransactionByTransactionHashAndOperationId401Response
from cryptoapis.model.get_address_details409_response import GetAddressDetails409Response
from cryptoapis.model.get_address_details429_response import GetAddressDetails429Response
from cryptoapis.model.get_internal_transaction_by_transaction_hash_and_operation_id404_response import GetInternalTransactionByTransactionHashAndOperationId404Response
from cryptoapis.model.get_internal_transaction_by_transaction_hash_and_operation_id_r import GetInternalTransactionByTransactionHashAndOperationIdR
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
    api_instance = internal_api.InternalApi(api_client)
    blockchain = "ethereum" # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    network = "mainnet" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    operation_id = "call_4" # str | Represents the unique internal transaction ID in regards to the parent transaction (type trace address).
    transaction_hash = "0x92bb77e16444e0417c8b50dfab68e89c7ad27d4140a766c3bbd4d0ac195f12fc" # str | String identifier of the parent transaction of the internal transaction represented in CryptoAPIs.
    context = "yourExampleString" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Internal Transaction by Transaction Hash and Operation Id
        api_response = api_instance.get_internal_transaction_by_transaction_hash_and_operation_id(blockchain, network, operation_id, transaction_hash)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling InternalApi->get_internal_transaction_by_transaction_hash_and_operation_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Internal Transaction by Transaction Hash and Operation Id
        api_response = api_instance.get_internal_transaction_by_transaction_hash_and_operation_id(blockchain, network, operation_id, transaction_hash, context=context)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling InternalApi->get_internal_transaction_by_transaction_hash_and_operation_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. |
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. |
 **operation_id** | **str**| Represents the unique internal transaction ID in regards to the parent transaction (type trace address). |
 **transaction_hash** | **str**| String identifier of the parent transaction of the internal transaction represented in CryptoAPIs. |
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]

### Return type

[**GetInternalTransactionByTransactionHashAndOperationIdR**](GetInternalTransactionByTransactionHashAndOperationIdR.md)

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
**404** | The specified internal transaction has not been found on the specific blockchain. |  -  |
**409** | The data provided seems to be invalid. |  -  |
**415** | The selected Media Type is unavailable. The Content-Type header should be &#39;application/json&#39;. |  -  |
**422** | Your request body for POST requests must have a structure of { data: { item: [...properties] } } |  -  |
**429** | The request limit has been reached. There can be maximum {requests} requests per {seconds} second(s) made. Please contact our team via email if you need more or upgrade your plan. |  -  |
**500** | An unexpected server error has occurred, we are working to fix this. Please try again later and in case it occurs again please report it to our team via email. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_internal_transaction_details_by_transaction_hash**
> ListInternalTransactionDetailsByTransactionHashR list_internal_transaction_details_by_transaction_hash(blockchain, network, transaction_hash)

List Internal Transaction Details by Transaction Hash

Through this endpoint customers can list internal transactions along with their details by a specific attribute `transactionHash`, which is the parent transaction's Hash.    An internal transaction is the result of a smart contract being triggered by an EOA or a subsequent contract call.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import internal_api
from cryptoapis.model.get_address_details402_response import GetAddressDetails402Response
from cryptoapis.model.list_internal_transaction_details_by_transaction_hash401_response import ListInternalTransactionDetailsByTransactionHash401Response
from cryptoapis.model.list_internal_transaction_details_by_transaction_hash403_response import ListInternalTransactionDetailsByTransactionHash403Response
from cryptoapis.model.get_address_details500_response import GetAddressDetails500Response
from cryptoapis.model.get_address_details415_response import GetAddressDetails415Response
from cryptoapis.model.get_address_details422_response import GetAddressDetails422Response
from cryptoapis.model.list_internal_transaction_details_by_transaction_hash400_response import ListInternalTransactionDetailsByTransactionHash400Response
from cryptoapis.model.get_address_details409_response import GetAddressDetails409Response
from cryptoapis.model.get_address_details429_response import GetAddressDetails429Response
from cryptoapis.model.list_internal_transaction_details_by_transaction_hash_r import ListInternalTransactionDetailsByTransactionHashR
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
    api_instance = internal_api.InternalApi(api_client)
    blockchain = "ethereum" # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    network = "mainnet" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    transaction_hash = "0x5d4ea0471b70de09fa3d6a4bc32f703ec44483bffa4d6169fa0a36c6a1dc108a" # str | String identifier of the parent transaction of the internal transaction represented in CryptoAPIs.
    context = "yourExampleString" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    limit = 50 # int | Defines how many items should be returned in the response per page basis. (optional) if omitted the server will use the default value of 50
    offset = 0 # int | The starting index of the response items, i.e. where the response should start listing the returned items. (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    try:
        # List Internal Transaction Details by Transaction Hash
        api_response = api_instance.list_internal_transaction_details_by_transaction_hash(blockchain, network, transaction_hash)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling InternalApi->list_internal_transaction_details_by_transaction_hash: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Internal Transaction Details by Transaction Hash
        api_response = api_instance.list_internal_transaction_details_by_transaction_hash(blockchain, network, transaction_hash, context=context, limit=limit, offset=offset)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling InternalApi->list_internal_transaction_details_by_transaction_hash: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. |
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. |
 **transaction_hash** | **str**| String identifier of the parent transaction of the internal transaction represented in CryptoAPIs. |
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]
 **limit** | **int**| Defines how many items should be returned in the response per page basis. | [optional] if omitted the server will use the default value of 50
 **offset** | **int**| The starting index of the response items, i.e. where the response should start listing the returned items. | [optional] if omitted the server will use the default value of 0

### Return type

[**ListInternalTransactionDetailsByTransactionHashR**](ListInternalTransactionDetailsByTransactionHashR.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request has been sussessful. |  -  |
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

# **list_internal_transactions_by_address**
> ListInternalTransactionsByAddressR list_internal_transactions_by_address(blockchain, network, address)

List Internal Transactions By Address

Through this endpoint customers can list internal transactions by the `address` attribute.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import internal_api
from cryptoapis.model.list_internal_transactions_by_address403_response import ListInternalTransactionsByAddress403Response
from cryptoapis.model.get_address_details402_response import GetAddressDetails402Response
from cryptoapis.model.get_address_details500_response import GetAddressDetails500Response
from cryptoapis.model.get_address_details415_response import GetAddressDetails415Response
from cryptoapis.model.get_address_details422_response import GetAddressDetails422Response
from cryptoapis.model.get_address_details409_response import GetAddressDetails409Response
from cryptoapis.model.list_internal_transactions_by_address400_response import ListInternalTransactionsByAddress400Response
from cryptoapis.model.get_address_details429_response import GetAddressDetails429Response
from cryptoapis.model.list_internal_transactions_by_address_r import ListInternalTransactionsByAddressR
from cryptoapis.model.list_internal_transactions_by_address401_response import ListInternalTransactionsByAddress401Response
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
    api_instance = internal_api.InternalApi(api_client)
    blockchain = "ethereum" # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    network = "ropsten" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    address = "0xc8fe2ceac93ad50e496b497357ae5385192dd28d" # str | String identifier of the address document represented in CryptoAPIs
    context = "yourExampleString" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    limit = 50 # int | Defines how many items should be returned in the response per page basis. (optional) if omitted the server will use the default value of 50
    offset = 0 # int | The starting index of the response items, i.e. where the response should start listing the returned items. (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    try:
        # List Internal Transactions By Address
        api_response = api_instance.list_internal_transactions_by_address(blockchain, network, address)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling InternalApi->list_internal_transactions_by_address: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Internal Transactions By Address
        api_response = api_instance.list_internal_transactions_by_address(blockchain, network, address, context=context, limit=limit, offset=offset)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling InternalApi->list_internal_transactions_by_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. |
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. |
 **address** | **str**| String identifier of the address document represented in CryptoAPIs |
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]
 **limit** | **int**| Defines how many items should be returned in the response per page basis. | [optional] if omitted the server will use the default value of 50
 **offset** | **int**| The starting index of the response items, i.e. where the response should start listing the returned items. | [optional] if omitted the server will use the default value of 0

### Return type

[**ListInternalTransactionsByAddressR**](ListInternalTransactionsByAddressR.md)

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

