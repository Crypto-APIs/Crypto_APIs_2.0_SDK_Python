# GetZilliqaBlockDetailsByBlockHashRI


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block_height** | **int** | Represents the number of blocks in the blockchain preceding this specific block. Block numbers have no gaps. A blockchain usually starts with block 0 called the \&quot;Genesis block\&quot;. | 
**difficulty** | **str** | Defines how difficult it is for a specific miner to mine the block. | 
**ds_block** | **int** | Represents the Directory Service block which contains metadata about the miners who participate in the consensus protocol. | 
**ds_difficulty** | **str** | Defines how difficult it is to mine the dsBlocks. | 
**ds_leader** | **str** | Represents a part of the DS Committee which leads the consensus protocol for the epoch. | 
**gas_limit** | **int** | Represents the maximum amount of gas allowed in the block in order to determine how many transactions it can fit. | 
**gas_used** | **int** | Defines how much of the gas for the block has been used. | 
**micro_blocks** | **[str]** |  | 
**next_block_hash** | **str** | Defines the hash of the next block from the specific blockchain. | 
**previous_block_hash** | **str** | Represents the hash of the previous block, also known as the parent block. | 
**timestamp** | **int** | Defines the exact date/time when this block was mined in Unix Timestamp. | 
**transactions_count** | **int** | Represents the total number of all transactions as part of this block. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


