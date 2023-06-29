# PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRI


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_data** | **str** | Representation of the additional data | [optional] 
**fee** | **str** | When isConfirmed is True - Defines the amount of the transaction fee When isConfirmed is False - For ETH-based blockchains this attribute represents the max fee value. | 
**fee_per_byte** | **str** | Defines the fee per byte value | [optional] 
**locktime** | **int** | Represents the time at which a particular transaction can be added to the blockchain. | 
**size** | **int** | Represents the total size of this transaction. | 
**version** | **int** | Representation of the transaction&#39;s version | [optional] 
**blockchain_specific** | [**PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBS**](PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBS.md) |  | 

## Example

```python
from cryptoapis.models.prepare_autxo_based_transaction_from_hd_wallet_x_pub_y_pub_z_pub_ri import PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRI

# TODO update the JSON string below
json = "{}"
# create an instance of PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRI from a JSON string
prepare_autxo_based_transaction_from_hd_wallet_x_pub_y_pub_z_pub_ri_instance = PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRI.from_json(json)
# print the JSON string representation of the object
print PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRI.to_json()

# convert the object into a dict
prepare_autxo_based_transaction_from_hd_wallet_x_pub_y_pub_z_pub_ri_dict = prepare_autxo_based_transaction_from_hd_wallet_x_pub_y_pub_z_pub_ri_instance.to_dict()
# create an instance of PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRI from a dict
prepare_autxo_based_transaction_from_hd_wallet_x_pub_y_pub_z_pub_ri_form_dict = prepare_autxo_based_transaction_from_hd_wallet_x_pub_y_pub_z_pub_ri.from_dict(prepare_autxo_based_transaction_from_hd_wallet_x_pub_y_pub_z_pub_ri_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


