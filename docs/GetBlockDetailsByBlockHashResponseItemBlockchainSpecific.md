# GetBlockDetailsByBlockHashResponseItemBlockchainSpecific


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**difficulty** | **str** | Represents a mathematical value of how hard it is to find a valid hash for this block. | [optional] 
**nonce** | **str** | Represents a random value that can be adjusted to satisfy the Proof of Work. | [optional] 
**size** | **int** | Represents the total size of the block in Bytes. | [optional] 
**bits** | **str** | Represents a specific sub-unit of Dash. Bits have two-decimal precision. | [optional] 
**chainwork** | **str** | Represents a hexadecimal number of all the hashes necessary to produce the current chain. E.g., when converting 0000000000000000000000000000000000000000000086859f7a841475b236fd to a decimal you get 635262017308958427068157 hashes, or 635262 exahashes. | [optional] 
**merkle_root** | **str** | Defines the single and final (root) node of a Merkle tree. It is the combined hash of all transactions&#39; hashes that are part of a blockchain block. | [optional] 
**stripped_size** | **int** | Defines the numeric representation of the block size excluding the witness data. | [optional] 
**version** | **int** | Represents the version of the specific block on the blockchain. | [optional] 
**version_hex** | **str** | Is the hexadecimal string representation of the block&#39;s version. | [optional] 
**weight** | **int** | Represents a measurement to compare the size of different transactions to each other in proportion to the block size limit. | [optional] 
**extra_data** | **str** | Represents any data that can be included by the miner in the block. | [optional] 
**gas_limit** | **str** | Defines the total gas limit of all transactions in the block. | [optional] 
**gas_used** | **str** | Represents the total amount of gas used by all transactions in this block. | [optional] 
**mined_in_seconds** | **int** | Specifies the amount of time required for the block to be mined in seconds. | [optional] 
**sha3_uncles** | **str** | Defines the combined hash of all uncles for a given parent. | [optional] 
**total_difficulty** | **str** | Defines the total difficulty of the chain until this block, i.e. how difficult it is for a specific miner to mine a new block. | [optional] 
**uncles** | **[str]** |  | [optional] 
**merkleroot** | **str** | Defines the single and final (root) node of a Merkle tree. It is the combined hash of all transactions&#39; hashes that are part of a blockchain block. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


