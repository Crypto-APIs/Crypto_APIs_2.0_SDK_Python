# cryptoapis.ZilliqaApi

All URIs are relative to *https://rest.cryptoapis.io/v2*

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
> GetLatestMinedZilliqaBlockR get_latest_mined_zilliqa_block()

Get Latest Mined Zilliqa Block

Through this endpoint users can obtain information on the latest block that has been mined on the Zilliqa blockchain. Data could include the current and previous block hashes, transaction count, and more.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import zilliqa_api
from cryptoapis.model.blockchain_data_block_not_found import BlockchainDataBlockNotFound
from cryptoapis.model.insufficient_credits import InsufficientCredits
from cryptoapis.model.invalid_api_key import InvalidApiKey
from cryptoapis.model.invalid_data import InvalidData
from cryptoapis.model.invalid_request_body_structure import InvalidRequestBodyStructure
from cryptoapis.model.request_limit_reached import RequestLimitReached
from cryptoapis.model.invalid_pagination import InvalidPagination
from cryptoapis.model.get_latest_mined_zilliqa_block_r import GetLatestMinedZilliqaBlockR
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
    api_instance = zilliqa_api.ZilliqaApi(api_client)
    context = "context_example" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Latest Mined Zilliqa Block
        api_response = api_instance.get_latest_mined_zilliqa_block()
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling ZilliqaApi->get_latest_mined_zilliqa_block: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Latest Mined Zilliqa Block
        api_response = api_instance.get_latest_mined_zilliqa_block(context=context)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling ZilliqaApi->get_latest_mined_zilliqa_block: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. | defaults to "mainnet"
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
**400** | The pagination attributes that have been used are invalid. Please check the Documentation to see details on pagination. |  -  |
**401** | The provided API key is invalid. Please, generate a new one from your Dashboard. |  -  |
**402** | You have insufficient credits. Please upgrade your plan from your Dashboard or contact our team via email. |  -  |
**403** | Mainnets access is not available for your current subscription plan, please upgrade your plan to be able to use it. |  -  |
**404** | The specified block has not been found on the specific blockchain. |  -  |
**409** | The data provided seems to be invalid. |  -  |
**415** | The selected Media Type is unavailable. The Content-Type header should be &#39;application/json&#39;. |  -  |
**422** | Your request body for POST requests must have a structure of { data: { item: [...properties] } } |  -  |
**429** | The request limit has been reached. There can be maximum {requests} requests per {seconds} second(s) made. Please contact our team via email if you need more or upgrade your plan. |  -  |
**500** | An unexpected server error has occurred, we are working to fix this. Please try again later and in case it occurs again please report it to our team via email. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_zilliqa_address_details**
> GetZilliqaAddressDetailsR get_zilliqa_address_details(address)

Get Zilliqa Address Details

