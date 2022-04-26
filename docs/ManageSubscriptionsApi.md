# cryptoapis.ManageSubscriptionsApi

All URIs are relative to *https://rest.cryptoapis.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_blockchain_event_subscription**](ManageSubscriptionsApi.md#activate_blockchain_event_subscription) | **POST** /blockchain-events/subscriptions/{referenceId}/activate | Activate Blockchain Event Subscription
[**delete_blockchain_event_subscription**](ManageSubscriptionsApi.md#delete_blockchain_event_subscription) | **DELETE** /blockchain-events/{blockchain}/{network}/subscriptions/{referenceId} | Delete Blockchain Event Subscription
[**get_blockchain_event_subscription_details_by_reference_id**](ManageSubscriptionsApi.md#get_blockchain_event_subscription_details_by_reference_id) | **GET** /blockchain-events/subscriptions/{referenceId} | Get Blockchain Event Subscription Details By Reference ID
[**list_blockchain_events_subscriptions**](ManageSubscriptionsApi.md#list_blockchain_events_subscriptions) | **GET** /blockchain-events/{blockchain}/{network}/subscriptions | List Blockchain Events Subscriptions


# **activate_blockchain_event_subscription**
> ActivateBlockchainEventSubscriptionR activate_blockchain_event_subscription(reference_id)

Activate Blockchain Event Subscription

Through this endpoint customers can reactivate an event subscription (callback) which has been deactivated by the system. Deactivations could happen due to various reasons, most often \"maximum retry attempts reached\".

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import manage_subscriptions_api
from cryptoapis.model.inline_response429 import InlineResponse429
from cryptoapis.model.inline_response422 import InlineResponse422
from cryptoapis.model.inline_response409 import InlineResponse409
from cryptoapis.model.inline_response402 import InlineResponse402
from cryptoapis.model.inline_response40081 import InlineResponse40081
from cryptoapis.model.inline_response4041 import InlineResponse4041
from cryptoapis.model.inline_response500 import InlineResponse500
from cryptoapis.model.inline_response415 import InlineResponse415
from cryptoapis.model.inline_response40181 import InlineResponse40181
from cryptoapis.model.activate_blockchain_event_subscription_rb import ActivateBlockchainEventSubscriptionRB
from cryptoapis.model.activate_blockchain_event_subscription_r import ActivateBlockchainEventSubscriptionR
from cryptoapis.model.inline_response40381 import InlineResponse40381
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
    api_instance = manage_subscriptions_api.ManageSubscriptionsApi(api_client)
    reference_id = "bc243c86-0902-4386-b30d-e6b30fa1f2aa" # str | Represents a unique ID used to reference the specific callback subscription.
    context = "yourExampleString" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    activate_blockchain_event_subscription_rb = ActivateBlockchainEventSubscriptionRB(
        context="yourExampleString",
        data=ActivateBlockchainEventSubscriptionRBData(
            item={},
        ),
    ) # ActivateBlockchainEventSubscriptionRB |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Activate Blockchain Event Subscription
        api_response = api_instance.activate_blockchain_event_subscription(reference_id)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling ManageSubscriptionsApi->activate_blockchain_event_subscription: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Activate Blockchain Event Subscription
        api_response = api_instance.activate_blockchain_event_subscription(reference_id, context=context, activate_blockchain_event_subscription_rb=activate_blockchain_event_subscription_rb)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling ManageSubscriptionsApi->activate_blockchain_event_subscription: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reference_id** | **str**| Represents a unique ID used to reference the specific callback subscription. |
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]
 **activate_blockchain_event_subscription_rb** | [**ActivateBlockchainEventSubscriptionRB**](ActivateBlockchainEventSubscriptionRB.md)|  | [optional]

### Return type

[**ActivateBlockchainEventSubscriptionR**](ActivateBlockchainEventSubscriptionR.md)

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

# **delete_blockchain_event_subscription**
> DeleteBlockchainEventSubscriptionR delete_blockchain_event_subscription(blockchain, network, reference_id)

Delete Blockchain Event Subscription

Through this endpoint the customer can delete blockchain event subscriptions they have by attributes `referenceId` and `network`.    Currently Crypto APIs 2.0 offers certain Blockchain event endpoints which allow the user to subscribe for one/a few/all and receive callback notifications when the specific event occurs.    {note}To have an operational callback subscription, you need to first verify a domain for the Callback URL. Please see more information on Callbacks [here](https://developers.cryptoapis.io/technical-documentation/general-information/callbacks#callback-url).{/note}    {warning}Crypto APIs will notify the user **only when** the event occurs. There are cases when the specific event doesn't happen at all, or takes a long time to do so. A callback notification **will not** be sent if the event does not or cannot occur, or will take long time to occur.{/warning}

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import manage_subscriptions_api
from cryptoapis.model.inline_response429 import InlineResponse429
from cryptoapis.model.inline_response422 import InlineResponse422
from cryptoapis.model.inline_response409 import InlineResponse409
from cryptoapis.model.inline_response40082 import InlineResponse40082
from cryptoapis.model.inline_response402 import InlineResponse402
from cryptoapis.model.inline_response4041 import InlineResponse4041
from cryptoapis.model.inline_response500 import InlineResponse500
from cryptoapis.model.inline_response40182 import InlineResponse40182
from cryptoapis.model.inline_response415 import InlineResponse415
from cryptoapis.model.inline_response40382 import InlineResponse40382
from cryptoapis.model.delete_blockchain_event_subscription_r import DeleteBlockchainEventSubscriptionR
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
    api_instance = manage_subscriptions_api.ManageSubscriptionsApi(api_client)
    blockchain = "bitcoin" # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    network = "testnet" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    reference_id = "d3fd6a0e-f2b6-4bb5-9fd3-7944bcec9e9f" # str | Represents a unique ID used to reference the specific callback subscription.
    context = "yourExampleString" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete Blockchain Event Subscription
        api_response = api_instance.delete_blockchain_event_subscription(blockchain, network, reference_id)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling ManageSubscriptionsApi->delete_blockchain_event_subscription: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete Blockchain Event Subscription
        api_response = api_instance.delete_blockchain_event_subscription(blockchain, network, reference_id, context=context)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling ManageSubscriptionsApi->delete_blockchain_event_subscription: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. |
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. |
 **reference_id** | **str**| Represents a unique ID used to reference the specific callback subscription. |
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]

### Return type

[**DeleteBlockchainEventSubscriptionR**](DeleteBlockchainEventSubscriptionR.md)

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

# **get_blockchain_event_subscription_details_by_reference_id**
> GetBlockchainEventSubscriptionDetailsByReferenceIDR get_blockchain_event_subscription_details_by_reference_id(reference_id)

Get Blockchain Event Subscription Details By Reference ID

Through this endpoint the customer can get detailed information for a callback subscription by providing its reference ID.    Currently Crypto APIs 2.0 offers certain Blockchain event endpoints which allow the user to subscribe for one/a few/all and receive callback notifications when the specific event occurs.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import manage_subscriptions_api
from cryptoapis.model.inline_response429 import InlineResponse429
from cryptoapis.model.inline_response422 import InlineResponse422
from cryptoapis.model.inline_response409 import InlineResponse409
from cryptoapis.model.inline_response402 import InlineResponse402
from cryptoapis.model.inline_response40080 import InlineResponse40080
from cryptoapis.model.inline_response4041 import InlineResponse4041
from cryptoapis.model.inline_response500 import InlineResponse500
from cryptoapis.model.inline_response415 import InlineResponse415
from cryptoapis.model.inline_response40180 import InlineResponse40180
from cryptoapis.model.get_blockchain_event_subscription_details_by_reference_idr import GetBlockchainEventSubscriptionDetailsByReferenceIDR
from cryptoapis.model.inline_response40380 import InlineResponse40380
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
    api_instance = manage_subscriptions_api.ManageSubscriptionsApi(api_client)
    reference_id = "bc243c86-0902-4386-b30d-e6b30fa1f2aa" # str | Represents a unique ID used to reference the specific callback subscription.
    context = "yourExampleString" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Blockchain Event Subscription Details By Reference ID
        api_response = api_instance.get_blockchain_event_subscription_details_by_reference_id(reference_id)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling ManageSubscriptionsApi->get_blockchain_event_subscription_details_by_reference_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Blockchain Event Subscription Details By Reference ID
        api_response = api_instance.get_blockchain_event_subscription_details_by_reference_id(reference_id, context=context)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling ManageSubscriptionsApi->get_blockchain_event_subscription_details_by_reference_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reference_id** | **str**| Represents a unique ID used to reference the specific callback subscription. |
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]

### Return type

[**GetBlockchainEventSubscriptionDetailsByReferenceIDR**](GetBlockchainEventSubscriptionDetailsByReferenceIDR.md)

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

# **list_blockchain_events_subscriptions**
> ListBlockchainEventsSubscriptionsR list_blockchain_events_subscriptions(blockchain, network)

List Blockchain Events Subscriptions

Through this endpoint the customer can obtain a list of their callback subscriptions for the available Blockchain events.    Currently Crypto APIs 2.0 offers certain Blockchain event endpoints which allow the user to subscribe for one/a few/all and receive callback notifications when the specific event occurs.    {note}To have an operational callback subscription, you need to first verify a domain for the Callback URL. Please see more information on Callbacks [here](https://developers.cryptoapis.io/technical-documentation/general-information/callbacks#callback-url).{/note}

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import manage_subscriptions_api
from cryptoapis.model.inline_response429 import InlineResponse429
from cryptoapis.model.inline_response422 import InlineResponse422
from cryptoapis.model.inline_response409 import InlineResponse409
from cryptoapis.model.inline_response402 import InlineResponse402
from cryptoapis.model.inline_response40379 import InlineResponse40379
from cryptoapis.model.inline_response500 import InlineResponse500
from cryptoapis.model.inline_response415 import InlineResponse415
from cryptoapis.model.list_blockchain_events_subscriptions_r import ListBlockchainEventsSubscriptionsR
from cryptoapis.model.inline_response40079 import InlineResponse40079
from cryptoapis.model.inline_response40179 import InlineResponse40179
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
    api_instance = manage_subscriptions_api.ManageSubscriptionsApi(api_client)
    blockchain = "bitcoin" # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    network = "testnet" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    context = "yourExampleString" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    limit = 50 # int | Defines how many items should be returned in the response per page basis. (optional) if omitted the server will use the default value of 50
    offset = 0 # int | The starting index of the response items, i.e. where the response should start listing the returned items. (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    try:
        # List Blockchain Events Subscriptions
        api_response = api_instance.list_blockchain_events_subscriptions(blockchain, network)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling ManageSubscriptionsApi->list_blockchain_events_subscriptions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Blockchain Events Subscriptions
        api_response = api_instance.list_blockchain_events_subscriptions(blockchain, network, context=context, limit=limit, offset=offset)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling ManageSubscriptionsApi->list_blockchain_events_subscriptions: %s\n" % e)
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

[**ListBlockchainEventsSubscriptionsR**](ListBlockchainEventsSubscriptionsR.md)

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

