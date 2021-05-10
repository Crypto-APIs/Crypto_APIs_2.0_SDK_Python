# GetBlockDetailsByBlockHeightResponseItemBlockchainSpecificDogecoin

Dogecoin

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**difficulty** | **str** | Represents a mathematical value of how hard it is to find a valid hash for this block. | 
**nonce** | **str** | Represents a random value that can be adjusted to satisfy the Proof of Work | 
**size** | **int** | Represents the total size of the block in Bytes. | 
**bits** | **str** | Represents a specific sub-unit of Doge. Bits have two-decimal precision. | 
**chainwork** | **str** | Represents a hexadecimal number of all the hashes necessary to produce the current chain. E.g., when converting 0000000000000000000000000000000000000000000086859f7a841475b236fd to a decimal you get 635262017308958427068157 hashes, or 635262 exahashes. | 
**merkle_root** | **str** | Defines the single and final (root) node of a Merkle tree. It is the combined hash of all transactions&#39; hashes that are part of a blockchain block. | 
**stripped_size** | **int** | Defines the numeric representation of the block size excluding the witness data. | 
**version** | **int** | Represents the version of the specific block on the blockchain. | 
**weight** | **int** | Represents a measurement to compare the size of different transactions to each other in proportion to the block size limit. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


