# ListLatestMinedBlocksRI


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hash** | **str** | Represents the same as transactionId for account-based protocols like Ethereum, while it could be different in UTXO-based protocols like Bitcoin. E.g., in UTXO-based protocols hash is different from transactionId for SegWit transactions. | 
**height** | **int** | Represents the hight of the block where this transaction was mined/confirmed for first time. The height is defined as the number of blocks in the blockchain preceding this specific block. | 
**previous_block_hash** | **str** | Represents the hash of the previous block, also known as the parent block. | 
**timestamp** | **int** | Defines the exact date/time when this block was mined in Unix Timestamp. | 
**transactions_count** | **int** | Represents the total number of all transactions as part of this block. | 
**blockchain_specific** | [**ListLatestMinedBlocksRIBS**](ListLatestMinedBlocksRIBS.md) |  | 

## Example

```python
from cryptoapis.models.list_latest_mined_blocks_ri import ListLatestMinedBlocksRI

# TODO update the JSON string below
json = "{}"
# create an instance of ListLatestMinedBlocksRI from a JSON string
list_latest_mined_blocks_ri_instance = ListLatestMinedBlocksRI.from_json(json)
# print the JSON string representation of the object
print ListLatestMinedBlocksRI.to_json()

# convert the object into a dict
list_latest_mined_blocks_ri_dict = list_latest_mined_blocks_ri_instance.to_dict()
# create an instance of ListLatestMinedBlocksRI from a dict
list_latest_mined_blocks_ri_form_dict = list_latest_mined_blocks_ri.from_dict(list_latest_mined_blocks_ri_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


