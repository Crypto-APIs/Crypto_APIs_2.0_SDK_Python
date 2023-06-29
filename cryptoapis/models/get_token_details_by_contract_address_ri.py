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


from typing import Optional
from pydantic import BaseModel, Field, StrictStr

class GetTokenDetailsByContractAddressRI(BaseModel):
    """
    GetTokenDetailsByContractAddressRI
    """
    token_decimals: StrictStr = Field(..., alias="tokenDecimals", description="Defines the number of decimals that the token possesses.")
    token_name: Optional[StrictStr] = Field(None, alias="tokenName", description="Specifies the token's name.")
    token_symbol: Optional[StrictStr] = Field(None, alias="tokenSymbol", description="Defines the unique symbol of the token.")
    token_type: StrictStr = Field(..., alias="tokenType", description="Defines the type of the token.")
    total_supply: StrictStr = Field(..., alias="totalSupply", description="Defines the total number of tokens created that exist on the market minus the ones that have been burned.")
    __properties = ["tokenDecimals", "tokenName", "tokenSymbol", "tokenType", "totalSupply"]

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
    def from_json(cls, json_str: str) -> GetTokenDetailsByContractAddressRI:
        """Create an instance of GetTokenDetailsByContractAddressRI from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GetTokenDetailsByContractAddressRI:
        """Create an instance of GetTokenDetailsByContractAddressRI from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GetTokenDetailsByContractAddressRI.parse_obj(obj)

        _obj = GetTokenDetailsByContractAddressRI.parse_obj({
            "token_decimals": obj.get("tokenDecimals"),
            "token_name": obj.get("tokenName"),
            "token_symbol": obj.get("tokenSymbol"),
            "token_type": obj.get("tokenType"),
            "total_supply": obj.get("totalSupply")
        })
        return _obj