Through this endpoint customers can obtain information address details from the Zilliqa blockchain.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import zilliqa_api
from cryptoapis.model.get_zilliqa_address_details_r import GetZilliqaAddressDetailsR
from cryptoapis.model.insufficient_credits import InsufficientCredits
from cryptoapis.model.invalid_api_key import InvalidApiKey
from cryptoapis.model.invalid_data import InvalidData
from cryptoapis.model.invalid_request_body_structure import InvalidRequestBodyStructure
from cryptoapis.model.request_limit_reached import RequestLimitReached
from cryptoapis.model.invalid_pagination import InvalidPagination
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
    api_instance = zilliqa_api.ZilliqaApi(api_client)
    address = "zil17v9gs6ctn9pq6wka8k668umdlaj88nrfej7rnm" # str | Defines the specific transaction's address.
    context = "context_example" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Zilliqa Address Details
        api_response = api_instance.get_zilliqa_address_details(address)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling ZilliqaApi->get_zilliqa_address_details: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Zilliqa Address Details
        api_response = api_instance.get_zilliqa_address_details(address, context=context)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling ZilliqaApi->get_zilliqa_address_details: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Defines the specific transaction&#39;s address. |
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. | defaults to "mainnet"
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
**400** | The pagination attributes that have been used are invalid. Please check the Documentation to see details on pagination. |  -  |
**401** | The provided API key is invalid. Please, generate a new one from your Dashboard. |  -  |
**402** | You have insufficient credits. Please upgrade your plan from your Dashboard or contact our team via email. |  -  |
**403** | Mainnets access is not available for your current subscription plan, please upgrade your plan to be able to use it. |  -  |
**409** | The data provided seems to be invalid. |  -  |
**415** | The selected Media Type is unavailable. The Content-Type header should be &#39;application/json&#39;. |  -  |
**422** | Your request body for POST requests must have a structure of { data: { item: [...properties] } } |  -  |
**429** | The request limit has been reached. There can be maximum {requests} requests per {seconds} second(s) made. Please contact our team via email if you need more or upgrade your plan. |  -  |
**500** | An unexpected server error has occurred, we are working to fix this. Please try again later and in case it occurs again please report it to our team via email. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_zilliqa_block_details_by_block_hash**
> GetZilliqaBlockDetailsByBlockHashR get_zilliqa_block_details_by_block_hash(block_hash)

Get Zilliqa Block Details By Block Hash

Through this endpoint customers can obtain block details from the Zilliqa blockchain by providing the block Hash parameter.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import zilliqa_api
from cryptoapis.model.blockchain_data_block_not_found import BlockchainDataBlockNotFound
from cryptoapis.model.insufficient_credits import InsufficientCredits
from cryptoapis.model.invalid_api_key import InvalidApiKey
from cryptoapis.model.invalid_data import InvalidData
from cryptoapis.model.invalid_request_body_structure import InvalidRequestBodyStructure
from cryptoapis.model.request_limit_reached import RequestLimitReached
from cryptoapis.model.invalid_pagination import InvalidPagination
from cryptoapis.model.feature_mainnets_not_allowed_for_plan import FeatureMainnetsNotAllowedForPlan
from cryptoapis.model.get_zilliqa_block_details_by_block_hash_r import GetZilliqaBlockDetailsByBlockHashR
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
    api_instance = zilliqa_api.ZilliqaApi(api_client)
    block_hash = "0xf679d0b5387f0b0b3c3c1f368305512b23860888ba4415063d464a09b8bb6205" # str | Represents the hash of the block, which is its unique identifier. It represents a cryptographic digital fingerprint made by hashing the block header twice through the SHA256 algorithm.
    context = "context_example" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Zilliqa Block Details By Block Hash
        api_response = api_instance.get_zilliqa_block_details_by_block_hash(block_hash)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling ZilliqaApi->get_zilliqa_block_details_by_block_hash: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Zilliqa Block Details By Block Hash
        api_response = api_instance.get_zilliqa_block_details_by_block_hash(block_hash, context=context)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling ZilliqaApi->get_zilliqa_block_details_by_block_hash: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_hash** | **str**| Represents the hash of the block, which is its unique identifier. It represents a cryptographic digital fingerprint made by hashing the block header twice through the SHA256 algorithm. |
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. | defaults to "mainnet"
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
**400** | The pagination attributes that have been used are invalid. Please check the Documentation to see details on pagination. |  -  |
**401** | The provided API key is invalid. Please, generate a new one from your Dashboard. |  -  |
**402** | You have insufficient credits. Please upgrade your plan from your Dashboard or contact our team via email. |  -  |
**403** | Mainnets access is not available for your current subscription plan, please upgrade your plan to be able to use it. |  -  |
**404** | The specified block has not been found on the specific blockchain. |  -  |
**409** | The data provided seems to be invalid. |  -  |
**415** | The selected Media Type is unavailable. The Content-Type header should be &#39;application/json&#39;. |  -  |
**422** | Your request body for POST requests must have a structure of { data: { item: [...properties] } } |  -  |
**429** | The request limit has been reached. There can be maximum {requests} requests per {seconds} second(s) made. Please contact our team via email if you need more or upgrade your plan. |  -  |
**500** | An unexpected server error has occurred, we are working to fix this. Please try again later and in case it occurs again please report it to our team via email. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_zilliqa_block_details_by_block_height**
> GetZilliqaBlockDetailsByBlockHeightR get_zilliqa_block_details_by_block_height(block_height)

