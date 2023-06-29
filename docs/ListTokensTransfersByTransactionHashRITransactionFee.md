# ListTokensTransfersByTransactionHashRITransactionFee


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | Represents the total fee of a transaction which includes token transfers. | 
**unit** | **str** | Represents the unit of the fee. | 

## Example

```python
from cryptoapis.models.list_tokens_transfers_by_transaction_hash_ri_transaction_fee import ListTokensTransfersByTransactionHashRITransactionFee

# TODO update the JSON string below
json = "{}"
# create an instance of ListTokensTransfersByTransactionHashRITransactionFee from a JSON string
list_tokens_transfers_by_transaction_hash_ri_transaction_fee_instance = ListTokensTransfersByTransactionHashRITransactionFee.from_json(json)
# print the JSON string representation of the object
print ListTokensTransfersByTransactionHashRITransactionFee.to_json()

# convert the object into a dict
list_tokens_transfers_by_transaction_hash_ri_transaction_fee_dict = list_tokens_transfers_by_transaction_hash_ri_transaction_fee_instance.to_dict()
# create an instance of ListTokensTransfersByTransactionHashRITransactionFee from a dict
list_tokens_transfers_by_transaction_hash_ri_transaction_fee_form_dict = list_tokens_transfers_by_transaction_hash_ri_transaction_fee.from_dict(list_tokens_transfers_by_transaction_hash_ri_transaction_fee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


