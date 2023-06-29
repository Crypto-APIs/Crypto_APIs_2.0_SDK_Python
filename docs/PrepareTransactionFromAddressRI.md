# PrepareTransactionFromAddressRI


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | Representation of the transacted amount | 
**data_hex** | **str** | Representation of the data in hex value | [optional] 
**nonce** | **str** | Represents the sequential running number for an address, starting from 0 for the first transaction. E.g., if the nonce of a transaction is 10, it would be the 11th transaction sent from the sender&#39;s address. | [optional] 
**recipient** | **str** | The address which receives this transaction. In UTXO-based protocols like Bitcoin there could be several senders while in account-based protocols like Ethereum there is always only one recipient. | 
**sender** | **str** | Represents the address which sends this transaction. In UTXO-based protocols like Bitcoin there could be several senders while in account-based protocols like Ethereum there is always only one sender. | 
**sighash** | **str** | Representation of the hash that should be signed | 
**blockchain_specific** | [**PrepareTransactionFromAddressRIBS**](PrepareTransactionFromAddressRIBS.md) |  | 

## Example

```python
from cryptoapis.models.prepare_transaction_from_address_ri import PrepareTransactionFromAddressRI

# TODO update the JSON string below
json = "{}"
# create an instance of PrepareTransactionFromAddressRI from a JSON string
prepare_transaction_from_address_ri_instance = PrepareTransactionFromAddressRI.from_json(json)
# print the JSON string representation of the object
print PrepareTransactionFromAddressRI.to_json()

# convert the object into a dict
prepare_transaction_from_address_ri_dict = prepare_transaction_from_address_ri_instance.to_dict()
# create an instance of PrepareTransactionFromAddressRI from a dict
prepare_transaction_from_address_ri_form_dict = prepare_transaction_from_address_ri.from_dict(prepare_transaction_from_address_ri_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


