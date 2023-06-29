# ListConfirmedTransactionsByAddressRIBS


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locktime** | **int** | Represents the locktime on the transaction on the specific blockchain, i.e. the blockheight at which the transaction is valid. | 
**size** | **int** | Represents the total size of this transaction. | 
**v_size** | **int** | Represents the virtual size of this transaction. | 
**version** | **int** | Defines the version of the transaction. | 
**vin** | [**List[ListConfirmedTransactionsByAddressRIBSZVinInner]**](ListConfirmedTransactionsByAddressRIBSZVinInner.md) | Object Array representation of transaction inputs | 
**vout** | [**List[GetTransactionDetailsByTransactionIDRIBSZVoutInner]**](GetTransactionDetailsByTransactionIDRIBSZVoutInner.md) | Object Array representation of transaction outputs | 
**contract** | **str** | Numeric representation of the transaction contract | 
**gas_limit** | **str** | Represents the amount of gas used by this specific transaction alone. | 
**gas_price** | [**ListConfirmedTransactionsByAddressRIBSBSCGasPrice**](ListConfirmedTransactionsByAddressRIBSBSCGasPrice.md) |  | 
**gas_used** | **str** | Represents the exact unit of gas that was used for the transaction. | 
**input_data** | **str** | Numeric representation of the transaction input | 
**internal_transactions_count** | **int** | Representation of the internal transactions count | 
**nonce** | **int** | Defines the nonce | 
**token_transfers_count** | **int** | Representation of the  token transfers count | 
**transaction_status** | **str** | Defines the transaction status | 
**binding_sig** | **str** | It is used to enforce balance of Spend and Output transfers, in order to prevent their replay across transactions. | 
**expiry_height** | **int** | Represents a block height after which the transaction will expire. | 
**join_split_pub_key** | **str** | Represents an encoding of a JoinSplitSig public validating key. | 
**join_split_sig** | **str** | Is used to sign transactions that contain at least one JoinSplit description. | 
**overwintered** | **bool** | \&quot;Overwinter\&quot; is the network upgrade for the Zcash blockchain. | 
**v_join_split** | [**List[ListConfirmedTransactionsByAddressRIBSZVJoinSplitInner]**](ListConfirmedTransactionsByAddressRIBSZVJoinSplitInner.md) | Represents a sequence of JoinSplit descriptions using BCTV14 proofs. | 
**v_shielded_output** | [**List[GetTransactionDetailsByTransactionIDRIBSZVShieldedOutputInner]**](GetTransactionDetailsByTransactionIDRIBSZVShieldedOutputInner.md) | Object Array representation of transaction output descriptions | 
**v_shielded_spend** | [**List[GetTransactionDetailsByTransactionIDRIBSZVShieldedSpendInner]**](GetTransactionDetailsByTransactionIDRIBSZVShieldedSpendInner.md) | Object Array representation of transaction spend descriptions | 
**value_balance** | **str** | Defines the transaction value balance. | 
**version_group_id** | **str** | Represents the transaction version group ID. | 
**bandwidth_used** | **str** | Numeric representation of the transaction used bandwidth | 
**energy_used** | **str** | String representation of the transaction used energy | 
**has_internal_transactions** | **bool** | Represents the presence of internal transactions | 
**has_token_transfers** | **bool** | Defines if there are  tokens transfers (true) or not (false) | 
**addresses** | **List[str]** |  | 
**counter** | **int** | Representation of the counter value | 
**is_confirmed** | **bool** | Representation of the confirmation status of the transfer | 

## Example

```python
from cryptoapis.models.list_confirmed_transactions_by_address_ribs import ListConfirmedTransactionsByAddressRIBS

# TODO update the JSON string below
json = "{}"
# create an instance of ListConfirmedTransactionsByAddressRIBS from a JSON string
list_confirmed_transactions_by_address_ribs_instance = ListConfirmedTransactionsByAddressRIBS.from_json(json)
# print the JSON string representation of the object
print ListConfirmedTransactionsByAddressRIBS.to_json()

# convert the object into a dict
list_confirmed_transactions_by_address_ribs_dict = list_confirmed_transactions_by_address_ribs_instance.to_dict()
# create an instance of ListConfirmedTransactionsByAddressRIBS from a dict
list_confirmed_transactions_by_address_ribs_form_dict = list_confirmed_transactions_by_address_ribs.from_dict(list_confirmed_transactions_by_address_ribs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