Get Zilliqa Block Details By Block Height

Through this endpoint customers can obtain block details from the Zilliqa blockchain by providing the block Height parameter.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import zilliqa_api
from cryptoapis.model.blockchain_data_block_not_found import BlockchainDataBlockNotFound
from cryptoapis.model.insufficient_credits import InsufficientCredits
from cryptoapis.model.invalid_api_key import InvalidApiKey
from cryptoapis.model.invalid_data import InvalidData
from cryptoapis.model.invalid_request_body_structure import InvalidRequestBodyStructure
from cryptoapis.model.request_limit_reached import RequestLimitReached
from cryptoapis.model.invalid_pagination import InvalidPagination
from cryptoapis.model.get_zilliqa_block_details_by_block_height_r import GetZilliqaBlockDetailsByBlockHeightR
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
    api_instance = zilliqa_api.ZilliqaApi(api_client)
    block_height = 1244298 # int | Represents the number of blocks in the blockchain preceding this specific block. Block numbers have no gaps. A blockchain usually starts with block 0 called the \"Genesis block\".
    context = "context_example" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Zilliqa Block Details By Block Height
        api_response = api_instance.get_zilliqa_block_details_by_block_height(block_height)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling ZilliqaApi->get_zilliqa_block_details_by_block_height: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Zilliqa Block Details By Block Height
        api_response = api_instance.get_zilliqa_block_details_by_block_height(block_height, context=context)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling ZilliqaApi->get_zilliqa_block_details_by_block_height: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_height** | **int**| Represents the number of blocks in the blockchain preceding this specific block. Block numbers have no gaps. A blockchain usually starts with block 0 called the \&quot;Genesis block\&quot;. |
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. | defaults to "mainnet"
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
**400** | The pagination attributes that have been used are invalid. Please check the Documentation to see details on pagination. |  -  |
**401** | The provided API key is invalid. Please, generate a new one from your Dashboard. |  -  |
**402** | You have insufficient credits. Please upgrade your plan from your Dashboard or contact our team via email. |  -  |
**403** | Mainnets access is not available for your current subscription plan, please upgrade your plan to be able to use it. |  -  |
**404** | The specified block has not been found on the specific blockchain. |  -  |
**409** | The data provided seems to be invalid. |  -  |
**415** | The selected Media Type is unavailable. The Content-Type header should be &#39;application/json&#39;. |  -  |
**422** | Your request body for POST requests must have a structure of { data: { item: [...properties] } } |  -  |
**429** | The request limit has been reached. There can be maximum {requests} requests per {seconds} second(s) made. Please contact our team via email if you need more or upgrade your plan. |  -  |
**500** | An unexpected server error has occurred, we are working to fix this. Please try again later and in case it occurs again please report it to our team via email. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_zilliqa_transaction_details_by_transaction_id**
> GetZilliqaTransactionDetailsByTransactionIDR get_zilliqa_transaction_details_by_transaction_id(transaction_hash)

Get Zilliqa Transaction Details by Transaction ID

