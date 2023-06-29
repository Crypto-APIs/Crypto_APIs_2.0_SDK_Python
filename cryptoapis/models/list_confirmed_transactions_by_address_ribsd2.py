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


from typing import List
from pydantic import BaseModel, Field, StrictInt, conlist
from cryptoapis.models.list_confirmed_transactions_by_address_ribsd2_vin_inner import ListConfirmedTransactionsByAddressRIBSD2VinInner
from cryptoapis.models.list_confirmed_transactions_by_address_ribsd2_vout_inner import ListConfirmedTransactionsByAddressRIBSD2VoutInner

class ListConfirmedTransactionsByAddressRIBSD2(BaseModel):
    """
    Dash
    """
    locktime: StrictInt = Field(..., description="Represents the locktime on the transaction on the specific blockchain, i.e. the blockheight at which the transaction is valid.")
    size: StrictInt = Field(..., description="Represents the total size of this transaction.")
    version: StrictInt = Field(..., description="Represents the transaction's version number.")
    vin: conlist(ListConfirmedTransactionsByAddressRIBSD2VinInner) = Field(..., description="Represents the transaction inputs.")
    vout: conlist(ListConfirmedTransactionsByAddressRIBSD2VoutInner) = Field(..., description="Represents the transaction outputs.")
    __properties = ["locktime", "size", "version", "vin", "vout"]

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
    def from_json(cls, json_str: str) -> ListConfirmedTransactionsByAddressRIBSD2:
        """Create an instance of ListConfirmedTransactionsByAddressRIBSD2 from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in vin (list)
        _items = []
        if self.vin:
            for _item in self.vin:
                if _item:
                    _items.append(_item.to_dict())
            _dict['vin'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in vout (list)
        _items = []
        if self.vout:
            for _item in self.vout:
                if _item:
                    _items.append(_item.to_dict())
            _dict['vout'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ListConfirmedTransactionsByAddressRIBSD2:
        """Create an instance of ListConfirmedTransactionsByAddressRIBSD2 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ListConfirmedTransactionsByAddressRIBSD2.parse_obj(obj)

        _obj = ListConfirmedTransactionsByAddressRIBSD2.parse_obj({
            "locktime": obj.get("locktime"),
            "size": obj.get("size"),
            "version": obj.get("version"),
            "vin": [ListConfirmedTransactionsByAddressRIBSD2VinInner.from_dict(_item) for _item in obj.get("vin")] if obj.get("vin") is not None else None,
            "vout": [ListConfirmedTransactionsByAddressRIBSD2VoutInner.from_dict(_item) for _item in obj.get("vout")] if obj.get("vout") is not None else None
        })
        return _obj

