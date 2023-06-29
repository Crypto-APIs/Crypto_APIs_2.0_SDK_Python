# GetZilliqaTransactionDetailsByTransactionIDRIFee

Represents the transaction fee.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | Represents the amount of the transaction fee. | 
**unit** | **str** | Represents the unit of the transaction fee. | 

## Example

```python
from cryptoapis.models.get_zilliqa_transaction_details_by_transaction_idri_fee import GetZilliqaTransactionDetailsByTransactionIDRIFee

# TODO update the JSON string below
json = "{}"
# create an instance of GetZilliqaTransactionDetailsByTransactionIDRIFee from a JSON string
get_zilliqa_transaction_details_by_transaction_idri_fee_instance = GetZilliqaTransactionDetailsByTransactionIDRIFee.from_json(json)
# print the JSON string representation of the object
print GetZilliqaTransactionDetailsByTransactionIDRIFee.to_json()

# convert the object into a dict
get_zilliqa_transaction_details_by_transaction_idri_fee_dict = get_zilliqa_transaction_details_by_transaction_idri_fee_instance.to_dict()
# create an instance of GetZilliqaTransactionDetailsByTransactionIDRIFee from a dict
get_zilliqa_transaction_details_by_transaction_idri_fee_form_dict = get_zilliqa_transaction_details_by_transaction_idri_fee.from_dict(get_zilliqa_transaction_details_by_transaction_idri_fee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


