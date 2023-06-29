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
from cryptoapis.models.list_synced_addresses_ri import ListSyncedAddressesRI

class ListSyncedAddressesRData(BaseModel):
    """
    ListSyncedAddressesRData
    """
    limit: StrictInt = Field(..., description="Defines how many items should be returned in the response per page basis.")
    offset: StrictInt = Field(..., description="The starting index of the response items, i.e. where the response should start listing the returned items.")
    total: StrictInt = Field(..., description="Defines the total number of items returned in the response.")
    items: conlist(ListSyncedAddressesRI) = Field(...)
    __properties = ["limit", "offset", "total", "items"]

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
    def from_json(cls, json_str: str) -> ListSyncedAddressesRData:
        """Create an instance of ListSyncedAddressesRData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in items (list)
        _items = []
        if self.items:
            for _item in self.items:
                if _item:
                    _items.append(_item.to_dict())
            _dict['items'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ListSyncedAddressesRData:
        """Create an instance of ListSyncedAddressesRData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ListSyncedAddressesRData.parse_obj(obj)

        _obj = ListSyncedAddressesRData.parse_obj({
            "limit": obj.get("limit"),
            "offset": obj.get("offset"),
            "total": obj.get("total"),
            "items": [ListSyncedAddressesRI.from_dict(_item) for _item in obj.get("items")] if obj.get("items") is not None else None
        })
        return _obj

