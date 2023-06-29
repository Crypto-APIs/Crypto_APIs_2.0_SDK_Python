# PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBSL

Litecoin

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**replaceable** | **bool** | Representation of whether the transaction is replaceable | [optional] 
**vin** | [**List[PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBSLVinInner]**](PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBSLVinInner.md) | Represents the transaction inputs. | 
**vout** | [**List[PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBSLVoutInner]**](PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBSLVoutInner.md) | Represents the transaction outputs. | 

## Example

```python
from cryptoapis.models.prepare_autxo_based_transaction_from_hd_wallet_x_pub_y_pub_z_pub_ribsl import PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBSL

# TODO update the JSON string below
json = "{}"
# create an instance of PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBSL from a JSON string
prepare_autxo_based_transaction_from_hd_wallet_x_pub_y_pub_z_pub_ribsl_instance = PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBSL.from_json(json)
# print the JSON string representation of the object
print PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBSL.to_json()

# convert the object into a dict
prepare_autxo_based_transaction_from_hd_wallet_x_pub_y_pub_z_pub_ribsl_dict = prepare_autxo_based_transaction_from_hd_wallet_x_pub_y_pub_z_pub_ribsl_instance.to_dict()
# create an instance of PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBSL from a dict
prepare_autxo_based_transaction_from_hd_wallet_x_pub_y_pub_z_pub_ribsl_form_dict = prepare_autxo_based_transaction_from_hd_wallet_x_pub_y_pub_z_pub_ribsl.from_dict(prepare_autxo_based_transaction_from_hd_wallet_x_pub_y_pub_z_pub_ribsl_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


