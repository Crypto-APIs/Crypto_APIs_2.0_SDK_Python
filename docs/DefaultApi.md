# cryptoapis.DefaultApi

All URIs are relative to *https://rest.cryptoapis.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_contract_details_by_address**](DefaultApi.md#get_contract_details_by_address) | **GET** /blockchain-data/{blockchain}/{network}/addresses/{contractAddress}/contract | Get Contract Details by Address


# **get_contract_details_by_address**
> GetContractDetailsByAddressResponse get_contract_details_by_address(blockchain, network, contract_address)

Get Contract Details by Address

This endpoint will return a smart contract details by address, this address is the address of the smart contract. It's not the same as the smart contract creator address.

### Example

* Api Key Authentication (ApiKey):
```python
import time
import cryptoapis
from cryptoapis.api import default_api
from cryptoapis.model.get_contract_details_by_address_response import GetContractDetailsByAddressResponse
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
    api_instance = default_api.DefaultApi(api_client)
    blockchain = "ethereum" # str | 
    network = "mainnet" # str | 
    contract_address = "contractAddress_example" # str | String identifier of the token
    context = "context_example" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Contract Details by Address
        api_response = api_instance.get_contract_details_by_address(blockchain, network, contract_address)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling DefaultApi->get_contract_details_by_address: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Contract Details by Address
        api_response = api_instance.get_contract_details_by_address(blockchain, network, contract_address, context=context)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling DefaultApi->get_contract_details_by_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain** | **str**|  |
 **network** | **str**|  |
 **contract_address** | **str**| String identifier of the token |
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]

### Return type

[**GetContractDetailsByAddressResponse**](GetContractDetailsByAddressResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TBD |  -  |
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

