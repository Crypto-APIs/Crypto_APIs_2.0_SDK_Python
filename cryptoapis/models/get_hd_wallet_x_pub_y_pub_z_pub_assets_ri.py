# coding: utf-8

"""
    CryptoAPIs

    Crypto APIs is a complex and innovative infrastructure layer that radically simplifies the development of any Blockchain and Crypto related applications. Organized around REST, Crypto APIs can assist both novice Bitcoin/Ethereum enthusiasts and crypto experts with the development of their blockchain applications. Crypto APIs provides unified endpoints and data, raw data, automatic tokens and coins forwardings, callback functionalities, and much more.  # noqa: E501

    The version of the OpenAPI document: 2021-03-20
    Contact: developers@cryptoapis.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, Field, conlist
from cryptoapis.models.get_hd_wallet_x_pub_y_pub_z_pub_assets_ri_confirmed_balance import GetHDWalletXPubYPubZPubAssetsRIConfirmedBalance
from cryptoapis.models.get_hd_wallet_x_pub_y_pub_z_pub_assets_ri_fungible_tokens_inner import GetHDWalletXPubYPubZPubAssetsRIFungibleTokensInner
from cryptoapis.models.get_hd_wallet_x_pub_y_pub_z_pub_assets_ri_non_fungible_tokens_inner import GetHDWalletXPubYPubZPubAssetsRINonFungibleTokensInner

class GetHDWalletXPubYPubZPubAssetsRI(BaseModel):
    """
    GetHDWalletXPubYPubZPubAssetsRI
    """
    fungible_tokens: Optional[conlist(GetHDWalletXPubYPubZPubAssetsRIFungibleTokensInner)] = Field(None, alias="fungibleTokens", description="Represents fungible tokens'es detailed information")
    non_fungible_tokens: Optional[conlist(GetHDWalletXPubYPubZPubAssetsRINonFungibleTokensInner)] = Field(None, alias="nonFungibleTokens", description="Represents non-fungible tokens'es detailed information.")
    confirmed_balance: GetHDWalletXPubYPubZPubAssetsRIConfirmedBalance = Field(..., alias="confirmedBalance")
    __properties = ["fungibleTokens", "nonFungibleTokens", "confirmedBalance"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> GetHDWalletXPubYPubZPubAssetsRI:
        """Create an instance of GetHDWalletXPubYPubZPubAssetsRI from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in fungible_tokens (list)
        _items = []
        if self.fungible_tokens:
            for _item in self.fungible_tokens:
                if _item:
                    _items.append(_item.to_dict())
            _dict['fungibleTokens'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in non_fungible_tokens (list)
        _items = []
        if self.non_fungible_tokens:
            for _item in self.non_fungible_tokens:
                if _item:
                    _items.append(_item.to_dict())
            _dict['nonFungibleTokens'] = _items
        # override the default output from pydantic by calling `to_dict()` of confirmed_balance
        if self.confirmed_balance:
            _dict['confirmedBalance'] = self.confirmed_balance.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GetHDWalletXPubYPubZPubAssetsRI:
        """Create an instance of GetHDWalletXPubYPubZPubAssetsRI from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GetHDWalletXPubYPubZPubAssetsRI.parse_obj(obj)

        _obj = GetHDWalletXPubYPubZPubAssetsRI.parse_obj({
            "fungible_tokens": [GetHDWalletXPubYPubZPubAssetsRIFungibleTokensInner.from_dict(_item) for _item in obj.get("fungibleTokens")] if obj.get("fungibleTokens") is not None else None,
            "non_fungible_tokens": [GetHDWalletXPubYPubZPubAssetsRINonFungibleTokensInner.from_dict(_item) for _item in obj.get("nonFungibleTokens")] if obj.get("nonFungibleTokens") is not None else None,
            "confirmed_balance": GetHDWalletXPubYPubZPubAssetsRIConfirmedBalance.from_dict(obj.get("confirmedBalance")) if obj.get("confirmedBalance") is not None else None
        })
        return _obj

