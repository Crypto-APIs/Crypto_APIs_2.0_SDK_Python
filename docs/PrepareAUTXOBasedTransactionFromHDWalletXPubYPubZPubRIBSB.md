# PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBSB

Bitcoin

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**replaceable** | **bool** | Representation of whether the transaction is replaceable | [optional] 
**vin** | [**List[PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBSBVinInner]**](PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBSBVinInner.md) | Represents the transaction inputs. | 
**vout** | [**List[PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBSBVoutInner]**](PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBSBVoutInner.md) | Represents the transaction outputs. | 

## Example

```python
from cryptoapis.models.prepare_autxo_based_transaction_from_hd_wallet_x_pub_y_pub_z_pub_ribsb import PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBSB

# TODO update the JSON string below
json = "{}"
# create an instance of PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBSB from a JSON string
prepare_autxo_based_transaction_from_hd_wallet_x_pub_y_pub_z_pub_ribsb_instance = PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBSB.from_json(json)
# print the JSON string representation of the object
print PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBSB.to_json()

# convert the object into a dict
prepare_autxo_based_transaction_from_hd_wallet_x_pub_y_pub_z_pub_ribsb_dict = prepare_autxo_based_transaction_from_hd_wallet_x_pub_y_pub_z_pub_ribsb_instance.to_dict()
# create an instance of PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBSB from a dict
prepare_autxo_based_transaction_from_hd_wallet_x_pub_y_pub_z_pub_ribsb_form_dict = prepare_autxo_based_transaction_from_hd_wallet_x_pub_y_pub_z_pub_ribsb.from_dict(prepare_autxo_based_transaction_from_hd_wallet_x_pub_y_pub_z_pub_ribsb_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


