# PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRIBST

Tron

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **str** | String representation of the data | 
**derivation_index** | **str** | Representation of the derivation index of the xpub address | 
**expiration** | **int** | Rrepresentation of the expiration value | 
**raw_data** | [**PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRIBSTRawData**](PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRIBSTRawData.md) |  | [optional] 
**raw_data_hex** | **str** | Representation of the raw data in hex format | 
**recipient** | **str** | Rrepresentation of the recipients&#39; address | 
**ref_block_bytes** | **str** | Representation of the block bytes | 
**ref_block_hash** | **str** | Representation of the block hash refference | 
**sender** | **str** | Representation of the sender | 
**timestamp** | **int** | Representation of the timestamp | 
**transaction_id** | **str** | Represents the reference transaction identifier. | 
**type** | **str** | Representation of the transfer type. | 
**type_url** | **str** | Representation of the URL | 
**unit** | **str** | Represents the unit of the amount to be sent. | 
**visible** | **bool** | Representation of the address visibility | 

## Example

```python
from cryptoapis.models.prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_ribst import PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRIBST

# TODO update the JSON string below
json = "{}"
# create an instance of PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRIBST from a JSON string
prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_ribst_instance = PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRIBST.from_json(json)
# print the JSON string representation of the object
print PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRIBST.to_json()

# convert the object into a dict
prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_ribst_dict = prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_ribst_instance.to_dict()
# create an instance of PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRIBST from a dict
prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_ribst_form_dict = prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_ribst.from_dict(prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_ribst_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


