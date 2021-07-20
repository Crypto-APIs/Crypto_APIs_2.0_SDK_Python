# cryptoapis.XRPRippleApi

All URIs are relative to *https://rest.cryptoapis.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_latest_mined_xrp__ripple_block**](XRPRippleApi.md#get_latest_mined_xrp__ripple_block) | **GET** /blockchain-data/xrp-specific/{network}/blocks/last | Get Latest Mined XRP (Ripple) Block
[**get_xrp__ripple_address_details**](XRPRippleApi.md#get_xrp__ripple_address_details) | **GET** /blockchain-data/xrp-specific/{network}/addresses/{address} | Get XRP (Ripple) Address Details
[**get_xrp__ripple_block_details_by_block_hash**](XRPRippleApi.md#get_xrp__ripple_block_details_by_block_hash) | **GET** /blockchain-data/xrp-specific/{network}/blocks/hash/{blockHash} | Get XRP (Ripple) Block Details By Block Hash
[**get_xrp__ripple_block_details_by_block_height**](XRPRippleApi.md#get_xrp__ripple_block_details_by_block_height) | **GET** /blockchain-data/xrp-specific/{network}/blocks/height/{blockHeight} | Get XRP (Ripple) Block Details By Block Height
[**get_xrp__ripple_transaction_details_by_transaction_id**](XRPRippleApi.md#get_xrp__ripple_transaction_details_by_transaction_id) | **GET** /blockchain-data/xrp-specific/{network}/transactions/{transactionHash} | Get XRP (Ripple) Transaction Details By Transaction ID
[**list_xrp__ripple_transactions_by_address**](XRPRippleApi.md#list_xrp__ripple_transactions_by_address) | **GET** /blockchain-data/xrp-specific/{network}/addresses/{address}/transactions | List XRP (Ripple) Transactions by Address
[**list_xrp__ripple_transactions_by_block_hash**](XRPRippleApi.md#list_xrp__ripple_transactions_by_block_hash) | **GET** /blockchain-data/xrp-specific/{network}/blocks/hash/{blockHash}/transactions | List XRP (Ripple) Transactions By Block Hash
[**list_xrp__ripple_transactions_by_block_height**](XRPRippleApi.md#list_xrp__ripple_transactions_by_block_height) | **GET** /blockchain-data/xrp-specific/{network}/blocks/height/{blockHeight}/transactions | List XRP (Ripple) Transactions By Block Height


# **get_latest_mined_xrp__ripple_block**
> GetLatestMinedXRPRippleBlockR get_latest_mined_xrp__ripple_block(network)

Get Latest Mined XRP (Ripple) Block

Through this endpoint customers can fetch the last mined XRP block in the blockchain, along with its details. These could include the hash of the specific, the previous and the next block, its transactions count, its height, etc.     Since XRP is a different blockchain than Bitcoin and Ethereum, it isn't unified.

### Example

* Api Key Authentication (ApiKey):
```python
import time
import cryptoapis
from cryptoapis.api import xrp__ripple_api
from cryptoapis.model.get_latest_mined_xrp_ripple_block_r import GetLatestMinedXRPRippleBlockR
from cryptoapis.model.insufficient_credits import InsufficientCredits
from cryptoapis.model.invalid_api_key import InvalidApiKey
from cryptoapis.model.invalid_data import InvalidData
from cryptoapis.model.invalid_request_body_structure import InvalidRequestBodyStructure
from cryptoapis.model.request_limit_reached import RequestLimitReached
from cryptoapis.model.invalid_pagination import InvalidPagination
from cryptoapis.model.feature_mainnets_not_allowed_for_plan import FeatureMainnetsNotAllowedForPlan
from cryptoapis.model.unexpected_server_error import UnexpectedServerError
from cryptoapis.model.resource_not_found import ResourceNotFound
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
    api_instance = xrp__ripple_api.XRPRippleApi(api_client)
    network = "testnet" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\", \"rinkeby\" are test networks.
    context = "context_example" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Latest Mined XRP (Ripple) Block
        api_response = api_instance.get_latest_mined_xrp__ripple_block(network)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling XRPRippleApi->get_latest_mined_xrp__ripple_block: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Latest Mined XRP (Ripple) Block
        api_response = api_instance.get_latest_mined_xrp__ripple_block(network, context=context)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling XRPRippleApi->get_latest_mined_xrp__ripple_block: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot;, \&quot;rinkeby\&quot; are test networks. |
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]

### Return type

[**GetLatestMinedXRPRippleBlockR**](GetLatestMinedXRPRippleBlockR.md)

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
**404** | Resource not found |  -  |
**409** | The data provided seems to be invalid. |  -  |
**415** | The selected Media Type is unavailable. The Content-Type header should be &#39;application/json&#39;. |  -  |
**422** | Your request body for POST requests must have a structure of { data: { item: [...properties] } } |  -  |
**429** | The request limit has been reached. There can be maximum {requests} requests per {seconds} second(s) made. Please contact our team via email if you need more or upgrade your plan. |  -  |
**500** | An unexpected server error was encountered, we are working on fixing this. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_xrp__ripple_address_details**
> GetXRPRippleAddressDetailsR get_xrp__ripple_address_details(network, address)

Get XRP (Ripple) Address Details

Through this endpoint the customer can receive basic information about a given XRP address based on confirmed/synced blocks only. In the case where there are any incoming or outgoing **unconfirmed** transactions for the specific address, they **will not** be counted or calculated here.    Since XRP is a different blockchain than Bitcoin and Ethereum, it isn't unified.

### Example

* Api Key Authentication (ApiKey):
```python
import time
import cryptoapis
from cryptoapis.api import xrp__ripple_api
from cryptoapis.model.get_xrp_ripple_address_details_r import GetXRPRippleAddressDetailsR
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
    api_instance = xrp__ripple_api.XRPRippleApi(api_client)
    network = "testnet" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\",  are test networks.
    address = "rA9bXGJcXvZKaWofrRphdJsBWzhyCfH3z" # str | Represents the public address, which is a compressed and shortened form of a public key.
    context = "context_example" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get XRP (Ripple) Address Details
        api_response = api_instance.get_xrp__ripple_address_details(network, address)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling XRPRippleApi->get_xrp__ripple_address_details: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get XRP (Ripple) Address Details
        api_response = api_instance.get_xrp__ripple_address_details(network, address, context=context)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling XRPRippleApi->get_xrp__ripple_address_details: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;,  are test networks. |
 **address** | **str**| Represents the public address, which is a compressed and shortened form of a public key. |
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]

### Return type

[**GetXRPRippleAddressDetailsR**](GetXRPRippleAddressDetailsR.md)

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
**409** | Invalid data |  -  |
**415** | The selected Media Type is unavailable. The Content-Type header should be &#39;application/json&#39;. |  -  |
**422** | Your request body for POST requests must have a structure of { data: { item: [...properties] } } |  -  |
**429** | The request limit has been reached. There can be maximum {requests} requests per {seconds} second(s) made. Please contact our team via email if you need more or upgrade your plan. |  -  |
**500** | An unexpected server error was encountered, we are working on fixing this. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_xrp__ripple_block_details_by_block_hash**
> GetXRPRippleBlockDetailsByBlockHashR get_xrp__ripple_block_details_by_block_hash(network, block_hash)

Get XRP (Ripple) Block Details By Block Hash

Through this endpoint customers can obtain basic information about a given XRP block (a block on the XRP blockchain), specifically by using the `hash` parameter. These block details could include the hash of the specific, the previous and the next block, the number of included transactions, etc.     Since XRP is a different blockchain than Bitcoin and Ethereum, it isn't unified.

### Example

* Api Key Authentication (ApiKey):
```python
import time
import cryptoapis
from cryptoapis.api import xrp__ripple_api
from cryptoapis.model.get_xrp_ripple_block_details_by_block_hash_r import GetXRPRippleBlockDetailsByBlockHashR
from cryptoapis.model.insufficient_credits import InsufficientCredits
from cryptoapis.model.invalid_api_key import InvalidApiKey
from cryptoapis.model.invalid_data import InvalidData
from cryptoapis.model.invalid_request_body_structure import InvalidRequestBodyStructure
from cryptoapis.model.request_limit_reached import RequestLimitReached
from cryptoapis.model.invalid_pagination import InvalidPagination
from cryptoapis.model.feature_mainnets_not_allowed_for_plan import FeatureMainnetsNotAllowedForPlan
from cryptoapis.model.unexpected_server_error import UnexpectedServerError
from cryptoapis.model.resource_not_found import ResourceNotFound
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
    api_instance = xrp__ripple_api.XRPRippleApi(api_client)
    network = "testnet" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\",  are test networks.
    block_hash = "1ab0614d2a438da8b23086cbceef7d443edbd295d9c7619fc8a19c7618bc22c9" # str | Represents the hash of the block, which is its unique identifier. It represents a cryptographic digital fingerprint made by hashing the block header twice through the SHA256 algorithm.
    context = "context_example" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get XRP (Ripple) Block Details By Block Hash
        api_response = api_instance.get_xrp__ripple_block_details_by_block_hash(network, block_hash)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling XRPRippleApi->get_xrp__ripple_block_details_by_block_hash: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get XRP (Ripple) Block Details By Block Hash
        api_response = api_instance.get_xrp__ripple_block_details_by_block_hash(network, block_hash, context=context)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling XRPRippleApi->get_xrp__ripple_block_details_by_block_hash: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;,  are test networks. |
 **block_hash** | **str**| Represents the hash of the block, which is its unique identifier. It represents a cryptographic digital fingerprint made by hashing the block header twice through the SHA256 algorithm. |
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]

### Return type

[**GetXRPRippleBlockDetailsByBlockHashR**](GetXRPRippleBlockDetailsByBlockHashR.md)

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
**404** | Resource not found |  -  |
**409** | Invalid data |  -  |
**415** | The selected Media Type is unavailable. The Content-Type header should be &#39;application/json&#39;. |  -  |
**422** | Your request body for POST requests must have a structure of { data: { item: [...properties] } } |  -  |
**429** | The request limit has been reached. There can be maximum {requests} requests per {seconds} second(s) made. Please contact our team via email if you need more or upgrade your plan. |  -  |
**500** | An unexpected server error was encountered, we are working on fixing this. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_xrp__ripple_block_details_by_block_height**
> GetXRPRippleBlockDetailsByBlockHeightR get_xrp__ripple_block_details_by_block_height(network, block_height)

Get XRP (Ripple) Block Details By Block Height

Through this endpoint customers can obtain basic information about a given XRP block (a block on the XRP blockchain), specifically by using the `height` parameter. These block details could include the hash of the specific, the previous and the next block, its transactions count, etc.    Since XRP is a different blockchain than Bitcoin and Ethereum, it isn't unified.

### Example

* Api Key Authentication (ApiKey):
```python
import time
import cryptoapis
from cryptoapis.api import xrp__ripple_api
from cryptoapis.model.get_xrp_ripple_block_details_by_block_height_r import GetXRPRippleBlockDetailsByBlockHeightR
from cryptoapis.model.insufficient_credits import InsufficientCredits
from cryptoapis.model.invalid_api_key import InvalidApiKey
from cryptoapis.model.invalid_data import InvalidData
from cryptoapis.model.invalid_request_body_structure import InvalidRequestBodyStructure
from cryptoapis.model.request_limit_reached import RequestLimitReached
from cryptoapis.model.invalid_pagination import InvalidPagination
from cryptoapis.model.feature_mainnets_not_allowed_for_plan import FeatureMainnetsNotAllowedForPlan
from cryptoapis.model.unexpected_server_error import UnexpectedServerError
from cryptoapis.model.resource_not_found import ResourceNotFound
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
    api_instance = xrp__ripple_api.XRPRippleApi(api_client)
    network = "testnet" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\",  are test networks.
    block_height = "15886156" # str | Represents the number of blocks in the blockchain preceding this specific block. Block numbers have no gaps. A blockchain usually starts with block 0 called the \"Genesis block\".
    context = "context_example" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get XRP (Ripple) Block Details By Block Height
        api_response = api_instance.get_xrp__ripple_block_details_by_block_height(network, block_height)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling XRPRippleApi->get_xrp__ripple_block_details_by_block_height: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get XRP (Ripple) Block Details By Block Height
        api_response = api_instance.get_xrp__ripple_block_details_by_block_height(network, block_height, context=context)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling XRPRippleApi->get_xrp__ripple_block_details_by_block_height: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;,  are test networks. |
 **block_height** | **str**| Represents the number of blocks in the blockchain preceding this specific block. Block numbers have no gaps. A blockchain usually starts with block 0 called the \&quot;Genesis block\&quot;. |
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]

### Return type

[**GetXRPRippleBlockDetailsByBlockHeightR**](GetXRPRippleBlockDetailsByBlockHeightR.md)

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
**404** | Resource not found |  -  |
**409** | Invalid data |  -  |
**415** | The selected Media Type is unavailable. The Content-Type header should be &#39;application/json&#39;. |  -  |
**422** | Your request body for POST requests must have a structure of { data: { item: [...properties] } } |  -  |
**429** | The request limit has been reached. There can be maximum {requests} requests per {seconds} second(s) made. Please contact our team via email if you need more or upgrade your plan. |  -  |
**500** | An unexpected server error was encountered, we are working on fixing this. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_xrp__ripple_transaction_details_by_transaction_id**
> GetXRPRippleTransactionDetailsByTransactionIDR get_xrp__ripple_transaction_details_by_transaction_id(network, transaction_hash)

Get XRP (Ripple) Transaction Details By Transaction ID

Through this endpoint customers can obtain details about a XRP transaction by the transaction's unique identifier.     Since XRP is a different blockchain than Bitcoin and Ethereum, it isn't unified.

### Example

* Api Key Authentication (ApiKey):
```python
import time
import cryptoapis
from cryptoapis.api import xrp__ripple_api
from cryptoapis.model.insufficient_credits import InsufficientCredits
from cryptoapis.model.invalid_api_key import InvalidApiKey
from cryptoapis.model.invalid_data import InvalidData
from cryptoapis.model.invalid_request_body_structure import InvalidRequestBodyStructure
from cryptoapis.model.request_limit_reached import RequestLimitReached
from cryptoapis.model.invalid_pagination import InvalidPagination
from cryptoapis.model.get_xrp_ripple_transaction_details_by_transaction_idr import GetXRPRippleTransactionDetailsByTransactionIDR
from cryptoapis.model.feature_mainnets_not_allowed_for_plan import FeatureMainnetsNotAllowedForPlan
from cryptoapis.model.unexpected_server_error import UnexpectedServerError
from cryptoapis.model.resource_not_found import ResourceNotFound
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
    api_instance = xrp__ripple_api.XRPRippleApi(api_client)
    network = "testnet" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\", \"rinkeby\" are test networks.
    transaction_hash = "36a1737481edec87bacc3101dfb752ae2c76f9171e7edebe587e330c1ea77c8d" # str | Represents the same as `transactionId` for account-based protocols like Ethereum, while it could be different in UTXO-based protocols like Bitcoin. E.g., in UTXO-based protocols `hash` is different from `transactionId` for SegWit transactions.
    context = "context_example" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get XRP (Ripple) Transaction Details By Transaction ID
        api_response = api_instance.get_xrp__ripple_transaction_details_by_transaction_id(network, transaction_hash)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling XRPRippleApi->get_xrp__ripple_transaction_details_by_transaction_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get XRP (Ripple) Transaction Details By Transaction ID
        api_response = api_instance.get_xrp__ripple_transaction_details_by_transaction_id(network, transaction_hash, context=context)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling XRPRippleApi->get_xrp__ripple_transaction_details_by_transaction_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot;, \&quot;rinkeby\&quot; are test networks. |
 **transaction_hash** | **str**| Represents the same as &#x60;transactionId&#x60; for account-based protocols like Ethereum, while it could be different in UTXO-based protocols like Bitcoin. E.g., in UTXO-based protocols &#x60;hash&#x60; is different from &#x60;transactionId&#x60; for SegWit transactions. |
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]

### Return type

[**GetXRPRippleTransactionDetailsByTransactionIDR**](GetXRPRippleTransactionDetailsByTransactionIDR.md)

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
**404** | Resource not found |  -  |
**409** | Invalid data |  -  |
**415** | The selected Media Type is unavailable. The Content-Type header should be &#39;application/json&#39;. |  -  |
**422** | Your request body for POST requests must have a structure of { data: { item: [...properties] } } |  -  |
**429** | The request limit has been reached. There can be maximum {requests} requests per {seconds} second(s) made. Please contact our team via email if you need more or upgrade your plan. |  -  |
**500** | An unexpected server error was encountered, we are working on fixing this. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_xrp__ripple_transactions_by_address**
> ListXRPRippleTransactionsByAddressR list_xrp__ripple_transactions_by_address(network, address)

List XRP (Ripple) Transactions by Address

This endpoint will list XRP transactions by a attribute `address`. The transactions listed will detail additional information such as hash, height, time of creation in Unix timestamp, etc.    Since XRP is a different blockchain than Bitcoin and Ethereum, it isn't unified.    {note}Please note that listing data from the same type will apply pagination on the results.{/note}

### Example

* Api Key Authentication (ApiKey):
```python
import time
import cryptoapis
from cryptoapis.api import xrp__ripple_api
from cryptoapis.model.insufficient_credits import InsufficientCredits
from cryptoapis.model.invalid_api_key import InvalidApiKey
from cryptoapis.model.invalid_data import InvalidData
from cryptoapis.model.invalid_request_body_structure import InvalidRequestBodyStructure
from cryptoapis.model.request_limit_reached import RequestLimitReached
from cryptoapis.model.invalid_pagination import InvalidPagination
from cryptoapis.model.feature_mainnets_not_allowed_for_plan import FeatureMainnetsNotAllowedForPlan
from cryptoapis.model.list_xrp_ripple_transactions_by_address_r import ListXRPRippleTransactionsByAddressR
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
    api_instance = xrp__ripple_api.XRPRippleApi(api_client)
    network = "testnet" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\",  are test networks.
    address = "rA9bXGJcXvZKaWofrRphdJsBWzhyCfH3z" # str | Represents the public address, which is a compressed and shortened form of a public key.
    context = "context_example" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    limit = 50 # int | Defines how many items should be returned in the response per page basis. (optional) if omitted the server will use the default value of 50
    offset = 10 # int | The starting index of the response items, i.e. where the response should start listing the returned items. (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    try:
        # List XRP (Ripple) Transactions by Address
        api_response = api_instance.list_xrp__ripple_transactions_by_address(network, address)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling XRPRippleApi->list_xrp__ripple_transactions_by_address: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List XRP (Ripple) Transactions by Address
        api_response = api_instance.list_xrp__ripple_transactions_by_address(network, address, context=context, limit=limit, offset=offset)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling XRPRippleApi->list_xrp__ripple_transactions_by_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;,  are test networks. |
 **address** | **str**| Represents the public address, which is a compressed and shortened form of a public key. |
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]
 **limit** | **int**| Defines how many items should be returned in the response per page basis. | [optional] if omitted the server will use the default value of 50
 **offset** | **int**| The starting index of the response items, i.e. where the response should start listing the returned items. | [optional] if omitted the server will use the default value of 0

### Return type

[**ListXRPRippleTransactionsByAddressR**](ListXRPRippleTransactionsByAddressR.md)

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
**409** | Invalid data |  -  |
**415** | The selected Media Type is unavailable. The Content-Type header should be &#39;application/json&#39;. |  -  |
**422** | Your request body for POST requests must have a structure of { data: { item: [...properties] } } |  -  |
**429** | The request limit has been reached. There can be maximum {requests} requests per {seconds} second(s) made. Please contact our team via email if you need more or upgrade your plan. |  -  |
**500** | An unexpected server error was encountered, we are working on fixing this. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_xrp__ripple_transactions_by_block_hash**
> ListXRPRippleTransactionsByBlockHashR list_xrp__ripple_transactions_by_block_hash(network, block_hash)

List XRP (Ripple) Transactions By Block Hash

This endpoint will list transactions by an attribute `blockHash`. The transactions listed will detail additional information such as hash, addresses, time of creation in Unix timestamp, etc.    Since XRP is a different blockchain than Bitcoin and Ethereum, it isn't unified.    {note}Please note that listing data from the same type will apply pagination on the results.{/note}

### Example

* Api Key Authentication (ApiKey):
```python
import time
import cryptoapis
from cryptoapis.api import xrp__ripple_api
from cryptoapis.model.insufficient_credits import InsufficientCredits
from cryptoapis.model.invalid_api_key import InvalidApiKey
from cryptoapis.model.invalid_data import InvalidData
from cryptoapis.model.invalid_request_body_structure import InvalidRequestBodyStructure
from cryptoapis.model.request_limit_reached import RequestLimitReached
from cryptoapis.model.invalid_pagination import InvalidPagination
from cryptoapis.model.feature_mainnets_not_allowed_for_plan import FeatureMainnetsNotAllowedForPlan
from cryptoapis.model.list_xrp_ripple_transactions_by_block_hash_r import ListXRPRippleTransactionsByBlockHashR
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
    api_instance = xrp__ripple_api.XRPRippleApi(api_client)
    network = "testnet" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\", \"rinkeby\" are test networks.
    block_hash = "14754656235f865a74eba27791fd41a47bdfe07fe811ff6d78f53db32e129e39" # str | Represents the hash of the block, which is its unique identifier. It represents a cryptographic digital fingerprint made by hashing the block header twice through the SHA256 algorithm.
    context = "context_example" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    limit = 50 # int | Defines how many items should be returned in the response per page basis. (optional) if omitted the server will use the default value of 50
    offset = 10 # int | The starting index of the response items, i.e. where the response should start listing the returned items. (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    try:
        # List XRP (Ripple) Transactions By Block Hash
        api_response = api_instance.list_xrp__ripple_transactions_by_block_hash(network, block_hash)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling XRPRippleApi->list_xrp__ripple_transactions_by_block_hash: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List XRP (Ripple) Transactions By Block Hash
        api_response = api_instance.list_xrp__ripple_transactions_by_block_hash(network, block_hash, context=context, limit=limit, offset=offset)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling XRPRippleApi->list_xrp__ripple_transactions_by_block_hash: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot;, \&quot;rinkeby\&quot; are test networks. |
 **block_hash** | **str**| Represents the hash of the block, which is its unique identifier. It represents a cryptographic digital fingerprint made by hashing the block header twice through the SHA256 algorithm. |
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]
 **limit** | **int**| Defines how many items should be returned in the response per page basis. | [optional] if omitted the server will use the default value of 50
 **offset** | **int**| The starting index of the response items, i.e. where the response should start listing the returned items. | [optional] if omitted the server will use the default value of 0

### Return type

[**ListXRPRippleTransactionsByBlockHashR**](ListXRPRippleTransactionsByBlockHashR.md)

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
**409** | Invalid data |  -  |
**415** | The selected Media Type is unavailable. The Content-Type header should be &#39;application/json&#39;. |  -  |
**422** | Your request body for POST requests must have a structure of { data: { item: [...properties] } } |  -  |
**429** | The request limit has been reached. There can be maximum {requests} requests per {seconds} second(s) made. Please contact our team via email if you need more or upgrade your plan. |  -  |
**500** | An unexpected server error was encountered, we are working on fixing this. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_xrp__ripple_transactions_by_block_height**
> ListXRPRippleTransactionsByBlockHeightR list_xrp__ripple_transactions_by_block_height(network, block_height)

List XRP (Ripple) Transactions By Block Height

This endpoint will list transactions by an attribute `blockHeight`. The transactions listed will detail additional information such as hash, addresses, time of creation in Unix timestamp, etc.    Since XRP is a different blockchain than Bitcoin and Ethereum, it isn't unified.    {note}Please note that listing data from the same type will apply pagination on the results.{/note}

### Example

* Api Key Authentication (ApiKey):
```python
import time
import cryptoapis
from cryptoapis.api import xrp__ripple_api
from cryptoapis.model.insufficient_credits import InsufficientCredits
from cryptoapis.model.invalid_api_key import InvalidApiKey
from cryptoapis.model.invalid_data import InvalidData
from cryptoapis.model.invalid_request_body_structure import InvalidRequestBodyStructure
from cryptoapis.model.request_limit_reached import RequestLimitReached
from cryptoapis.model.invalid_pagination import InvalidPagination
from cryptoapis.model.feature_mainnets_not_allowed_for_plan import FeatureMainnetsNotAllowedForPlan
from cryptoapis.model.list_xrp_ripple_transactions_by_block_height_r import ListXRPRippleTransactionsByBlockHeightR
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
    api_instance = xrp__ripple_api.XRPRippleApi(api_client)
    network = "testnet" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\", \"rinkeby\" are test networks.
    block_height = 15971358 # int | 
    context = "context_example" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    limit = 50 # int | Defines how many items should be returned in the response per page basis. (optional) if omitted the server will use the default value of 50
    offset = 10 # int | The starting index of the response items, i.e. where the response should start listing the returned items. (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    try:
        # List XRP (Ripple) Transactions By Block Height
        api_response = api_instance.list_xrp__ripple_transactions_by_block_height(network, block_height)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling XRPRippleApi->list_xrp__ripple_transactions_by_block_height: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List XRP (Ripple) Transactions By Block Height
        api_response = api_instance.list_xrp__ripple_transactions_by_block_height(network, block_height, context=context, limit=limit, offset=offset)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling XRPRippleApi->list_xrp__ripple_transactions_by_block_height: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot;, \&quot;rinkeby\&quot; are test networks. |
 **block_height** | **int**|  |
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]
 **limit** | **int**| Defines how many items should be returned in the response per page basis. | [optional] if omitted the server will use the default value of 50
 **offset** | **int**| The starting index of the response items, i.e. where the response should start listing the returned items. | [optional] if omitted the server will use the default value of 0

### Return type

[**ListXRPRippleTransactionsByBlockHeightR**](ListXRPRippleTransactionsByBlockHeightR.md)

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
**409** | Invalid data |  -  |
**415** | The selected Media Type is unavailable. The Content-Type header should be &#39;application/json&#39;. |  -  |
**422** | Your request body for POST requests must have a structure of { data: { item: [...properties] } } |  -  |
**429** | The request limit has been reached. There can be maximum {requests} requests per {seconds} second(s) made. Please contact our team via email if you need more or upgrade your plan. |  -  |
**500** | An unexpected server error was encountered, we are working on fixing this. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

