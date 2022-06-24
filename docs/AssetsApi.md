# cryptoapis.AssetsApi

All URIs are relative to *https://rest.cryptoapis.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_asset_details_by_asset_id**](AssetsApi.md#get_asset_details_by_asset_id) | **GET** /market-data/assets/assetId/{assetId} | Get Asset Details By Asset ID
[**get_asset_details_by_asset_symbol**](AssetsApi.md#get_asset_details_by_asset_symbol) | **GET** /market-data/assets/{assetSymbol} | Get Asset Details By Asset Symbol
[**list_assets_details**](AssetsApi.md#list_assets_details) | **GET** /market-data/assets/details | List Assets Details


# **get_asset_details_by_asset_id**
> GetAssetDetailsByAssetIDR get_asset_details_by_asset_id(asset_id)

Get Asset Details By Asset ID

Through this endpoint users can obtain information on assets by `assetId`.    The details returned could include information on the latest rate and rate fluctuation of different periods of time - 24 hours, a week, one hour, the encoding of the logo, and more.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import assets_api
from cryptoapis.model.get_asset_details_by_asset_idr import GetAssetDetailsByAssetIDR
from cryptoapis.model.get_address_details402_response import GetAddressDetails402Response
from cryptoapis.model.get_address_details500_response import GetAddressDetails500Response
from cryptoapis.model.get_address_details415_response import GetAddressDetails415Response
from cryptoapis.model.get_address_details422_response import GetAddressDetails422Response
from cryptoapis.model.get_address_details409_response import GetAddressDetails409Response
from cryptoapis.model.get_address_details429_response import GetAddressDetails429Response
from cryptoapis.model.get_asset_details_by_asset_id401_response import GetAssetDetailsByAssetID401Response
from cryptoapis.model.get_asset_details_by_asset_id400_response import GetAssetDetailsByAssetID400Response
from cryptoapis.model.get_asset_details_by_asset_id403_response import GetAssetDetailsByAssetID403Response
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
    api_instance = assets_api.AssetsApi(api_client)
    asset_id = "5b1ea92e584bf50020130612" # str | Defines the unique ID of the specific asset.
    context = "yourExampleString" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Asset Details By Asset ID
        api_response = api_instance.get_asset_details_by_asset_id(asset_id)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling AssetsApi->get_asset_details_by_asset_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Asset Details By Asset ID
        api_response = api_instance.get_asset_details_by_asset_id(asset_id, context=context)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling AssetsApi->get_asset_details_by_asset_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**| Defines the unique ID of the specific asset. |
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]

### Return type

[**GetAssetDetailsByAssetIDR**](GetAssetDetailsByAssetIDR.md)

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

# **get_asset_details_by_asset_symbol**
> GetAssetDetailsByAssetSymbolR get_asset_details_by_asset_symbol(asset_symbol)

Get Asset Details By Asset Symbol

Through this endpoint users can obtain information on assets by asset symbol.    The details returned could include information on the latest rate and rate fluctuation of different periods of time - 24 hours, a week, one hour, the encoding of the logo, and more.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import assets_api
from cryptoapis.model.get_address_details402_response import GetAddressDetails402Response
from cryptoapis.model.get_address_details500_response import GetAddressDetails500Response
from cryptoapis.model.get_address_details415_response import GetAddressDetails415Response
from cryptoapis.model.get_address_details422_response import GetAddressDetails422Response
from cryptoapis.model.get_address_details409_response import GetAddressDetails409Response
from cryptoapis.model.get_asset_details_by_asset_symbol403_response import GetAssetDetailsByAssetSymbol403Response
from cryptoapis.model.get_address_details429_response import GetAddressDetails429Response
from cryptoapis.model.get_asset_details_by_asset_symbol401_response import GetAssetDetailsByAssetSymbol401Response
from cryptoapis.model.get_asset_details_by_asset_symbol400_response import GetAssetDetailsByAssetSymbol400Response
from cryptoapis.model.get_asset_details_by_asset_symbol_r import GetAssetDetailsByAssetSymbolR
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
    api_instance = assets_api.AssetsApi(api_client)
    asset_symbol = "BTC" # str | Specifies the asset's unique symbol in the Crypto APIs listings.
    context = "yourExampleString" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Asset Details By Asset Symbol
        api_response = api_instance.get_asset_details_by_asset_symbol(asset_symbol)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling AssetsApi->get_asset_details_by_asset_symbol: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Asset Details By Asset Symbol
        api_response = api_instance.get_asset_details_by_asset_symbol(asset_symbol, context=context)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling AssetsApi->get_asset_details_by_asset_symbol: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_symbol** | **str**| Specifies the asset&#39;s unique symbol in the Crypto APIs listings. |
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]

### Return type

[**GetAssetDetailsByAssetSymbolR**](GetAssetDetailsByAssetSymbolR.md)

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

# **list_assets_details**
> ListAssetsDetailsR list_assets_details()

List Assets Details

This endpoint will return a list of details on assets. These could be cryptocurrencies or FIAT assets that we support. Each asset has a unique identifier - `assetId` and a unique symbol in the form of a string, e.g. \"BTC\".    The details returned could include information on the latest rate and rate fluctuation of different periods of time - 24 hours, a week, one hour, the encoding of the logo, and more.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import assets_api
from cryptoapis.model.get_address_details402_response import GetAddressDetails402Response
from cryptoapis.model.get_address_details500_response import GetAddressDetails500Response
from cryptoapis.model.get_address_details415_response import GetAddressDetails415Response
from cryptoapis.model.get_address_details422_response import GetAddressDetails422Response
from cryptoapis.model.list_assets_details403_response import ListAssetsDetails403Response
from cryptoapis.model.list_assets_details_r import ListAssetsDetailsR
from cryptoapis.model.get_address_details409_response import GetAddressDetails409Response
from cryptoapis.model.get_address_details429_response import GetAddressDetails429Response
from cryptoapis.model.list_assets_details400_response import ListAssetsDetails400Response
from cryptoapis.model.list_assets_details401_response import ListAssetsDetails401Response
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
    api_instance = assets_api.AssetsApi(api_client)
    context = "yourExampleString" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    asset_type = "crypto" # str | Defines the type of the supported asset. This could be either \"crypto\" or \"fiat\". (optional)
    crypto_type = "coin" # str | Subtype of the crypto assets. Could be COIN or TOKEN (optional)
    limit = 50 # int | Defines how many items should be returned in the response per page basis. (optional) if omitted the server will use the default value of 50
    offset = 0 # int | The starting index of the response items, i.e. where the response should start listing the returned items. (optional) if omitted the server will use the default value of 0
    waas_enabled = True # bool | Show only if WaaS is/not enabled (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Assets Details
        api_response = api_instance.list_assets_details(context=context, asset_type=asset_type, crypto_type=crypto_type, limit=limit, offset=offset, waas_enabled=waas_enabled)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling AssetsApi->list_assets_details: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]
 **asset_type** | **str**| Defines the type of the supported asset. This could be either \&quot;crypto\&quot; or \&quot;fiat\&quot;. | [optional]
 **crypto_type** | **str**| Subtype of the crypto assets. Could be COIN or TOKEN | [optional]
 **limit** | **int**| Defines how many items should be returned in the response per page basis. | [optional] if omitted the server will use the default value of 50
 **offset** | **int**| The starting index of the response items, i.e. where the response should start listing the returned items. | [optional] if omitted the server will use the default value of 0
 **waas_enabled** | **bool**| Show only if WaaS is/not enabled | [optional]

### Return type

[**ListAssetsDetailsR**](ListAssetsDetailsR.md)

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

