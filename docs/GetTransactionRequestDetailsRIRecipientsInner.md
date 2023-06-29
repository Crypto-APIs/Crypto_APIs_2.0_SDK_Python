# GetTransactionRequestDetailsRIRecipientsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The address which receives this transaction. In UTXO-based protocols like Bitcoin there could be several senders while in account-based protocols like Ethereum there is always only one recipient. | 
**address_tag** | **int** | Defines a specific Tag that is an additional XRP address feature. It helps identify a transaction recipient beyond a wallet address. The tag that was encoded into the x-Address along with the Classic Address. | [optional] 
**amount** | **str** | Represents the amount received to this address. | 
**classic_address** | **str** | Represents the public address, which is a compressed and shortened form of a public key. A classic address is shown when the destination address is an x-Address. | [optional] 
**unit** | **str** | Defines the unit of the amount. | 

## Example

```python
from cryptoapis.models.get_transaction_request_details_ri_recipients_inner import GetTransactionRequestDetailsRIRecipientsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetTransactionRequestDetailsRIRecipientsInner from a JSON string
get_transaction_request_details_ri_recipients_inner_instance = GetTransactionRequestDetailsRIRecipientsInner.from_json(json)
# print the JSON string representation of the object
print GetTransactionRequestDetailsRIRecipientsInner.to_json()

# convert the object into a dict
get_transaction_request_details_ri_recipients_inner_dict = get_transaction_request_details_ri_recipients_inner_instance.to_dict()
# create an instance of GetTransactionRequestDetailsRIRecipientsInner from a dict
get_transaction_request_details_ri_recipients_inner_form_dict = get_transaction_request_details_ri_recipients_inner.from_dict(get_transaction_request_details_ri_recipients_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


