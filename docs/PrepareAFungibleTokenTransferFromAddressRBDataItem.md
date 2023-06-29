# PrepareAFungibleTokenTransferFromAddressRBDataItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | Representation of the amount to be transferred | 
**contract** | **str** | Represents the contract address of the token, which controls its logic. It is not the address that holds the tokens. | 
**nonce** | **str** | Represents the sequential running number for an address, starting from 0 for the first transaction. E.g., if the nonce of a transaction is 10, it would be the 11th transaction sent from the sender&#39;s address. | [optional] 
**recipient** | **str** | The address which receives this transaction. In UTXO-based protocols like Bitcoin there could be several senders while in account-based protocols like Ethereum there is always only one recipient. | 
**sender** | **str** | Represents the address which sends this transaction. In UTXO-based protocols like Bitcoin there could be several senders while in account-based protocols like Ethereum there is always only one sender. | 
**fee** | [**PrepareAFungibleTokenTransferFromAddressRBDataItemFee**](PrepareAFungibleTokenTransferFromAddressRBDataItemFee.md) |  | 
**transaction_type** | **str** | Representation of the transaction type. For Ethereum-Classic and Binance Smart Chain there is no need to provide \&quot;transactionType\&quot; in the request. | [optional] 

## Example

```python
from cryptoapis.models.prepare_a_fungible_token_transfer_from_address_rb_data_item import PrepareAFungibleTokenTransferFromAddressRBDataItem

# TODO update the JSON string below
json = "{}"
# create an instance of PrepareAFungibleTokenTransferFromAddressRBDataItem from a JSON string
prepare_a_fungible_token_transfer_from_address_rb_data_item_instance = PrepareAFungibleTokenTransferFromAddressRBDataItem.from_json(json)
# print the JSON string representation of the object
print PrepareAFungibleTokenTransferFromAddressRBDataItem.to_json()

# convert the object into a dict
prepare_a_fungible_token_transfer_from_address_rb_data_item_dict = prepare_a_fungible_token_transfer_from_address_rb_data_item_instance.to_dict()
# create an instance of PrepareAFungibleTokenTransferFromAddressRBDataItem from a dict
prepare_a_fungible_token_transfer_from_address_rb_data_item_form_dict = prepare_a_fungible_token_transfer_from_address_rb_data_item.from_dict(prepare_a_fungible_token_transfer_from_address_rb_data_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


