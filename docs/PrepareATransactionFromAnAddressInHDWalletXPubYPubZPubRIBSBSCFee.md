# PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRIBSBSCFee

When isConfirmed is True - Defines the amount of the transaction fee When isConfirmed is False - For ETH-based blockchains this attribute represents the max fee value.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gas_limit** | **str** | Represents the amount of gas used by this specific transaction alone. | 
**gas_price** | **str** | Represents the price offered to the miner to purchase this amount of gas. | [optional] 

## Example

```python
from cryptoapis.models.prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_ribsbsc_fee import PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRIBSBSCFee

# TODO update the JSON string below
json = "{}"
# create an instance of PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRIBSBSCFee from a JSON string
prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_ribsbsc_fee_instance = PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRIBSBSCFee.from_json(json)
# print the JSON string representation of the object
print PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRIBSBSCFee.to_json()

# convert the object into a dict
prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_ribsbsc_fee_dict = prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_ribsbsc_fee_instance.to_dict()
# create an instance of PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRIBSBSCFee from a dict
prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_ribsbsc_fee_form_dict = prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_ribsbsc_fee.from_dict(prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_ribsbsc_fee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


