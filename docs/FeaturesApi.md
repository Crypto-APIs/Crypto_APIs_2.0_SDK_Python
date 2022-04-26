# cryptoapis.FeaturesApi

All URIs are relative to *https://rest.cryptoapis.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**broadcast_locally_signed_transaction**](FeaturesApi.md#broadcast_locally_signed_transaction) | **POST** /blockchain-tools/{blockchain}/{network}/transactions/broadcast | Broadcast Locally Signed Transaction
[**decode_raw_transaction_hex**](FeaturesApi.md#decode_raw_transaction_hex) | **POST** /blockchain-tools/{blockchain}/{network}/decode-raw-transaction | Decode Raw Transaction Hex
[**decode_x_address**](FeaturesApi.md#decode_x_address) | **GET** /blockchain-tools/{blockchain}/{network}/decode-x-address/{xAddress} | Decode X-Address
[**derive_hd_wallet__x_pub_y_pub_z_pub_change_or_receiving_addresses**](FeaturesApi.md#derive_hd_wallet__x_pub_y_pub_z_pub_change_or_receiving_addresses) | **GET** /blockchain-tools/{blockchain}/{network}/hd/{extendedPublicKey}/addresses/derive-address | Derive HD Wallet (xPub, yPub, zPub) Change Or Receiving Addresses
[**encode_x_address**](FeaturesApi.md#encode_x_address) | **GET** /blockchain-tools/{blockchain}/{network}/encode-x-address/{classicAddress}/{addressTag} | Encode X-Address
[**estimate_gas_limit**](FeaturesApi.md#estimate_gas_limit) | **POST** /blockchain-tools/{blockchain}/{network}/gas-limit | Estimate Gas Limit
[**estimate_token_gas_limit**](FeaturesApi.md#estimate_token_gas_limit) | **POST** /blockchain-tools/{blockchain}/{network}/gas-limit/contract | Estimate Token Gas Limit
[**get_eip_1559_fee_recommendations**](FeaturesApi.md#get_eip_1559_fee_recommendations) | **GET** /blockchain-tools/{blockchain}/{network}/fees/eip1559 | Get EIP 1559 Fee Recommendations
[**validate_address**](FeaturesApi.md#validate_address) | **POST** /blockchain-tools/{blockchain}/{network}/addresses/validate | Validate Address


# **broadcast_locally_signed_transaction**
> BroadcastLocallySignedTransactionR broadcast_locally_signed_transaction(blockchain, network)

Broadcast Locally Signed Transaction

Through this endpoint customers can broadcast transactions that have been already signed locally. Instead of using a node for broadcasting a signed transaction users can use this endpoint. We then keep the user posted about the status by sending you a callback with a success or failure status.    {warning}This can be prepared and signed **only** locally, not through the API. We can provide support only for the process of broadcasting.{/warning}

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import features_api
from cryptoapis.model.inline_response40199 import InlineResponse40199
from cryptoapis.model.broadcast_locally_signed_transaction_r import BroadcastLocallySignedTransactionR
from cryptoapis.model.inline_response429 import InlineResponse429
from cryptoapis.model.inline_response422 import InlineResponse422
from cryptoapis.model.inline_response402 import InlineResponse402
from cryptoapis.model.broadcast_locally_signed_transaction_rb import BroadcastLocallySignedTransactionRB
from cryptoapis.model.inline_response40399 import InlineResponse40399
from cryptoapis.model.inline_response4041 import InlineResponse4041
from cryptoapis.model.inline_response500 import InlineResponse500
from cryptoapis.model.inline_response415 import InlineResponse415
from cryptoapis.model.inline_response40917 import InlineResponse40917
from cryptoapis.model.inline_response40099 import InlineResponse40099
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
    api_instance = features_api.FeaturesApi(api_client)
    blockchain = "bitcoin" # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    network = "testnet" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    context = "yourExampleString" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    broadcast_locally_signed_transaction_rb = BroadcastLocallySignedTransactionRB(
        context="yourExampleString",
        data=BroadcastLocallySignedTransactionRBData(
            item=BroadcastLocallySignedTransactionRBDataItem(
                callback_secret_key="yourSecretString",
                callback_url="https://example.com",
                signed_transaction_hex="0xf86a22827d00831e8480941b85a43e2e7f52e766ddfdfa2b901c42cb1201be8801b27f33b807c0008029a084ccbf02b27e0842fb1eda7a187a5589c3759be0e969e0ca989dc469a5e5e394a02e111e1156b197f1de4c1d9ba4af26e50665ea6d617d05b3e4047da12b915e69",
            ),
        ),
    ) # BroadcastLocallySignedTransactionRB |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Broadcast Locally Signed Transaction
        api_response = api_instance.broadcast_locally_signed_transaction(blockchain, network)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling FeaturesApi->broadcast_locally_signed_transaction: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Broadcast Locally Signed Transaction
        api_response = api_instance.broadcast_locally_signed_transaction(blockchain, network, context=context, broadcast_locally_signed_transaction_rb=broadcast_locally_signed_transaction_rb)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling FeaturesApi->broadcast_locally_signed_transaction: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. |
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. |
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]
 **broadcast_locally_signed_transaction_rb** | [**BroadcastLocallySignedTransactionRB**](BroadcastLocallySignedTransactionRB.md)|  | [optional]

### Return type

[**BroadcastLocallySignedTransactionR**](BroadcastLocallySignedTransactionR.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The resource has been successfully submitted. |  -  |
**400** | 400 |  -  |
**401** | 401 |  -  |
**402** | You have insufficient credits. Please upgrade your plan from your Dashboard or contact our team via email. |  -  |
**403** | 403 |  -  |
**404** | The specified resource has not been found. |  -  |
**409** | 409 |  -  |
**415** | The selected Media Type is unavailable. The Content-Type header should be &#39;application/json&#39;. |  -  |
**422** | Your request body for POST requests must have a structure of { data: { item: [...properties] } } |  -  |
**429** | The request limit has been reached. There can be maximum {requests} requests per {seconds} second(s) made. Please contact our team via email if you need more or upgrade your plan. |  -  |
**500** | An unexpected server error has occurred, we are working to fix this. Please try again later and in case it occurs again please report it to our team via email. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **decode_raw_transaction_hex**
> DecodeRawTransactionHexR decode_raw_transaction_hex(blockchain, network)

Decode Raw Transaction Hex

Through this endpoint customers can decode a raw transaction hex and see the decoded transactions' details.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import features_api
from cryptoapis.model.inline_response429 import InlineResponse429
from cryptoapis.model.inline_response400102 import InlineResponse400102
from cryptoapis.model.inline_response422 import InlineResponse422
from cryptoapis.model.inline_response409 import InlineResponse409
from cryptoapis.model.inline_response401102 import InlineResponse401102
from cryptoapis.model.inline_response402 import InlineResponse402
from cryptoapis.model.inline_response403102 import InlineResponse403102
from cryptoapis.model.inline_response500 import InlineResponse500
from cryptoapis.model.inline_response415 import InlineResponse415
from cryptoapis.model.decode_raw_transaction_hex_r import DecodeRawTransactionHexR
from cryptoapis.model.decode_raw_transaction_hex_rb import DecodeRawTransactionHexRB
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
    api_instance = features_api.FeaturesApi(api_client)
    blockchain = "bitcoin" # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    network = "testnet" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    context = "yourExampleString" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    decode_raw_transaction_hex_rb = DecodeRawTransactionHexRB(
        context="yourExampleString",
        data=DecodeRawTransactionHexRBData(
            item=DecodeRawTransactionHexRBDataItem(
                raw_transaction_hex="0100000001f3f6a909f8521adb57d898d2985834e632374e770fd9e2b98656f1bf1fdfd427010000006b48304502203a776322ebf8eb8b58cc6ced4f2574f4c73aa664edce0b0022690f2f6f47c521022100b82353305988cb0ebd443089a173ceec93fe4dbfe98d74419ecc84a6a698e31d012103c5c1bc61f60ce3d6223a63cedbece03b12ef9f0068f2f3c4a7e7f06c523c3664ffffffff0260e31600000000001976a914977ae6e32349b99b72196cb62b5ef37329ed81b488ac063d1000000000001976a914f76bc4190f3d8e2315e5c11c59cfc8be9df747e388ac00000000",
            ),
        ),
    ) # DecodeRawTransactionHexRB |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Decode Raw Transaction Hex
        api_response = api_instance.decode_raw_transaction_hex(blockchain, network)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling FeaturesApi->decode_raw_transaction_hex: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Decode Raw Transaction Hex
        api_response = api_instance.decode_raw_transaction_hex(blockchain, network, context=context, decode_raw_transaction_hex_rb=decode_raw_transaction_hex_rb)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling FeaturesApi->decode_raw_transaction_hex: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. |
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. |
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]
 **decode_raw_transaction_hex_rb** | [**DecodeRawTransactionHexRB**](DecodeRawTransactionHexRB.md)|  | [optional]

### Return type

[**DecodeRawTransactionHexR**](DecodeRawTransactionHexR.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The resource has been successfully created. |  -  |
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

# **decode_x_address**
> DecodeXAddressR decode_x_address(network, x_address)

Decode X-Address

Through this endpoint, customers can decode an encoded XRP address with tag, by providing the specific x-address. The response includes the decoded classic address and the tag.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import features_api
from cryptoapis.model.inline_response429 import InlineResponse429
from cryptoapis.model.inline_response401103 import InlineResponse401103
from cryptoapis.model.inline_response422 import InlineResponse422
from cryptoapis.model.inline_response409 import InlineResponse409
from cryptoapis.model.inline_response403103 import InlineResponse403103
from cryptoapis.model.inline_response402 import InlineResponse402
from cryptoapis.model.inline_response500 import InlineResponse500
from cryptoapis.model.decode_x_address_r import DecodeXAddressR
from cryptoapis.model.inline_response415 import InlineResponse415
from cryptoapis.model.inline_response400103 import InlineResponse400103
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
    api_instance = features_api.FeaturesApi(api_client)
    network = "testnet" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    x_address = "TVTMSyg6nRscAm2JtRd8hnpF9nD21CgZx6ibb9iy3EWHotV" # str | Represents the encoded classic address with its destination tag.
    context = "yourExampleString" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Decode X-Address
        api_response = api_instance.decode_x_address(network, x_address)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling FeaturesApi->decode_x_address: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Decode X-Address
        api_response = api_instance.decode_x_address(network, x_address, context=context)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling FeaturesApi->decode_x_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. |
 **x_address** | **str**| Represents the encoded classic address with its destination tag. |
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. | defaults to "xrp"
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]

### Return type

[**DecodeXAddressR**](DecodeXAddressR.md)

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

# **derive_hd_wallet__x_pub_y_pub_z_pub_change_or_receiving_addresses**
> DeriveHDWalletXPubYPubZPubChangeOrReceivingAddressesR derive_hd_wallet__x_pub_y_pub_z_pub_change_or_receiving_addresses(blockchain, extended_public_key, network)

Derive HD Wallet (xPub, yPub, zPub) Change Or Receiving Addresses

Through this endpoint, customers can derive up to 10 addresses - both change and receive, from a certain HD Wallet (xPub, yPub, zPub), by providing an extended public key. By default the system creates a receiving/deposit address, unless the isChange attribute is set to 'true'. In that case the system derives a 'change' address. The change address can be derived only for UTXO based blockchains, for all the rest, this endpoint always creates a deposit/receiving address.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import features_api
from cryptoapis.model.inline_response429 import InlineResponse429
from cryptoapis.model.inline_response422 import InlineResponse422
from cryptoapis.model.inline_response409 import InlineResponse409
from cryptoapis.model.inline_response402 import InlineResponse402
from cryptoapis.model.inline_response40070 import InlineResponse40070
from cryptoapis.model.inline_response500 import InlineResponse500
from cryptoapis.model.inline_response415 import InlineResponse415
from cryptoapis.model.derive_hd_wallet_x_pub_y_pub_z_pub_change_or_receiving_addresses_r import DeriveHDWalletXPubYPubZPubChangeOrReceivingAddressesR
from cryptoapis.model.inline_response40170 import InlineResponse40170
from cryptoapis.model.inline_response40370 import InlineResponse40370
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
    api_instance = features_api.FeaturesApi(api_client)
    blockchain = "bitcoin" # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    extended_public_key = "upub5Ei6bRNneqozk6smK7dvtXHC5PjUyEL4ynCfMKvjznLcXi9DQaikETzQjHvJC43XexMvQs64jxB1njMjCHpRZ4xQWAmv3ge9cVtjfsHmbvQ" # str | Defines the account extended publicly known key which is used to derive all child public keys.
    network = "testnet" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    context = "yourExampleString" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    address_format = "p2sh" # str | Represents the format of the address. (optional)
    addresses_count = 2 # int | Represents the addresses count. (optional)
    is_change = True # bool | Defines if the specific address is a change or deposit address. If the value is True - it is a change address, if it is False - it is a Deposit address. (optional)
    start_index = 3 # int | The starting index of the response items, i.e. where the response should start listing the returned items. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Derive HD Wallet (xPub, yPub, zPub) Change Or Receiving Addresses
        api_response = api_instance.derive_hd_wallet__x_pub_y_pub_z_pub_change_or_receiving_addresses(blockchain, extended_public_key, network)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling FeaturesApi->derive_hd_wallet__x_pub_y_pub_z_pub_change_or_receiving_addresses: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Derive HD Wallet (xPub, yPub, zPub) Change Or Receiving Addresses
        api_response = api_instance.derive_hd_wallet__x_pub_y_pub_z_pub_change_or_receiving_addresses(blockchain, extended_public_key, network, context=context, address_format=address_format, addresses_count=addresses_count, is_change=is_change, start_index=start_index)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling FeaturesApi->derive_hd_wallet__x_pub_y_pub_z_pub_change_or_receiving_addresses: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. |
 **extended_public_key** | **str**| Defines the account extended publicly known key which is used to derive all child public keys. |
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. |
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]
 **address_format** | **str**| Represents the format of the address. | [optional]
 **addresses_count** | **int**| Represents the addresses count. | [optional]
 **is_change** | **bool**| Defines if the specific address is a change or deposit address. If the value is True - it is a change address, if it is False - it is a Deposit address. | [optional]
 **start_index** | **int**| The starting index of the response items, i.e. where the response should start listing the returned items. | [optional]

### Return type

[**DeriveHDWalletXPubYPubZPubChangeOrReceivingAddressesR**](DeriveHDWalletXPubYPubZPubChangeOrReceivingAddressesR.md)

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

# **encode_x_address**
> EncodeXAddressR encode_x_address(address_tag, classic_address, network)

Encode X-Address

Through this endpoint, customers can encode an encoded XRP address with tag, by providing the specific x-address. The response includes the encoded classic address and the tag.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import features_api
from cryptoapis.model.inline_response429 import InlineResponse429
from cryptoapis.model.inline_response403104 import InlineResponse403104
from cryptoapis.model.inline_response422 import InlineResponse422
from cryptoapis.model.inline_response409 import InlineResponse409
from cryptoapis.model.inline_response402 import InlineResponse402
from cryptoapis.model.inline_response500 import InlineResponse500
from cryptoapis.model.inline_response415 import InlineResponse415
from cryptoapis.model.encode_x_address_r import EncodeXAddressR
from cryptoapis.model.inline_response400104 import InlineResponse400104
from cryptoapis.model.inline_response401104 import InlineResponse401104
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
    api_instance = features_api.FeaturesApi(api_client)
    address_tag = 3999472835 # int | Defines a specific Tag that is an additional XRP address feature. It helps identifying a transaction recipient beyond a wallet address.
    classic_address = "rA9bXGJcXvZKaWofrRphdJsBWzhyCfH3z" # str | Represents the public address, which is a compressed and shortened form of a public key.
    network = "testnet" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    context = "yourExampleString" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Encode X-Address
        api_response = api_instance.encode_x_address(address_tag, classic_address, network)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling FeaturesApi->encode_x_address: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Encode X-Address
        api_response = api_instance.encode_x_address(address_tag, classic_address, network, context=context)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling FeaturesApi->encode_x_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address_tag** | **int**| Defines a specific Tag that is an additional XRP address feature. It helps identifying a transaction recipient beyond a wallet address. |
 **classic_address** | **str**| Represents the public address, which is a compressed and shortened form of a public key. |
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. |
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. | defaults to "xrp"
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]

### Return type

[**EncodeXAddressR**](EncodeXAddressR.md)

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

# **estimate_gas_limit**
> EstimateGasLimitR estimate_gas_limit(blockchain, network)

Estimate Gas Limit

This endpoint helps customer in estimating the gas limit needed for a transaction. It gives information for gas expenses when sending ether to contracts or making a transaction with additional data in it.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import features_api
from cryptoapis.model.inline_response429 import InlineResponse429
from cryptoapis.model.inline_response422 import InlineResponse422
from cryptoapis.model.inline_response409 import InlineResponse409
from cryptoapis.model.inline_response402 import InlineResponse402
from cryptoapis.model.inline_response4041 import InlineResponse4041
from cryptoapis.model.inline_response500 import InlineResponse500
from cryptoapis.model.inline_response400100 import InlineResponse400100
from cryptoapis.model.estimate_gas_limit_rb import EstimateGasLimitRB
from cryptoapis.model.inline_response401100 import InlineResponse401100
from cryptoapis.model.inline_response415 import InlineResponse415
from cryptoapis.model.inline_response403100 import InlineResponse403100
from cryptoapis.model.estimate_gas_limit_r import EstimateGasLimitR
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
    api_instance = features_api.FeaturesApi(api_client)
    blockchain = "ethereum" # str | Represents the specific blockchain protocol name, e.g. Ethereum.
    network = "ropsten" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    context = "yourExampleString" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    estimate_gas_limit_rb = EstimateGasLimitRB(
        context="yourExampleString",
        data=EstimateGasLimitRBData(
            item=EstimateGasLimitRBDataItem(
                additional_data="yourAdditionalString",
                amount="0.002",
                recipient="0xc065b539490f81b6c297c37b1925c3be2f190738",
                sender="0x6f61e3c2fbb8c8be698bd0907ba6c04b62800fe5",
            ),
        ),
    ) # EstimateGasLimitRB |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Estimate Gas Limit
        api_response = api_instance.estimate_gas_limit(blockchain, network)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling FeaturesApi->estimate_gas_limit: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Estimate Gas Limit
        api_response = api_instance.estimate_gas_limit(blockchain, network, context=context, estimate_gas_limit_rb=estimate_gas_limit_rb)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling FeaturesApi->estimate_gas_limit: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum. |
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. |
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]
 **estimate_gas_limit_rb** | [**EstimateGasLimitRB**](EstimateGasLimitRB.md)|  | [optional]

### Return type

[**EstimateGasLimitR**](EstimateGasLimitR.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
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

# **estimate_token_gas_limit**
> EstimateTokenGasLimitR estimate_token_gas_limit(blockchain, network)

Estimate Token Gas Limit

This endpoint helps customer in estimating the Contract Gas Limit needed for a transaction. It gives information for gas expenses for a specific contract when sending ethers or making a transaction with additional data in it.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import features_api
from cryptoapis.model.inline_response400101 import InlineResponse400101
from cryptoapis.model.inline_response429 import InlineResponse429
from cryptoapis.model.inline_response422 import InlineResponse422
from cryptoapis.model.inline_response409 import InlineResponse409
from cryptoapis.model.inline_response402 import InlineResponse402
from cryptoapis.model.inline_response401101 import InlineResponse401101
from cryptoapis.model.estimate_token_gas_limit_rb import EstimateTokenGasLimitRB
from cryptoapis.model.inline_response500 import InlineResponse500
from cryptoapis.model.estimate_token_gas_limit_r import EstimateTokenGasLimitR
from cryptoapis.model.inline_response415 import InlineResponse415
from cryptoapis.model.inline_response403101 import InlineResponse403101
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
    api_instance = features_api.FeaturesApi(api_client)
    blockchain = "ethereum" # str | Represents the specific blockchain protocol name, e.g. Ethereum.
    network = "ropsten" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    context = "yourExampleString" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    estimate_token_gas_limit_rb = EstimateTokenGasLimitRB(
        context="yourExampleString",
        data=EstimateTokenGasLimitRBData(
            item=EstimateTokenGasLimitRBDataItem(
                amount="0.12",
                contract="0x092de782a7e1e0a92991ad829a0a33aef3c7545e",
                contract_type="ERC-20",
                recipient="0xc065b539490f81b6c297c37b1925c3be2f190738",
                sender="0x6f61e3c2fbb8c8be698bd0907ba6c04b62800fe5",
            ),
        ),
    ) # EstimateTokenGasLimitRB |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Estimate Token Gas Limit
        api_response = api_instance.estimate_token_gas_limit(blockchain, network)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling FeaturesApi->estimate_token_gas_limit: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Estimate Token Gas Limit
        api_response = api_instance.estimate_token_gas_limit(blockchain, network, context=context, estimate_token_gas_limit_rb=estimate_token_gas_limit_rb)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling FeaturesApi->estimate_token_gas_limit: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum. |
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. |
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]
 **estimate_token_gas_limit_rb** | [**EstimateTokenGasLimitRB**](EstimateTokenGasLimitRB.md)|  | [optional]

### Return type

[**EstimateTokenGasLimitR**](EstimateTokenGasLimitR.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
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

# **get_eip_1559_fee_recommendations**
> GetEIP1559FeeRecommendationsR get_eip_1559_fee_recommendations(network, )

Get EIP 1559 Fee Recommendations

Through this endpoint customers can obtain fee recommendations specifically for EIP 1559.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import features_api
from cryptoapis.model.get_eip1559_fee_recommendations_r import GetEIP1559FeeRecommendationsR
from cryptoapis.model.inline_response429 import InlineResponse429
from cryptoapis.model.inline_response40198 import InlineResponse40198
from cryptoapis.model.inline_response422 import InlineResponse422
from cryptoapis.model.inline_response409 import InlineResponse409
from cryptoapis.model.inline_response402 import InlineResponse402
from cryptoapis.model.inline_response4041 import InlineResponse4041
from cryptoapis.model.inline_response500 import InlineResponse500
from cryptoapis.model.inline_response40398 import InlineResponse40398
from cryptoapis.model.inline_response415 import InlineResponse415
from cryptoapis.model.inline_response40098 import InlineResponse40098
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
    api_instance = features_api.FeaturesApi(api_client)
    network = "ropsten" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    context = "yourExampleString" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get EIP 1559 Fee Recommendations
        api_response = api_instance.get_eip_1559_fee_recommendations(network, )
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling FeaturesApi->get_eip_1559_fee_recommendations: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get EIP 1559 Fee Recommendations
        api_response = api_instance.get_eip_1559_fee_recommendations(network, context=context)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling FeaturesApi->get_eip_1559_fee_recommendations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. |
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum. | defaults to "ethereum"
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]

### Return type

[**GetEIP1559FeeRecommendationsR**](GetEIP1559FeeRecommendationsR.md)

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

# **validate_address**
> ValidateAddressR validate_address(blockchain, network)

Validate Address

This endpoint checks user public addresses whether they are valid or not.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import features_api
from cryptoapis.model.validate_address_rb import ValidateAddressRB
from cryptoapis.model.inline_response429 import InlineResponse429
from cryptoapis.model.inline_response40197 import InlineResponse40197
from cryptoapis.model.inline_response422 import InlineResponse422
from cryptoapis.model.inline_response409 import InlineResponse409
from cryptoapis.model.inline_response402 import InlineResponse402
from cryptoapis.model.validate_address_r import ValidateAddressR
from cryptoapis.model.inline_response500 import InlineResponse500
from cryptoapis.model.inline_response415 import InlineResponse415
from cryptoapis.model.inline_response40397 import InlineResponse40397
from cryptoapis.model.inline_response40097 import InlineResponse40097
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
    api_instance = features_api.FeaturesApi(api_client)
    blockchain = "bitcoin" # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    network = "testnet" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    context = "yourExampleString" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    validate_address_rb = ValidateAddressRB(
        context="yourExampleString",
        data=ValidateAddressRBData(
            item=ValidateAddressRBDataItem(
                address="mho4jHBcrNCncKt38trJahXakuaBnS7LK5",
            ),
        ),
    ) # ValidateAddressRB |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Validate Address
        api_response = api_instance.validate_address(blockchain, network)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling FeaturesApi->validate_address: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Validate Address
        api_response = api_instance.validate_address(blockchain, network, context=context, validate_address_rb=validate_address_rb)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling FeaturesApi->validate_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. |
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. |
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]
 **validate_address_rb** | [**ValidateAddressRB**](ValidateAddressRB.md)|  | [optional]

### Return type

[**ValidateAddressR**](ValidateAddressR.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
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