Through this endpoint customers can obtain transaction details on the Zilliqa blockchain by providing a Transaction ID parameter.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import zilliqa_api
from cryptoapis.model.get_zilliqa_transaction_details_by_transaction_idr import GetZilliqaTransactionDetailsByTransactionIDR
from cryptoapis.model.insufficient_credits import InsufficientCredits
from cryptoapis.model.invalid_api_key import InvalidApiKey
from cryptoapis.model.invalid_data import InvalidData
from cryptoapis.model.invalid_request_body_structure import InvalidRequestBodyStructure
from cryptoapis.model.request_limit_reached import RequestLimitReached
from cryptoapis.model.invalid_pagination import InvalidPagination
from cryptoapis.model.feature_mainnets_not_allowed_for_plan import FeatureMainnetsNotAllowedForPlan
from cryptoapis.model.blockchain_data_transaction_not_found import BlockchainDataTransactionNotFound
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
    api_instance = zilliqa_api.ZilliqaApi(api_client)
    transaction_hash = "0xe649afbe2849c70a7a8b3087bee2c7b2fa0b6b77ab658b4fff390a1d06f0a8bc" # str | String identifier of the transaction
    context = "context_example" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Zilliqa Transaction Details by Transaction ID
        api_response = api_instance.get_zilliqa_transaction_details_by_transaction_id(transaction_hash)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling ZilliqaApi->get_zilliqa_transaction_details_by_transaction_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Zilliqa Transaction Details by Transaction ID
        api_response = api_instance.get_zilliqa_transaction_details_by_transaction_id(transaction_hash, context=context)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling ZilliqaApi->get_zilliqa_transaction_details_by_transaction_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_hash** | **str**| String identifier of the transaction |
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. | defaults to "mainnet"
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
**400** | The pagination attributes that have been used are invalid. Please check the Documentation to see details on pagination. |  -  |
**401** | The provided API key is invalid. Please, generate a new one from your Dashboard. |  -  |
**402** | You have insufficient credits. Please upgrade your plan from your Dashboard or contact our team via email. |  -  |
**403** | Mainnets access is not available for your current subscription plan, please upgrade your plan to be able to use it. |  -  |
**404** | The specified transaction has not been found on the specific blockchain. |  -  |
**409** | The data provided seems to be invalid. |  -  |
**415** | The selected Media Type is unavailable. The Content-Type header should be &#39;application/json&#39;. |  -  |
**422** | Your request body for POST requests must have a structure of { data: { item: [...properties] } } |  -  |
**429** | The request limit has been reached. There can be maximum {requests} requests per {seconds} second(s) made. Please contact our team via email if you need more or upgrade your plan. |  -  |
**500** | An unexpected server error has occurred, we are working to fix this. Please try again later and in case it occurs again please report it to our team via email. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_zilliqa_transactions_by_address**
> ListZilliqaTransactionsByAddressR list_zilliqa_transactions_by_address(address)

List Zilliqa Transactions by Address

Through this endpoint customers can list transactions on the Zilliqa blockchain by the address parameter.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import zilliqa_api
from cryptoapis.model.list_zilliqa_transactions_by_address_r import ListZilliqaTransactionsByAddressR
from cryptoapis.model.insufficient_credits import InsufficientCredits
from cryptoapis.model.invalid_api_key import InvalidApiKey
from cryptoapis.model.invalid_data import InvalidData
from cryptoapis.model.invalid_request_body_structure import InvalidRequestBodyStructure
from cryptoapis.model.request_limit_reached import RequestLimitReached
from cryptoapis.model.invalid_pagination import InvalidPagination
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
    api_instance = zilliqa_api.ZilliqaApi(api_client)
    address = "zil17v9gs6ctn9pq6wka8k668umdlaj88nrfej7rnm" # str | Defines the specific address of the sender.
    context = "context_example" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    limit = 50 # int | Defines how many items should be returned in the response per page basis. (optional) if omitted the server will use the default value of 50
    offset = 10 # int | The starting index of the response items, i.e. where the response should start listing the returned items. (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    try:
        # List Zilliqa Transactions by Address
        api_response = api_instance.list_zilliqa_transactions_by_address(address)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling ZilliqaApi->list_zilliqa_transactions_by_address: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Zilliqa Transactions by Address
        api_response = api_instance.list_zilliqa_transactions_by_address(address, context=context, limit=limit, offset=offset)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling ZilliqaApi->list_zilliqa_transactions_by_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Defines the specific address of the sender. |
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. | defaults to "mainnet"
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]
 **limit** | **int**| Defines how many items should be returned in the response per page basis. | [optional] if omitted the server will use the default value of 50
 **offset** | **int**| The starting index of the response items, i.e. where the response should start listing the returned items. | [optional] if omitted the server will use the default value of 0

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
**400** | The pagination attributes that have been used are invalid. Please check the Documentation to see details on pagination. |  -  |
**401** | The provided API key is invalid. Please, generate a new one from your Dashboard. |  -  |
**402** | You have insufficient credits. Please upgrade your plan from your Dashboard or contact our team via email. |  -  |
**403** | Mainnets access is not available for your current subscription plan, please upgrade your plan to be able to use it. |  -  |
**409** | The data provided seems to be invalid. |  -  |
**415** | The selected Media Type is unavailable. The Content-Type header should be &#39;application/json&#39;. |  -  |
**422** | Your request body for POST requests must have a structure of { data: { item: [...properties] } } |  -  |
**429** | The request limit has been reached. There can be maximum {requests} requests per {seconds} second(s) made. Please contact our team via email if you need more or upgrade your plan. |  -  |
**500** | An unexpected server error has occurred, we are working to fix this. Please try again later and in case it occurs again please report it to our team via email. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_zilliqa_transactions_by_block_hash**
> ListZilliqaTransactionsByBlockHashR list_zilliqa_transactions_by_block_hash(block_hash)

