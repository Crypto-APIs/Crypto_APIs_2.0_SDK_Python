# GetTransactionDetailsByTransactionIDRIBSECGasPrice


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | Represents the price offered to the miner to purchase this amount of gas. | 
**unit** | **str** | Defines the unit of the gas price amount, e.g. BTC, ETH, XRP. | 

## Example

```python
from cryptoapis.models.get_transaction_details_by_transaction_idribsec_gas_price import GetTransactionDetailsByTransactionIDRIBSECGasPrice

# TODO update the JSON string below
json = "{}"
# create an instance of GetTransactionDetailsByTransactionIDRIBSECGasPrice from a JSON string
get_transaction_details_by_transaction_idribsec_gas_price_instance = GetTransactionDetailsByTransactionIDRIBSECGasPrice.from_json(json)
# print the JSON string representation of the object
print GetTransactionDetailsByTransactionIDRIBSECGasPrice.to_json()

# convert the object into a dict
get_transaction_details_by_transaction_idribsec_gas_price_dict = get_transaction_details_by_transaction_idribsec_gas_price_instance.to_dict()
# create an instance of GetTransactionDetailsByTransactionIDRIBSECGasPrice from a dict
get_transaction_details_by_transaction_idribsec_gas_price_form_dict = get_transaction_details_by_transaction_idribsec_gas_price.from_dict(get_transaction_details_by_transaction_idribsec_gas_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


