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
from cryptoapis.models.decode_raw_transaction_hex_risb_vin_inner_script_sig import DecodeRawTransactionHexRISBVinInnerScriptSig

class DecodeRawTransactionHexRISBVinInner(BaseModel):
    """
    DecodeRawTransactionHexRISBVinInner
    """
    address: Optional[StrictStr] = Field(None, description="Represents the address which send/receive the amount.")
    input_hash: Optional[StrictStr] = Field(None, alias="inputHash", description="Represents the transaction inputs' indentifier.")
    output_index: Optional[StrictInt] = Field(None, alias="outputIndex", description="Represents the output of a transaction.")
    script_sig: DecodeRawTransactionHexRISBVinInnerScriptSig = Field(..., alias="scriptSig")
    sequence: Optional[StrictStr] = Field(None, description="Represents the script sequence number.")
    txinwitness: Optional[conlist(StrictStr)] = None
    __properties = ["address", "inputHash", "outputIndex", "scriptSig", "sequence", "txinwitness"]

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
    def from_json(cls, json_str: str) -> DecodeRawTransactionHexRISBVinInner:
        """Create an instance of DecodeRawTransactionHexRISBVinInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of script_sig
        if self.script_sig:
            _dict['scriptSig'] = self.script_sig.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DecodeRawTransactionHexRISBVinInner:
        """Create an instance of DecodeRawTransactionHexRISBVinInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DecodeRawTransactionHexRISBVinInner.parse_obj(obj)

        _obj = DecodeRawTransactionHexRISBVinInner.parse_obj({
            "address": obj.get("address"),
            "input_hash": obj.get("inputHash"),
            "output_index": obj.get("outputIndex"),
            "script_sig": DecodeRawTransactionHexRISBVinInnerScriptSig.from_dict(obj.get("scriptSig")) if obj.get("scriptSig") is not None else None,
            "sequence": obj.get("sequence"),
            "txinwitness": obj.get("txinwitness")
        })
        return _obj

