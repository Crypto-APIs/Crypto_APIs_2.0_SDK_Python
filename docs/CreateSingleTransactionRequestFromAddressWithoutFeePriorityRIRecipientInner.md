# CreateSingleTransactionRequestFromAddressWithoutFeePriorityRIRecipientInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Defines the destination address. | 
**amount** | **str** | Defines the amount sent to the destination address. | 
**classic_address** | **str** | Represents the public address, which is a compressed and shortened form of a public key. The classic address is shown when the source address is an x-Address. | [optional] 
**unit** | **str** | Defines the unit of the recieved amount for the address. | 

## Example

```python
from cryptoapis.models.create_single_transaction_request_from_address_without_fee_priority_ri_recipient_inner import CreateSingleTransactionRequestFromAddressWithoutFeePriorityRIRecipientInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSingleTransactionRequestFromAddressWithoutFeePriorityRIRecipientInner from a JSON string
create_single_transaction_request_from_address_without_fee_priority_ri_recipient_inner_instance = CreateSingleTransactionRequestFromAddressWithoutFeePriorityRIRecipientInner.from_json(json)
# print the JSON string representation of the object
print CreateSingleTransactionRequestFromAddressWithoutFeePriorityRIRecipientInner.to_json()

# convert the object into a dict
create_single_transaction_request_from_address_without_fee_priority_ri_recipient_inner_dict = create_single_transaction_request_from_address_without_fee_priority_ri_recipient_inner_instance.to_dict()
# create an instance of CreateSingleTransactionRequestFromAddressWithoutFeePriorityRIRecipientInner from a dict
create_single_transaction_request_from_address_without_fee_priority_ri_recipient_inner_form_dict = create_single_transaction_request_from_address_without_fee_priority_ri_recipient_inner.from_dict(create_single_transaction_request_from_address_without_fee_priority_ri_recipient_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


