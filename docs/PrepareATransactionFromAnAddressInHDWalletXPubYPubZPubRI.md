# PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRI


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | Representation of the amount of the transaction | 
**recipient** | **str** | Represents a recipient addresses. In account-based protocols like Ethereum there is only one address in this list. | 
**sender** | **str** | Represents a sender address with the respective amount. In account-based protocols like Ethereum there is only one address in this list. | 
**sig_hash** | **str** | Representation of the hash that should be signed. | 
**blockchain_specific** | [**PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRIBS**](PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRIBS.md) |  | 

## Example

```python
from cryptoapis.models.prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_ri import PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRI

# TODO update the JSON string below
json = "{}"
# create an instance of PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRI from a JSON string
prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_ri_instance = PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRI.from_json(json)
# print the JSON string representation of the object
print PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRI.to_json()

# convert the object into a dict
prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_ri_dict = prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_ri_instance.to_dict()
# create an instance of PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRI from a dict
prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_ri_form_dict = prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_ri.from_dict(prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_ri_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


