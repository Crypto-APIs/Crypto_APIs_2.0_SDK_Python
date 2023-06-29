# BlockRevertedDataItem

Defines an item as one result.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blockchain** | **str** | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. | 
**network** | **str** | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot;, \&quot;rinkeby\&quot; are test networks. | 
**height** | **int** | Defines the number of blocks in the blockchain preceding this specific block. | 
**hash** | **str** | Represents the hash of the block&#39;s header, i.e. an output that has a fixed length. | 
**timestamp** | **int** | Defines the exact date/time when this block was mined in seconds since Unix Epoch time. | 

## Example

```python
from cryptoapis.models.block_reverted_data_item import BlockRevertedDataItem

# TODO update the JSON string below
json = "{}"
# create an instance of BlockRevertedDataItem from a JSON string
block_reverted_data_item_instance = BlockRevertedDataItem.from_json(json)
# print the JSON string representation of the object
print BlockRevertedDataItem.to_json()

# convert the object into a dict
block_reverted_data_item_dict = block_reverted_data_item_instance.to_dict()
# create an instance of BlockRevertedDataItem from a dict
block_reverted_data_item_form_dict = block_reverted_data_item.from_dict(block_reverted_data_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


