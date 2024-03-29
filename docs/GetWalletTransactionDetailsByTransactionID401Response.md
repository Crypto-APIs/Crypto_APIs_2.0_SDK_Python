# GetWalletTransactionDetailsByTransactionID401Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | Specifies the version of the API that incorporates this endpoint. | 
**request_id** | **str** | Defines the ID of the request. The &#x60;requestId&#x60; is generated by Crypto APIs and it&#39;s unique for every request. | 
**context** | **str** | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional] 
**error** | [**GetWalletTransactionDetailsByTransactionIDE401**](GetWalletTransactionDetailsByTransactionIDE401.md) |  | 

## Example

```python
from cryptoapis.models.get_wallet_transaction_details_by_transaction_id401_response import GetWalletTransactionDetailsByTransactionID401Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetWalletTransactionDetailsByTransactionID401Response from a JSON string
get_wallet_transaction_details_by_transaction_id401_response_instance = GetWalletTransactionDetailsByTransactionID401Response.from_json(json)
# print the JSON string representation of the object
print GetWalletTransactionDetailsByTransactionID401Response.to_json()

# convert the object into a dict
get_wallet_transaction_details_by_transaction_id401_response_dict = get_wallet_transaction_details_by_transaction_id401_response_instance.to_dict()
# create an instance of GetWalletTransactionDetailsByTransactionID401Response from a dict
get_wallet_transaction_details_by_transaction_id401_response_form_dict = get_wallet_transaction_details_by_transaction_id401_response.from_dict(get_wallet_transaction_details_by_transaction_id401_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