List Zilliqa Transactions By Block Hash

Through this endpoint customers can list transactions on the Zilliqa blockchain by the block hash parameter.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import zilliqa_api
from cryptoapis.model.insufficient_credits import InsufficientCredits
from cryptoapis.model.invalid_api_key import InvalidApiKey
from cryptoapis.model.invalid_data import InvalidData
from cryptoapis.model.invalid_request_body_structure import InvalidRequestBodyStructure
from cryptoapis.model.request_limit_reached import RequestLimitReached
from cryptoapis.model.invalid_pagination import InvalidPagination
from cryptoapis.model.feature_mainnets_not_allowed_for_plan import FeatureMainnetsNotAllowedForPlan
from cryptoapis.model.list_zilliqa_transactions_by_block_hash_r import ListZilliqaTransactionsByBlockHashR
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
    api_instance = zilliqa_api.ZilliqaApi(api_client)
    block_hash = "0x3160ca05ac12f60023de6b6987596eccbf084629f1a92b59534c5c021bf27041" # str | Represents the hash of the block, which is its unique identifier. It represents a cryptographic digital fingerprint made by hashing the block header twice through the SHA256 algorithm.
    context = "context_example" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    limit = 50 # int | Defines how many items should be returned in the response per page basis. (optional) if omitted the server will use the default value of 50
    offset = 10 # int | The starting index of the response items, i.e. where the response should start listing the returned items. (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    try:
        # List Zilliqa Transactions By Block Hash
        api_response = api_instance.list_zilliqa_transactions_by_block_hash(block_hash)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling ZilliqaApi->list_zilliqa_transactions_by_block_hash: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Zilliqa Transactions By Block Hash
        api_response = api_instance.list_zilliqa_transactions_by_block_hash(block_hash, context=context, limit=limit, offset=offset)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling ZilliqaApi->list_zilliqa_transactions_by_block_hash: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_hash** | **str**| Represents the hash of the block, which is its unique identifier. It represents a cryptographic digital fingerprint made by hashing the block header twice through the SHA256 algorithm. |
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. | defaults to "mainnet"
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]
 **limit** | **int**| Defines how many items should be returned in the response per page basis. | [optional] if omitted the server will use the default value of 50
 **offset** | **int**| The starting index of the response items, i.e. where the response should start listing the returned items. | [optional] if omitted the server will use the default value of 0

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
**400** | The pagination attributes that have been used are invalid. Please check the Documentation to see details on pagination. |  -  |
**401** | The provided API key is invalid. Please, generate a new one from your Dashboard. |  -  |
**402** | You have insufficient credits. Please upgrade your plan from your Dashboard or contact our team via email. |  -  |
**403** | Mainnets access is not available for your current subscription plan, please upgrade your plan to be able to use it. |  -  |
**409** | The data provided seems to be invalid. |  -  |
**415** | The selected Media Type is unavailable. The Content-Type header should be &#39;application/json&#39;. |  -  |
**422** | Your request body for POST requests must have a structure of { data: { item: [...properties] } } |  -  |
**429** | The request limit has been reached. There can be maximum {requests} requests per {seconds} second(s) made. Please contact our team via email if you need more or upgrade your plan. |  -  |
**500** | An unexpected server error has occurred, we are working to fix this. Please try again later and in case it occurs again please report it to our team via email. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_zilliqa_transactions_by_block_height**
> ListZilliqaTransactionsByBlockHeightR list_zilliqa_transactions_by_block_height(block_height)

