# ListUnspentTransactionOutputsByAddressRI


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Represents the address that has unspend funds per which the result is returned. | 
**amount** | **str** | Represents the sent/received amount. | 
**index** | **int** | Represents the index position of the transaction in the block. | 
**is_available** | **bool** | Represents if the UTXO has been used from another unconfirmed transaction. If it is - the value will be \&quot;false\&quot;. | 
**is_confirmed** | **bool** | Represents the state of the transaction whether it is confirmed or not confirmed. | 
**timestamp** | **int** | Defines the exact date/time in Unix Timestamp when this transaction was mined, confirmed or first seen in Mempool, if it is unconfirmed. | 
**transaction_id** | **str** | Represents the unique identifier of a transaction, i.e. it could be &#x60;transactionId&#x60; in UTXO-based protocols like Bitcoin, and transaction &#x60;hash&#x60; in Ethereum blockchain. | 

## Example

```python
from cryptoapis.models.list_unspent_transaction_outputs_by_address_ri import ListUnspentTransactionOutputsByAddressRI

# TODO update the JSON string below
json = "{}"
# create an instance of ListUnspentTransactionOutputsByAddressRI from a JSON string
list_unspent_transaction_outputs_by_address_ri_instance = ListUnspentTransactionOutputsByAddressRI.from_json(json)
# print the JSON string representation of the object
print ListUnspentTransactionOutputsByAddressRI.to_json()

# convert the object into a dict
list_unspent_transaction_outputs_by_address_ri_dict = list_unspent_transaction_outputs_by_address_ri_instance.to_dict()
# create an instance of ListUnspentTransactionOutputsByAddressRI from a dict
list_unspent_transaction_outputs_by_address_ri_form_dict = list_unspent_transaction_outputs_by_address_ri.from_dict(list_unspent_transaction_outputs_by_address_ri_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


