# PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBS


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**replaceable** | **bool** | Representation of whether the transaction is replaceable | [optional] 
**vin** | [**List[PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBSZVinInner]**](PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBSZVinInner.md) | Represents the transaction inputs. | 
**vout** | [**List[PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBSZVoutInner]**](PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBSZVoutInner.md) | Represents the transaction outputs. | 

## Example

```python
from cryptoapis.models.prepare_autxo_based_transaction_from_hd_wallet_x_pub_y_pub_z_pub_ribs import PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBS

# TODO update the JSON string below
json = "{}"
# create an instance of PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBS from a JSON string
prepare_autxo_based_transaction_from_hd_wallet_x_pub_y_pub_z_pub_ribs_instance = PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBS.from_json(json)
# print the JSON string representation of the object
print PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBS.to_json()

# convert the object into a dict
prepare_autxo_based_transaction_from_hd_wallet_x_pub_y_pub_z_pub_ribs_dict = prepare_autxo_based_transaction_from_hd_wallet_x_pub_y_pub_z_pub_ribs_instance.to_dict()
# create an instance of PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBS from a dict
prepare_autxo_based_transaction_from_hd_wallet_x_pub_y_pub_z_pub_ribs_form_dict = prepare_autxo_based_transaction_from_hd_wallet_x_pub_y_pub_z_pub_ribs.from_dict(prepare_autxo_based_transaction_from_hd_wallet_x_pub_y_pub_z_pub_ribs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


