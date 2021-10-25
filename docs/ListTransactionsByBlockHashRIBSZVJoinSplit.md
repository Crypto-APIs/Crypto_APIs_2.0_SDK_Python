# ListTransactionsByBlockHashRIBSZVJoinSplit


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anchor** | **str** | Defines a Merkle tree root of a note commitment tree which uniquely identifies a note commitment tree state given the assumed security properties of the Merkle tree’s  hash function. | 
**cipher_texts** | **[str]** |  | 
**commitments** | **[str]** |  | 
**macs** | **[str]** |  | 
**nullifiers** | **[str]** |  | 
**one_time_pub_key** | **str** | Defines the one time public key. | 
**proof** | **str** | Defines the proof. | 
**random_seed** | **str** | Represents a 256-bit seed that must be chosen independently at random for each JoinSplit description. | 
**v_pub_new** | **str** | Defines the value that the joinSplit transfer will insert into the transparent transaction value pool. | 
**v_pub_old** | **str** | Defines the value that the joinSplit transfer will remove from the transparent transaction value pool. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


