# GetBlockDetailsByBlockHeightFromCallbackRIBS


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bits** | **str** | Represents a specific sub-unit of Zcash. Bits have two-decimal precision | 
**chainwork** | **str** | Represents a hexadecimal number of all the hashes necessary to produce the current chain. E.g., when converting 0000000000000000000000000000000000000000000086859f7a841475b236fd to a decimal you get 635262017308958427068157 hashes, or 635262 exahashes. | 
**difficulty** | **str** | Represents a mathematical value of how hard it is to find a valid hash for this block. | 
**merkle_root** | **str** | Defines the single and final (root) node of a Merkle tree. It is the combined hash of all transactions&#39; hashes that are part of a blockchain block. | 
**nonce** | **str** | Represents the sequential running number for an address, starting from 0 for the first transaction. E.g., if the nonce of a transaction is 10, it would be the 11th transaction sent from the sender&#39;s address. | 
**size** | **int** | Represents the total size of the block in Bytes. | 
**stripped_size** | **int** | Defines the numeric representation of the block size excluding the witness data. | 
**version** | **int** | Represents the transaction version number. | 
**version_hex** | **str** | Is the hexadecimal string representation of the block&#39;s version. | 
**weight** | **int** | Represents a measurement to compare the size of different transactions to each other in proportion to the block size limit. | 
**strippedsize** | **int** | Defines the numeric representation of the block size excluding the witness data. | 
**extra_data** | **str** | Represents any data that can be included by the miner in the block. | 
**gas_limit** | **str** | Represents the amount of gas used by this specific transaction alone. | 
**gas_used** | **str** | Represents the exact unit of gas that was used for the transaction. | 
**mined_in_seconds** | **int** | Specifies the amount of time required for the block to be mined in seconds. | 
**sha3_uncles** | **str** | Defines the combined hash of all uncles for a given parent. | 
**total_difficulty** | **str** | Defines the total difficulty of the chain until this block, i.e. how difficult it is for a specific miner to mine a new block. | 
**uncles** | **List[str]** |  | 
**total_coins** | [**GetLatestMinedXRPRippleBlockRITotalCoins**](GetLatestMinedXRPRippleBlockRITotalCoins.md) |  | 
**total_fees** | [**GetLatestMinedXRPRippleBlockRITotalFees**](GetLatestMinedXRPRippleBlockRITotalFees.md) |  | 
**bandwidth_used** | **str** | Represents the bandwidth used for the transaction. | 
**burned_trx** | **str** | Represents the block burned TRX. | 
**energy_used** | **str** | Representats the used energy for the transaction. | 

## Example

```python
from cryptoapis.models.get_block_details_by_block_height_from_callback_ribs import GetBlockDetailsByBlockHeightFromCallbackRIBS

# TODO update the JSON string below
json = "{}"
# create an instance of GetBlockDetailsByBlockHeightFromCallbackRIBS from a JSON string
get_block_details_by_block_height_from_callback_ribs_instance = GetBlockDetailsByBlockHeightFromCallbackRIBS.from_json(json)
# print the JSON string representation of the object
print GetBlockDetailsByBlockHeightFromCallbackRIBS.to_json()

# convert the object into a dict
get_block_details_by_block_height_from_callback_ribs_dict = get_block_details_by_block_height_from_callback_ribs_instance.to_dict()
# create an instance of GetBlockDetailsByBlockHeightFromCallbackRIBS from a dict
get_block_details_by_block_height_from_callback_ribs_form_dict = get_block_details_by_block_height_from_callback_ribs.from_dict(get_block_details_by_block_height_from_callback_ribs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


