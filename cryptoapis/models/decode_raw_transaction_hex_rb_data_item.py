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

class DecodeRawTransactionHexRBDataItem(BaseModel):
    """
    DecodeRawTransactionHexRBDataItem
    """
    raw_transaction_hex: StrictStr = Field(..., alias="rawTransactionHex", description="Represents the raw transaction Hex that has to be decoded.")
    __properties = ["rawTransactionHex"]

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
    def from_json(cls, json_str: str) -> DecodeRawTransactionHexRBDataItem:
        """Create an instance of DecodeRawTransactionHexRBDataItem from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DecodeRawTransactionHexRBDataItem:
        """Create an instance of DecodeRawTransactionHexRBDataItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DecodeRawTransactionHexRBDataItem.parse_obj(obj)

        _obj = DecodeRawTransactionHexRBDataItem.parse_obj({
            "raw_transaction_hex": obj.get("rawTransactionHex")
        })
        return _obj

