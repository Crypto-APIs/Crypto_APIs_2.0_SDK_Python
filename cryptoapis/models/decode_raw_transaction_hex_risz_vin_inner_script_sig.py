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

class DecodeRawTransactionHexRISZVinInnerScriptSig(BaseModel):
    """
    Specifies the required signatures.
    """
    asm: Optional[StrictStr] = Field(None, description="The asm strands for assembly, which is the symbolic representation of the Bitcoin's Script language op-codes.")
    hex: Optional[StrictStr] = Field(None, description="Represents the hex of the public key of the address.")
    type: Optional[StrictStr] = Field(None, description="Represents the script type of the reference transaction identifier.")
    __properties = ["asm", "hex", "type"]

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
    def from_json(cls, json_str: str) -> DecodeRawTransactionHexRISZVinInnerScriptSig:
        """Create an instance of DecodeRawTransactionHexRISZVinInnerScriptSig from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DecodeRawTransactionHexRISZVinInnerScriptSig:
        """Create an instance of DecodeRawTransactionHexRISZVinInnerScriptSig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DecodeRawTransactionHexRISZVinInnerScriptSig.parse_obj(obj)

        _obj = DecodeRawTransactionHexRISZVinInnerScriptSig.parse_obj({
            "asm": obj.get("asm"),
            "hex": obj.get("hex"),
            "type": obj.get("type")
        })
        return _obj

