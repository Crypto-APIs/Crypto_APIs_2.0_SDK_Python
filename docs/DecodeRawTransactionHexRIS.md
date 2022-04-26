# DecodeRawTransactionHexRIS

Represents the specific transaction data according to the blockchain

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**weight** | **int** | Represents the size of a block, measured in weight units and including the segwit discount. | [optional] 
**approximate_fee** | **str** | Defines the approximate fee value. When isConfirmed is True - Defines the amount of the transaction fee When isConfirmed is False - For ETH-based blockchains this attribute represents the max fee value. | [optional] 
**approximate_minimum_required_fee** | **str** | Defines the approximate minimum fee that is required for the transaction. | [optional] 
**gas_paid_for_data** | **str** | Represents the amount of gas paid for the data in the transaction. | [optional] 
**gas_price** | **str** | Represents the price offered to the miner to purchase this amount of gas. | [optional] 
**input_data** | **str** | Represents additional information that is required for the transaction. | [optional] 
**max_fee_per_gas** | **str** | Defines the maximum amount that customer is willing to pay per unit of gas to get his transaction included in a block. | [optional] 
**max_fee_priority_per_gas** | **str** | Represents determined by the user value that is paid directly to miners. | [optional] 
**r** | **str** | Represents output of an ECDSA signature. | [optional] 
**s** | **str** | Represents output of an ECDSA signature. | [optional] 
**v** | **str** | Defines the the recovery id. | [optional] 
**value** | **str** | Represents the sent/received amount. | [optional] 
**locktime** | **int** | Represents the locktime on the transaction on the specific blockchain, i.e. the blockheight at which the transaction is valid. | [optional] 
**transaction_hash** | **str** | Represents the same as transactionId for account-based protocols like Ethereum, while it could be different in UTXO-based protocols like Bitcoin. E.g., in UTXO-based protocols hash is different from transactionId for SegWit transactions. | [optional] 
**v_size** | **int** | Represents the virtual size of this transaction. | [optional] 
**version** | **int** | Represents the transaction version number. | [optional] 
**vin** | [**[DecodeRawTransactionHexRISZVin]**](DecodeRawTransactionHexRISZVin.md) | Represents the Inputs of the transaction | [optional] 
**vout** | [**[DecodeRawTransactionHexRISZVout]**](DecodeRawTransactionHexRISZVout.md) | Represents the Inputs of the transaction | [optional] 
**gas_limit** | **str** | Represents the amount of gas used by this specific transaction alone. | [optional] 
**nonce** | **int** | Represents the sequential running number for an address, starting from 0 for the first transaction. E.g., if the nonce of a transaction is 10, it would be the 11th transaction sent from the sender&#39;s address. | [optional] 
**recipient** | **str** | The address which receives this transaction. In UTXO-based protocols like Bitcoin there could be several senders while in account-based protocols like Ethereum there is always only one recipient. | [optional] 
**sender** | **str** | Represents the address which sends this transaction. In UTXO-based protocols like Bitcoin there could be several senders while in account-based protocols like Ethereum there is always only one sender. | [optional] 
**type** | **int** | Specifies the transaction type as one from three options: if response returns a &#x60;\&quot;0\&quot;&#x60; it means the raw transaction includes legacy transaction data, if it is &#x60;\&quot;1\&quot;&#x60; - includes access lists for EIP2930, and if it is &#x60;\&quot;2\&quot;&#x60; - EIP1559 data. | [optional] 
**expiry_height** | **int** | Represents a block height after which the transaction will expire. | [optional] 
**overwintered** | **bool** | \&quot;Overwinter\&quot; is the network upgrade for the Zcash blockchain. | [optional] 
**saplinged** | **bool** | Defines if the transaction includes sapling or not. | [optional] 
**value_balance** | **str** | Defines the transaction value balance. | [optional] 
**version_group_id** | **str** | Represents the transaction version group ID | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


