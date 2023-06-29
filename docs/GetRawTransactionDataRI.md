# GetRawTransactionDataRI


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_hex** | **str** | Represents the raw transaction data in hexadecimal format. | 

## Example

```python
from cryptoapis.models.get_raw_transaction_data_ri import GetRawTransactionDataRI

# TODO update the JSON string below
json = "{}"
# create an instance of GetRawTransactionDataRI from a JSON string
get_raw_transaction_data_ri_instance = GetRawTransactionDataRI.from_json(json)
# print the JSON string representation of the object
print GetRawTransactionDataRI.to_json()

# convert the object into a dict
get_raw_transaction_data_ri_dict = get_raw_transaction_data_ri_instance.to_dict()
# create an instance of GetRawTransactionDataRI from a dict
get_raw_transaction_data_ri_form_dict = get_raw_transaction_data_ri.from_dict(get_raw_transaction_data_ri_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


