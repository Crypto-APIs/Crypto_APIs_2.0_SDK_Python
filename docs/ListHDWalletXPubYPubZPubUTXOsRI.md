# ListHDWalletXPubYPubZPubUTXOsRI


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Represents the public address, which is a compressed and shortened form of a public key. | 
**address_path** | **str** | Defines a data which tells a Hierarchical Deterministic wallet how to derive a specific key within a tree of keys. | 
**amount** | **str** | Represents the UTXO amount value. | 
**derivation** | **str** | The way how the HD walled derives, for example when the type is ACCOUNT, it derives change and receive addresses while when the type is BIP32 it derives directly. | 
**index** | **int** | Represents the output index. It refers to the UTXO sequence in the transaction outputs (vout). | 
**is_available** | **bool** | Represents if the UTXO has been used from another unconfirmed transaction. If it is - the value will be \&quot;false\&quot;. | 
**is_confirmed** | **bool** | Represents the state of the transaction whether it is confirmed or not confirmed. | 
**reference_id** | **str** | Represents the reference id of the record. It may be used for the startingAfter pagination attribute. | 
**transaction_id** | **str** | Represents the unique identifier of a transaction, i.e. it could be transactionId in UTXO-based protocols like Bitcoin, and transaction hash in Ethereum blockchain. | 

## Example

```python
from cryptoapis.models.list_hd_wallet_x_pub_y_pub_z_pub_utxos_ri import ListHDWalletXPubYPubZPubUTXOsRI

# TODO update the JSON string below
json = "{}"
# create an instance of ListHDWalletXPubYPubZPubUTXOsRI from a JSON string
list_hd_wallet_x_pub_y_pub_z_pub_utxos_ri_instance = ListHDWalletXPubYPubZPubUTXOsRI.from_json(json)
# print the JSON string representation of the object
print ListHDWalletXPubYPubZPubUTXOsRI.to_json()

# convert the object into a dict
list_hd_wallet_x_pub_y_pub_z_pub_utxos_ri_dict = list_hd_wallet_x_pub_y_pub_z_pub_utxos_ri_instance.to_dict()
# create an instance of ListHDWalletXPubYPubZPubUTXOsRI from a dict
list_hd_wallet_x_pub_y_pub_z_pub_utxos_ri_form_dict = list_hd_wallet_x_pub_y_pub_z_pub_utxos_ri.from_dict(list_hd_wallet_x_pub_y_pub_z_pub_utxos_ri_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


