# PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRIBSE

Ethereum

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_hex** | **str** | Representation of the data in hex value | 
**derivation_index** | **int** | Representation of the derivation index of the xpub address | 
**fee** | [**PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRIBSEFee**](PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRIBSEFee.md) |  | 
**nonce** | **str** | Represents the sequential running number for an address, starting from 0 for the first transaction. E.g., if the nonce of a transaction is 10, it would be the 11th transaction sent from the sender&#39;s address. | 
**transaction_type** | **str** | Representation of the transaction type | 
**unit** | **str** | Represents the unit of the amount to be sent. | 

## Example

```python
from cryptoapis.models.prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_ribse import PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRIBSE

# TODO update the JSON string below
json = "{}"
# create an instance of PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRIBSE from a JSON string
prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_ribse_instance = PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRIBSE.from_json(json)
# print the JSON string representation of the object
print PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRIBSE.to_json()

# convert the object into a dict
prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_ribse_dict = prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_ribse_instance.to_dict()
# create an instance of PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRIBSE from a dict
prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_ribse_form_dict = prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_ribse.from_dict(prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_ribse_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


