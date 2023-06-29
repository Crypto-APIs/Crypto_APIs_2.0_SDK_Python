# ListUnconfirmedTransactionsByAddressRIBSECFee

Object representation of the transaction fee

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | String representation of the fee value | 
**unit** | **str** |  | 

## Example

```python
from cryptoapis.models.list_unconfirmed_transactions_by_address_ribsec_fee import ListUnconfirmedTransactionsByAddressRIBSECFee

# TODO update the JSON string below
json = "{}"
# create an instance of ListUnconfirmedTransactionsByAddressRIBSECFee from a JSON string
list_unconfirmed_transactions_by_address_ribsec_fee_instance = ListUnconfirmedTransactionsByAddressRIBSECFee.from_json(json)
# print the JSON string representation of the object
print ListUnconfirmedTransactionsByAddressRIBSECFee.to_json()

# convert the object into a dict
list_unconfirmed_transactions_by_address_ribsec_fee_dict = list_unconfirmed_transactions_by_address_ribsec_fee_instance.to_dict()
# create an instance of ListUnconfirmedTransactionsByAddressRIBSECFee from a dict
list_unconfirmed_transactions_by_address_ribsec_fee_form_dict = list_unconfirmed_transactions_by_address_ribsec_fee.from_dict(list_unconfirmed_transactions_by_address_ribsec_fee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


