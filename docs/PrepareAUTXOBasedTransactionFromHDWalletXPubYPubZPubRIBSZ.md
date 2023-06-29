# PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBSZ

Zcash

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**replaceable** | **bool** | Representation of whether the transaction is replaceable | [optional] 
**vin** | [**List[PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBSZVinInner]**](PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBSZVinInner.md) | Represents the transaction inputs. | 
**vout** | [**List[PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBSZVoutInner]**](PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBSZVoutInner.md) | Represents the transaction outputs. | 

## Example

```python
from cryptoapis.models.prepare_autxo_based_transaction_from_hd_wallet_x_pub_y_pub_z_pub_ribsz import PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBSZ

# TODO update the JSON string below
json = "{}"
# create an instance of PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBSZ from a JSON string
prepare_autxo_based_transaction_from_hd_wallet_x_pub_y_pub_z_pub_ribsz_instance = PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBSZ.from_json(json)
# print the JSON string representation of the object
print PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBSZ.to_json()

# convert the object into a dict
prepare_autxo_based_transaction_from_hd_wallet_x_pub_y_pub_z_pub_ribsz_dict = prepare_autxo_based_transaction_from_hd_wallet_x_pub_y_pub_z_pub_ribsz_instance.to_dict()
# create an instance of PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBSZ from a dict
prepare_autxo_based_transaction_from_hd_wallet_x_pub_y_pub_z_pub_ribsz_form_dict = prepare_autxo_based_transaction_from_hd_wallet_x_pub_y_pub_z_pub_ribsz.from_dict(prepare_autxo_based_transaction_from_hd_wallet_x_pub_y_pub_z_pub_ribsz_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


