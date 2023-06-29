# AddressTokensTransactionConfirmedEachConfirmationDataItem

Defines an `item` as one result.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blockchain** | **str** | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. | 
**network** | **str** | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;goerli\&quot;,  are test networks. | 
**address** | **str** | Defines the specific address to which the transaction has been sent. | 
**mined_in_block** | [**AddressTokensTransactionConfirmedDataItemMinedInBlock**](AddressTokensTransactionConfirmedDataItemMinedInBlock.md) |  | 
**transaction_id** | **str** | Defines the unique ID of the specific transaction, i.e. its identification number. | 
**current_confirmations** | **int** | Defines the number of currently received confirmations for the transaction. | 
**target_confirmations** | **int** | Defines the number of confirmation transactions requested as callbacks, i.e. the system can notify till the n-th confirmation. | 
**token_type** | **str** | Defines the type of token sent with the transaction, e.g. ERC 20. | 
**token** | [**AddressTokensTransactionConfirmedEachConfirmationToken**](AddressTokensTransactionConfirmedEachConfirmationToken.md) |  | 
**direction** | **str** | Defines whether the transaction is \&quot;incoming\&quot; or \&quot;outgoing\&quot;. | 

## Example

```python
from cryptoapis.models.address_tokens_transaction_confirmed_each_confirmation_data_item import AddressTokensTransactionConfirmedEachConfirmationDataItem

# TODO update the JSON string below
json = "{}"
# create an instance of AddressTokensTransactionConfirmedEachConfirmationDataItem from a JSON string
address_tokens_transaction_confirmed_each_confirmation_data_item_instance = AddressTokensTransactionConfirmedEachConfirmationDataItem.from_json(json)
# print the JSON string representation of the object
print AddressTokensTransactionConfirmedEachConfirmationDataItem.to_json()

# convert the object into a dict
address_tokens_transaction_confirmed_each_confirmation_data_item_dict = address_tokens_transaction_confirmed_each_confirmation_data_item_instance.to_dict()
# create an instance of AddressTokensTransactionConfirmedEachConfirmationDataItem from a dict
address_tokens_transaction_confirmed_each_confirmation_data_item_form_dict = address_tokens_transaction_confirmed_each_confirmation_data_item.from_dict(address_tokens_transaction_confirmed_each_confirmation_data_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


