# cryptoapis.GeneratingApi

All URIs are relative to *https://rest.cryptoapis.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_new_master_wallet**](GeneratingApi.md#create_new_master_wallet) | **POST** /wallet-as-a-service/wallets/generate | Create New Master Wallet
[**generate_deposit_address**](GeneratingApi.md#generate_deposit_address) | **POST** /wallet-as-a-service/wallets/{walletId}/{blockchain}/{network}/addresses | Generate Deposit Address


# **create_new_master_wallet**
> CreateNewMasterWalletR create_new_master_wallet(context=context, create_new_master_wallet_rb=create_new_master_wallet_rb)

Create New Master Wallet

Through this endpoint users can easily create a new Master Wallet through the API. The user provides the desired Wallet name and in return the response includes the `walletId`. That new Wallet can be additionally also backed up through the Crypto APIs Dashboard.

### Example

* Api Key Authentication (ApiKey):
```python
import time
import os
import cryptoapis
from cryptoapis.models.create_new_master_wallet_r import CreateNewMasterWalletR
from cryptoapis.models.create_new_master_wallet_rb import CreateNewMasterWalletRB
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
    api_instance = cryptoapis.GeneratingApi(api_client)
    context = 'yourExampleString' # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    create_new_master_wallet_rb = cryptoapis.CreateNewMasterWalletRB() # CreateNewMasterWalletRB |  (optional)

    try:
        # Create New Master Wallet
        api_response = api_instance.create_new_master_wallet(context=context, create_new_master_wallet_rb=create_new_master_wallet_rb)
        print("The response of GeneratingApi->create_new_master_wallet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeneratingApi->create_new_master_wallet: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional] 
 **create_new_master_wallet_rb** | [**CreateNewMasterWalletRB**](CreateNewMasterWalletRB.md)|  | [optional] 

### Return type

[**CreateNewMasterWalletR**](CreateNewMasterWalletR.md)

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
**409** | The data provided seems to be invalid. |  -  |
**415** | The selected Media Type is unavailable. The Content-Type header should be &#39;application/json&#39;. |  -  |
**422** | Your request body for POST requests must have a structure of { data: { item: [...properties] } } |  -  |
**429** | The request limit has been reached. There can be maximum {requests} requests per {seconds} second(s) made. Please contact our team via email if you need more or upgrade your plan. |  -  |
**500** | An unexpected server error has occurred, we are working to fix this. Please try again later and in case it occurs again please report it to our team via email. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_deposit_address**
> GenerateDepositAddressR generate_deposit_address(blockchain, network, wallet_id, context=context, generate_deposit_address_rb=generate_deposit_address_rb)

Generate Deposit Address

Through this endpoint customers can generate a new Receiving/Deposit Addresses into their Wallet.

### Example

* Api Key Authentication (ApiKey):
```python
import time
import os
import cryptoapis
from cryptoapis.models.generate_deposit_address_r import GenerateDepositAddressR
from cryptoapis.models.generate_deposit_address_rb import GenerateDepositAddressRB
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
    api_instance = cryptoapis.GeneratingApi(api_client)
    blockchain = 'bitcoin' # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    network = 'testnet' # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"goerli\" are test networks.
    wallet_id = '60c9d9921c38030006675ff6' # str | Represents the unique ID of the specific Wallet.
    context = 'yourExampleString' # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    generate_deposit_address_rb = cryptoapis.GenerateDepositAddressRB() # GenerateDepositAddressRB |  (optional)

    try:
        # Generate Deposit Address
        api_response = api_instance.generate_deposit_address(blockchain, network, wallet_id, context=context, generate_deposit_address_rb=generate_deposit_address_rb)
        print("The response of GeneratingApi->generate_deposit_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeneratingApi->generate_deposit_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. | 
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;goerli\&quot; are test networks. | 
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

