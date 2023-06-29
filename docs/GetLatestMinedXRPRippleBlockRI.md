# GetLatestMinedXRPRippleBlockRI


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block_hash** | **str** | Represents the hash of the block, which is its unique identifier. It represents a cryptographic digital fingerprint made by hashing the block header twice through the SHA256 algorithm. | 
**block_height** | **int** | Represents the number of blocks in the blockchain preceding this specific block. Block numbers have no gaps. A blockchain usually starts with block 0 called the \&quot;Genesis block\&quot;. | 
**previous_block_hash** | **str** | Represents the hash of the previous block, also known as the parent block. | 
**timestamp** | **int** | Defines the exact date/time when this block was mined in Unix Timestamp. | 
**transactions_count** | **int** | Represents the total number of all transactions as part of this block. | 
**total_coins** | [**GetLatestMinedXRPRippleBlockRITotalCoins**](GetLatestMinedXRPRippleBlockRITotalCoins.md) |  | 
**total_fees** | [**GetLatestMinedXRPRippleBlockRITotalFees**](GetLatestMinedXRPRippleBlockRITotalFees.md) |  | 

## Example

```python
from cryptoapis.models.get_latest_mined_xrp_ripple_block_ri import GetLatestMinedXRPRippleBlockRI

# TODO update the JSON string below
json = "{}"
# create an instance of GetLatestMinedXRPRippleBlockRI from a JSON string
get_latest_mined_xrp_ripple_block_ri_instance = GetLatestMinedXRPRippleBlockRI.from_json(json)
# print the JSON string representation of the object
print GetLatestMinedXRPRippleBlockRI.to_json()

# convert the object into a dict
get_latest_mined_xrp_ripple_block_ri_dict = get_latest_mined_xrp_ripple_block_ri_instance.to_dict()
# create an instance of GetLatestMinedXRPRippleBlockRI from a dict
get_latest_mined_xrp_ripple_block_ri_form_dict = get_latest_mined_xrp_ripple_block_ri.from_dict(get_latest_mined_xrp_ripple_block_ri_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


