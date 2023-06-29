# GetXRPRippleAddressDetailsRI


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balance** | [**GetXRPRippleAddressDetailsRIBalance**](GetXRPRippleAddressDetailsRIBalance.md) |  | 
**incoming_transactions_count** | **int** | Defines the count of all confirmed incoming transactions from the address for coins. This applies to coins only, not to tokens transfers | 
**outgoing_transactions_count** | **int** | Defines the count of all confirmed outgoing transactions for coins. This applies to coins only, not to tokens transfers | 
**sequence** | **int** | Defines the transaction input&#39;s sequence as an integer, which is is used when transactions are replaced with newer versions before LockTime. | 
**transactions_count** | **int** | Represents the total number of all transactions as part of this block. | 

## Example

```python
from cryptoapis.models.get_xrp_ripple_address_details_ri import GetXRPRippleAddressDetailsRI

# TODO update the JSON string below
json = "{}"
# create an instance of GetXRPRippleAddressDetailsRI from a JSON string
get_xrp_ripple_address_details_ri_instance = GetXRPRippleAddressDetailsRI.from_json(json)
# print the JSON string representation of the object
print GetXRPRippleAddressDetailsRI.to_json()

# convert the object into a dict
get_xrp_ripple_address_details_ri_dict = get_xrp_ripple_address_details_ri_instance.to_dict()
# create an instance of GetXRPRippleAddressDetailsRI from a dict
get_xrp_ripple_address_details_ri_form_dict = get_xrp_ripple_address_details_ri.from_dict(get_xrp_ripple_address_details_ri_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


