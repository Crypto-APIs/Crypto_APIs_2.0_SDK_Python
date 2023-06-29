# TokensForwardingFailDataItem

Defines an `item` as one result.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blockchain** | **str** | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. | 
**network** | **str** | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot;, \&quot;rinkeby\&quot; are test networks. | 
**from_address** | **str** | Represents the hash of the address that provides the tokens. | 
**to_address** | **str** | Represents the hash of the address to forward the tokens to. | 
**trigger_transaction_id** | **str** | Defines the unique Transaction ID that triggered the token forwarding. | 
**error_code** | **str** | Represents the error code received for the failed token forwarding. | 
**error_message** | **str** | Represents the error message received for the failed token forwarding. | 

## Example

```python
from cryptoapis.models.tokens_forwarding_fail_data_item import TokensForwardingFailDataItem

# TODO update the JSON string below
json = "{}"
# create an instance of TokensForwardingFailDataItem from a JSON string
tokens_forwarding_fail_data_item_instance = TokensForwardingFailDataItem.from_json(json)
# print the JSON string representation of the object
print TokensForwardingFailDataItem.to_json()

# convert the object into a dict
tokens_forwarding_fail_data_item_dict = tokens_forwarding_fail_data_item_instance.to_dict()
# create an instance of TokensForwardingFailDataItem from a dict
tokens_forwarding_fail_data_item_form_dict = tokens_forwarding_fail_data_item.from_dict(tokens_forwarding_fail_data_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


