# cryptoapis.ZilliqaApi

All URIs are relative to *https://rest.cryptoapis.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_latest_mined_zilliqa_block**](ZilliqaApi.md#get_latest_mined_zilliqa_block) | **GET** /blockchain-data/zilliqa-specific/{network}/blocks/last | Get Latest Mined Zilliqa Block
[**get_zilliqa_address_details**](ZilliqaApi.md#get_zilliqa_address_details) | **GET** /blockchain-data/zilliqa-specific/{network}/addresses/{address} | Get Zilliqa Address Details
[**get_zilliqa_block_details_by_block_hash**](ZilliqaApi.md#get_zilliqa_block_details_by_block_hash) | **GET** /blockchain-data/zilliqa-specific/{network}/blocks/hash/{blockHash} | Get Zilliqa Block Details By Block Hash
[**get_zilliqa_block_details_by_block_height**](ZilliqaApi.md#get_zilliqa_block_details_by_block_height) | **GET** /blockchain-data/zilliqa-specific/{network}/blocks/height/{blockHeight} | Get Zilliqa Block Details By Block Height
[**get_zilliqa_transaction_details_by_transaction_id**](ZilliqaApi.md#get_zilliqa_transaction_details_by_transaction_id) | **GET** /blockchain-data/zilliqa-specific/{network}/transactions/{transactionHash} | Get Zilliqa Transaction Details by Transaction ID
[**list_zilliqa_transactions_by_address**](ZilliqaApi.md#list_zilliqa_transactions_by_address) | **GET** /blockchain-data/zilliqa-specific/{network}/addresses/{address}/transactions | List Zilliqa Transactions by Address
[**list_zilliqa_transactions_by_block_hash**](ZilliqaApi.md#list_zilliqa_transactions_by_block_hash) | **GET** /blockchain-data/zilliqa-specific/{network}/blocks/hash/{blockHash}/transactions | List Zilliqa Transactions By Block Hash
[**list_zilliqa_transactions_by_block_height**](ZilliqaApi.md#list_zilliqa_transactions_by_block_height) | **GET** /blockchain-data/zilliqa-specific/{network}/blocks/height/{blockHeight}/transactions | List Zilliqa Transactions By Block Height


# **get_latest_mined_zilliqa_block**
> GetLatestMinedZilliqaBlockR get_latest_mined_zilliqa_block(network, context=context)

Get Latest Mined Zilliqa Block

Through this endpoint users can obtain information on the latest block that has been mined on the Zilliqa blockchain. Data could include the current and previous block hashes, transaction count, and more.

### Example

* Api Key Authentication (ApiKey):
```python
import time
import os
import cryptoapis
from cryptoapis.models.get_latest_mined_zilliqa_block_r import GetLatestMinedZilliqaBlockR
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
    api_instance = cryptoapis.ZilliqaApi(api_client)
    network = 'mainnet' # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    context = 'yourExampleString' # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)

    try:
        # Get Latest Mined Zilliqa Block
        api_response = api_instance.get_latest_mined_zilliqa_block(network, context=context)
        print("The response of ZilliqaApi->get_latest_mined_zilliqa_block:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZilliqaApi->get_latest_mined_zilliqa_block: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. | 
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional] 

### Return type

[**GetLatestMinedZilliqaBlockR**](GetLatestMinedZilliqaBlockR.md)

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
**404** | The specified block has not been found on the specific blockchain. |  -  |
**409** | The data provided seems to be invalid. |  -  |
**415** | The selected Media Type is unavailable. The Content-Type header should be &#39;application/json&#39;. |  -  |
**422** | Your request body for POST requests must have a structure of { data: { item: [...properties] } } |  -  |
**429** | The request limit has been reached. There can be maximum {requests} requests per {seconds} second(s) made. Please contact our team via email if you need more or upgrade your plan. |  -  |
**500** | An unexpected server error has occurred, we are working to fix this. Please try again later and in case it occurs again please report it to our team via email. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_zilliqa_address_details**
> GetZilliqaAddressDetailsR get_zilliqa_address_details(network, address, context=context)

Get Zilliqa Address Details

Through this endpoint customers can obtain information address details from the Zilliqa blockchain.

### Example

* Api Key Authentication (ApiKey):
```python
import time
import os
import cryptoapis
from cryptoapis.models.get_zilliqa_address_details_r import GetZilliqaAddressDetailsR
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
    api_instance = cryptoapis.ZilliqaApi(api_client)
    network = 'mainnet' # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    address = 'zil17v9gs6ctn9pq6wka8k668umdlaj88nrfej7rnm' # str | Defines the specific transaction's address.
    context = 'yourExampleString' # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)

    try:
        # Get Zilliqa Address Details
        api_response = api_instance.get_zilliqa_address_details(network, address, context=context)
        print("The response of ZilliqaApi->get_zilliqa_address_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZilliqaApi->get_zilliqa_address_details: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. | 
 **address** | **str**| Defines the specific transaction&#39;s address. | 
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional] 

### Return type

[**GetZilliqaAddressDetailsR**](GetZilliqaAddressDetailsR.md)

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

# **get_zilliqa_block_details_by_block_hash**
> GetZilliqaBlockDetailsByBlockHashR get_zilliqa_block_details_by_block_hash(network, block_hash, context=context)

Get Zilliqa Block Details By Block Hash

Through this endpoint customers can obtain block details from the Zilliqa blockchain by providing the block Hash parameter.

### Example

* Api Key Authentication (ApiKey):
```python
import time
import os
import cryptoapis
from cryptoapis.models.get_zilliqa_block_details_by_block_hash_r import GetZilliqaBlockDetailsByBlockHashR
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
    api_instance = cryptoapis.ZilliqaApi(api_client)
    network = 'mainnet' # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    block_hash = '0xf679d0b5387f0b0b3c3c1f368305512b23860888ba4415063d464a09b8bb6205' # str | Represents the hash of the block, which is its unique identifier. It represents a cryptographic digital fingerprint made by hashing the block header twice through the SHA256 algorithm.
    context = 'yourExampleString' # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)

    try:
        # Get Zilliqa Block Details By Block Hash
        api_response = api_instance.get_zilliqa_block_details_by_block_hash(network, block_hash, context=context)
        print("The response of ZilliqaApi->get_zilliqa_block_details_by_block_hash:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZilliqaApi->get_zilliqa_block_details_by_block_hash: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. | 
 **block_hash** | **str**| Represents the hash of the block, which is its unique identifier. It represents a cryptographic digital fingerprint made by hashing the block header twice through the SHA256 algorithm. | 
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional] 

### Return type

[**GetZilliqaBlockDetailsByBlockHashR**](GetZilliqaBlockDetailsByBlockHashR.md)

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
**404** | The specified block has not been found on the specific blockchain. |  -  |
**409** | The data provided seems to be invalid. |  -  |
**415** | The selected Media Type is unavailable. The Content-Type header should be &#39;application/json&#39;. |  -  |
**422** | Your request body for POST requests must have a structure of { data: { item: [...properties] } } |  -  |
**429** | The request limit has been reached. There can be maximum {requests} requests per {seconds} second(s) made. Please contact our team via email if you need more or upgrade your plan. |  -  |
**500** | An unexpected server error has occurred, we are working to fix this. Please try again later and in case it occurs again please report it to our team via email. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_zilliqa_block_details_by_block_height**
> GetZilliqaBlockDetailsByBlockHeightR get_zilliqa_block_details_by_block_height(network, block_height, context=context)

Get Zilliqa Block Details By Block Height

Through this endpoint customers can obtain block details from the Zilliqa blockchain by providing the block Height parameter.

### Example

* Api Key Authentication (ApiKey):
```python
import time
import os
import cryptoapis
from cryptoapis.models.get_zilliqa_block_details_by_block_height_r import GetZilliqaBlockDetailsByBlockHeightR
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
    api_instance = cryptoapis.ZilliqaApi(api_client)
    network = 'mainnet' # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    block_height = 1244298 # int | Represents the number of blocks in the blockchain preceding this specific block. Block numbers have no gaps. A blockchain usually starts with block 0 called the \"Genesis block\".
    context = 'yourExampleString' # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)

    try:
        # Get Zilliqa Block Details By Block Height
        api_response = api_instance.get_zilliqa_block_details_by_block_height(network, block_height, context=context)
        print("The response of ZilliqaApi->get_zilliqa_block_details_by_block_height:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZilliqaApi->get_zilliqa_block_details_by_block_height: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. | 
 **block_height** | **int**| Represents the number of blocks in the blockchain preceding this specific block. Block numbers have no gaps. A blockchain usually starts with block 0 called the \&quot;Genesis block\&quot;. | 
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional] 

### Return type

[**GetZilliqaBlockDetailsByBlockHeightR**](GetZilliqaBlockDetailsByBlockHeightR.md)

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
**404** | The specified block has not been found on the specific blockchain. |  -  |
**409** | The data provided seems to be invalid. |  -  |
**415** | The selected Media Type is unavailable. The Content-Type header should be &#39;application/json&#39;. |  -  |
**422** | Your request body for POST requests must have a structure of { data: { item: [...properties] } } |  -  |
**429** | The request limit has been reached. There can be maximum {requests} requests per {seconds} second(s) made. Please contact our team via email if you need more or upgrade your plan. |  -  |
**500** | An unexpected server error has occurred, we are working to fix this. Please try again later and in case it occurs again please report it to our team via email. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_zilliqa_transaction_details_by_transaction_id**
> GetZilliqaTransactionDetailsByTransactionIDR get_zilliqa_transaction_details_by_transaction_id(network, transaction_hash, context=context)

Get Zilliqa Transaction Details by Transaction ID

Through this endpoint customers can obtain transaction details on the Zilliqa blockchain by providing a Transaction ID parameter.

### Example

* Api Key Authentication (ApiKey):
```python
import time
import os
import cryptoapis
from cryptoapis.models.get_zilliqa_transaction_details_by_transaction_idr import GetZilliqaTransactionDetailsByTransactionIDR
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
    api_instance = cryptoapis.ZilliqaApi(api_client)
    network = 'mainnet' # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    transaction_hash = '0xe649afbe2849c70a7a8b3087bee2c7b2fa0b6b77ab658b4fff390a1d06f0a8bc' # str | String identifier of the transaction
    context = 'yourExampleString' # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)

    try:
        # Get Zilliqa Transaction Details by Transaction ID
        api_response = api_instance.get_zilliqa_transaction_details_by_transaction_id(network, transaction_hash, context=context)
        print("The response of ZilliqaApi->get_zilliqa_transaction_details_by_transaction_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZilliqaApi->get_zilliqa_transaction_details_by_transaction_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. | 
 **transaction_hash** | **str**| String identifier of the transaction | 
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional] 

### Return type

[**GetZilliqaTransactionDetailsByTransactionIDR**](GetZilliqaTransactionDetailsByTransactionIDR.md)

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
**404** | The specified transaction has not been found on the specific blockchain. |  -  |
**409** | The data provided seems to be invalid. |  -  |
**415** | The selected Media Type is unavailable. The Content-Type header should be &#39;application/json&#39;. |  -  |
**422** | Your request body for POST requests must have a structure of { data: { item: [...properties] } } |  -  |
**429** | The request limit has been reached. There can be maximum {requests} requests per {seconds} second(s) made. Please contact our team via email if you need more or upgrade your plan. |  -  |
**500** | An unexpected server error has occurred, we are working to fix this. Please try again later and in case it occurs again please report it to our team via email. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_zilliqa_transactions_by_address**
> ListZilliqaTransactionsByAddressR list_zilliqa_transactions_by_address(network, address, context=context, limit=limit, offset=offset)

List Zilliqa Transactions by Address

Through this endpoint customers can list transactions on the Zilliqa blockchain by the address parameter.

### Example

* Api Key Authentication (ApiKey):
```python
import time
import os
import cryptoapis
from cryptoapis.models.list_zilliqa_transactions_by_address_r import ListZilliqaTransactionsByAddressR
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
    api_instance = cryptoapis.ZilliqaApi(api_client)
    network = 'mainnet' # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    address = 'zil17v9gs6ctn9pq6wka8k668umdlaj88nrfej7rnm' # str | Defines the specific address of the sender.
    context = 'yourExampleString' # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    limit = 50 # int | Defines how many items should be returned in the response per page basis. (optional) (default to 50)
    offset = 0 # int | The starting index of the response items, i.e. where the response should start listing the returned items. (optional) (default to 0)

    try:
        # List Zilliqa Transactions by Address
        api_response = api_instance.list_zilliqa_transactions_by_address(network, address, context=context, limit=limit, offset=offset)
        print("The response of ZilliqaApi->list_zilliqa_transactions_by_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZilliqaApi->list_zilliqa_transactions_by_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. | 
 **address** | **str**| Defines the specific address of the sender. | 
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional] 
 **limit** | **int**| Defines how many items should be returned in the response per page basis. | [optional] [default to 50]
 **offset** | **int**| The starting index of the response items, i.e. where the response should start listing the returned items. | [optional] [default to 0]

### Return type

[**ListZilliqaTransactionsByAddressR**](ListZilliqaTransactionsByAddressR.md)

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

# **list_zilliqa_transactions_by_block_hash**
> ListZilliqaTransactionsByBlockHashR list_zilliqa_transactions_by_block_hash(network, block_hash, context=context, limit=limit, offset=offset)

List Zilliqa Transactions By Block Hash

Through this endpoint customers can list transactions on the Zilliqa blockchain by the block hash parameter.

### Example

* Api Key Authentication (ApiKey):
```python
import time
import os
import cryptoapis
from cryptoapis.models.list_zilliqa_transactions_by_block_hash_r import ListZilliqaTransactionsByBlockHashR
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
    api_instance = cryptoapis.ZilliqaApi(api_client)
    network = 'mainnet' # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    block_hash = '0x3160ca05ac12f60023de6b6987596eccbf084629f1a92b59534c5c021bf27041' # str | Represents the hash of the block, which is its unique identifier. It represents a cryptographic digital fingerprint made by hashing the block header twice through the SHA256 algorithm.
    context = 'yourExampleString' # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    limit = 50 # int | Defines how many items should be returned in the response per page basis. (optional) (default to 50)
    offset = 0 # int | The starting index of the response items, i.e. where the response should start listing the returned items. (optional) (default to 0)

    try:
        # List Zilliqa Transactions By Block Hash
        api_response = api_instance.list_zilliqa_transactions_by_block_hash(network, block_hash, context=context, limit=limit, offset=offset)
        print("The response of ZilliqaApi->list_zilliqa_transactions_by_block_hash:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZilliqaApi->list_zilliqa_transactions_by_block_hash: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. | 
 **block_hash** | **str**| Represents the hash of the block, which is its unique identifier. It represents a cryptographic digital fingerprint made by hashing the block header twice through the SHA256 algorithm. | 
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional] 
 **limit** | **int**| Defines how many items should be returned in the response per page basis. | [optional] [default to 50]
 **offset** | **int**| The starting index of the response items, i.e. where the response should start listing the returned items. | [optional] [default to 0]

### Return type

[**ListZilliqaTransactionsByBlockHashR**](ListZilliqaTransactionsByBlockHashR.md)

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

# **list_zilliqa_transactions_by_block_height**
> ListZilliqaTransactionsByBlockHeightR list_zilliqa_transactions_by_block_height(network, block_height, context=context, limit=limit, offset=offset)

List Zilliqa Transactions By Block Height

Through this endpoint customers can list transactions on the Zilliqa blockchain by the block height parameter.

### Example

* Api Key Authentication (ApiKey):
```python
import time
import os
import cryptoapis
from cryptoapis.models.list_zilliqa_transactions_by_block_height_r import ListZilliqaTransactionsByBlockHeightR
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
    api_instance = cryptoapis.ZilliqaApi(api_client)
    network = 'mainnet' # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    block_height = 1250392 # int | Represents the number of blocks in the blockchain preceding this specific block. Block numbers have no gaps. A blockchain usually starts with block 0 called the \"Genesis block\".
    context = 'yourExampleString' # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    limit = 50 # int | Defines how many items should be returned in the response per page basis. (optional) (default to 50)
    offset = 0 # int | The starting index of the response items, i.e. where the response should start listing the returned items. (optional) (default to 0)

    try:
        # List Zilliqa Transactions By Block Height
        api_response = api_instance.list_zilliqa_transactions_by_block_height(network, block_height, context=context, limit=limit, offset=offset)
        print("The response of ZilliqaApi->list_zilliqa_transactions_by_block_height:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZilliqaApi->list_zilliqa_transactions_by_block_height: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. | 
 **block_height** | **int**| Represents the number of blocks in the blockchain preceding this specific block. Block numbers have no gaps. A blockchain usually starts with block 0 called the \&quot;Genesis block\&quot;. | 
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional] 
 **limit** | **int**| Defines how many items should be returned in the response per page basis. | [optional] [default to 50]
 **offset** | **int**| The starting index of the response items, i.e. where the response should start listing the returned items. | [optional] [default to 0]

### Return type

[**ListZilliqaTransactionsByBlockHeightR**](ListZilliqaTransactionsByBlockHeightR.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request was successfully executed. |  -  |
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

