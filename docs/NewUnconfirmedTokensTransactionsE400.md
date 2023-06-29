# NewUnconfirmedTokensTransactionsE400


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Specifies an error code, e.g. error 404. | 
**message** | **str** | Specifies the message of the error, i.e. why the error was returned, e.g. error 404 stands for “not found”. | 
**details** | [**List[BannedIpAddressDetailsInner]**](BannedIpAddressDetailsInner.md) |  | [optional] 

## Example

```python
from cryptoapis.models.new_unconfirmed_tokens_transactions_e400 import NewUnconfirmedTokensTransactionsE400

# TODO update the JSON string below
json = "{}"
# create an instance of NewUnconfirmedTokensTransactionsE400 from a JSON string
new_unconfirmed_tokens_transactions_e400_instance = NewUnconfirmedTokensTransactionsE400.from_json(json)
# print the JSON string representation of the object
print NewUnconfirmedTokensTransactionsE400.to_json()

# convert the object into a dict
new_unconfirmed_tokens_transactions_e400_dict = new_unconfirmed_tokens_transactions_e400_instance.to_dict()
# create an instance of NewUnconfirmedTokensTransactionsE400 from a dict
new_unconfirmed_tokens_transactions_e400_form_dict = new_unconfirmed_tokens_transactions_e400.from_dict(new_unconfirmed_tokens_transactions_e400_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


