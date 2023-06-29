# CreateCoinsTransactionRequestFromAddressRISenders

Defines details about the source, i.e. the sender.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Defines the sender&#39;s public address. | 

## Example

```python
from cryptoapis.models.create_coins_transaction_request_from_address_ri_senders import CreateCoinsTransactionRequestFromAddressRISenders

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCoinsTransactionRequestFromAddressRISenders from a JSON string
create_coins_transaction_request_from_address_ri_senders_instance = CreateCoinsTransactionRequestFromAddressRISenders.from_json(json)
# print the JSON string representation of the object
print CreateCoinsTransactionRequestFromAddressRISenders.to_json()

# convert the object into a dict
create_coins_transaction_request_from_address_ri_senders_dict = create_coins_transaction_request_from_address_ri_senders_instance.to_dict()
# create an instance of CreateCoinsTransactionRequestFromAddressRISenders from a dict
create_coins_transaction_request_from_address_ri_senders_form_dict = create_coins_transaction_request_from_address_ri_senders.from_dict(create_coins_transaction_request_from_address_ri_senders_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


