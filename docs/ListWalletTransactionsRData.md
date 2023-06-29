# ListWalletTransactionsRData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | Defines how many items should be returned in the response per page basis. | 
**offset** | **int** | The starting index of the response items, i.e. where the response should start listing the returned items. | 
**total** | **int** | Defines the total number of items returned in the response. | 
**items** | [**List[ListWalletTransactionsRI]**](ListWalletTransactionsRI.md) |  | 

## Example

```python
from cryptoapis.models.list_wallet_transactions_r_data import ListWalletTransactionsRData

# TODO update the JSON string below
json = "{}"
# create an instance of ListWalletTransactionsRData from a JSON string
list_wallet_transactions_r_data_instance = ListWalletTransactionsRData.from_json(json)
# print the JSON string representation of the object
print ListWalletTransactionsRData.to_json()

# convert the object into a dict
list_wallet_transactions_r_data_dict = list_wallet_transactions_r_data_instance.to_dict()
# create an instance of ListWalletTransactionsRData from a dict
list_wallet_transactions_r_data_form_dict = list_wallet_transactions_r_data.from_dict(list_wallet_transactions_r_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


