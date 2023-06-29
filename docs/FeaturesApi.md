# cryptoapis.FeaturesApi

All URIs are relative to *https://rest.cryptoapis.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**broadcast_locally_signed_transaction**](FeaturesApi.md#broadcast_locally_signed_transaction) | **POST** /blockchain-tools/{blockchain}/{network}/transactions/broadcast | Broadcast Locally Signed Transaction
[**convert_bitcoin_cash_address**](FeaturesApi.md#convert_bitcoin_cash_address) | **POST** /blockchain-tools/{blockchain}/{network}/address/convert | Convert Bitcoin Cash Address
[**decode_raw_transaction_hex**](FeaturesApi.md#decode_raw_transaction_hex) | **POST** /blockchain-tools/{blockchain}/{network}/decode-raw-transaction | Decode Raw Transaction Hex
[**decode_x_address**](FeaturesApi.md#decode_x_address) | **GET** /blockchain-tools/{blockchain}/{network}/decode-x-address/{xAddress} | Decode X-Address
[**derive_hd_wallet__x_pub_y_pub_z_pub_change_or_receiving_addresses**](FeaturesApi.md#derive_hd_wallet__x_pub_y_pub_z_pub_change_or_receiving_addresses) | **GET** /blockchain-tools/{blockchain}/{network}/hd/{extendedPublicKey}/addresses/derive-address | Derive HD Wallet (xPub, yPub, zPub) Change Or Receiving Addresses
[**encode_x_address**](FeaturesApi.md#encode_x_address) | **GET** /blockchain-tools/{blockchain}/{network}/encode-x-address/{classicAddress}/{addressTag} | Encode X-Address
[**estimate_gas_limit**](FeaturesApi.md#estimate_gas_limit) | **POST** /blockchain-tools/{blockchain}/{network}/gas-limit | Estimate Gas Limit
[**estimate_token_gas_limit**](FeaturesApi.md#estimate_token_gas_limit) | **POST** /blockchain-tools/{blockchain}/{network}/gas-limit/contract | Estimate Token Gas Limit
[**get_eip_1559_fee_recommendations**](FeaturesApi.md#get_eip_1559_fee_recommendations) | **GET** /blockchain-tools/{blockchain}/{network}/fees/eip1559 | Get EIP 1559 Fee Recommendations
[**prepare_a_fungible_token_transfer_from_address**](FeaturesApi.md#prepare_a_fungible_token_transfer_from_address) | **POST** /blockchain-tools/{blockchain}/{network}/transactions/prepare-token-from-address | Prepare A Fungible Token Transfer From Address
[**prepare_a_non_fungible_token_transfer_from_address**](FeaturesApi.md#prepare_a_non_fungible_token_transfer_from_address) | **POST** /blockchain-tools/{blockchain}/{network}/transactions/prepare-nft-from-address | Prepare A Non Fungible Token Transfer From Address
[**prepare_transaction_from_address**](FeaturesApi.md#prepare_transaction_from_address) | **POST** /blockchain-data/{blockchain}/{network}/transactions/prepare-from-address | Prepare Transaction From Address
[**validate_address**](FeaturesApi.md#validate_address) | **POST** /blockchain-tools/{blockchain}/{network}/addresses/validate | Validate Address


# **broadcast_locally_signed_transaction**
> BroadcastLocallySignedTransactionR broadcast_locally_signed_transaction(blockchain, network, context=context, broadcast_locally_signed_transaction_rb=broadcast_locally_signed_transaction_rb)

Broadcast Locally Signed Transaction

Through this endpoint customers can broadcast transactions that have been already signed locally. Instead of using a node for broadcasting a signed transaction users can use this endpoint. We then keep the user posted about the status by sending you a callback with a success or failure status.    {warning}This can be prepared and signed **only** locally, not through the API. We can provide support only for the process of broadcasting.{/warning}

### Example

* Api Key Authentication (ApiKey):
```python
import time
import os
import cryptoapis
from cryptoapis.models.broadcast_locally_signed_transaction_r import BroadcastLocallySignedTransactionR
from cryptoapis.models.broadcast_locally_signed_transaction_rb import BroadcastLocallySignedTransactionRB
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
    api_instance = cryptoapis.FeaturesApi(api_client)
    blockchain = 'bitcoin' # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    network = 'testnet' # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    context = 'yourExampleString' # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    broadcast_locally_signed_transaction_rb = cryptoapis.BroadcastLocallySignedTransactionRB() # BroadcastLocallySignedTransactionRB |  (optional)

    try:
        # Broadcast Locally Signed Transaction
        api_response = api_instance.broadcast_locally_signed_transaction(blockchain, network, context=context, broadcast_locally_signed_transaction_rb=broadcast_locally_signed_transaction_rb)
        print("The response of FeaturesApi->broadcast_locally_signed_transaction:\n")
        pprint(api_response)
    except Exception as e:
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

# **convert_bitcoin_cash_address**
> ConvertBitcoinCashAddressR convert_bitcoin_cash_address(blockchain, network, context=context, convert_bitcoin_cash_address_rb=convert_bitcoin_cash_address_rb)

Convert Bitcoin Cash Address

Through this endpoint customers will be able to convert addresses for the BCH (Bitcoin Cash) protocol from BCH legacy to cash address and vice versa.

### Example

* Api Key Authentication (ApiKey):
```python
import time
import os
import cryptoapis
from cryptoapis.models.convert_bitcoin_cash_address_r import ConvertBitcoinCashAddressR
from cryptoapis.models.convert_bitcoin_cash_address_rb import ConvertBitcoinCashAddressRB
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
    api_instance = cryptoapis.FeaturesApi(api_client)
    blockchain = 'bitcoin-cash' # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    network = 'testnet' # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    context = 'yourExampleString' # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    convert_bitcoin_cash_address_rb = cryptoapis.ConvertBitcoinCashAddressRB() # ConvertBitcoinCashAddressRB |  (optional)

    try:
        # Convert Bitcoin Cash Address
        api_response = api_instance.convert_bitcoin_cash_address(blockchain, network, context=context, convert_bitcoin_cash_address_rb=convert_bitcoin_cash_address_rb)
        print("The response of FeaturesApi->convert_bitcoin_cash_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeaturesApi->convert_bitcoin_cash_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. | 
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. | 
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional] 
 **convert_bitcoin_cash_address_rb** | [**ConvertBitcoinCashAddressRB**](ConvertBitcoinCashAddressRB.md)|  | [optional] 

### Return type

[**ConvertBitcoinCashAddressR**](ConvertBitcoinCashAddressR.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The request has been successful. |  -  |
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

# **decode_raw_transaction_hex**
> DecodeRawTransactionHexR decode_raw_transaction_hex(blockchain, network, context=context, decode_raw_transaction_hex_rb=decode_raw_transaction_hex_rb)

Decode Raw Transaction Hex

Through this endpoint customers can decode a raw transaction hex and see the decoded transactions' details.

### Example

* Api Key Authentication (ApiKey):
```python
import time
import os
import cryptoapis
from cryptoapis.models.decode_raw_transaction_hex_r import DecodeRawTransactionHexR
from cryptoapis.models.decode_raw_transaction_hex_rb import DecodeRawTransactionHexRB
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
    api_instance = cryptoapis.FeaturesApi(api_client)
    blockchain = 'bitcoin' # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    network = 'testnet' # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    context = 'yourExampleString' # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    decode_raw_transaction_hex_rb = cryptoapis.DecodeRawTransactionHexRB() # DecodeRawTransactionHexRB |  (optional)

    try:
        # Decode Raw Transaction Hex
        api_response = api_instance.decode_raw_transaction_hex(blockchain, network, context=context, decode_raw_transaction_hex_rb=decode_raw_transaction_hex_rb)
        print("The response of FeaturesApi->decode_raw_transaction_hex:\n")
        pprint(api_response)
    except Exception as e:
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
> DecodeXAddressR decode_x_address(blockchain, network, x_address, context=context)

Decode X-Address

Through this endpoint, customers can decode an encoded XRP address with tag, by providing the specific x-address. The response includes the decoded classic address and the tag.

### Example

* Api Key Authentication (ApiKey):
```python
import time
import os
import cryptoapis
from cryptoapis.models.decode_x_address_r import DecodeXAddressR
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
    api_instance = cryptoapis.FeaturesApi(api_client)
    blockchain = 'xrp' # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    network = 'testnet' # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    x_address = 'TVTMSyg6nRscAm2JtRd8hnpF9nD21CgZx6ibb9iy3EWHotV' # str | Represents the encoded classic address with its destination tag.
    context = 'yourExampleString' # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)

    try:
        # Decode X-Address
        api_response = api_instance.decode_x_address(blockchain, network, x_address, context=context)
        print("The response of FeaturesApi->decode_x_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeaturesApi->decode_x_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. | 
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. | 
 **x_address** | **str**| Represents the encoded classic address with its destination tag. | 
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
> DeriveHDWalletXPubYPubZPubChangeOrReceivingAddressesR derive_hd_wallet__x_pub_y_pub_z_pub_change_or_receiving_addresses(blockchain, extended_public_key, network, context=context, address_format=address_format, addresses_count=addresses_count, is_change=is_change, start_index=start_index)

Derive HD Wallet (xPub, yPub, zPub) Change Or Receiving Addresses

Through this endpoint, customers can derive up to 10 addresses - both change and receive, from a certain HD Wallet (xPub, yPub, zPub), by providing an extended public key. By default the system creates a receiving/deposit address, unless the isChange attribute is set to 'true'. In that case the system derives a 'change' address. The change address can be derived only for UTXO based blockchains, for all the rest, this endpoint always creates a deposit/receiving address.

### Example

* Api Key Authentication (ApiKey):
```python
import time
import os
import cryptoapis
from cryptoapis.models.derive_hd_wallet_x_pub_y_pub_z_pub_change_or_receiving_addresses_r import DeriveHDWalletXPubYPubZPubChangeOrReceivingAddressesR
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
    api_instance = cryptoapis.FeaturesApi(api_client)
    blockchain = 'bitcoin' # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    extended_public_key = 'upub5Ei6bRNneqozk6smK7dvtXHC5PjUyEL4ynCfMKvjznLcXi9DQaikETzQjHvJC43XexMvQs64jxB1njMjCHpRZ4xQWAmv3ge9cVtjfsHmbvQ' # str | Defines the account extended publicly known key which is used to derive all child public keys.
    network = 'testnet' # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    context = 'yourExampleString' # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    address_format = 'p2sh' # str | Represents the format of the address. (optional)
    addresses_count = 2 # int | Represents the addresses count. (optional)
    is_change = true # bool | Defines if the specific address is a change or deposit address. If the value is True - it is a change address, if it is False - it is a Deposit address. (optional)
    start_index = 3 # int | The starting index of the response items, i.e. where the response should start listing the returned items. (optional)

    try:
        # Derive HD Wallet (xPub, yPub, zPub) Change Or Receiving Addresses
        api_response = api_instance.derive_hd_wallet__x_pub_y_pub_z_pub_change_or_receiving_addresses(blockchain, extended_public_key, network, context=context, address_format=address_format, addresses_count=addresses_count, is_change=is_change, start_index=start_index)
        print("The response of FeaturesApi->derive_hd_wallet__x_pub_y_pub_z_pub_change_or_receiving_addresses:\n")
        pprint(api_response)
    except Exception as e:
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
> EncodeXAddressR encode_x_address(address_tag, blockchain, classic_address, network, context=context)

Encode X-Address

Through this endpoint, customers can encode an encoded XRP address with tag, by providing the specific x-address. The response includes the encoded classic address and the tag.

### Example

* Api Key Authentication (ApiKey):
```python
import time
import os
import cryptoapis
from cryptoapis.models.encode_x_address_r import EncodeXAddressR
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
    api_instance = cryptoapis.FeaturesApi(api_client)
    address_tag = 3999472835 # int | Defines a specific Tag that is an additional XRP address feature. It helps identifying a transaction recipient beyond a wallet address.
    blockchain = 'xrp' # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    classic_address = 'rA9bXGJcXvZKaWofrRphdJsBWzhyCfH3z' # str | Represents the public address, which is a compressed and shortened form of a public key.
    network = 'testnet' # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    context = 'yourExampleString' # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)

    try:
        # Encode X-Address
        api_response = api_instance.encode_x_address(address_tag, blockchain, classic_address, network, context=context)
        print("The response of FeaturesApi->encode_x_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeaturesApi->encode_x_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address_tag** | **int**| Defines a specific Tag that is an additional XRP address feature. It helps identifying a transaction recipient beyond a wallet address. | 
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. | 
 **classic_address** | **str**| Represents the public address, which is a compressed and shortened form of a public key. | 
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. | 
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
> EstimateGasLimitR estimate_gas_limit(blockchain, network, context=context, estimate_gas_limit_rb=estimate_gas_limit_rb)

Estimate Gas Limit

This endpoint helps customer in estimating the gas limit needed for a transaction. It gives information for gas expenses when sending ether to contracts or making a transaction with additional data in it.

### Example

* Api Key Authentication (ApiKey):
```python
import time
import os
import cryptoapis
from cryptoapis.models.estimate_gas_limit_r import EstimateGasLimitR
from cryptoapis.models.estimate_gas_limit_rb import EstimateGasLimitRB
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
    api_instance = cryptoapis.FeaturesApi(api_client)
    blockchain = 'ethereum' # str | Represents the specific blockchain protocol name, e.g. Ethereum.
    network = 'ropsten' # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    context = 'yourExampleString' # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    estimate_gas_limit_rb = cryptoapis.EstimateGasLimitRB() # EstimateGasLimitRB |  (optional)

    try:
        # Estimate Gas Limit
        api_response = api_instance.estimate_gas_limit(blockchain, network, context=context, estimate_gas_limit_rb=estimate_gas_limit_rb)
        print("The response of FeaturesApi->estimate_gas_limit:\n")
        pprint(api_response)
    except Exception as e:
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
> EstimateTokenGasLimitR estimate_token_gas_limit(blockchain, network, context=context, estimate_token_gas_limit_rb=estimate_token_gas_limit_rb)

Estimate Token Gas Limit

This endpoint helps customer in estimating the Contract Gas Limit needed for a transaction. It gives information for gas expenses for a specific contract when sending ethers or making a transaction with additional data in it.

### Example

* Api Key Authentication (ApiKey):
```python
import time
import os
import cryptoapis
from cryptoapis.models.estimate_token_gas_limit_r import EstimateTokenGasLimitR
from cryptoapis.models.estimate_token_gas_limit_rb import EstimateTokenGasLimitRB
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
    api_instance = cryptoapis.FeaturesApi(api_client)
    blockchain = 'ethereum' # str | Represents the specific blockchain protocol name, e.g. Ethereum.
    network = 'ropsten' # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    context = 'yourExampleString' # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    estimate_token_gas_limit_rb = cryptoapis.EstimateTokenGasLimitRB() # EstimateTokenGasLimitRB |  (optional)

    try:
        # Estimate Token Gas Limit
        api_response = api_instance.estimate_token_gas_limit(blockchain, network, context=context, estimate_token_gas_limit_rb=estimate_token_gas_limit_rb)
        print("The response of FeaturesApi->estimate_token_gas_limit:\n")
        pprint(api_response)
    except Exception as e:
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
> GetEIP1559FeeRecommendationsR get_eip_1559_fee_recommendations(network, blockchain, context=context)

Get EIP 1559 Fee Recommendations

Through this endpoint customers can obtain fee recommendations specifically for EIP 1559.

### Example

* Api Key Authentication (ApiKey):
```python
import time
import os
import cryptoapis
from cryptoapis.models.get_eip1559_fee_recommendations_r import GetEIP1559FeeRecommendationsR
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
    api_instance = cryptoapis.FeaturesApi(api_client)
    network = 'ropsten' # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    blockchain = 'ethereum' # str | Represents the specific blockchain protocol name, e.g. Ethereum.
    context = 'yourExampleString' # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)

    try:
        # Get EIP 1559 Fee Recommendations
        api_response = api_instance.get_eip_1559_fee_recommendations(network, blockchain, context=context)
        print("The response of FeaturesApi->get_eip_1559_fee_recommendations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeaturesApi->get_eip_1559_fee_recommendations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. | 
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum. | 
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

# **prepare_a_fungible_token_transfer_from_address**
> PrepareAFungibleTokenTransferFromAddressR prepare_a_fungible_token_transfer_from_address(blockchain, network, context=context, prepare_a_fungible_token_transfer_from_address_rb=prepare_a_fungible_token_transfer_from_address_rb)

Prepare A Fungible Token Transfer From Address

Using this endpoint customers can prepare a fungible token transfer from an address with private and public keys. The address doesn’t have to belong to a wallet. The response will include the transaction fee in Wei.

### Example

* Api Key Authentication (ApiKey):
```python
import time
import os
import cryptoapis
from cryptoapis.models.prepare_a_fungible_token_transfer_from_address_r import PrepareAFungibleTokenTransferFromAddressR
from cryptoapis.models.prepare_a_fungible_token_transfer_from_address_rb import PrepareAFungibleTokenTransferFromAddressRB
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
    api_instance = cryptoapis.FeaturesApi(api_client)
    blockchain = 'ethereum' # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    network = 'goerli' # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"mordor\" are test networks.
    context = 'yourExampleString' # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    prepare_a_fungible_token_transfer_from_address_rb = cryptoapis.PrepareAFungibleTokenTransferFromAddressRB() # PrepareAFungibleTokenTransferFromAddressRB |  (optional)

    try:
        # Prepare A Fungible Token Transfer From Address
        api_response = api_instance.prepare_a_fungible_token_transfer_from_address(blockchain, network, context=context, prepare_a_fungible_token_transfer_from_address_rb=prepare_a_fungible_token_transfer_from_address_rb)
        print("The response of FeaturesApi->prepare_a_fungible_token_transfer_from_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeaturesApi->prepare_a_fungible_token_transfer_from_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. | 
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;mordor\&quot; are test networks. | 
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional] 
 **prepare_a_fungible_token_transfer_from_address_rb** | [**PrepareAFungibleTokenTransferFromAddressRB**](PrepareAFungibleTokenTransferFromAddressRB.md)|  | [optional] 

### Return type

[**PrepareAFungibleTokenTransferFromAddressR**](PrepareAFungibleTokenTransferFromAddressR.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The resource has been successfully submitted. |  -  |
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

# **prepare_a_non_fungible_token_transfer_from_address**
> PrepareANonFungibleTokenTransferFromAddressR prepare_a_non_fungible_token_transfer_from_address(blockchain, network, context=context, prepare_a_non_fungible_token_transfer_from_address_rb=prepare_a_non_fungible_token_transfer_from_address_rb)

Prepare A Non Fungible Token Transfer From Address

Using this endpoint customers can prepare a non-fungible token transfer from an address with private and public keys. The address doesn’t have to belong to a wallet. The response will include the transaction fee in Wei.

### Example

* Api Key Authentication (ApiKey):
```python
import time
import os
import cryptoapis
from cryptoapis.models.prepare_a_non_fungible_token_transfer_from_address_r import PrepareANonFungibleTokenTransferFromAddressR
from cryptoapis.models.prepare_a_non_fungible_token_transfer_from_address_rb import PrepareANonFungibleTokenTransferFromAddressRB
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
    api_instance = cryptoapis.FeaturesApi(api_client)
    blockchain = 'ethereum' # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    network = 'goerli' # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"mordor\" are test networks.
    context = 'yourExampleString' # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    prepare_a_non_fungible_token_transfer_from_address_rb = cryptoapis.PrepareANonFungibleTokenTransferFromAddressRB() # PrepareANonFungibleTokenTransferFromAddressRB |  (optional)

    try:
        # Prepare A Non Fungible Token Transfer From Address
        api_response = api_instance.prepare_a_non_fungible_token_transfer_from_address(blockchain, network, context=context, prepare_a_non_fungible_token_transfer_from_address_rb=prepare_a_non_fungible_token_transfer_from_address_rb)
        print("The response of FeaturesApi->prepare_a_non_fungible_token_transfer_from_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeaturesApi->prepare_a_non_fungible_token_transfer_from_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. | 
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;mordor\&quot; are test networks. | 
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional] 
 **prepare_a_non_fungible_token_transfer_from_address_rb** | [**PrepareANonFungibleTokenTransferFromAddressRB**](PrepareANonFungibleTokenTransferFromAddressRB.md)|  | [optional] 

### Return type

[**PrepareANonFungibleTokenTransferFromAddressR**](PrepareANonFungibleTokenTransferFromAddressR.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The resource has been successfully submitted. |  -  |
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

# **prepare_transaction_from_address**
> PrepareTransactionFromAddressR prepare_transaction_from_address(blockchain, network, context=context, prepare_transaction_from_address_rb=prepare_transaction_from_address_rb)

Prepare Transaction From Address

Through this endpoint customers can prepare a transaction from an address with private and public keys. The address doesn’t have to belong to a wallet.  The response will include the transaction fee in Wei.

### Example

* Api Key Authentication (ApiKey):
```python
import time
import os
import cryptoapis
from cryptoapis.models.prepare_transaction_from_address_r import PrepareTransactionFromAddressR
from cryptoapis.models.prepare_transaction_from_address_rb import PrepareTransactionFromAddressRB
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
    api_instance = cryptoapis.FeaturesApi(api_client)
    blockchain = 'ethereum' # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    network = 'goerli' # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"goerli\" are test networks.
    context = 'yourExampleString' # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    prepare_transaction_from_address_rb = cryptoapis.PrepareTransactionFromAddressRB() # PrepareTransactionFromAddressRB |  (optional)

    try:
        # Prepare Transaction From Address
        api_response = api_instance.prepare_transaction_from_address(blockchain, network, context=context, prepare_transaction_from_address_rb=prepare_transaction_from_address_rb)
        print("The response of FeaturesApi->prepare_transaction_from_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeaturesApi->prepare_transaction_from_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. | 
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;goerli\&quot; are test networks. | 
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional] 
 **prepare_transaction_from_address_rb** | [**PrepareTransactionFromAddressRB**](PrepareTransactionFromAddressRB.md)|  | [optional] 

### Return type

[**PrepareTransactionFromAddressR**](PrepareTransactionFromAddressR.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The resource has been successfully submitted. |  -  |
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

# **validate_address**
> ValidateAddressR validate_address(blockchain, network, context=context, validate_address_rb=validate_address_rb)

Validate Address

This endpoint checks user public addresses whether they are valid or not.

### Example

* Api Key Authentication (ApiKey):
```python
import time
import os
import cryptoapis
from cryptoapis.models.validate_address_r import ValidateAddressR
from cryptoapis.models.validate_address_rb import ValidateAddressRB
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
    api_instance = cryptoapis.FeaturesApi(api_client)
    blockchain = 'bitcoin' # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    network = 'testnet' # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    context = 'yourExampleString' # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    validate_address_rb = cryptoapis.ValidateAddressRB() # ValidateAddressRB |  (optional)

    try:
        # Validate Address
        api_response = api_instance.validate_address(blockchain, network, context=context, validate_address_rb=validate_address_rb)
        print("The response of FeaturesApi->validate_address:\n")
        pprint(api_response)
    except Exception as e:
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

