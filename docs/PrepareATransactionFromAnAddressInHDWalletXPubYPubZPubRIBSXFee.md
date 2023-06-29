# PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRIBSXFee

When isConfirmed is True - Defines the amount of the transaction fee When isConfirmed is False - For ETH-based blockchains this attribute represents the max fee value.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee_in_drops** | **str** | Representation of the fee in drops value | 
**fee_in_xrp** | **str** | Representation of the fee in XRP | 

## Example

```python
from cryptoapis.models.prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_ribsx_fee import PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRIBSXFee

# TODO update the JSON string below
json = "{}"
# create an instance of PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRIBSXFee from a JSON string
prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_ribsx_fee_instance = PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRIBSXFee.from_json(json)
# print the JSON string representation of the object
print PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRIBSXFee.to_json()

# convert the object into a dict
prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_ribsx_fee_dict = prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_ribsx_fee_instance.to_dict()
# create an instance of PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRIBSXFee from a dict
prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_ribsx_fee_form_dict = prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_ribsx_fee.from_dict(prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_ribsx_fee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


