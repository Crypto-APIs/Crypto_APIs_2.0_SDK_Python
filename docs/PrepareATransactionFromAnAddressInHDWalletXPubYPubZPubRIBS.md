# PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRIBS


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_hex** | **str** | Representation of the data in hex value | 
**derivation_index** | **int** | Representation of the derivation index of the xpub address | 
**fee** | [**PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRIBSXFee**](PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRIBSXFee.md) |  | 
**nonce** | **str** | Represents the sequential running number for an address, starting from 0 for the first transaction. E.g., if the nonce of a transaction is 10, it would be the 11th transaction sent from the sender&#39;s address. | 
**transaction_type** | **str** | Representation of the transaction type | 
**unit** | **str** | Represents the unit of the amount to be sent. | 
**data** | **str** | String representation of the data | 
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
**visible** | **bool** | Representation of the address visibility | 
**public_key** | **str** | Representation of the public key. | 
**sequence** | **str** | Representation of the sequence | 

## Example

```python
from cryptoapis.models.prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_ribs import PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRIBS

# TODO update the JSON string below
json = "{}"
# create an instance of PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRIBS from a JSON string
prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_ribs_instance = PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRIBS.from_json(json)
# print the JSON string representation of the object
print PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRIBS.to_json()

# convert the object into a dict
prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_ribs_dict = prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_ribs_instance.to_dict()
# create an instance of PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRIBS from a dict
prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_ribs_form_dict = prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_ribs.from_dict(prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_ribs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


