# GetTransactionDetailsByTransactionIDRIBSZVShieldedSpendInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anchor** | **str** | Defines a Merkle tree root of a note commitment tree which uniquely identifies a note commitment tree state given the assumed security properties of the Merkle tree’s  hash function. | 
**cv** | **str** | Defines a value commitment to the value of the input note. | 
**nullifier** | **str** | Represents a sequence of nullifiers of the input notes. | 
**proof** | **str** | Represents the proof. | 
**rk** | **str** | Represents the randomized validating key for spendAuthSig. | 
**spend_auth_sig** | **str** | Used to prove knowledge of the spending key authorizing spending of an input note. | 

## Example

```python
from cryptoapis.models.get_transaction_details_by_transaction_idribszv_shielded_spend_inner import GetTransactionDetailsByTransactionIDRIBSZVShieldedSpendInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetTransactionDetailsByTransactionIDRIBSZVShieldedSpendInner from a JSON string
get_transaction_details_by_transaction_idribszv_shielded_spend_inner_instance = GetTransactionDetailsByTransactionIDRIBSZVShieldedSpendInner.from_json(json)
# print the JSON string representation of the object
print GetTransactionDetailsByTransactionIDRIBSZVShieldedSpendInner.to_json()

# convert the object into a dict
get_transaction_details_by_transaction_idribszv_shielded_spend_inner_dict = get_transaction_details_by_transaction_idribszv_shielded_spend_inner_instance.to_dict()
# create an instance of GetTransactionDetailsByTransactionIDRIBSZVShieldedSpendInner from a dict
get_transaction_details_by_transaction_idribszv_shielded_spend_inner_form_dict = get_transaction_details_by_transaction_idribszv_shielded_spend_inner.from_dict(get_transaction_details_by_transaction_idribszv_shielded_spend_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


