# DecodeRawTransactionHexRISZ

Zcash

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expiry_height** | **int** | Represents a block height after which the transaction will expire. | 
**locktime** | **int** | Represents the locktime on the transaction on the specific blockchain, i.e. the blockheight at which the transaction is valid. | 
**overwintered** | **bool** | \&quot;Overwinter\&quot; is the network upgrade for the Zcash blockchain. | 
**saplinged** | **bool** | Defines if the transaction includes sapling or not. | 
**transaction_hash** | **str** | Represents the same as transactionId for account-based protocols like Ethereum, while it could be different in UTXO-based protocols like Bitcoin. E.g., in UTXO-based protocols hash is different from transactionId for SegWit transactions. | 
**value_balance** | **str** | Defines the transaction value balance. | 
**version** | **int** | Represents the transaction version number. | 
**version_group_id** | **str** | Represents the transaction version group ID | 
**vin** | [**List[DecodeRawTransactionHexRISZVinInner]**](DecodeRawTransactionHexRISZVinInner.md) | Represents the Inputs of the transaction | 
**vout** | [**List[DecodeRawTransactionHexRISZVoutInner]**](DecodeRawTransactionHexRISZVoutInner.md) | Represents the Inputs of the transaction | 

## Example

```python
from cryptoapis.models.decode_raw_transaction_hex_risz import DecodeRawTransactionHexRISZ

# TODO update the JSON string below
json = "{}"
# create an instance of DecodeRawTransactionHexRISZ from a JSON string
decode_raw_transaction_hex_risz_instance = DecodeRawTransactionHexRISZ.from_json(json)
# print the JSON string representation of the object
print DecodeRawTransactionHexRISZ.to_json()

# convert the object into a dict
decode_raw_transaction_hex_risz_dict = decode_raw_transaction_hex_risz_instance.to_dict()
# create an instance of DecodeRawTransactionHexRISZ from a dict
decode_raw_transaction_hex_risz_form_dict = decode_raw_transaction_hex_risz.from_dict(decode_raw_transaction_hex_risz_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


