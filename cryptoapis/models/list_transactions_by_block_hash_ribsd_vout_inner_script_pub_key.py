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
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist

class ListTransactionsByBlockHashRIBSDVoutInnerScriptPubKey(BaseModel):
    """
    Represents the script public key.
    """
    addresses: conlist(StrictStr) = Field(...)
    asm: StrictStr = Field(..., description="Represents the assembly of the script public key of the address.")
    hex: StrictStr = Field(..., description="Represents the hex of the script public key of the address.")
    req_sigs: Optional[StrictInt] = Field(None, alias="reqSigs", description="Represents the required signatures.")
    type: StrictStr = Field(..., description="Represents the script type.")
    __properties = ["addresses", "asm", "hex", "reqSigs", "type"]

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
    def from_json(cls, json_str: str) -> ListTransactionsByBlockHashRIBSDVoutInnerScriptPubKey:
        """Create an instance of ListTransactionsByBlockHashRIBSDVoutInnerScriptPubKey from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ListTransactionsByBlockHashRIBSDVoutInnerScriptPubKey:
        """Create an instance of ListTransactionsByBlockHashRIBSDVoutInnerScriptPubKey from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ListTransactionsByBlockHashRIBSDVoutInnerScriptPubKey.parse_obj(obj)

        _obj = ListTransactionsByBlockHashRIBSDVoutInnerScriptPubKey.parse_obj({
            "addresses": obj.get("addresses"),
            "asm": obj.get("asm"),
            "hex": obj.get("hex"),
            "req_sigs": obj.get("reqSigs"),
            "type": obj.get("type")
        })
        return _obj

