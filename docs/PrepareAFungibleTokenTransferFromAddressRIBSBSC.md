# PrepareAFungibleTokenTransferFromAddressRIBSBSC

Binance Smart Chain

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_hex** | **str** | Representation of the data in hex value | [optional] 
**sig_hash** | **str** | Representation of the hash that should be signed | 
**fee** | [**PrepareANonFungibleTokenTransferFromAddressRIBSBSCFee**](PrepareANonFungibleTokenTransferFromAddressRIBSBSCFee.md) |  | 
**transaction_type** | **str** | Representation of the transaction type | 

## Example

```python
from cryptoapis.models.prepare_a_fungible_token_transfer_from_address_ribsbsc import PrepareAFungibleTokenTransferFromAddressRIBSBSC

# TODO update the JSON string below
json = "{}"
# create an instance of PrepareAFungibleTokenTransferFromAddressRIBSBSC from a JSON string
prepare_a_fungible_token_transfer_from_address_ribsbsc_instance = PrepareAFungibleTokenTransferFromAddressRIBSBSC.from_json(json)
# print the JSON string representation of the object
print PrepareAFungibleTokenTransferFromAddressRIBSBSC.to_json()

# convert the object into a dict
prepare_a_fungible_token_transfer_from_address_ribsbsc_dict = prepare_a_fungible_token_transfer_from_address_ribsbsc_instance.to_dict()
# create an instance of PrepareAFungibleTokenTransferFromAddressRIBSBSC from a dict
prepare_a_fungible_token_transfer_from_address_ribsbsc_form_dict = prepare_a_fungible_token_transfer_from_address_ribsbsc.from_dict(prepare_a_fungible_token_transfer_from_address_ribsbsc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


