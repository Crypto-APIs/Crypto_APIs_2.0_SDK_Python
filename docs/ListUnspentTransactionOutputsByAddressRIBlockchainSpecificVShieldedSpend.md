# ListUnspentTransactionOutputsByAddressRIBlockchainSpecificVShieldedSpend


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anchor** | **str** | Defines a Merkle tree root of a note commitment tree which uniquely identifies a note commitment tree state given the assumed security properties of the Merkle tree’s hash function. | 
**cv** | **str** | Defines a value commitment to the value of the input note. | 
**nullifier** | **str** | Represents a sequence of nullifiers of the input notes. | 
**proof** | **str** | Represents the proof. | 
**rk** | **str** | Represents the randomized validating key for spendAuthSig. | 
**spend_auth_sig** | **str** | Used to prove knowledge of the spending key authorizing spending of an input note. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


