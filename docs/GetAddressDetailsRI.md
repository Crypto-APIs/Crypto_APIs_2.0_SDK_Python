# GetAddressDetailsRI


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transactions_count** | **int** | Represents the total number of confirmed coins transactions for this address, both incoming and outgoing. Applies for coins only **and not** tokens transfers e.g. for Ethereum. &#x60;transactionsCount&#x60; could result as less than incoming and outgoing transactions put together (e.g. in Bitcoin), due to the fact that one and the same address could be in senders and receivers addresses. | 
**confirmed_balance** | [**GetAddressDetailsRIConfirmedBalance**](GetAddressDetailsRIConfirmedBalance.md) |  | 
**total_received** | [**GetAddressDetailsRITotalReceived**](GetAddressDetailsRITotalReceived.md) |  | 
**total_spent** | [**GetAddressDetailsRITotalSpent**](GetAddressDetailsRITotalSpent.md) |  | 
**incoming_transactions_count** | **int** | Numeric representation of the received transaction count of the address | 
**outgoing_transactions_count** | **int** | Numeric representation of the sent transaction count of the address | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


