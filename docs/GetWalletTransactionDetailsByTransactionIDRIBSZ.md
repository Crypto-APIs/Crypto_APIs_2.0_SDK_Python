# GetWalletTransactionDetailsByTransactionIDRIBSZ

Zcash

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**binding_sig** | **str** | It is used to enforce balance of Spend and Output transfers, in order to prevent their replay across transactions. | 
**expiry_height** | **int** | Represents a block height after which the transaction will expire. | 
**join_split_pub_key** | **str** | Represents an encoding of a JoinSplitSig public validating key. | 
**join_split_sig** | **str** | Is used to sign transactions that contain at least one JoinSplit description. | 
**locktime** | **int** | Represents the time at which a particular transaction can be added to the blockchain. | 
**overwintered** | **bool** | \&quot;Overwinter\&quot; is the network upgrade for the Zcash blockchain. | 
**size** | **int** | Represents the total size of this transaction. | 
**v_join_split** | [**List[GetTransactionDetailsByTransactionIDRIBSZVJoinSplitInner]**](GetTransactionDetailsByTransactionIDRIBSZVJoinSplitInner.md) | Represents a sequence of JoinSplit descriptions using BCTV14 proofs. | [optional] 
**v_shielded_output** | [**List[GetTransactionDetailsByTransactionIDRIBSZVShieldedOutputInner]**](GetTransactionDetailsByTransactionIDRIBSZVShieldedOutputInner.md) | Object Array representation of transaction output descriptions | [optional] 
**v_shielded_spend** | [**List[GetTransactionDetailsByTransactionIDRIBSZVShieldedSpendInner]**](GetTransactionDetailsByTransactionIDRIBSZVShieldedSpendInner.md) | Object Array representation of transaction spend descriptions | [optional] 
**value_balance** | **str** | String representation of the transaction value balance | 
**version** | **int** | Represents the transaction version number. | 
**version_group_id** | **str** | Represents the transaction version group ID. | 
**vin** | [**List[GetWalletTransactionDetailsByTransactionIDRIBSZVinInner]**](GetWalletTransactionDetailsByTransactionIDRIBSZVinInner.md) | Object Array representation of transaction inputs | 
**vout** | [**List[ListTransactionsByBlockHeightRIBSZVoutInner]**](ListTransactionsByBlockHeightRIBSZVoutInner.md) | Object Array representation of transaction outputs | 

## Example

```python
from cryptoapis.models.get_wallet_transaction_details_by_transaction_idribsz import GetWalletTransactionDetailsByTransactionIDRIBSZ

# TODO update the JSON string below
json = "{}"
# create an instance of GetWalletTransactionDetailsByTransactionIDRIBSZ from a JSON string
get_wallet_transaction_details_by_transaction_idribsz_instance = GetWalletTransactionDetailsByTransactionIDRIBSZ.from_json(json)
# print the JSON string representation of the object
print GetWalletTransactionDetailsByTransactionIDRIBSZ.to_json()

# convert the object into a dict
get_wallet_transaction_details_by_transaction_idribsz_dict = get_wallet_transaction_details_by_transaction_idribsz_instance.to_dict()
# create an instance of GetWalletTransactionDetailsByTransactionIDRIBSZ from a dict
get_wallet_transaction_details_by_transaction_idribsz_form_dict = get_wallet_transaction_details_by_transaction_idribsz.from_dict(get_wallet_transaction_details_by_transaction_idribsz_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


