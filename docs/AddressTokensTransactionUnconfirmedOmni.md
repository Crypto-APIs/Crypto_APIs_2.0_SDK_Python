# AddressTokensTransactionUnconfirmedOmni

OMNI

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Specifies the name of the token. | 
**property_id** | **str** | Defines the ID of the property for Omni Layer. | 
**transaction_type** | **str** | Defines the type of the transaction made. | 
**created_by_transaction_id** | **str** | The transaction ID used to create the token. | 
**amount** | **str** | Defines the amount of tokens sent with the transaction that is pending confirmation. | 

## Example

```python
from cryptoapis.models.address_tokens_transaction_unconfirmed_omni import AddressTokensTransactionUnconfirmedOmni

# TODO update the JSON string below
json = "{}"
# create an instance of AddressTokensTransactionUnconfirmedOmni from a JSON string
address_tokens_transaction_unconfirmed_omni_instance = AddressTokensTransactionUnconfirmedOmni.from_json(json)
# print the JSON string representation of the object
print AddressTokensTransactionUnconfirmedOmni.to_json()

# convert the object into a dict
address_tokens_transaction_unconfirmed_omni_dict = address_tokens_transaction_unconfirmed_omni_instance.to_dict()
# create an instance of AddressTokensTransactionUnconfirmedOmni from a dict
address_tokens_transaction_unconfirmed_omni_form_dict = address_tokens_transaction_unconfirmed_omni.from_dict(address_tokens_transaction_unconfirmed_omni_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


