# GetWalletTransactionDetailsByTransactionIDRIBS


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locktime** | **int** | Represents the time at which a particular transaction can be added to the blockchain. | 
**size** | **int** | Represents the total size of this transaction. | 
**v_size** | **int** | Represents the virtual size of this transaction. | 
**version** | **int** | Represents the transaction version number. | 
**vin** | [**List[GetWalletTransactionDetailsByTransactionIDRIBSZVinInner]**](GetWalletTransactionDetailsByTransactionIDRIBSZVinInner.md) | Object Array representation of transaction inputs | 
**vout** | [**List[ListTransactionsByBlockHeightRIBSZVoutInner]**](ListTransactionsByBlockHeightRIBSZVoutInner.md) | Object Array representation of transaction outputs | 
**contract** | **str** | Numeric representation of the transaction contract | 
**gas_limit** | **str** | Represents the amount of gas used by this specific transaction alone. | 
**gas_price** | [**GetTransactionDetailsByTransactionIDRIBSBSCGasPrice**](GetTransactionDetailsByTransactionIDRIBSBSCGasPrice.md) |  | 
**gas_used** | **str** | Defines the unit of the gas price amount, e.g. BTC, ETH, XRP. | 
**input_data** | **str** | Represents additional information that is required for the transaction. | 
**nonce** | **int** | Represents the sequential running number for an address, starting from 0 for the first transaction. E.g., if the nonce of a transaction is 10, it would be the 11th transaction sent from the sender&#39;s address. | 
**transaction_status** | **str** | String representation of the transaction status | 
**binding_sig** | **str** | It is used to enforce balance of Spend and Output transfers, in order to prevent their replay across transactions. | 
**expiry_height** | **int** | Represents a block height after which the transaction will expire. | 
**join_split_pub_key** | **str** | Represents an encoding of a JoinSplitSig public validating key. | 
**join_split_sig** | **str** | Is used to sign transactions that contain at least one JoinSplit description. | 
**overwintered** | **bool** | \&quot;Overwinter\&quot; is the network upgrade for the Zcash blockchain. | 
**v_join_split** | [**List[GetTransactionDetailsByTransactionIDRIBSZVJoinSplitInner]**](GetTransactionDetailsByTransactionIDRIBSZVJoinSplitInner.md) | Represents a sequence of JoinSplit descriptions using BCTV14 proofs. | [optional] 
**v_shielded_output** | [**List[GetTransactionDetailsByTransactionIDRIBSZVShieldedOutputInner]**](GetTransactionDetailsByTransactionIDRIBSZVShieldedOutputInner.md) | Object Array representation of transaction output descriptions | [optional] 
**v_shielded_spend** | [**List[GetTransactionDetailsByTransactionIDRIBSZVShieldedSpendInner]**](GetTransactionDetailsByTransactionIDRIBSZVShieldedSpendInner.md) | Object Array representation of transaction spend descriptions | [optional] 
**value_balance** | **str** | String representation of the transaction value balance | 
**version_group_id** | **str** | Represents the transaction version group ID. | 
**amount** | **str** | String representation of the amount value | 
**bandwidth_used** | **str** | Numeric representation of the transaction used bandwidth | 
**energy_used** | **str** | String representation of the transaction used energy | 
**has_internal_transactions** | **bool** |  | 
**has_token_transfers** | **bool** |  | 
**input** | **str** | Numeric representation of the transaction input | 
**status** | **str** | String representation of the transaction status | 

## Example

```python
from cryptoapis.models.get_wallet_transaction_details_by_transaction_idribs import GetWalletTransactionDetailsByTransactionIDRIBS

# TODO update the JSON string below
json = "{}"
# create an instance of GetWalletTransactionDetailsByTransactionIDRIBS from a JSON string
get_wallet_transaction_details_by_transaction_idribs_instance = GetWalletTransactionDetailsByTransactionIDRIBS.from_json(json)
# print the JSON string representation of the object
print GetWalletTransactionDetailsByTransactionIDRIBS.to_json()

# convert the object into a dict
get_wallet_transaction_details_by_transaction_idribs_dict = get_wallet_transaction_details_by_transaction_idribs_instance.to_dict()
# create an instance of GetWalletTransactionDetailsByTransactionIDRIBS from a dict
get_wallet_transaction_details_by_transaction_idribs_form_dict = get_wallet_transaction_details_by_transaction_idribs.from_dict(get_wallet_transaction_details_by_transaction_idribs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


