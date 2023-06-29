# GetTransactionDetailsByTransactionIDFromCallbackRIBSZ

Zcash

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**binding_sig** | **str** | It is used to enforce balance of Spend and Output transfers, in order to prevent their replay across transactions. | 
**expiry_height** | **int** | Represents a block height after which the transaction will expire. | 
**join_split_pub_key** | **str** | Represents an encoding of a JoinSplitSig public validating key. | 
**join_split_sig** | **str** | Is used to sign transactions that contain at least one JoinSplit description. | 
**locktime** | **int** | Represents the locktime on the transaction on the specific blockchain, i.e. the blockheight at which the transaction is valid. | 
**overwintered** | **bool** | \&quot;Overwinter\&quot; is the network upgrade for the Zcash blockchain. | 
**size** | **int** | Represents the total size of this transaction. | 
**v_join_split** | [**List[GetTransactionDetailsByTransactionIDRIBSZVJoinSplitInner]**](GetTransactionDetailsByTransactionIDRIBSZVJoinSplitInner.md) | Represents a sequence of JoinSplit descriptions using BCTV14 proofs. | 
**v_shielded_output** | [**List[GetTransactionDetailsByTransactionIDRIBSZVShieldedOutputInner]**](GetTransactionDetailsByTransactionIDRIBSZVShieldedOutputInner.md) | Object Array representation of transaction output descriptions | 
**v_shielded_spend** | [**List[GetTransactionDetailsByTransactionIDRIBSZVShieldedSpendInner]**](GetTransactionDetailsByTransactionIDRIBSZVShieldedSpendInner.md) | Object Array representation of transaction spend descriptions | 
**value_balance** | **str** | String representation of the transaction value balance | 
**version** | **int** | Defines the version of the transaction. | 
**version_group_id** | **str** | Represents the transaction version group ID | 
**vin** | [**List[GetTransactionDetailsByTransactionIDRIBSZVinInner]**](GetTransactionDetailsByTransactionIDRIBSZVinInner.md) | Object Array representation of transaction inputs | 
**vout** | [**List[GetTransactionDetailsByTransactionIDFromCallbackRIBSZVoutInner]**](GetTransactionDetailsByTransactionIDFromCallbackRIBSZVoutInner.md) | Object Array representation of transaction outputs | 

## Example

```python
from cryptoapis.models.get_transaction_details_by_transaction_id_from_callback_ribsz import GetTransactionDetailsByTransactionIDFromCallbackRIBSZ

# TODO update the JSON string below
json = "{}"
# create an instance of GetTransactionDetailsByTransactionIDFromCallbackRIBSZ from a JSON string
get_transaction_details_by_transaction_id_from_callback_ribsz_instance = GetTransactionDetailsByTransactionIDFromCallbackRIBSZ.from_json(json)
# print the JSON string representation of the object
print GetTransactionDetailsByTransactionIDFromCallbackRIBSZ.to_json()

# convert the object into a dict
get_transaction_details_by_transaction_id_from_callback_ribsz_dict = get_transaction_details_by_transaction_id_from_callback_ribsz_instance.to_dict()
# create an instance of GetTransactionDetailsByTransactionIDFromCallbackRIBSZ from a dict
get_transaction_details_by_transaction_id_from_callback_ribsz_form_dict = get_transaction_details_by_transaction_id_from_callback_ribsz.from_dict(get_transaction_details_by_transaction_id_from_callback_ribsz_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


