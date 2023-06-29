# GetTransactionDetailsByTransactionIDFromCallbackRIFee


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | When isConfirmed is True - Defines the amount of the transaction fee  When isConfirmed is False - For ETH-based blockchains this attribute represents the max fee value. | 
**unit** | **str** | Defines the unit of the fee. | 

## Example

```python
from cryptoapis.models.get_transaction_details_by_transaction_id_from_callback_ri_fee import GetTransactionDetailsByTransactionIDFromCallbackRIFee

# TODO update the JSON string below
json = "{}"
# create an instance of GetTransactionDetailsByTransactionIDFromCallbackRIFee from a JSON string
get_transaction_details_by_transaction_id_from_callback_ri_fee_instance = GetTransactionDetailsByTransactionIDFromCallbackRIFee.from_json(json)
# print the JSON string representation of the object
print GetTransactionDetailsByTransactionIDFromCallbackRIFee.to_json()

# convert the object into a dict
get_transaction_details_by_transaction_id_from_callback_ri_fee_dict = get_transaction_details_by_transaction_id_from_callback_ri_fee_instance.to_dict()
# create an instance of GetTransactionDetailsByTransactionIDFromCallbackRIFee from a dict
get_transaction_details_by_transaction_id_from_callback_ri_fee_form_dict = get_transaction_details_by_transaction_id_from_callback_ri_fee.from_dict(get_transaction_details_by_transaction_id_from_callback_ri_fee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


