# GetTransactionDetailsByTransactionIDRIBSZVShieldedOutputInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cmu** | **str** | Represents the 𝑢-coordinate of the note commitment for the output note. | 
**cv** | **str** | Defines a value commitment to the value of the input note. | 
**enc_cipher_text** | **str** | Represents a ciphertext component for the encrypted output note. | 
**ephemeral_key** | **str** | Represents an encoding of an ephemeral Jubjub public key. | 
**out_cipher_text** | **str** | Represents a ciphertext component that allows the holder of the outgoing cipher key to recover the diversified transmission key pkd and ephemeral private key esk, hence the entire note plaintext. | 
**proof** | **str** | Represents the proof. | 

## Example

```python
from cryptoapis.models.get_transaction_details_by_transaction_idribszv_shielded_output_inner import GetTransactionDetailsByTransactionIDRIBSZVShieldedOutputInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetTransactionDetailsByTransactionIDRIBSZVShieldedOutputInner from a JSON string
get_transaction_details_by_transaction_idribszv_shielded_output_inner_instance = GetTransactionDetailsByTransactionIDRIBSZVShieldedOutputInner.from_json(json)
# print the JSON string representation of the object
print GetTransactionDetailsByTransactionIDRIBSZVShieldedOutputInner.to_json()

# convert the object into a dict
get_transaction_details_by_transaction_idribszv_shielded_output_inner_dict = get_transaction_details_by_transaction_idribszv_shielded_output_inner_instance.to_dict()
# create an instance of GetTransactionDetailsByTransactionIDRIBSZVShieldedOutputInner from a dict
get_transaction_details_by_transaction_idribszv_shielded_output_inner_form_dict = get_transaction_details_by_transaction_idribszv_shielded_output_inner.from_dict(get_transaction_details_by_transaction_idribszv_shielded_output_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


