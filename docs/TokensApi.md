# cryptoapis.TokensApi

All URIs are relative to *https://rest.cryptoapis.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_token_details_by_contract_address**](TokensApi.md#get_token_details_by_contract_address) | **GET** /blockchain-data/{blockchain}/{network}/addresses/{contractAddress}/contract | Get Token Details by Contract Address
[**list_confirmed_tokens_transfers_by_address**](TokensApi.md#list_confirmed_tokens_transfers_by_address) | **GET** /blockchain-data/{blockchain}/{network}/addresses/{address}/tokens-transfers | List Confirmed Tokens Transfers By Address
[**list_tokens_by_address**](TokensApi.md#list_tokens_by_address) | **GET** /blockchain-data/{blockchain}/{network}/addresses/{address}/tokens | List Tokens By Address
[**list_tokens_transfers_by_transaction_hash**](TokensApi.md#list_tokens_transfers_by_transaction_hash) | **GET** /blockchain-data/{blockchain}/{network}/transactions/{transactionHash}/tokens-transfers | List Tokens Transfers By Transaction Hash
[**list_unconfirmed_tokens_transfers_by_address**](TokensApi.md#list_unconfirmed_tokens_transfers_by_address) | **GET** /blockchain-data/{blockchain}/{network}/addresses/{address}/tokens-transfers-unconfirmed | List Unconfirmed Tokens Transfers By Address


# **get_token_details_by_contract_address**
> GetTokenDetailsByContractAddressR get_token_details_by_contract_address(blockchain, network, contract_address, context=context)

Get Token Details by Contract Address

Though this endpoint customers can obtain information about token details. This can be done by providing the `contact address` parameter.    {note}This address is **not** the same as the smart contract creator address.{/note}

### Example

* Api Key Authentication (ApiKey):
```python
import time
import os
import cryptoapis
from cryptoapis.models.get_token_details_by_contract_address_r import GetTokenDetailsByContractAddressR
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
    api_instance = cryptoapis.TokensApi(api_client)
    blockchain = 'ethereum' # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    network = 'goerli' # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"goerli\" are test networks.
    contract_address = '0x534bD102153EF199abAe8296a2FaE4599fC44Cdc' # str | Defines the specific address of the contract.
    context = 'yourExampleString' # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)

    try:
        # Get Token Details by Contract Address
        api_response = api_instance.get_token_details_by_contract_address(blockchain, network, contract_address, context=context)
        print("The response of TokensApi->get_token_details_by_contract_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokensApi->get_token_details_by_contract_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. | 
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;goerli\&quot; are test networks. | 
 **contract_address** | **str**| Defines the specific address of the contract. | 
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional] 

### Return type

[**GetTokenDetailsByContractAddressR**](GetTokenDetailsByContractAddressR.md)

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

# **list_confirmed_tokens_transfers_by_address**
> ListConfirmedTokensTransfersByAddressR list_confirmed_tokens_transfers_by_address(blockchain, network, address, context=context, limit=limit, offset=offset)

List Confirmed Tokens Transfers By Address

Through this endpoint customers can obtain a list with **confirmed** token transfers by the `address` attribute. Token transfers may include information such as addresses of the sender and recipient, token name, token symbol, etc.    {note}This refers only to transfers done for **confirmed tokens** not coins.{/note}

### Example

* Api Key Authentication (ApiKey):
```python
import time
import os
import cryptoapis
from cryptoapis.models.list_confirmed_tokens_transfers_by_address_r import ListConfirmedTokensTransfersByAddressR
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
    api_instance = cryptoapis.TokensApi(api_client)
    blockchain = 'ethereum' # str | Represents the specific blockchain protocol name, e.g. Ethereum, Ethereum Classic, etc.
    network = 'goerli' # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"goerli\" are test networks.
    address = '0x0902a667d6a3f287835e0a4593cae4167384abc6' # str | Represents the public address, which is a compressed and shortened form of a public key.
    context = 'yourExampleString' # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    limit = 50 # int | Defines how many items should be returned in the response per page basis. (optional) (default to 50)
    offset = 0 # int | The starting index of the response items, i.e. where the response should start listing the returned items. (optional) (default to 0)

    try:
        # List Confirmed Tokens Transfers By Address
        api_response = api_instance.list_confirmed_tokens_transfers_by_address(blockchain, network, address, context=context, limit=limit, offset=offset)
        print("The response of TokensApi->list_confirmed_tokens_transfers_by_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokensApi->list_confirmed_tokens_transfers_by_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Ethereum Classic, etc. | 
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;goerli\&quot; are test networks. | 
 **address** | **str**| Represents the public address, which is a compressed and shortened form of a public key. | 
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional] 
 **limit** | **int**| Defines how many items should be returned in the response per page basis. | [optional] [default to 50]
 **offset** | **int**| The starting index of the response items, i.e. where the response should start listing the returned items. | [optional] [default to 0]

### Return type

[**ListConfirmedTokensTransfersByAddressR**](ListConfirmedTokensTransfersByAddressR.md)

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

# **list_tokens_by_address**
> ListTokensByAddressR list_tokens_by_address(blockchain, network, address, context=context, limit=limit, offset=offset)

List Tokens By Address

Through this endpoint customers can obtain token data by providing an attribute - `address`.  The information that can be returned can include the contract address, the token symbol, type and balance.

### Example

* Api Key Authentication (ApiKey):
```python
import time
import os
import cryptoapis
from cryptoapis.models.list_tokens_by_address_r import ListTokensByAddressR
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
    api_instance = cryptoapis.TokensApi(api_client)
    blockchain = 'ethereum' # str | Represents the specific blockchain protocol name, e.g. Ethereum, Ethereum Classic, etc.
    network = 'goerli' # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"goerli\" are test networks.
    address = '0x6890303Cfca4f2571c3A5A5982b44c0Ca82b124A' # str | Represents the public address, which is a compressed and shortened form of a public key.
    context = 'yourExampleString' # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    limit = 50 # int | Defines how many items should be returned in the response per page basis. (optional) (default to 50)
    offset = 0 # int | The starting index of the response items, i.e. where the response should start listing the returned items. (optional) (default to 0)

    try:
        # List Tokens By Address
        api_response = api_instance.list_tokens_by_address(blockchain, network, address, context=context, limit=limit, offset=offset)
        print("The response of TokensApi->list_tokens_by_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokensApi->list_tokens_by_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Ethereum Classic, etc. | 
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;goerli\&quot; are test networks. | 
 **address** | **str**| Represents the public address, which is a compressed and shortened form of a public key. | 
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional] 
 **limit** | **int**| Defines how many items should be returned in the response per page basis. | [optional] [default to 50]
 **offset** | **int**| The starting index of the response items, i.e. where the response should start listing the returned items. | [optional] [default to 0]

### Return type

[**ListTokensByAddressR**](ListTokensByAddressR.md)

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

# **list_tokens_transfers_by_transaction_hash**
> ListTokensTransfersByTransactionHashR list_tokens_transfers_by_transaction_hash(blockchain, network, transaction_hash, context=context, limit=limit, offset=offset)

List Tokens Transfers By Transaction Hash

Through this endpoint customers can obtain a list with token transfers by the `transactionHash` attribute. Token transfers may include information such as addresses of the sender and recipient, token name, token symbol, etc.    {note}This refers only to transfers done for **tokens** not coins.{/note}

### Example

* Api Key Authentication (ApiKey):
```python
import time
import os
import cryptoapis
from cryptoapis.models.list_tokens_transfers_by_transaction_hash_r import ListTokensTransfersByTransactionHashR
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
    api_instance = cryptoapis.TokensApi(api_client)
    blockchain = 'ethereum' # str | Represents the specific blockchain protocol name, e.g. Ethereum, Ethereum Classic, etc.
    network = 'goerli' # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"goerli\" are test networks.
    transaction_hash = '0xbc8245ba5cccb524d91256224689ac0f16678321a266bab8197ad7daab4c9e16' # str | Represents the hash of the transaction, which is its unique identifier. It represents a cryptographic digital fingerprint made by hashing the block header twice through the SHA256 algorithm.
    context = 'yourExampleString' # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    limit = 50 # int | Defines how many items should be returned in the response per page basis. (optional) (default to 50)
    offset = 0 # int | The starting index of the response items, i.e. where the response should start listing the returned items. (optional) (default to 0)

    try:
        # List Tokens Transfers By Transaction Hash
        api_response = api_instance.list_tokens_transfers_by_transaction_hash(blockchain, network, transaction_hash, context=context, limit=limit, offset=offset)
        print("The response of TokensApi->list_tokens_transfers_by_transaction_hash:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokensApi->list_tokens_transfers_by_transaction_hash: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Ethereum Classic, etc. | 
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;goerli\&quot; are test networks. | 
 **transaction_hash** | **str**| Represents the hash of the transaction, which is its unique identifier. It represents a cryptographic digital fingerprint made by hashing the block header twice through the SHA256 algorithm. | 
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional] 
 **limit** | **int**| Defines how many items should be returned in the response per page basis. | [optional] [default to 50]
 **offset** | **int**| The starting index of the response items, i.e. where the response should start listing the returned items. | [optional] [default to 0]

### Return type

[**ListTokensTransfersByTransactionHashR**](ListTokensTransfersByTransactionHashR.md)

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

# **list_unconfirmed_tokens_transfers_by_address**
> ListUnconfirmedTokensTransfersByAddressR list_unconfirmed_tokens_transfers_by_address(blockchain, network, address, context=context, limit=limit, offset=offset)

List Unconfirmed Tokens Transfers By Address

Through this endpoint customers can obtain a list with **unconfirmed** token transfers by the `address` attribute. Token transfers may include information such as addresses of the sender and recipient, token name, token symbol, etc.    {note}This refers only to transfers done for **unconfirmed tokens** not coins.{/note}

### Example

* Api Key Authentication (ApiKey):
```python
import time
import os
import cryptoapis
from cryptoapis.models.list_unconfirmed_tokens_transfers_by_address_r import ListUnconfirmedTokensTransfersByAddressR
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
    api_instance = cryptoapis.TokensApi(api_client)
    blockchain = 'ethereum' # str | Represents the specific blockchain protocol name, e.g. Ethereum, Ethereum Classic, etc.
    network = 'goerli' # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"goerli\" are test networks.
    address = '0x0902a667d6a3f287835e0a4593cae4167384abc6' # str | Represents the public address, which is a compressed and shortened form of a public key.
    context = 'yourExampleString' # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    limit = 50 # int | Defines how many items should be returned in the response per page basis. (optional) (default to 50)
    offset = 0 # int | The starting index of the response items, i.e. where the response should start listing the returned items. (optional) (default to 0)

    try:
        # List Unconfirmed Tokens Transfers By Address
        api_response = api_instance.list_unconfirmed_tokens_transfers_by_address(blockchain, network, address, context=context, limit=limit, offset=offset)
        print("The response of TokensApi->list_unconfirmed_tokens_transfers_by_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokensApi->list_unconfirmed_tokens_transfers_by_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Ethereum Classic, etc. | 
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;goerli\&quot; are test networks. | 
 **address** | **str**| Represents the public address, which is a compressed and shortened form of a public key. | 
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional] 
 **limit** | **int**| Defines how many items should be returned in the response per page basis. | [optional] [default to 50]
 **offset** | **int**| The starting index of the response items, i.e. where the response should start listing the returned items. | [optional] [default to 0]

### Return type

[**ListUnconfirmedTokensTransfersByAddressR**](ListUnconfirmedTokensTransfersByAddressR.md)

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

