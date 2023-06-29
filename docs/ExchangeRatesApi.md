# cryptoapis.ExchangeRatesApi

All URIs are relative to *https://rest.cryptoapis.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_exchange_rate_by_asset_symbols**](ExchangeRatesApi.md#get_exchange_rate_by_asset_symbols) | **GET** /market-data/exchange-rates/by-symbols/{fromAssetSymbol}/{toAssetSymbol} | Get Exchange Rate By Asset Symbols
[**get_exchange_rate_by_assets_ids**](ExchangeRatesApi.md#get_exchange_rate_by_assets_ids) | **GET** /market-data/exchange-rates/by-asset-ids/{fromAssetId}/{toAssetId} | Get Exchange Rate By Assets IDs


# **get_exchange_rate_by_asset_symbols**
> GetExchangeRateByAssetSymbolsR get_exchange_rate_by_asset_symbols(from_asset_symbol, to_asset_symbol, context=context, calculation_timestamp=calculation_timestamp)

Get Exchange Rate By Asset Symbols

Through this endpoint customers can obtain exchange rates by asset symbols. The process represents the exchange rate value of a single unit of one asset versus another one. Data is provided per unique asset symbol.

### Example

* Api Key Authentication (ApiKey):
```python
import time
import os
import cryptoapis
from cryptoapis.models.get_exchange_rate_by_asset_symbols_r import GetExchangeRateByAssetSymbolsR
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
    api_instance = cryptoapis.ExchangeRatesApi(api_client)
    from_asset_symbol = 'btc' # str | Defines the base asset symbol to get a rate for.
    to_asset_symbol = 'usd' # str | Defines the relation asset symbol in which the base asset rate will be displayed.
    context = 'yourExampleString' # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    calculation_timestamp = 1635514425 # int | Defines the time of the market data used to calculate the exchange rate in UNIX Timestamp. Oldest possible timestamp is 30 days. (optional)

    try:
        # Get Exchange Rate By Asset Symbols
        api_response = api_instance.get_exchange_rate_by_asset_symbols(from_asset_symbol, to_asset_symbol, context=context, calculation_timestamp=calculation_timestamp)
        print("The response of ExchangeRatesApi->get_exchange_rate_by_asset_symbols:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExchangeRatesApi->get_exchange_rate_by_asset_symbols: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **from_asset_symbol** | **str**| Defines the base asset symbol to get a rate for. | 
 **to_asset_symbol** | **str**| Defines the relation asset symbol in which the base asset rate will be displayed. | 
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional] 
 **calculation_timestamp** | **int**| Defines the time of the market data used to calculate the exchange rate in UNIX Timestamp. Oldest possible timestamp is 30 days. | [optional] 

### Return type

[**GetExchangeRateByAssetSymbolsR**](GetExchangeRateByAssetSymbolsR.md)

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
**422** | 422 |  -  |
**429** | The request limit has been reached. There can be maximum {requests} requests per {seconds} second(s) made. Please contact our team via email if you need more or upgrade your plan. |  -  |
**500** | An unexpected server error has occurred, we are working to fix this. Please try again later and in case it occurs again please report it to our team via email. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_exchange_rate_by_assets_ids**
> GetExchangeRateByAssetsIDsR get_exchange_rate_by_assets_ids(from_asset_id, to_asset_id, context=context, calculation_timestamp=calculation_timestamp)

Get Exchange Rate By Assets IDs

Through this endpoint customers can obtain exchange rates by asset IDs. The process represents the exchange rate value of a single unit of one asset versus another one. Data is provided per unique asset Reference ID.

### Example

* Api Key Authentication (ApiKey):
```python
import time
import os
import cryptoapis
from cryptoapis.models.get_exchange_rate_by_assets_ids_r import GetExchangeRateByAssetsIDsR
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
    api_instance = cryptoapis.ExchangeRatesApi(api_client)
    from_asset_id = '5b1ea92e584bf50020130612' # str | Defines the base asset Reference ID to get a rate for.
    to_asset_id = '5b1ea92e584bf50020130615' # str | Defines the relation asset Reference ID in which the base asset rate will be displayed.
    context = 'yourExampleString' # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    calculation_timestamp = 1618577849 # int | Defines the time of the market data used to calculate the exchange rate in UNIX Timestamp. Oldest possible timestamp is 30 days. (optional)

    try:
        # Get Exchange Rate By Assets IDs
        api_response = api_instance.get_exchange_rate_by_assets_ids(from_asset_id, to_asset_id, context=context, calculation_timestamp=calculation_timestamp)
        print("The response of ExchangeRatesApi->get_exchange_rate_by_assets_ids:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExchangeRatesApi->get_exchange_rate_by_assets_ids: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **from_asset_id** | **str**| Defines the base asset Reference ID to get a rate for. | 
 **to_asset_id** | **str**| Defines the relation asset Reference ID in which the base asset rate will be displayed. | 
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional] 
 **calculation_timestamp** | **int**| Defines the time of the market data used to calculate the exchange rate in UNIX Timestamp. Oldest possible timestamp is 30 days. | [optional] 

### Return type

[**GetExchangeRateByAssetsIDsR**](GetExchangeRateByAssetsIDsR.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request has been successfull. |  -  |
**400** | 400 |  -  |
**401** | 401 |  -  |
**402** | You have insufficient credits. Please upgrade your plan from your Dashboard or contact our team via email. |  -  |
**403** | 403 |  -  |
**409** | The data provided seems to be invalid. |  -  |
**415** | The selected Media Type is unavailable. The Content-Type header should be &#39;application/json&#39;. |  -  |
**422** | 422 |  -  |
**429** | The request limit has been reached. There can be maximum {requests} requests per {seconds} second(s) made. Please contact our team via email if you need more or upgrade your plan. |  -  |
**500** | An unexpected server error has occurred, we are working to fix this. Please try again later and in case it occurs again please report it to our team via email. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

