# PrepareAFungibleTokenTransferFromAddressRIBS


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_hex** | **str** | Representation of the data in hex value | [optional] 
**sig_hash** | **str** | Representation of the hash that should be signed | 
**fee** | [**PrepareANonFungibleTokenTransferFromAddressRIBSBSCFee**](PrepareANonFungibleTokenTransferFromAddressRIBSBSCFee.md) |  | 
**transaction_type** | **str** | Representation of the transaction type | 

## Example

```python
from cryptoapis.models.prepare_a_fungible_token_transfer_from_address_ribs import PrepareAFungibleTokenTransferFromAddressRIBS

# TODO update the JSON string below
json = "{}"
# create an instance of PrepareAFungibleTokenTransferFromAddressRIBS from a JSON string
prepare_a_fungible_token_transfer_from_address_ribs_instance = PrepareAFungibleTokenTransferFromAddressRIBS.from_json(json)
# print the JSON string representation of the object
print PrepareAFungibleTokenTransferFromAddressRIBS.to_json()

# convert the object into a dict
prepare_a_fungible_token_transfer_from_address_ribs_dict = prepare_a_fungible_token_transfer_from_address_ribs_instance.to_dict()
# create an instance of PrepareAFungibleTokenTransferFromAddressRIBS from a dict
prepare_a_fungible_token_transfer_from_address_ribs_form_dict = prepare_a_fungible_token_transfer_from_address_ribs.from_dict(prepare_a_fungible_token_transfer_from_address_ribs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


