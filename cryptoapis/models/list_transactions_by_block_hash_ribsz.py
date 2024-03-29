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
from cryptoapis.models.get_transaction_details_by_transaction_idribsz_vout_inner import GetTransactionDetailsByTransactionIDRIBSZVoutInner
from cryptoapis.models.get_transaction_details_by_transaction_idribszv_shielded_output_inner import GetTransactionDetailsByTransactionIDRIBSZVShieldedOutputInner
from cryptoapis.models.get_transaction_details_by_transaction_idribszv_shielded_spend_inner import GetTransactionDetailsByTransactionIDRIBSZVShieldedSpendInner
from cryptoapis.models.list_transactions_by_block_hash_ribsz_vin_inner import ListTransactionsByBlockHashRIBSZVinInner
from cryptoapis.models.list_transactions_by_block_hash_ribszv_join_split_inner import ListTransactionsByBlockHashRIBSZVJoinSplitInner

class ListTransactionsByBlockHashRIBSZ(BaseModel):
    """
    Zcash
    """
    binding_sig: StrictStr = Field(..., alias="bindingSig", description="It is used to enforce balance of Spend and Output transfers, in order to prevent their replay across transactions.")
    expiry_height: StrictInt = Field(..., alias="expiryHeight", description="Represents a block height after which the transaction will expire.")
    join_split_pub_key: StrictStr = Field(..., alias="joinSplitPubKey", description="Represents an encoding of a JoinSplitSig public validating key.")
    join_split_sig: StrictStr = Field(..., alias="joinSplitSig", description="Is used to sign transactions that contain at least one JoinSplit description.")
    locktime: StrictInt = Field(..., description="Represents the time at which a particular transaction can be added to the blockchain.")
    overwintered: StrictBool = Field(..., description="\"Overwinter\" is the network upgrade for the Zcash blockchain.")
    size: StrictInt = Field(..., description="Represents the total size of this transaction.")
    v_join_split: conlist(ListTransactionsByBlockHashRIBSZVJoinSplitInner) = Field(..., alias="vJoinSplit", description="Represents a sequence of JoinSplit descriptions using BCTV14 proofs.")
    v_shielded_output: conlist(GetTransactionDetailsByTransactionIDRIBSZVShieldedOutputInner) = Field(..., alias="vShieldedOutput", description="Object Array representation of transaction output descriptions")
    v_shielded_spend: conlist(GetTransactionDetailsByTransactionIDRIBSZVShieldedSpendInner) = Field(..., alias="vShieldedSpend", description="Object Array representation of transaction spend descriptions")
    value_balance: StrictStr = Field(..., alias="valueBalance", description="Defines the transaction value balance.")
    version: StrictInt = Field(..., description="Numeric representation of the transaction Represents the transaction version number.")
    version_group_id: StrictStr = Field(..., alias="versionGroupId", description="Represents the transaction version group ID.")
    vin: conlist(ListTransactionsByBlockHashRIBSZVinInner) = Field(..., description="Object Array representation of transaction inputs")
    vout: conlist(GetTransactionDetailsByTransactionIDRIBSZVoutInner) = Field(..., description="Object Array representation of transaction outputs")
    __properties = ["bindingSig", "expiryHeight", "joinSplitPubKey", "joinSplitSig", "locktime", "overwintered", "size", "vJoinSplit", "vShieldedOutput", "vShieldedSpend", "valueBalance", "version", "versionGroupId", "vin", "vout"]

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
    def from_json(cls, json_str: str) -> ListTransactionsByBlockHashRIBSZ:
        """Create an instance of ListTransactionsByBlockHashRIBSZ from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in v_join_split (list)
        _items = []
        if self.v_join_split:
            for _item in self.v_join_split:
                if _item:
                    _items.append(_item.to_dict())
            _dict['vJoinSplit'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in v_shielded_output (list)
        _items = []
        if self.v_shielded_output:
            for _item in self.v_shielded_output:
                if _item:
                    _items.append(_item.to_dict())
            _dict['vShieldedOutput'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in v_shielded_spend (list)
        _items = []
        if self.v_shielded_spend:
            for _item in self.v_shielded_spend:
                if _item:
                    _items.append(_item.to_dict())
            _dict['vShieldedSpend'] = _items
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
    def from_dict(cls, obj: dict) -> ListTransactionsByBlockHashRIBSZ:
        """Create an instance of ListTransactionsByBlockHashRIBSZ from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ListTransactionsByBlockHashRIBSZ.parse_obj(obj)

        _obj = ListTransactionsByBlockHashRIBSZ.parse_obj({
            "binding_sig": obj.get("bindingSig"),
            "expiry_height": obj.get("expiryHeight"),
            "join_split_pub_key": obj.get("joinSplitPubKey"),
            "join_split_sig": obj.get("joinSplitSig"),
            "locktime": obj.get("locktime"),
            "overwintered": obj.get("overwintered"),
            "size": obj.get("size"),
            "v_join_split": [ListTransactionsByBlockHashRIBSZVJoinSplitInner.from_dict(_item) for _item in obj.get("vJoinSplit")] if obj.get("vJoinSplit") is not None else None,
            "v_shielded_output": [GetTransactionDetailsByTransactionIDRIBSZVShieldedOutputInner.from_dict(_item) for _item in obj.get("vShieldedOutput")] if obj.get("vShieldedOutput") is not None else None,
            "v_shielded_spend": [GetTransactionDetailsByTransactionIDRIBSZVShieldedSpendInner.from_dict(_item) for _item in obj.get("vShieldedSpend")] if obj.get("vShieldedSpend") is not None else None,
            "value_balance": obj.get("valueBalance"),
            "version": obj.get("version"),
            "version_group_id": obj.get("versionGroupId"),
            "vin": [ListTransactionsByBlockHashRIBSZVinInner.from_dict(_item) for _item in obj.get("vin")] if obj.get("vin") is not None else None,
            "vout": [GetTransactionDetailsByTransactionIDRIBSZVoutInner.from_dict(_item) for _item in obj.get("vout")] if obj.get("vout") is not None else None
        })
        return _obj

