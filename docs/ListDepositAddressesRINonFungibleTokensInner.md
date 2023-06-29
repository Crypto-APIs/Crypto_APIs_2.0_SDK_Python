# ListDepositAddressesRINonFungibleTokensInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Defines the specific token identifier. For Bitcoin-based transactions it should be the propertyId and for Ethereum-based transactions - the contract. | 
**name** | **str** | Defines the token&#39;s name as a string. | 
**symbol** | **str** | Defines the symbol of the non-fungible tokens. | 
**token_id** | **str** | Represents tokens&#39; unique identifier. | 
**type** | **str** | Defines the specific token type. | 

## Example

```python
from cryptoapis.models.list_deposit_addresses_ri_non_fungible_tokens_inner import ListDepositAddressesRINonFungibleTokensInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListDepositAddressesRINonFungibleTokensInner from a JSON string
list_deposit_addresses_ri_non_fungible_tokens_inner_instance = ListDepositAddressesRINonFungibleTokensInner.from_json(json)
# print the JSON string representation of the object
print ListDepositAddressesRINonFungibleTokensInner.to_json()

# convert the object into a dict
list_deposit_addresses_ri_non_fungible_tokens_inner_dict = list_deposit_addresses_ri_non_fungible_tokens_inner_instance.to_dict()
# create an instance of ListDepositAddressesRINonFungibleTokensInner from a dict
list_deposit_addresses_ri_non_fungible_tokens_inner_form_dict = list_deposit_addresses_ri_non_fungible_tokens_inner.from_dict(list_deposit_addresses_ri_non_fungible_tokens_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


