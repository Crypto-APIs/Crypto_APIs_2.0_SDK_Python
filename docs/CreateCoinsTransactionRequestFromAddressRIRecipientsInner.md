# CreateCoinsTransactionRequestFromAddressRIRecipientsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Defines the destination address. | 
**address_tag** | **int** | Defines a specific Tag that is an additional XRP address feature. It helps identify a transaction recipient beyond a wallet address. The tag that was encoded into the x-Address along with the Source Classic Address. | [optional] 
**amount** | **str** | Defines the amount sent to the destination address. | 
**classic_address** | **str** | Represents the public address, which is a compressed and shortened form of a public key. The classic address is shown when the source address is an x-Address. | [optional] 

## Example

```python
from cryptoapis.models.create_coins_transaction_request_from_address_ri_recipients_inner import CreateCoinsTransactionRequestFromAddressRIRecipientsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCoinsTransactionRequestFromAddressRIRecipientsInner from a JSON string
create_coins_transaction_request_from_address_ri_recipients_inner_instance = CreateCoinsTransactionRequestFromAddressRIRecipientsInner.from_json(json)
# print the JSON string representation of the object
print CreateCoinsTransactionRequestFromAddressRIRecipientsInner.to_json()

# convert the object into a dict
create_coins_transaction_request_from_address_ri_recipients_inner_dict = create_coins_transaction_request_from_address_ri_recipients_inner_instance.to_dict()
# create an instance of CreateCoinsTransactionRequestFromAddressRIRecipientsInner from a dict
create_coins_transaction_request_from_address_ri_recipients_inner_form_dict = create_coins_transaction_request_from_address_ri_recipients_inner.from_dict(create_coins_transaction_request_from_address_ri_recipients_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


