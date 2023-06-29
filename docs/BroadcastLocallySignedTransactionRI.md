# BroadcastLocallySignedTransactionRI


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | Represents the unique identifier of a transaction, i.e. it could be &#x60;transactionId&#x60; in UTXO-based protocols like Bitcoin, and transaction &#x60;hash&#x60; in Ethereum blockchain. | 

## Example

```python
from cryptoapis.models.broadcast_locally_signed_transaction_ri import BroadcastLocallySignedTransactionRI

# TODO update the JSON string below
json = "{}"
# create an instance of BroadcastLocallySignedTransactionRI from a JSON string
broadcast_locally_signed_transaction_ri_instance = BroadcastLocallySignedTransactionRI.from_json(json)
# print the JSON string representation of the object
print BroadcastLocallySignedTransactionRI.to_json()

# convert the object into a dict
broadcast_locally_signed_transaction_ri_dict = broadcast_locally_signed_transaction_ri_instance.to_dict()
# create an instance of BroadcastLocallySignedTransactionRI from a dict
broadcast_locally_signed_transaction_ri_form_dict = broadcast_locally_signed_transaction_ri.from_dict(broadcast_locally_signed_transaction_ri_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


