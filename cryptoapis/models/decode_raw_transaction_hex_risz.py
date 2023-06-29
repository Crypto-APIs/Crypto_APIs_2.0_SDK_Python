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
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conlist
from cryptoapis.models.decode_raw_transaction_hex_risz_vin_inner import DecodeRawTransactionHexRISZVinInner
from cryptoapis.models.decode_raw_transaction_hex_risz_vout_inner import DecodeRawTransactionHexRISZVoutInner

class DecodeRawTransactionHexRISZ(BaseModel):
    """
    Zcash
    """
    expiry_height: StrictInt = Field(..., alias="expiryHeight", description="Represents a block height after which the transaction will expire.")
    locktime: StrictInt = Field(..., description="Represents the locktime on the transaction on the specific blockchain, i.e. the blockheight at which the transaction is valid.")
    overwintered: StrictBool = Field(..., description="\"Overwinter\" is the network upgrade for the Zcash blockchain.")
    saplinged: StrictBool = Field(..., description="Defines if the transaction includes sapling or not.")
    transaction_hash: StrictStr = Field(..., alias="transactionHash", description="Represents the same as transactionId for account-based protocols like Ethereum, while it could be different in UTXO-based protocols like Bitcoin. E.g., in UTXO-based protocols hash is different from transactionId for SegWit transactions.")
    value_balance: StrictStr = Field(..., alias="valueBalance", description="Defines the transaction value balance.")
    version: StrictInt = Field(..., description="Represents the transaction version number.")
    version_group_id: StrictStr = Field(..., alias="versionGroupId", description="Represents the transaction version group ID")
    vin: conlist(DecodeRawTransactionHexRISZVinInner) = Field(..., description="Represents the Inputs of the transaction")
    vout: conlist(DecodeRawTransactionHexRISZVoutInner) = Field(..., description="Represents the Inputs of the transaction")
    __properties = ["expiryHeight", "locktime", "overwintered", "saplinged", "transactionHash", "valueBalance", "version", "versionGroupId", "vin", "vout"]

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
    def from_json(cls, json_str: str) -> DecodeRawTransactionHexRISZ:
        """Create an instance of DecodeRawTransactionHexRISZ from a JSON string"""
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
    def from_dict(cls, obj: dict) -> DecodeRawTransactionHexRISZ:
        """Create an instance of DecodeRawTransactionHexRISZ from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DecodeRawTransactionHexRISZ.parse_obj(obj)

        _obj = DecodeRawTransactionHexRISZ.parse_obj({
            "expiry_height": obj.get("expiryHeight"),
            "locktime": obj.get("locktime"),
            "overwintered": obj.get("overwintered"),
            "saplinged": obj.get("saplinged"),
            "transaction_hash": obj.get("transactionHash"),
            "value_balance": obj.get("valueBalance"),
            "version": obj.get("version"),
            "version_group_id": obj.get("versionGroupId"),
            "vin": [DecodeRawTransactionHexRISZVinInner.from_dict(_item) for _item in obj.get("vin")] if obj.get("vin") is not None else None,
            "vout": [DecodeRawTransactionHexRISZVoutInner.from_dict(_item) for _item in obj.get("vout")] if obj.get("vout") is not None else None
        })
        return _obj
