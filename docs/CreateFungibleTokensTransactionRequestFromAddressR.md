# CreateFungibleTokensTransactionRequestFromAddressR


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | Specifies the version of the API that incorporates this endpoint. | 
**request_id** | **str** | Defines the ID of the request. The &#x60;requestId&#x60; is generated by Crypto APIs and it&#39;s unique for every request. | 
**context** | **str** | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional] 
**data** | [**CreateFungibleTokensTransactionRequestFromAddressRData**](CreateFungibleTokensTransactionRequestFromAddressRData.md) |  | 

## Example

```python
from cryptoapis.models.create_fungible_tokens_transaction_request_from_address_r import CreateFungibleTokensTransactionRequestFromAddressR

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFungibleTokensTransactionRequestFromAddressR from a JSON string
create_fungible_tokens_transaction_request_from_address_r_instance = CreateFungibleTokensTransactionRequestFromAddressR.from_json(json)
# print the JSON string representation of the object
print CreateFungibleTokensTransactionRequestFromAddressR.to_json()

# convert the object into a dict
create_fungible_tokens_transaction_request_from_address_r_dict = create_fungible_tokens_transaction_request_from_address_r_instance.to_dict()
# create an instance of CreateFungibleTokensTransactionRequestFromAddressR from a dict
create_fungible_tokens_transaction_request_from_address_r_form_dict = create_fungible_tokens_transaction_request_from_address_r.from_dict(create_fungible_tokens_transaction_request_from_address_r_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


