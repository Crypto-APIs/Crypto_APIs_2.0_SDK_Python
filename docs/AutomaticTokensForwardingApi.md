# cryptoapis.AutomaticTokensForwardingApi

All URIs are relative to *https://rest.cryptoapis.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_tokens_to_existing_from_address**](AutomaticTokensForwardingApi.md#add_tokens_to_existing_from_address) | **POST** /blockchain-automations/{blockchain}/{network}/tokens-forwarding/automations/add-token | Add Tokens To Existing fromAddress
[**create_automatic_tokens_forwarding**](AutomaticTokensForwardingApi.md#create_automatic_tokens_forwarding) | **POST** /blockchain-automations/{blockchain}/{network}/tokens-forwarding/automations | Create Automatic Tokens Forwarding
[**delete_automatic_tokens_forwarding**](AutomaticTokensForwardingApi.md#delete_automatic_tokens_forwarding) | **DELETE** /blockchain-automations/{blockchain}/{network}/tokens-forwarding/automations/{referenceId} | Delete Automatic Tokens Forwarding
[**get_fee_address_details**](AutomaticTokensForwardingApi.md#get_fee_address_details) | **GET** /blockchain-automations/{blockchain}/{network}/tokens-forwarding/fee-addresses | Get Fee Address Details
[**list_tokens_forwarding_automations**](AutomaticTokensForwardingApi.md#list_tokens_forwarding_automations) | **GET** /blockchain-automations/{blockchain}/{network}/tokens-forwarding/automations | List Tokens Forwarding Automations


# **add_tokens_to_existing_from_address**
> AddTokensToExistingFromAddressR add_tokens_to_existing_from_address(blockchain, network)

Add Tokens To Existing fromAddress

Through this endpoint customers can add **Automatic Tokens forwardings** to an already existing `fromAddress`. Unlike the \"Create Automatic Tokens Forwarding\" endpoint, where the `fromAddress` is generated each time, with this endpoint customers can add an automation from another token to one and the same `fromAddress`.    The `fromAddress` can be used as a deposit address. Any funds received by this address will be automatically forwarded to `toAddress` based on what the customer has set for the automation. The  `toAddress` is essentially the main address and destination for the automatic tokens forwarding.    There is also a `minimumTransferAmount` which only when reached will then trigger the forwarding. Through this the customer can save from fees.    Moreover, `feePriority` can be also set,  which defines how quickly to move the tokens once they are received. The higher priority, the larger the fee will be. It can be \"SLOW\", \"STANDARD\" or \"FAST\".    For this automatic forwarding the customer can set a callback subscription.    {warning}Currently we support fungible tokens (ERC-20) **only**, NFTs (ERC-721) are **not** supported.{/warning}    {warning}The subscription will work for all incoming transactions until it is deleted. There is no need to do that for every transaction.{/warning}

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import automatic_tokens_forwarding_api
from cryptoapis.model.convert_bitcoin_cash_address429_response import ConvertBitcoinCashAddress429Response
from cryptoapis.model.convert_bitcoin_cash_address500_response import ConvertBitcoinCashAddress500Response
from cryptoapis.model.convert_bitcoin_cash_address422_response import ConvertBitcoinCashAddress422Response
from cryptoapis.model.add_tokens_to_existing_from_address401_response import AddTokensToExistingFromAddress401Response
from cryptoapis.model.add_tokens_to_existing_from_address403_response import AddTokensToExistingFromAddress403Response
from cryptoapis.model.add_tokens_to_existing_from_address_rb import AddTokensToExistingFromAddressRB
from cryptoapis.model.get_xrp_ripple_transaction_details_by_transaction_id404_response import GetXRPRippleTransactionDetailsByTransactionID404Response
from cryptoapis.model.add_tokens_to_existing_from_address400_response import AddTokensToExistingFromAddress400Response
from cryptoapis.model.convert_bitcoin_cash_address402_response import ConvertBitcoinCashAddress402Response
from cryptoapis.model.convert_bitcoin_cash_address409_response import ConvertBitcoinCashAddress409Response
from cryptoapis.model.add_tokens_to_existing_from_address_r import AddTokensToExistingFromAddressR
from cryptoapis.model.convert_bitcoin_cash_address415_response import ConvertBitcoinCashAddress415Response
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
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with cryptoapis.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = automatic_tokens_forwarding_api.AutomaticTokensForwardingApi(api_client)
    blockchain = "bitcoin" # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    network = "testnet" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    context = "yourExampleString" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    add_tokens_to_existing_from_address_rb = AddTokensToExistingFromAddressRB(
        context="yourExampleString",
        data=AddTokensToExistingFromAddressRBData(
            item=AddTokensToExistingFromAddressRBDataItem(
                callback_secret_key="yourSecretString",
                callback_url="https://example.com",
                confirmations_count=3,
                fee_priority="standard",
                from_address="mizRduUBKEbJ6uzYJUegPh78gEGgM3WjAr",
                minimum_transfer_amount="0.00001",
                to_address="mnumE76iEKN47bUsdni85oped5D1fRwKWi",
                token_data=AddTokensToExistingFromAddressRBTokenData(),
            ),
        ),
    ) # AddTokensToExistingFromAddressRB |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add Tokens To Existing fromAddress
        api_response = api_instance.add_tokens_to_existing_from_address(blockchain, network)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling AutomaticTokensForwardingApi->add_tokens_to_existing_from_address: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add Tokens To Existing fromAddress
        api_response = api_instance.add_tokens_to_existing_from_address(blockchain, network, context=context, add_tokens_to_existing_from_address_rb=add_tokens_to_existing_from_address_rb)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling AutomaticTokensForwardingApi->add_tokens_to_existing_from_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. |
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. |
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]
 **add_tokens_to_existing_from_address_rb** | [**AddTokensToExistingFromAddressRB**](AddTokensToExistingFromAddressRB.md)|  | [optional]

### Return type

[**AddTokensToExistingFromAddressR**](AddTokensToExistingFromAddressR.md)

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

# **create_automatic_tokens_forwarding**
> CreateAutomaticTokensForwardingR create_automatic_tokens_forwarding(blockchain, network)

Create Automatic Tokens Forwarding

Through this endpoint customers can set up an automatic forwarding function specifically for tokens (**not** coins). They can have a `toAddress` which is essentially the main address and the destination for the automatic tokens forwarding.     There is also a `minimumTransferAmount` which only when reached will then trigger the forwarding. Through this the customer can save from fees.    Moreover, `feePriority` can be also set,  which defines how quickly to move the tokens once they are received. The higher priority, the larger the fee will be. It can be \"SLOW\", \"STANDARD\" or \"FAST\".    The response of this endpoint contains an attribute `fromAddress` which can be used as a deposit address. Any funds received by this address will be automatically forwarded to `toAddress` based on what the customer has set for the automation.    For this automatic forwarding the customer can set a callback subscription.    {warning}Currently we support fungible tokens (ERC-20) **only**, NFTs (ERC-721) are **not** supported.{/warning}    {warning}The subscription will work for all incoming transactions until it is deleted. There is no need to do that for every transaction.{/warning}    {note}This endpoint generates a new `fromAddress` each time.{/note}

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import automatic_tokens_forwarding_api
from cryptoapis.model.convert_bitcoin_cash_address429_response import ConvertBitcoinCashAddress429Response
from cryptoapis.model.convert_bitcoin_cash_address500_response import ConvertBitcoinCashAddress500Response
from cryptoapis.model.create_automatic_tokens_forwarding_rb import CreateAutomaticTokensForwardingRB
from cryptoapis.model.convert_bitcoin_cash_address422_response import ConvertBitcoinCashAddress422Response
from cryptoapis.model.create_automatic_tokens_forwarding400_response import CreateAutomaticTokensForwarding400Response
from cryptoapis.model.get_xrp_ripple_transaction_details_by_transaction_id404_response import GetXRPRippleTransactionDetailsByTransactionID404Response
from cryptoapis.model.convert_bitcoin_cash_address402_response import ConvertBitcoinCashAddress402Response
from cryptoapis.model.convert_bitcoin_cash_address409_response import ConvertBitcoinCashAddress409Response
from cryptoapis.model.create_automatic_tokens_forwarding401_response import CreateAutomaticTokensForwarding401Response
from cryptoapis.model.create_automatic_tokens_forwarding_r import CreateAutomaticTokensForwardingR
from cryptoapis.model.create_automatic_tokens_forwarding403_response import CreateAutomaticTokensForwarding403Response
from cryptoapis.model.convert_bitcoin_cash_address415_response import ConvertBitcoinCashAddress415Response
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
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with cryptoapis.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = automatic_tokens_forwarding_api.AutomaticTokensForwardingApi(api_client)
    blockchain = "bitcoin" # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    network = "testnet" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    context = "yourExampleString" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    create_automatic_tokens_forwarding_rb = CreateAutomaticTokensForwardingRB(
        context="yourExampleString",
        data=CreateAutomaticTokensForwardingRBData(
            item=CreateAutomaticTokensForwardingRBDataItem(
                callback_secret_key="yourSecretString",
                callback_url="https://example.com",
                confirmations_count="3",
                fee_priority="standard",
                minimum_transfer_amount="0.00002",
                to_address="tb1q54j7qcu7kgsrx87yn0r9zjdvsxrnvxg4qua2z6",
                token_data=CreateAutomaticTokensForwardingRBTokenData(),
            ),
        ),
    ) # CreateAutomaticTokensForwardingRB |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create Automatic Tokens Forwarding
        api_response = api_instance.create_automatic_tokens_forwarding(blockchain, network)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling AutomaticTokensForwardingApi->create_automatic_tokens_forwarding: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Automatic Tokens Forwarding
        api_response = api_instance.create_automatic_tokens_forwarding(blockchain, network, context=context, create_automatic_tokens_forwarding_rb=create_automatic_tokens_forwarding_rb)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling AutomaticTokensForwardingApi->create_automatic_tokens_forwarding: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. |
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. |
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]
 **create_automatic_tokens_forwarding_rb** | [**CreateAutomaticTokensForwardingRB**](CreateAutomaticTokensForwardingRB.md)|  | [optional]

