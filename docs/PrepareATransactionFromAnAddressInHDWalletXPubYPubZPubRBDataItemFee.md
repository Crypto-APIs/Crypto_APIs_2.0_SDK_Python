# PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRBDataItemFee

When isConfirmed is True - Defines the amount of the transaction fee When isConfirmed is False - For ETH-based blockchains this attribute represents the max fee value.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exact_amount** | **str** | String representation of the exact amount | [optional] 
**priority** | **str** | Enum representation of the fee priority | 

## Example

```python
from cryptoapis.models.prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_rb_data_item_fee import PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRBDataItemFee

# TODO update the JSON string below
json = "{}"
# create an instance of PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRBDataItemFee from a JSON string
prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_rb_data_item_fee_instance = PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRBDataItemFee.from_json(json)
# print the JSON string representation of the object
print PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRBDataItemFee.to_json()

# convert the object into a dict
prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_rb_data_item_fee_dict = prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_rb_data_item_fee_instance.to_dict()
# create an instance of PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRBDataItemFee from a dict
prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_rb_data_item_fee_form_dict = prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_rb_data_item_fee.from_dict(prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_rb_data_item_fee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


