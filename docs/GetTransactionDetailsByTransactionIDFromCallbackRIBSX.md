# GetTransactionDetailsByTransactionIDFromCallbackRIBSX

XRP

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_data** | **str** | Represents additional data that may be needed. | 
**destination_tag** | **int** | Defines the destination tag value. | [optional] 
**offer** | [**GetXRPRippleTransactionDetailsByTransactionIDRIOffer**](GetXRPRippleTransactionDetailsByTransactionIDRIOffer.md) |  | 
**receive** | [**GetXRPRippleTransactionDetailsByTransactionIDRIReceive**](GetXRPRippleTransactionDetailsByTransactionIDRIReceive.md) |  | 
**sequence** | **int** | Defines the transaction input&#39;s sequence as an integer, which is is used when transactions are replaced with newer versions before LockTime. | 
**status** | **str** | Defines the status of the transaction. | 
**type** | **str** | Defines the type of the transaction. | 
**value** | [**GetTransactionDetailsByTransactionIDFromCallbackRIBSXValue**](GetTransactionDetailsByTransactionIDFromCallbackRIBSXValue.md) |  | 

## Example

```python
from cryptoapis.models.get_transaction_details_by_transaction_id_from_callback_ribsx import GetTransactionDetailsByTransactionIDFromCallbackRIBSX

# TODO update the JSON string below
json = "{}"
# create an instance of GetTransactionDetailsByTransactionIDFromCallbackRIBSX from a JSON string
get_transaction_details_by_transaction_id_from_callback_ribsx_instance = GetTransactionDetailsByTransactionIDFromCallbackRIBSX.from_json(json)
# print the JSON string representation of the object
print GetTransactionDetailsByTransactionIDFromCallbackRIBSX.to_json()

# convert the object into a dict
get_transaction_details_by_transaction_id_from_callback_ribsx_dict = get_transaction_details_by_transaction_id_from_callback_ribsx_instance.to_dict()
# create an instance of GetTransactionDetailsByTransactionIDFromCallbackRIBSX from a dict
get_transaction_details_by_transaction_id_from_callback_ribsx_form_dict = get_transaction_details_by_transaction_id_from_callback_ribsx.from_dict(get_transaction_details_by_transaction_id_from_callback_ribsx_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


