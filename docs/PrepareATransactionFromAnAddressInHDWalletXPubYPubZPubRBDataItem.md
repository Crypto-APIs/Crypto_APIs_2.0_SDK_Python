# PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRBDataItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_data** | **str** | Representation of the additional data. | [optional] 
**amount** | **str** | Representation of the amount of the transaction | 
**recipient** | **str** | Represents a list of recipient addresses with the respective amounts. In account-based protocols like Ethereum there is only one address in this list. | 
**sender** | **str** | Represents a  sender address with the respective amount. In account-based protocols like Ethereum there is only one address in this list. | 
**xpub** | **str** | Defines the account extended publicly known key which is used to derive all child public keys. | 
**fee** | [**PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRBDataItemFee**](PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRBDataItemFee.md) |  | 
**nonce** | **str** | Representation of the nonce value | [optional] 
**transaction_type** | **str** | Representation of the transaction type. For Ethereum-Classic and Binance Smart Chain there is no need to provide \&quot;transactionType\&quot; in the request. | [optional] [default to 'gas-fee-market-transaction']
**sequence** | **str** | String representation of the sequence | 

## Example

```python
from cryptoapis.models.prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_rb_data_item import PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRBDataItem

# TODO update the JSON string below
json = "{}"
# create an instance of PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRBDataItem from a JSON string
prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_rb_data_item_instance = PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRBDataItem.from_json(json)
# print the JSON string representation of the object
print PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRBDataItem.to_json()

# convert the object into a dict
prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_rb_data_item_dict = prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_rb_data_item_instance.to_dict()
# create an instance of PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRBDataItem from a dict
prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_rb_data_item_form_dict = prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_rb_data_item.from_dict(prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_rb_data_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


