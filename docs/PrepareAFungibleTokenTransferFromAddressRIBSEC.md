# PrepareAFungibleTokenTransferFromAddressRIBSEC

Ethereum Classic

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_hex** | **str** | Representation of the data in hex value | [optional] 
**sig_hash** | **str** | Representation of the hash that should be signed | 
**fee** | [**PrepareANonFungibleTokenTransferFromAddressRIBSBSCFee**](PrepareANonFungibleTokenTransferFromAddressRIBSBSCFee.md) |  | 
**transaction_type** | **str** | Representation of the transaction type | 

## Example

```python
from cryptoapis.models.prepare_a_fungible_token_transfer_from_address_ribsec import PrepareAFungibleTokenTransferFromAddressRIBSEC

# TODO update the JSON string below
json = "{}"
# create an instance of PrepareAFungibleTokenTransferFromAddressRIBSEC from a JSON string
prepare_a_fungible_token_transfer_from_address_ribsec_instance = PrepareAFungibleTokenTransferFromAddressRIBSEC.from_json(json)
# print the JSON string representation of the object
print PrepareAFungibleTokenTransferFromAddressRIBSEC.to_json()

# convert the object into a dict
prepare_a_fungible_token_transfer_from_address_ribsec_dict = prepare_a_fungible_token_transfer_from_address_ribsec_instance.to_dict()
# create an instance of PrepareAFungibleTokenTransferFromAddressRIBSEC from a dict
prepare_a_fungible_token_transfer_from_address_ribsec_form_dict = prepare_a_fungible_token_transfer_from_address_ribsec.from_dict(prepare_a_fungible_token_transfer_from_address_ribsec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


