# PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBSBVinInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Representation of the address | 
**change** | **int** | Representation of the change value | 
**derivation_index** | **int** | Representation of the derivation index of the xpub | 
**output_index** | **int** | Representation of the output index | 
**satoshis** | **int** | Representation of the satoshis value | 
**script** | **str** | Representation of the script string | 
**sighash** | **str** | Representation of the hash that should be signed. | 
**transaction_id** | **str** | Represents the reference transaction identifier. | 

## Example

```python
from cryptoapis.models.prepare_autxo_based_transaction_from_hd_wallet_x_pub_y_pub_z_pub_ribsb_vin_inner import PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBSBVinInner

# TODO update the JSON string below
json = "{}"
# create an instance of PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBSBVinInner from a JSON string
prepare_autxo_based_transaction_from_hd_wallet_x_pub_y_pub_z_pub_ribsb_vin_inner_instance = PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBSBVinInner.from_json(json)
# print the JSON string representation of the object
print PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBSBVinInner.to_json()

# convert the object into a dict
prepare_autxo_based_transaction_from_hd_wallet_x_pub_y_pub_z_pub_ribsb_vin_inner_dict = prepare_autxo_based_transaction_from_hd_wallet_x_pub_y_pub_z_pub_ribsb_vin_inner_instance.to_dict()
# create an instance of PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBSBVinInner from a dict
prepare_autxo_based_transaction_from_hd_wallet_x_pub_y_pub_z_pub_ribsb_vin_inner_form_dict = prepare_autxo_based_transaction_from_hd_wallet_x_pub_y_pub_z_pub_ribsb_vin_inner.from_dict(prepare_autxo_based_transaction_from_hd_wallet_x_pub_y_pub_z_pub_ribsb_vin_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


