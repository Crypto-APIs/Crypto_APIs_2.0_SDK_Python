# cryptoapis.GeneratingApi

All URIs are relative to *https://rest.cryptoapis.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_deposit_address**](GeneratingApi.md#generate_deposit_address) | **POST** /wallet-as-a-service/wallets/{walletId}/{blockchain}/{network}/addresses | Generate Deposit Address


# **generate_deposit_address**
> GenerateDepositAddressR generate_deposit_address(blockchain, network, wallet_id)

Generate Deposit Address

Through this endpoint customers can generate a new Receiving/Deposit Addresses into their Wallet.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import generating_api
from cryptoapis.model.inline_response4008 import InlineResponse4008
from cryptoapis.model.inline_response429 import InlineResponse429
from cryptoapis.model.inline_response422 import InlineResponse422
from cryptoapis.model.inline_response409 import InlineResponse409
from cryptoapis.model.inline_response402 import InlineResponse402
from cryptoapis.model.inline_response4041 import InlineResponse4041
from cryptoapis.model.inline_response500 import InlineResponse500
from cryptoapis.model.generate_deposit_address_r import GenerateDepositAddressR
from cryptoapis.model.inline_response415 import InlineResponse415
from cryptoapis.model.generate_deposit_address_rb import GenerateDepositAddressRB
from cryptoapis.model.inline_response4018 import InlineResponse4018
from cryptoapis.model.inline_response4038 import InlineResponse4038
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
    network = "testnet" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    wallet_id = "60c9d9921c38030006675ff6" # str | Represents the unique ID of the specific Wallet.
    context = "yourExampleString" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    generate_deposit_address_rb = GenerateDepositAddressRB(
        context="yourExampleString",
        data=GenerateDepositAddressRBData(
            item=GenerateDepositAddressRBDataItem(
                label="yourLabelStringHere",
            ),
        ),
    ) # GenerateDepositAddressRB |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Generate Deposit Address
        api_response = api_instance.generate_deposit_address(blockchain, network, wallet_id)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling GeneratingApi->generate_deposit_address: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Generate Deposit Address
        api_response = api_instance.generate_deposit_address(blockchain, network, wallet_id, context=context, generate_deposit_address_rb=generate_deposit_address_rb)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling GeneratingApi->generate_deposit_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. |
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. |
 **wallet_id** | **str**| Represents the unique ID of the specific Wallet. |
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]
 **generate_deposit_address_rb** | [**GenerateDepositAddressRB**](GenerateDepositAddressRB.md)|  | [optional]

### Return type

[**GenerateDepositAddressR**](GenerateDepositAddressR.md)

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
**404** | The specified resource has not been found. |  -  |
**409** | The data provided seems to be invalid. |  -  |
**415** | The selected Media Type is unavailable. The Content-Type header should be &#39;application/json&#39;. |  -  |
**422** | Your request body for POST requests must have a structure of { data: { item: [...properties] } } |  -  |
**429** | The request limit has been reached. There can be maximum {requests} requests per {seconds} second(s) made. Please contact our team via email if you need more or upgrade your plan. |  -  |
**500** | An unexpected server error has occurred, we are working to fix this. Please try again later and in case it occurs again please report it to our team via email. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

