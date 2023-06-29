# ListDepositAddressesRI


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Specifies the specific address&#39;s unique string value. | 
**confirmed_balance** | [**ListDepositAddressesRIConfirmedBalance**](ListDepositAddressesRIConfirmedBalance.md) |  | 
**created_timestamp** | **int** | Defines the specific UNIX time when the deposit address was created. | 
**fungible_tokens** | [**List[ListDepositAddressesRIFungibleTokensInner]**](ListDepositAddressesRIFungibleTokensInner.md) | Represents fungible tokens&#39;es detailed information | 
**index** | **str** | Represents the index of the address in the wallet. | 
**label** | **str** | Represents a custom tag that customers can set up for their Wallets and addresses. E.g. custom label named \&quot;Special addresses\&quot;. | 
**non_fungible_tokens** | [**List[ListDepositAddressesRINonFungibleTokensInner]**](ListDepositAddressesRINonFungibleTokensInner.md) | Represents non-fungible tokens&#39;es detailed information. | 

## Example

```python
from cryptoapis.models.list_deposit_addresses_ri import ListDepositAddressesRI

# TODO update the JSON string below
json = "{}"
# create an instance of ListDepositAddressesRI from a JSON string
list_deposit_addresses_ri_instance = ListDepositAddressesRI.from_json(json)
# print the JSON string representation of the object
print ListDepositAddressesRI.to_json()

# convert the object into a dict
list_deposit_addresses_ri_dict = list_deposit_addresses_ri_instance.to_dict()
# create an instance of ListDepositAddressesRI from a dict
list_deposit_addresses_ri_form_dict = list_deposit_addresses_ri.from_dict(list_deposit_addresses_ri_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


