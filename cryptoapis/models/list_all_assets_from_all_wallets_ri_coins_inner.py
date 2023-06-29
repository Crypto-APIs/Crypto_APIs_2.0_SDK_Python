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



from pydantic import BaseModel, Field, StrictStr

class ListAllAssetsFromAllWalletsRICoinsInner(BaseModel):
    """
    ListAllAssetsFromAllWalletsRICoinsInner
    """
    blockchain: StrictStr = Field(..., description="Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.")
    confirmed_balance: StrictStr = Field(..., alias="confirmedBalance", description="Defines the total balance of the address that is confirmed. It doesn't include unconfirmed transactions.")
    network: StrictStr = Field(..., description="Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"goerli\" are test networks.")
    total_received: StrictStr = Field(..., alias="totalReceived", description="Defines the total amount of all coins received to the address, based on confirmed transactions.")
    total_spent: StrictStr = Field(..., alias="totalSpent", description="Defines the total amount of all spent by this address coins, based on confirmed transactions.")
    unit: StrictStr = Field(..., description="Represents the unit of the confirmed balance.")
    __properties = ["blockchain", "confirmedBalance", "network", "totalReceived", "totalSpent", "unit"]

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
    def from_json(cls, json_str: str) -> ListAllAssetsFromAllWalletsRICoinsInner:
        """Create an instance of ListAllAssetsFromAllWalletsRICoinsInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ListAllAssetsFromAllWalletsRICoinsInner:
        """Create an instance of ListAllAssetsFromAllWalletsRICoinsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ListAllAssetsFromAllWalletsRICoinsInner.parse_obj(obj)

        _obj = ListAllAssetsFromAllWalletsRICoinsInner.parse_obj({
            "blockchain": obj.get("blockchain"),
            "confirmed_balance": obj.get("confirmedBalance"),
            "network": obj.get("network"),
            "total_received": obj.get("totalReceived"),
            "total_spent": obj.get("totalSpent"),
            "unit": obj.get("unit")
        })
        return _obj

