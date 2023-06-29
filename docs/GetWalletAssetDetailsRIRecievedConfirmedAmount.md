# GetWalletAssetDetailsRIRecievedConfirmedAmount

Specifies the confirmed amount that has been received.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | Specifies the confirmed amount that has been received. | 
**unit** | **str** | Specifies the unit of the confirmed amount that has been received. | 

## Example

```python
from cryptoapis.models.get_wallet_asset_details_ri_recieved_confirmed_amount import GetWalletAssetDetailsRIRecievedConfirmedAmount

# TODO update the JSON string below
json = "{}"
# create an instance of GetWalletAssetDetailsRIRecievedConfirmedAmount from a JSON string
get_wallet_asset_details_ri_recieved_confirmed_amount_instance = GetWalletAssetDetailsRIRecievedConfirmedAmount.from_json(json)
# print the JSON string representation of the object
print GetWalletAssetDetailsRIRecievedConfirmedAmount.to_json()

# convert the object into a dict
get_wallet_asset_details_ri_recieved_confirmed_amount_dict = get_wallet_asset_details_ri_recieved_confirmed_amount_instance.to_dict()
# create an instance of GetWalletAssetDetailsRIRecievedConfirmedAmount from a dict
get_wallet_asset_details_ri_recieved_confirmed_amount_form_dict = get_wallet_asset_details_ri_recieved_confirmed_amount.from_dict(get_wallet_asset_details_ri_recieved_confirmed_amount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


