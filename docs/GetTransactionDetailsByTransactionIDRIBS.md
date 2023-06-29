# GetTransactionDetailsByTransactionIDRIBS


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locktime** | **int** | Represents the locktime on the transaction on the specific blockchain, i.e. the blockheight at which the transaction is valid. | 
**size** | **int** | Represents the total size of this transaction. | 
**v_size** | **int** | Represents the virtual size of this transaction. | 
**version** | **int** | Defines the version of the transaction. | 
**vin** | [**List[GetTransactionDetailsByTransactionIDRIBSZVinInner]**](GetTransactionDetailsByTransactionIDRIBSZVinInner.md) | Object Array representation of transaction inputs | 
**vout** | [**List[GetTransactionDetailsByTransactionIDRIBSZVoutInner]**](GetTransactionDetailsByTransactionIDRIBSZVoutInner.md) | Object Array representation of transaction outputs | 
**contract** | **str** | Represents the specific transaction contract | [optional] 
**gas_limit** | **str** | Represents the amount of gas used by this specific transaction alone. | 
**gas_price** | [**GetTransactionDetailsByTransactionIDRIBSBSCGasPrice**](GetTransactionDetailsByTransactionIDRIBSBSCGasPrice.md) |  | 
**gas_used** | **str** | Defines the unit of the gas price amount, e.g. BTC, ETH, XRP. | 
**input_data** | **str** | Represents additional information that is required for the transaction. | [optional] 
**nonce** | **int** | Represents the sequential running number for an address, starting from 0 for the first transaction. E.g., if the nonce of a transaction is 10, it would be the 11th transaction sent from the sender&#39;s address. | 
**transaction_status** | **str** | Represents the status of this transaction. | 
**binding_sig** | **str** | It is used to enforce balance of Spend and Output transfers, in order to prevent their replay across transactions. | 
**expiry_height** | **int** | Represents a block height after which the transaction will expire. | 
**join_split_pub_key** | **str** | Represents an encoding of a JoinSplitSig public validating key. | 
**join_split_sig** | **str** | Is used to sign transactions that contain at least one JoinSplit description. | 
**overwintered** | **bool** | \&quot;Overwinter\&quot; is the network upgrade for the Zcash blockchain. | 
**v_join_split** | [**List[GetTransactionDetailsByTransactionIDRIBSZVJoinSplitInner]**](GetTransactionDetailsByTransactionIDRIBSZVJoinSplitInner.md) | Represents a sequence of JoinSplit descriptions using BCTV14 proofs. | 
**v_shielded_output** | [**List[GetTransactionDetailsByTransactionIDRIBSZVShieldedOutputInner]**](GetTransactionDetailsByTransactionIDRIBSZVShieldedOutputInner.md) | Object Array representation of transaction output descriptions | 
**v_shielded_spend** | [**List[GetTransactionDetailsByTransactionIDRIBSZVShieldedSpendInner]**](GetTransactionDetailsByTransactionIDRIBSZVShieldedSpendInner.md) | Object Array representation of transaction spend descriptions | 
**value_balance** | **str** | String representation of the transaction value balance | 
**version_group_id** | **str** | Represents the transaction version group ID. | 

## Example

```python
from cryptoapis.models.get_transaction_details_by_transaction_idribs import GetTransactionDetailsByTransactionIDRIBS

# TODO update the JSON string below
json = "{}"
# create an instance of GetTransactionDetailsByTransactionIDRIBS from a JSON string
get_transaction_details_by_transaction_idribs_instance = GetTransactionDetailsByTransactionIDRIBS.from_json(json)
# print the JSON string representation of the object
print GetTransactionDetailsByTransactionIDRIBS.to_json()

# convert the object into a dict
get_transaction_details_by_transaction_idribs_dict = get_transaction_details_by_transaction_idribs_instance.to_dict()
# create an instance of GetTransactionDetailsByTransactionIDRIBS from a dict
get_transaction_details_by_transaction_idribs_form_dict = get_transaction_details_by_transaction_idribs.from_dict(get_transaction_details_by_transaction_idribs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


