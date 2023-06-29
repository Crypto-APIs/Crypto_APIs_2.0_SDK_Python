# AddressTokensTransactionConfirmedTrc20

TRC-20

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**symbol** | **str** |  | 
**decimals** | **str** |  | [optional] 
**amount** | **str** |  | 
**contract_address** | **str** |  | 

## Example

```python
from cryptoapis.models.address_tokens_transaction_confirmed_trc20 import AddressTokensTransactionConfirmedTrc20

# TODO update the JSON string below
json = "{}"
# create an instance of AddressTokensTransactionConfirmedTrc20 from a JSON string
address_tokens_transaction_confirmed_trc20_instance = AddressTokensTransactionConfirmedTrc20.from_json(json)
# print the JSON string representation of the object
print AddressTokensTransactionConfirmedTrc20.to_json()

# convert the object into a dict
address_tokens_transaction_confirmed_trc20_dict = address_tokens_transaction_confirmed_trc20_instance.to_dict()
# create an instance of AddressTokensTransactionConfirmedTrc20 from a dict
address_tokens_transaction_confirmed_trc20_form_dict = address_tokens_transaction_confirmed_trc20.from_dict(address_tokens_transaction_confirmed_trc20_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


