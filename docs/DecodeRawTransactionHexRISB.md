# DecodeRawTransactionHexRISB

Bitcoin

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locktime** | **int** | Represents the time at which a particular transaction can be added to the blockchain. | 
**transaction_hash** | **str** | Represents the same as transactionId for account-based protocols like Ethereum, while it could be different in UTXO-based protocols like Bitcoin. E.g., in UTXO-based protocols hash is different from transactionId for SegWit transactions. | 
**v_size** | **int** | Represents the virtual size of this transaction. | 
**version** | **int** | Represents the transaction version number. | 
**vin** | [**List[DecodeRawTransactionHexRISBVinInner]**](DecodeRawTransactionHexRISBVinInner.md) | Represents the transaction inputs. | 
**vout** | [**List[DecodeRawTransactionHexRISBVoutInner]**](DecodeRawTransactionHexRISBVoutInner.md) | Represents the transaction outputs. | 
**weight** | **int** | Represents the size of Bitcoin block, measured in weight units and including the segwit discount. | [optional] 

## Example

```python
from cryptoapis.models.decode_raw_transaction_hex_risb import DecodeRawTransactionHexRISB

# TODO update the JSON string below
json = "{}"
# create an instance of DecodeRawTransactionHexRISB from a JSON string
decode_raw_transaction_hex_risb_instance = DecodeRawTransactionHexRISB.from_json(json)
# print the JSON string representation of the object
print DecodeRawTransactionHexRISB.to_json()

# convert the object into a dict
decode_raw_transaction_hex_risb_dict = decode_raw_transaction_hex_risb_instance.to_dict()
# create an instance of DecodeRawTransactionHexRISB from a dict
decode_raw_transaction_hex_risb_form_dict = decode_raw_transaction_hex_risb.from_dict(decode_raw_transaction_hex_risb_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


