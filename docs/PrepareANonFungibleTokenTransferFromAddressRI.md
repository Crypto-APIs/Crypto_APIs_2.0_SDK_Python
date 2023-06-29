# PrepareANonFungibleTokenTransferFromAddressRI


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipient** | **str** | Represents the address which sends this transaction. In UTXO-based protocols like Bitcoin there could be several senders while in account-based protocols like Ethereum there is always only one sender. | 
**sender** | **str** | The address which receives this transaction. In UTXO-based protocols like Bitcoin there could be several senders while in account-based protocols like Ethereum there is always only one recipient. | 
**token_id** | **str** | Represents the unique token identifier. | 
**blockchain_specific** | [**PrepareANonFungibleTokenTransferFromAddressRIBS**](PrepareANonFungibleTokenTransferFromAddressRIBS.md) |  | 

## Example

```python
from cryptoapis.models.prepare_a_non_fungible_token_transfer_from_address_ri import PrepareANonFungibleTokenTransferFromAddressRI

# TODO update the JSON string below
json = "{}"
# create an instance of PrepareANonFungibleTokenTransferFromAddressRI from a JSON string
prepare_a_non_fungible_token_transfer_from_address_ri_instance = PrepareANonFungibleTokenTransferFromAddressRI.from_json(json)
# print the JSON string representation of the object
print PrepareANonFungibleTokenTransferFromAddressRI.to_json()

# convert the object into a dict
prepare_a_non_fungible_token_transfer_from_address_ri_dict = prepare_a_non_fungible_token_transfer_from_address_ri_instance.to_dict()
# create an instance of PrepareANonFungibleTokenTransferFromAddressRI from a dict
prepare_a_non_fungible_token_transfer_from_address_ri_form_dict = prepare_a_non_fungible_token_transfer_from_address_ri.from_dict(prepare_a_non_fungible_token_transfer_from_address_ri_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


