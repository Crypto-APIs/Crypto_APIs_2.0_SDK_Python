# EstimateTokenGasLimitRBDataItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | Represents transactions&#39; amount. | 
**contract** | **str** | Defines the specific token identifier.  For Ethereum-based transactions it is the contract. | 
**contract_type** | **str** | Represents the ERC contract type. It can be ERC20 or ERC721 | 
**recipient** | **str** | The address which receives this transaction. In UTXO-based protocols like Bitcoin there could be several senders while in account-based protocols like Ethereum there is always only one recipient. | 
**sender** | **str** | Represents the address which sends this transaction. In UTXO-based protocols like Bitcoin there could be several senders while in account-based protocols like Ethereum there is always only one sender. | 

## Example

```python
from cryptoapis.models.estimate_token_gas_limit_rb_data_item import EstimateTokenGasLimitRBDataItem

# TODO update the JSON string below
json = "{}"
# create an instance of EstimateTokenGasLimitRBDataItem from a JSON string
estimate_token_gas_limit_rb_data_item_instance = EstimateTokenGasLimitRBDataItem.from_json(json)
# print the JSON string representation of the object
print EstimateTokenGasLimitRBDataItem.to_json()

# convert the object into a dict
estimate_token_gas_limit_rb_data_item_dict = estimate_token_gas_limit_rb_data_item_instance.to_dict()
# create an instance of EstimateTokenGasLimitRBDataItem from a dict
estimate_token_gas_limit_rb_data_item_form_dict = estimate_token_gas_limit_rb_data_item.from_dict(estimate_token_gas_limit_rb_data_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


