# ListHDWalletXPubYPubZPubTransactionsRIRecipientsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The address which receives this transaction. In UTXO-based protocols like Bitcoin there could be several senders while in account-based protocols like Ethereum there is always only one recipient. | 
**amount** | **str** | Represents the amount received to this address. | 
**is_member** | **bool** | Defines whether an address is a child address derived from the HD wallet (xPub, yPub, zPub) as boolean. | 

## Example

```python
from cryptoapis.models.list_hd_wallet_x_pub_y_pub_z_pub_transactions_ri_recipients_inner import ListHDWalletXPubYPubZPubTransactionsRIRecipientsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListHDWalletXPubYPubZPubTransactionsRIRecipientsInner from a JSON string
list_hd_wallet_x_pub_y_pub_z_pub_transactions_ri_recipients_inner_instance = ListHDWalletXPubYPubZPubTransactionsRIRecipientsInner.from_json(json)
# print the JSON string representation of the object
print ListHDWalletXPubYPubZPubTransactionsRIRecipientsInner.to_json()

# convert the object into a dict
list_hd_wallet_x_pub_y_pub_z_pub_transactions_ri_recipients_inner_dict = list_hd_wallet_x_pub_y_pub_z_pub_transactions_ri_recipients_inner_instance.to_dict()
# create an instance of ListHDWalletXPubYPubZPubTransactionsRIRecipientsInner from a dict
list_hd_wallet_x_pub_y_pub_z_pub_transactions_ri_recipients_inner_form_dict = list_hd_wallet_x_pub_y_pub_z_pub_transactions_ri_recipients_inner.from_dict(list_hd_wallet_x_pub_y_pub_z_pub_transactions_ri_recipients_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