### Return type

[**CreateAutomaticTokensForwardingR**](CreateAutomaticTokensForwardingR.md)

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

# **delete_automatic_tokens_forwarding**
> DeleteAutomaticTokensForwardingR delete_automatic_tokens_forwarding(blockchain, network, reference_id)

Delete Automatic Tokens Forwarding

Through this endpoint customers can delete a forwarding function they have set for **tokens** (**not** coins).    By setting a `fromAddress` and a `toAddress`, and specifying the amount, tokens can be transferred between addresses.     A `feePriority` will be returned which represents the fee priority of the automation whether it is \"SLOW\", \"STANDARD\" OR \"FAST\".    {warning}Currently we support fungible tokens (ERC-20) **only**, NFTs (ERC-721) are **not** supported.{/warning}    {warning}The subscription will work for all incoming transactions until it is deleted. There is no need to do that for every transaction.{/warning}

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import automatic_tokens_forwarding_api
from cryptoapis.model.convert_bitcoin_cash_address429_response import ConvertBitcoinCashAddress429Response
from cryptoapis.model.convert_bitcoin_cash_address500_response import ConvertBitcoinCashAddress500Response
from cryptoapis.model.delete_automatic_tokens_forwarding401_response import DeleteAutomaticTokensForwarding401Response
from cryptoapis.model.delete_automatic_tokens_forwarding403_response import DeleteAutomaticTokensForwarding403Response
from cryptoapis.model.convert_bitcoin_cash_address422_response import ConvertBitcoinCashAddress422Response
from cryptoapis.model.delete_automatic_tokens_forwarding_r import DeleteAutomaticTokensForwardingR
from cryptoapis.model.delete_automatic_tokens_forwarding400_response import DeleteAutomaticTokensForwarding400Response
from cryptoapis.model.get_xrp_ripple_transaction_details_by_transaction_id404_response import GetXRPRippleTransactionDetailsByTransactionID404Response
from cryptoapis.model.convert_bitcoin_cash_address402_response import ConvertBitcoinCashAddress402Response
from cryptoapis.model.convert_bitcoin_cash_address409_response import ConvertBitcoinCashAddress409Response
from cryptoapis.model.convert_bitcoin_cash_address415_response import ConvertBitcoinCashAddress415Response
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
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with cryptoapis.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = automatic_tokens_forwarding_api.AutomaticTokensForwardingApi(api_client)
    blockchain = "bitcoin" # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    network = "testnet" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    reference_id = "6017dd02a309213863be9e55" # str | Represents a unique ID used to reference the specific callback subscription.
    context = "yourExampleString" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete Automatic Tokens Forwarding
        api_response = api_instance.delete_automatic_tokens_forwarding(blockchain, network, reference_id)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling AutomaticTokensForwardingApi->delete_automatic_tokens_forwarding: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete Automatic Tokens Forwarding
        api_response = api_instance.delete_automatic_tokens_forwarding(blockchain, network, reference_id, context=context)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling AutomaticTokensForwardingApi->delete_automatic_tokens_forwarding: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. |
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. |
 **reference_id** | **str**| Represents a unique ID used to reference the specific callback subscription. |
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]