List Zilliqa Transactions By Block Height

Through this endpoint customers can list transactions on the Zilliqa blockchain by the block height parameter.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import zilliqa_api
from cryptoapis.model.list_zilliqa_transactions_by_block_height_r import ListZilliqaTransactionsByBlockHeightR
from cryptoapis.model.insufficient_credits import InsufficientCredits
from cryptoapis.model.invalid_api_key import InvalidApiKey
from cryptoapis.model.invalid_data import InvalidData
from cryptoapis.model.invalid_request_body_structure import InvalidRequestBodyStructure
from cryptoapis.model.request_limit_reached import RequestLimitReached
from cryptoapis.model.invalid_pagination import InvalidPagination
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
    api_instance = zilliqa_api.ZilliqaApi(api_client)
    block_height = 1250392 # int | Represents the number of blocks in the blockchain preceding this specific block. Block numbers have no gaps. A blockchain usually starts with block 0 called the \"Genesis block\".
    context = "context_example" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    limit = 50 # int | Defines how many items should be returned in the response per page basis. (optional) if omitted the server will use the default value of 50
    offset = 10 # int | The starting index of the response items, i.e. where the response should start listing the returned items. (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    try:
        # List Zilliqa Transactions By Block Height
        api_response = api_instance.list_zilliqa_transactions_by_block_height(block_height)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling ZilliqaApi->list_zilliqa_transactions_by_block_height: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Zilliqa Transactions By Block Height
        api_response = api_instance.list_zilliqa_transactions_by_block_height(block_height, context=context, limit=limit, offset=offset)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling ZilliqaApi->list_zilliqa_transactions_by_block_height: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_height** | **int**| Represents the number of blocks in the blockchain preceding this specific block. Block numbers have no gaps. A blockchain usually starts with block 0 called the \&quot;Genesis block\&quot;. |
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. | defaults to "mainnet"
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]
 **limit** | **int**| Defines how many items should be returned in the response per page basis. | [optional] if omitted the server will use the default value of 50
 **offset** | **int**| The starting index of the response items, i.e. where the response should start listing the returned items. | [optional] if omitted the server will use the default value of 0

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
**400** | The pagination attributes that have been used are invalid. Please check the Documentation to see details on pagination. |  -  |
**401** | The provided API key is invalid. Please, generate a new one from your Dashboard. |  -  |
**402** | You have insufficient credits. Please upgrade your plan from your Dashboard or contact our team via email. |  -  |
**403** | Mainnets access is not available for your current subscription plan, please upgrade your plan to be able to use it. |  -  |
**409** | The data provided seems to be invalid. |  -  |
**415** | The selected Media Type is unavailable. The Content-Type header should be &#39;application/json&#39;. |  -  |
**422** | Your request body for POST requests must have a structure of { data: { item: [...properties] } } |  -  |
**429** | The request limit has been reached. There can be maximum {requests} requests per {seconds} second(s) made. Please contact our team via email if you need more or upgrade your plan. |  -  |
**500** | An unexpected server error has occurred, we are working to fix this. Please try again later and in case it occurs again please report it to our team via email. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

