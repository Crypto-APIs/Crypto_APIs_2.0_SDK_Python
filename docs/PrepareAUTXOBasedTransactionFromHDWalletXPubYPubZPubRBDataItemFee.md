# PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRBDataItemFee

When isConfirmed is True - Defines the amount of the transaction fee When isConfirmed is False - For ETH-based blockchains this attribute represents the max fee value.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Representation of the address | [optional] 
**exact_amount** | **str** | Representation of the exact amount | [optional] 
**priority** | **str** | Representation of the fee priority | [optional] 

## Example

```python
from cryptoapis.models.prepare_autxo_based_transaction_from_hd_wallet_x_pub_y_pub_z_pub_rb_data_item_fee import PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRBDataItemFee

# TODO update the JSON string below
json = "{}"
# create an instance of PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRBDataItemFee from a JSON string
prepare_autxo_based_transaction_from_hd_wallet_x_pub_y_pub_z_pub_rb_data_item_fee_instance = PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRBDataItemFee.from_json(json)
# print the JSON string representation of the object
print PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRBDataItemFee.to_json()

# convert the object into a dict
prepare_autxo_based_transaction_from_hd_wallet_x_pub_y_pub_z_pub_rb_data_item_fee_dict = prepare_autxo_based_transaction_from_hd_wallet_x_pub_y_pub_z_pub_rb_data_item_fee_instance.to_dict()
# create an instance of PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRBDataItemFee from a dict
prepare_autxo_based_transaction_from_hd_wallet_x_pub_y_pub_z_pub_rb_data_item_fee_form_dict = prepare_autxo_based_transaction_from_hd_wallet_x_pub_y_pub_z_pub_rb_data_item_fee.from_dict(prepare_autxo_based_transaction_from_hd_wallet_x_pub_y_pub_z_pub_rb_data_item_fee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


