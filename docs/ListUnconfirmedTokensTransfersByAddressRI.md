# ListUnconfirmedTokensTransfersByAddressRI


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contract_address** | **str** | Represents the contract address of the token, which controls its logic. It is not the address that holds the tokens. | 
**recipient_address** | **str** | Defines the address to which the recipient receives the transferred tokens. | 
**sender_address** | **str** | Defines the address from which the sender transfers tokens. | 
**token_decimals** | **int** | Defines the decimals of the token, i.e. the number of digits that come after the decimal coma of the token. | [optional] 
**token_id** | **str** | Represents the unique token identifier. | [optional] 
**token_name** | **str** | Defines the token&#39;s name as a string. | [optional] 
**token_symbol** | **str** | Defines the token symbol by which the token contract is known. It is usually 3-4 characters in length. | [optional] 
**token_type** | **str** | Defines the specific token type. | 
**tokens_amount** | **str** | Defines the token amount of the transfer. | [optional] 
**transaction_hash** | **str** | Represents the hash of the transaction, which is its unique identifier. It represents a cryptographic digital fingerprint made by hashing the block header twice through the SHA256 algorithm. | 
**transaction_timestamp** | **int** | Defines the specific time/date when the transaction was created in Unix Timestamp. | 

## Example

```python
from cryptoapis.models.list_unconfirmed_tokens_transfers_by_address_ri import ListUnconfirmedTokensTransfersByAddressRI

# TODO update the JSON string below
json = "{}"
# create an instance of ListUnconfirmedTokensTransfersByAddressRI from a JSON string
list_unconfirmed_tokens_transfers_by_address_ri_instance = ListUnconfirmedTokensTransfersByAddressRI.from_json(json)
# print the JSON string representation of the object
print ListUnconfirmedTokensTransfersByAddressRI.to_json()

# convert the object into a dict
list_unconfirmed_tokens_transfers_by_address_ri_dict = list_unconfirmed_tokens_transfers_by_address_ri_instance.to_dict()
# create an instance of ListUnconfirmedTokensTransfersByAddressRI from a dict
list_unconfirmed_tokens_transfers_by_address_ri_form_dict = list_unconfirmed_tokens_transfers_by_address_ri.from_dict(list_unconfirmed_tokens_transfers_by_address_ri_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


