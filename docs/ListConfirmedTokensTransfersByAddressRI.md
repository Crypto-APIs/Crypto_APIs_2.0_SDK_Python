# ListConfirmedTokensTransfersByAddressRI


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contract_address** | **str** | Represents the contract address of the token, which controls its logic. It is not the address that holds the tokens. | 
**mined_in_block_height** | **int** | Defines the block height in which this transaction was confirmed/mined. | 
**recipient_address** | **str** | Defines the address to which the recipient receives the transferred tokens. | 
**sender_address** | **str** | Defines the address from which the sender transfers tokens. | 
**token_decimals** | **int** | Defines the decimals of the token, i.e. the number of digits that come after the decimal coma of the token. | 
**token_id** | **str** | Represents the unique token identifier. | [optional] 
**token_name** | **str** | Defines the token&#39;s name as a string. | 
**token_symbol** | **str** | Defines the token symbol by which the token contract is known. It is usually 3-4 characters in length. | 
**token_type** | **str** | Defines the specific token type. | 
**tokens_amount** | **str** | Defines the token amount of the transfer. | [optional] 
**transaction_hash** | **str** | Represents the hash of the transaction, which is its unique identifier. It represents a cryptographic digital fingerprint made by hashing the block header twice through the SHA256 algorithm. | 
**transaction_timestamp** | **int** | Defines the specific time/date when the transaction was created in Unix Timestamp. | 
**transaction_fee** | [**ListTokensTransfersByTransactionHashRITransactionFee**](ListTokensTransfersByTransactionHashRITransactionFee.md) |  | 

## Example

```python
from cryptoapis.models.list_confirmed_tokens_transfers_by_address_ri import ListConfirmedTokensTransfersByAddressRI

# TODO update the JSON string below
json = "{}"
# create an instance of ListConfirmedTokensTransfersByAddressRI from a JSON string
list_confirmed_tokens_transfers_by_address_ri_instance = ListConfirmedTokensTransfersByAddressRI.from_json(json)
# print the JSON string representation of the object
print ListConfirmedTokensTransfersByAddressRI.to_json()

# convert the object into a dict
list_confirmed_tokens_transfers_by_address_ri_dict = list_confirmed_tokens_transfers_by_address_ri_instance.to_dict()
# create an instance of ListConfirmedTokensTransfersByAddressRI from a dict
list_confirmed_tokens_transfers_by_address_ri_form_dict = list_confirmed_tokens_transfers_by_address_ri.from_dict(list_confirmed_tokens_transfers_by_address_ri_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


