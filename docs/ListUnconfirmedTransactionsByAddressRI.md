# ListUnconfirmedTransactionsByAddressRI


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipients** | [**List[ListUnconfirmedTransactionsByAddressRIRecipientsInner]**](ListUnconfirmedTransactionsByAddressRIRecipientsInner.md) | Represents a list of recipient addresses with the respective amounts. In account-based protocols like Ethereum there is only one address in this list. | 
**senders** | [**List[ListUnconfirmedTransactionsByAddressRISendersInner]**](ListUnconfirmedTransactionsByAddressRISendersInner.md) | Represents a list of sender addresses with the respective amounts. In account-based protocols like Ethereum there is only one address in this list. | 
**timestamp** | **int** | Defines the exact date/time in Unix Timestamp when this transaction was mined, confirmed or first seen in Mempool, if it is unconfirmed. | 
**transaction_hash** | **str** | Represents the same as &#x60;transactionId&#x60; for account-based protocols like Ethereum, while it could be different in UTXO-based protocols like Bitcoin. E.g., in UTXO-based protocols &#x60;hash&#x60; is different from &#x60;transactionId&#x60; for SegWit transactions. | 
**transaction_id** | **str** | Represents the unique identifier of a transaction, i.e. it could be &#x60;transactionId&#x60; in UTXO-based protocols like Bitcoin, and transaction &#x60;hash&#x60; in Ethereum blockchain. | 
**blockchain_specific** | [**ListUnconfirmedTransactionsByAddressRIBS**](ListUnconfirmedTransactionsByAddressRIBS.md) |  | 

## Example

```python
from cryptoapis.models.list_unconfirmed_transactions_by_address_ri import ListUnconfirmedTransactionsByAddressRI

# TODO update the JSON string below
json = "{}"
# create an instance of ListUnconfirmedTransactionsByAddressRI from a JSON string
list_unconfirmed_transactions_by_address_ri_instance = ListUnconfirmedTransactionsByAddressRI.from_json(json)
# print the JSON string representation of the object
print ListUnconfirmedTransactionsByAddressRI.to_json()

# convert the object into a dict
list_unconfirmed_transactions_by_address_ri_dict = list_unconfirmed_transactions_by_address_ri_instance.to_dict()
# create an instance of ListUnconfirmedTransactionsByAddressRI from a dict
list_unconfirmed_transactions_by_address_ri_form_dict = list_unconfirmed_transactions_by_address_ri.from_dict(list_unconfirmed_transactions_by_address_ri_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


