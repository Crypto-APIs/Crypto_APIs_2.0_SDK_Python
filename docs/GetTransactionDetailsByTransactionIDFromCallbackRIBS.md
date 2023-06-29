# GetTransactionDetailsByTransactionIDFromCallbackRIBS


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locktime** | **int** | Represents the locktime on the transaction on the specific blockchain, i.e. the blockheight at which the transaction is valid. | 
**size** | **int** | Represents the total size of this transaction. | 
**v_size** | **int** | Represents the virtual size of this transaction. | 
**version** | **int** | Defines the version of the transaction. | 
**vin** | [**List[GetTransactionDetailsByTransactionIDRIBSZVinInner]**](GetTransactionDetailsByTransactionIDRIBSZVinInner.md) | Object Array representation of transaction inputs | 
**vout** | [**List[GetTransactionDetailsByTransactionIDFromCallbackRIBSZVoutInner]**](GetTransactionDetailsByTransactionIDFromCallbackRIBSZVoutInner.md) | Object Array representation of transaction outputs | 
**contract** | **str** | Represents the specific transaction contract. | 
**gas_limit** | **str** | Represents the amount of gas used by this specific transaction alone. | 
**gas_price** | **str** | Represents the price offered to the miner to purchase this amount of gas. | 
**gas_used** | **str** | Represents the exact unit of gas that was used for the transaction. | 
**input_data** | **str** | Represents additional information that is required for the transaction. | 
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
**version_group_id** | **str** | Represents the transaction version group ID | 
**additional_data** | **str** | Represents additional data that may be needed. | 
**destination_tag** | **int** | Defines the destination tag value. | [optional] 
**offer** | [**GetXRPRippleTransactionDetailsByTransactionIDRIOffer**](GetXRPRippleTransactionDetailsByTransactionIDRIOffer.md) |  | 
**receive** | [**GetXRPRippleTransactionDetailsByTransactionIDRIReceive**](GetXRPRippleTransactionDetailsByTransactionIDRIReceive.md) |  | 
**sequence** | **int** | Defines the transaction input&#39;s sequence as an integer, which is is used when transactions are replaced with newer versions before LockTime. | 
**status** | **str** | Defines the status of the transaction. | 
**type** | **str** | Defines the type of the transaction. | 
**value** | [**GetTransactionDetailsByTransactionIDFromCallbackRIBSXValue**](GetTransactionDetailsByTransactionIDFromCallbackRIBSXValue.md) |  | 
**amount** | **str** | Representation of the amount value. | 
**bandwidth_used** | [**GetTransactionDetailsByTransactionIDFromCallbackRIBSTBandwidthUsed**](GetTransactionDetailsByTransactionIDFromCallbackRIBSTBandwidthUsed.md) |  | 
**energy_used** | [**GetTransactionDetailsByTransactionIDFromCallbackRIBSTEnergyUsed**](GetTransactionDetailsByTransactionIDFromCallbackRIBSTEnergyUsed.md) |  | 
**has_internal_transactions** | **bool** | Defines if the transaction includes internal transactions (true) or not (false). | 
**has_token_transfers** | **str** | Defines if the transaction includes token transfers (true) or not (false). | 
**input** | **str** | Represents additional information that is required for the transaction. | 
**recipients** | **str** | Represents a list of recipient addresses with the respective amounts. In account-based protocols like Ethereum there is only one address in this list. | 
**senders** | **str** | Represents a list of sender addresses with the respective amounts. In account-based protocols like Ethereum there is only one address in this list. | 
**gas** | **str** | Represents the price offered to the miner to purchase this amount of gas. | 
**txid** | **str** | Represents the unique identifier of a transaction, i.e. it could be transactionId in UTXO-based protocols like Bitcoin, and transaction hash in Ethereum blockchain. | 

## Example

```python
from cryptoapis.models.get_transaction_details_by_transaction_id_from_callback_ribs import GetTransactionDetailsByTransactionIDFromCallbackRIBS

# TODO update the JSON string below
json = "{}"
# create an instance of GetTransactionDetailsByTransactionIDFromCallbackRIBS from a JSON string
get_transaction_details_by_transaction_id_from_callback_ribs_instance = GetTransactionDetailsByTransactionIDFromCallbackRIBS.from_json(json)
# print the JSON string representation of the object
print GetTransactionDetailsByTransactionIDFromCallbackRIBS.to_json()

# convert the object into a dict
get_transaction_details_by_transaction_id_from_callback_ribs_dict = get_transaction_details_by_transaction_id_from_callback_ribs_instance.to_dict()
# create an instance of GetTransactionDetailsByTransactionIDFromCallbackRIBS from a dict
get_transaction_details_by_transaction_id_from_callback_ribs_form_dict = get_transaction_details_by_transaction_id_from_callback_ribs.from_dict(get_transaction_details_by_transaction_id_from_callback_ribs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