### Return type

[**DeleteAutomaticTokensForwardingR**](DeleteAutomaticTokensForwardingR.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The delete request has been successful. |  -  |
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

# **get_fee_address_details**
> GetFeeAddressDetailsR get_fee_address_details(blockchain, network)

Get Fee Address Details

Through this endpoint customers can obtain details about a fee address. Only one fee address per currency per network for a user's account can be set no matter how many tokens or subscriptions they have or want to automatically forward.    {warning}Currently we support fungible tokens (ERC-20) **only**, NFTs (ERC-721) are **not** supported.{/warning}

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import automatic_tokens_forwarding_api
from cryptoapis.model.convert_bitcoin_cash_address429_response import ConvertBitcoinCashAddress429Response
from cryptoapis.model.convert_bitcoin_cash_address500_response import ConvertBitcoinCashAddress500Response
from cryptoapis.model.convert_bitcoin_cash_address422_response import ConvertBitcoinCashAddress422Response
from cryptoapis.model.get_fee_address_details400_response import GetFeeAddressDetails400Response
from cryptoapis.model.get_fee_address_details403_response import GetFeeAddressDetails403Response
from cryptoapis.model.get_fee_address_details401_response import GetFeeAddressDetails401Response
from cryptoapis.model.get_xrp_ripple_transaction_details_by_transaction_id404_response import GetXRPRippleTransactionDetailsByTransactionID404Response
from cryptoapis.model.get_fee_address_details_r import GetFeeAddressDetailsR
from cryptoapis.model.convert_bitcoin_cash_address402_response import ConvertBitcoinCashAddress402Response
from cryptoapis.model.convert_bitcoin_cash_address409_response import ConvertBitcoinCashAddress409Response
from cryptoapis.model.convert_bitcoin_cash_address415_response import ConvertBitcoinCashAddress415Response
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
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with cryptoapis.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = automatic_tokens_forwarding_api.AutomaticTokensForwardingApi(api_client)
    blockchain = "bitcoin" # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    network = "testnet" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    context = "yourExampleString" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Fee Address Details
        api_response = api_instance.get_fee_address_details(blockchain, network)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling AutomaticTokensForwardingApi->get_fee_address_details: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Fee Address Details
        api_response = api_instance.get_fee_address_details(blockchain, network, context=context)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling AutomaticTokensForwardingApi->get_fee_address_details: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. |
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. |
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]

