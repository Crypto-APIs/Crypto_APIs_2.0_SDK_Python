# PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRIBSECFee

When isConfirmed is True - Defines the amount of the transaction fee When isConfirmed is False - For ETH-based blockchains this attribute represents the max fee value.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gas_limit** | **str** | Represents the amount of gas used by this specific transaction alone. | 
**gas_price** | **str** | Represents the price offered to the miner to purchase this amount of gas. | 

## Example

```python
from cryptoapis.models.prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_ribsec_fee import PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRIBSECFee

# TODO update the JSON string below
json = "{}"
# create an instance of PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRIBSECFee from a JSON string
prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_ribsec_fee_instance = PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRIBSECFee.from_json(json)
# print the JSON string representation of the object
print PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRIBSECFee.to_json()

# convert the object into a dict
prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_ribsec_fee_dict = prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_ribsec_fee_instance.to_dict()
# create an instance of PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRIBSECFee from a dict
prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_ribsec_fee_form_dict = prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_ribsec_fee.from_dict(prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_ribsec_fee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


