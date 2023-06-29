# PrepareANonFungibleTokenTransferFromAddressRIBSBSC

Binance Smart Chain

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_hex** | **str** | 0x0079006f00750072004100640064006900740069006f006e0061006c00440061007400610048006500720065 | [optional] 
**nonce** | **str** | Represents the sequential running number for an address, starting from 0 for the first transaction. E.g., if the nonce of a transaction is 10, it would be the 11th transaction sent from the sender&#39;s address. | [optional] 
**sig_hash** | **str** | Representation of the hash that should be signed | 
**fee** | [**PrepareANonFungibleTokenTransferFromAddressRIBSBSCFee**](PrepareANonFungibleTokenTransferFromAddressRIBSBSCFee.md) |  | 
**transaction_type** | **str** | Representation of the transaction type | 

## Example

```python
from cryptoapis.models.prepare_a_non_fungible_token_transfer_from_address_ribsbsc import PrepareANonFungibleTokenTransferFromAddressRIBSBSC

# TODO update the JSON string below
json = "{}"
# create an instance of PrepareANonFungibleTokenTransferFromAddressRIBSBSC from a JSON string
prepare_a_non_fungible_token_transfer_from_address_ribsbsc_instance = PrepareANonFungibleTokenTransferFromAddressRIBSBSC.from_json(json)
# print the JSON string representation of the object
print PrepareANonFungibleTokenTransferFromAddressRIBSBSC.to_json()

# convert the object into a dict
prepare_a_non_fungible_token_transfer_from_address_ribsbsc_dict = prepare_a_non_fungible_token_transfer_from_address_ribsbsc_instance.to_dict()
# create an instance of PrepareANonFungibleTokenTransferFromAddressRIBSBSC from a dict
prepare_a_non_fungible_token_transfer_from_address_ribsbsc_form_dict = prepare_a_non_fungible_token_transfer_from_address_ribsbsc.from_dict(prepare_a_non_fungible_token_transfer_from_address_ribsbsc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


