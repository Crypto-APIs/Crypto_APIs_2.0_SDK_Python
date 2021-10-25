# GetLastMinedBlockRIBSD2

Dash

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**difficulty** | **str** | Represents a mathematical value of how hard it is to find a valid hash for this block. | 
**nonce** | **str** | Represents a random value that can be adjusted to satisfy the proof of work | 
**size** | **int** | Represents the total size of the block in Bytes. | 
**bits** | **str** | Represents a specific sub-unit of Dash. Bits have two-decimal precision. | 
**chainwork** | **str** | Represents a hexadecimal number of all the hashes necessary to produce the current chain. E.g., when converting 0000000000000000000000000000000000000000000086859f7a841475b236fd to a decimal you get 635262017308958427068157 hashes, or 635262 exahashes. | 
**merkle_root** | **str** | Defines the single and final (root) node of a Merkle tree. It is the combined hash of all transactions&#39; hashes that are part of a blockchain block. | 
**version** | **int** | Represents the version of the specific block on the blockchain. | 
**version_hex** | **str** | Is the hexadecimal string representation of the block&#39;s version. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


