# PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRBDataItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_data** | **str** | Representation of the additional data. | [optional] 
**locktime** | **int** | Represents the time at which a particular transaction can be added to the blockchain. | [optional] 
**xpub** | **str** | Defines the account extended publicly known key which is used to derive all child public keys. | 
**fee** | [**PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRBDataItemFee**](PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRBDataItemFee.md) |  | 
**prepare_strategy** | **str** | Representation of the transaction&#39;s strategy type | [optional] 
**recipients** | [**List[PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRBDataItemRecipientsInner]**](PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRBDataItemRecipientsInner.md) | Object Array representation of transaction receivers | 
**replaceable** | **bool** | Representation of whether the transaction is replaceable. This is an Optional attribute that is not supported for Dogecoin, Dash and Bitcoin-Cash. | [optional] 

## Example

```python
from cryptoapis.models.prepare_autxo_based_transaction_from_hd_wallet_x_pub_y_pub_z_pub_rb_data_item import PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRBDataItem

# TODO update the JSON string below
json = "{}"
# create an instance of PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRBDataItem from a JSON string
prepare_autxo_based_transaction_from_hd_wallet_x_pub_y_pub_z_pub_rb_data_item_instance = PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRBDataItem.from_json(json)
# print the JSON string representation of the object
print PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRBDataItem.to_json()

# convert the object into a dict
prepare_autxo_based_transaction_from_hd_wallet_x_pub_y_pub_z_pub_rb_data_item_dict = prepare_autxo_based_transaction_from_hd_wallet_x_pub_y_pub_z_pub_rb_data_item_instance.to_dict()
# create an instance of PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRBDataItem from a dict
prepare_autxo_based_transaction_from_hd_wallet_x_pub_y_pub_z_pub_rb_data_item_form_dict = prepare_autxo_based_transaction_from_hd_wallet_x_pub_y_pub_z_pub_rb_data_item.from_dict(prepare_autxo_based_transaction_from_hd_wallet_x_pub_y_pub_z_pub_rb_data_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


