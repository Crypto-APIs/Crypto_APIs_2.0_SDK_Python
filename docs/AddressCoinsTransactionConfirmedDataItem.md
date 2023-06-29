# AddressCoinsTransactionConfirmedDataItem

Defines an `item` as one result.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blockchain** | **str** | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. | 
**network** | **str** | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;goerli\&quot;, \&quot;nile\&quot; are test networks. | 
**address** | **str** | Defines the specific address to which the coin transaction has been sent and is confirmed. | 
**mined_in_block** | [**AddressCoinsTransactionConfirmedDataItemMinedInBlock**](AddressCoinsTransactionConfirmedDataItemMinedInBlock.md) |  | 
**transaction_id** | **str** | Defines the unique ID of the specific transaction, i.e. its identification number. | 
**amount** | **str** | Defines the amount of coins sent with the confirmed transaction. | 
**unit** | **str** | Defines the unit of the transaction, e.g. BTC. | 
**direction** | **str** | Defines whether the transaction is \&quot;incoming\&quot; or \&quot;outgoing\&quot;. | 

## Example

```python
from cryptoapis.models.address_coins_transaction_confirmed_data_item import AddressCoinsTransactionConfirmedDataItem

# TODO update the JSON string below
json = "{}"
# create an instance of AddressCoinsTransactionConfirmedDataItem from a JSON string
address_coins_transaction_confirmed_data_item_instance = AddressCoinsTransactionConfirmedDataItem.from_json(json)
# print the JSON string representation of the object
print AddressCoinsTransactionConfirmedDataItem.to_json()

# convert the object into a dict
address_coins_transaction_confirmed_data_item_dict = address_coins_transaction_confirmed_data_item_instance.to_dict()
# create an instance of AddressCoinsTransactionConfirmedDataItem from a dict
address_coins_transaction_confirmed_data_item_form_dict = address_coins_transaction_confirmed_data_item.from_dict(address_coins_transaction_confirmed_data_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


