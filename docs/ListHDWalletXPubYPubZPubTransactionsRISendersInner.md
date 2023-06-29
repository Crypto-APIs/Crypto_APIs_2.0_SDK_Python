# ListHDWalletXPubYPubZPubTransactionsRISendersInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Represents the address which sends this transaction. In UTXO-based protocols like Bitcoin there could be several senders while in account-based protocols like Ethereum there is always only one sender. | 
**amount** | **str** | Represents the amount sent by this address. | 
**is_member** | **bool** | Defines whether an address is a child address derived from the HD wallet (xPub, yPub, zPub) as boolean. | 

## Example

```python
from cryptoapis.models.list_hd_wallet_x_pub_y_pub_z_pub_transactions_ri_senders_inner import ListHDWalletXPubYPubZPubTransactionsRISendersInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListHDWalletXPubYPubZPubTransactionsRISendersInner from a JSON string
list_hd_wallet_x_pub_y_pub_z_pub_transactions_ri_senders_inner_instance = ListHDWalletXPubYPubZPubTransactionsRISendersInner.from_json(json)
# print the JSON string representation of the object
print ListHDWalletXPubYPubZPubTransactionsRISendersInner.to_json()

# convert the object into a dict
list_hd_wallet_x_pub_y_pub_z_pub_transactions_ri_senders_inner_dict = list_hd_wallet_x_pub_y_pub_z_pub_transactions_ri_senders_inner_instance.to_dict()
# create an instance of ListHDWalletXPubYPubZPubTransactionsRISendersInner from a dict
list_hd_wallet_x_pub_y_pub_z_pub_transactions_ri_senders_inner_form_dict = list_hd_wallet_x_pub_y_pub_z_pub_transactions_ri_senders_inner.from_dict(list_hd_wallet_x_pub_y_pub_z_pub_transactions_ri_senders_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