### Return type

[**GetFeeAddressDetailsR**](GetFeeAddressDetailsR.md)

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

# **list_tokens_forwarding_automations**
> ListTokensForwardingAutomationsR list_tokens_forwarding_automations(blockchain, network)

List Tokens Forwarding Automations

Through this endpoint customers can list all of their **tokens** forwarding automations (**not** coins).    Customers can set up automatic forwarding functions for tokens by setting a `fromAddress` and a `toAddress`, and specifying the amount that can be transferred between addresses.     A `feePriority` will be returned which represents the fee priority of the automation whether it is \"SLOW\", \"STANDARD\" OR \"FAST\".     {warning}Currently we support fungible tokens (ERC-20) **only**, NFTs (ERC-721) are **not** supported.{/warning}    {warning}The subscription will work for all transactions until it is deleted. There is no need to do that for every transaction.{/warning}

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import automatic_tokens_forwarding_api
from cryptoapis.model.convert_bitcoin_cash_address429_response import ConvertBitcoinCashAddress429Response
from cryptoapis.model.convert_bitcoin_cash_address500_response import ConvertBitcoinCashAddress500Response
from cryptoapis.model.convert_bitcoin_cash_address422_response import ConvertBitcoinCashAddress422Response
from cryptoapis.model.list_tokens_forwarding_automations_r import ListTokensForwardingAutomationsR
from cryptoapis.model.list_tokens_forwarding_automations401_response import ListTokensForwardingAutomations401Response
from cryptoapis.model.list_tokens_forwarding_automations403_response import ListTokensForwardingAutomations403Response
from cryptoapis.model.get_xrp_ripple_transaction_details_by_transaction_id404_response import GetXRPRippleTransactionDetailsByTransactionID404Response
from cryptoapis.model.convert_bitcoin_cash_address402_response import ConvertBitcoinCashAddress402Response
from cryptoapis.model.convert_bitcoin_cash_address409_response import ConvertBitcoinCashAddress409Response
from cryptoapis.model.list_tokens_forwarding_automations400_response import ListTokensForwardingAutomations400Response
from cryptoapis.model.convert_bitcoin_cash_address415_response import ConvertBitcoinCashAddress415Response
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
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with cryptoapis.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = automatic_tokens_forwarding_api.AutomaticTokensForwardingApi(api_client)
    blockchain = "bitcoin" # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    network = "testnet" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    context = "yourExampleString" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    limit = 50 # int | Defines how many items should be returned in the response per page basis. (optional) if omitted the server will use the default value of 50
    offset = 0 # int | The starting index of the response items, i.e. where the response should start listing the returned items. (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    try:
        # List Tokens Forwarding Automations
        api_response = api_instance.list_tokens_forwarding_automations(blockchain, network)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling AutomaticTokensForwardingApi->list_tokens_forwarding_automations: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Tokens Forwarding Automations
        api_response = api_instance.list_tokens_forwarding_automations(blockchain, network, context=context, limit=limit, offset=offset)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling AutomaticTokensForwardingApi->list_tokens_forwarding_automations: %s\n" % e)
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

[**ListTokensForwardingAutomationsR**](ListTokensForwardingAutomationsR.md)

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

