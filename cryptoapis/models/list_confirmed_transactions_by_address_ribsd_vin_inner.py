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
from cryptoapis.models.list_confirmed_transactions_by_address_ribsd_vin_inner_script_sig import ListConfirmedTransactionsByAddressRIBSDVinInnerScriptSig

class ListConfirmedTransactionsByAddressRIBSDVinInner(BaseModel):
    """
    ListConfirmedTransactionsByAddressRIBSDVinInner
    """
    addresses: conlist(StrictStr) = Field(...)
    coinbase: StrictStr = Field(..., description="Represents the coinbase hex.")
    script_sig: ListConfirmedTransactionsByAddressRIBSDVinInnerScriptSig = Field(..., alias="scriptSig")
    sequence: StrictStr = Field(..., description="Represents the script sequence number.")
    txid: Optional[StrictStr] = Field(None, description="Represents the reference transaction identifier.")
    txinwitness: conlist(StrictStr) = Field(...)
    value: StrictStr = Field(..., description="Represents the sent/received amount.")
    vout: Optional[StrictInt] = Field(None, description="It refers to the index of the output address of this transaction. The index starts from 0.")
    __properties = ["addresses", "coinbase", "scriptSig", "sequence", "txid", "txinwitness", "value", "vout"]

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
    def from_json(cls, json_str: str) -> ListConfirmedTransactionsByAddressRIBSDVinInner:
        """Create an instance of ListConfirmedTransactionsByAddressRIBSDVinInner from a JSON string"""
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
    def from_dict(cls, obj: dict) -> ListConfirmedTransactionsByAddressRIBSDVinInner:
        """Create an instance of ListConfirmedTransactionsByAddressRIBSDVinInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ListConfirmedTransactionsByAddressRIBSDVinInner.parse_obj(obj)

        _obj = ListConfirmedTransactionsByAddressRIBSDVinInner.parse_obj({
            "addresses": obj.get("addresses"),
            "coinbase": obj.get("coinbase"),
            "script_sig": ListConfirmedTransactionsByAddressRIBSDVinInnerScriptSig.from_dict(obj.get("scriptSig")) if obj.get("scriptSig") is not None else None,
            "sequence": obj.get("sequence"),
            "txid": obj.get("txid"),
            "txinwitness": obj.get("txinwitness"),
            "value": obj.get("value"),
            "vout": obj.get("vout")
        })
        return _obj

