# GetXRPRippleTransactionDetailsByTransactionIDRIReceive

Defines on object array of the funds for which an offer is made.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | Defines the amount of the funds for which an offer is made. | 
**unit** | **str** | Defines the unit of the funds for which an offer is made. | 

## Example

```python
from cryptoapis.models.get_xrp_ripple_transaction_details_by_transaction_idri_receive import GetXRPRippleTransactionDetailsByTransactionIDRIReceive

# TODO update the JSON string below
json = "{}"
# create an instance of GetXRPRippleTransactionDetailsByTransactionIDRIReceive from a JSON string
get_xrp_ripple_transaction_details_by_transaction_idri_receive_instance = GetXRPRippleTransactionDetailsByTransactionIDRIReceive.from_json(json)
# print the JSON string representation of the object
print GetXRPRippleTransactionDetailsByTransactionIDRIReceive.to_json()

# convert the object into a dict
get_xrp_ripple_transaction_details_by_transaction_idri_receive_dict = get_xrp_ripple_transaction_details_by_transaction_idri_receive_instance.to_dict()
# create an instance of GetXRPRippleTransactionDetailsByTransactionIDRIReceive from a dict
get_xrp_ripple_transaction_details_by_transaction_idri_receive_form_dict = get_xrp_ripple_transaction_details_by_transaction_idri_receive.from_dict(get_xrp_ripple_transaction_details_by_transaction_idri_receive_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


