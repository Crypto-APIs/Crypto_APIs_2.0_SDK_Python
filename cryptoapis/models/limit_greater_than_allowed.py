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
from pydantic import BaseModel, Field, StrictStr, conlist
from cryptoapis.models.banned_ip_address_details_inner import BannedIpAddressDetailsInner

class LimitGreaterThanAllowed(BaseModel):
    """
    limit_greater_than_allowed
    """
    code: StrictStr = Field(..., description="Specifies an error code, e.g. error 404.")
    message: StrictStr = Field(..., description="Specifies the message of the error, i.e. why the error was returned, e.g. error 404 stands for “not found”.")
    details: Optional[conlist(BannedIpAddressDetailsInner)] = None
    __properties = ["code", "message", "details"]

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
    def from_json(cls, json_str: str) -> LimitGreaterThanAllowed:
        """Create an instance of LimitGreaterThanAllowed from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in details (list)
        _items = []
        if self.details:
            for _item in self.details:
                if _item:
                    _items.append(_item.to_dict())
            _dict['details'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> LimitGreaterThanAllowed:
        """Create an instance of LimitGreaterThanAllowed from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return LimitGreaterThanAllowed.parse_obj(obj)

        _obj = LimitGreaterThanAllowed.parse_obj({
            "code": obj.get("code"),
            "message": obj.get("message"),
            "details": [BannedIpAddressDetailsInner.from_dict(_item) for _item in obj.get("details")] if obj.get("details") is not None else None
        })
        return _obj

