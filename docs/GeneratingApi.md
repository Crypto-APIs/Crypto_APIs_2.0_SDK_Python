# cryptoapis.GeneratingApi

All URIs are relative to *https://rest.cryptoapis.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_receiving_address**](GeneratingApi.md#generate_receiving_address) | **POST** /wallet-as-a-service/wallets/{walletId}/{blockchain}/{network}/addresses | Generate Receiving Address


# **generate_receiving_address**
> GenerateReceivingAddressR generate_receiving_address(blockchain, network, wallet_id)

Generate Receiving Address

Through this endpoint customers can generate a new Receiving/Deposit Addresses into their Wallet.

### Example

* Api Key Authentication (ApiKey):
```python
import time
import cryptoapis
from cryptoapis.api import generating_api
from cryptoapis.model.wallet_as_a_service_deposit_addresses_limit_reached import WalletAsAServiceDepositAddressesLimitReached
from cryptoapis.model.insufficient_credits import InsufficientCredits
from cryptoapis.model.invalid_api_key import InvalidApiKey
from cryptoapis.model.invalid_data import InvalidData
from cryptoapis.model.invalid_request_body_structure import InvalidRequestBodyStructure
from cryptoapis.model.request_limit_reached import RequestLimitReached
from cryptoapis.model.generate_receiving_address_r import GenerateReceivingAddressR
from cryptoapis.model.invalid_pagination import InvalidPagination
from cryptoapis.model.generate_receiving_address_rb import GenerateReceivingAddressRB
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
    api_instance = generating_api.GeneratingApi(api_client)
    blockchain = "bitcoin" # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    network = "testnet" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\", \"rinkeby\" are test networks.
    wallet_id = "60c9d9921c38030006675ff6" # str | Represents the unique ID of the specific Wallet.
    context = "context_example" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    generate_receiving_address_rb = GenerateReceivingAddressRB(
        context="context_example",
        data=GenerateReceivingAddressRBData(
            item=GenerateReceivingAddressRBDataItem(
                label="yourLabelStringHere",
            ),
        ),
    ) # GenerateReceivingAddressRB |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Generate Receiving Address
        api_response = api_instance.generate_receiving_address(blockchain, network, wallet_id)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling GeneratingApi->generate_receiving_address: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Generate Receiving Address
        api_response = api_instance.generate_receiving_address(blockchain, network, wallet_id, context=context, generate_receiving_address_rb=generate_receiving_address_rb)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling GeneratingApi->generate_receiving_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. |
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot;, \&quot;rinkeby\&quot; are test networks. |
 **wallet_id** | **str**| Represents the unique ID of the specific Wallet. |
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]
 **generate_receiving_address_rb** | [**GenerateReceivingAddressRB**](GenerateReceivingAddressRB.md)|  | [optional]

### Return type

[**GenerateReceivingAddressR**](GenerateReceivingAddressR.md)

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
**403** | You have reached the maximum Deposit Addresses count which is currently {depositAddressesCount}. Please, upgrade your plan in order to have a higher Deposit Address count. |  -  |
**404** | The specified resource has not been found. |  -  |
**409** | The data provided seems to be invalid. |  -  |
**415** | The selected Media Type is unavailable. The Content-Type header should be &#39;application/json&#39;. |  -  |
**422** | Your request body for POST requests must have a structure of { data: { item: [...properties] } } |  -  |
**429** | The request limit has been reached. There can be maximum {requests} requests per {seconds} second(s) made. Please contact our team via email if you need more or upgrade your plan. |  -  |
**500** | An unexpected server error has occurred, we are working to fix this. Please try again later and in case it occurs again please report it to our team via email. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
