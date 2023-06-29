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

class GetTransactionDetailsByTransactionIDRIBSZVShieldedSpendInner(BaseModel):
    """
    GetTransactionDetailsByTransactionIDRIBSZVShieldedSpendInner
    """
    anchor: StrictStr = Field(..., description="Defines a Merkle tree root of a note commitment tree which uniquely identifies a note commitment tree state given the assumed security properties of the Merkle tree’s  hash function.")
    cv: StrictStr = Field(..., description="Defines a value commitment to the value of the input note.")
    nullifier: StrictStr = Field(..., description="Represents a sequence of nullifiers of the input notes.")
    proof: StrictStr = Field(..., description="Represents the proof.")
    rk: StrictStr = Field(..., description="Represents the randomized validating key for spendAuthSig.")
    spend_auth_sig: StrictStr = Field(..., alias="spendAuthSig", description="Used to prove knowledge of the spending key authorizing spending of an input note.")
    __properties = ["anchor", "cv", "nullifier", "proof", "rk", "spendAuthSig"]

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
    def from_json(cls, json_str: str) -> GetTransactionDetailsByTransactionIDRIBSZVShieldedSpendInner:
        """Create an instance of GetTransactionDetailsByTransactionIDRIBSZVShieldedSpendInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GetTransactionDetailsByTransactionIDRIBSZVShieldedSpendInner:
        """Create an instance of GetTransactionDetailsByTransactionIDRIBSZVShieldedSpendInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GetTransactionDetailsByTransactionIDRIBSZVShieldedSpendInner.parse_obj(obj)

        _obj = GetTransactionDetailsByTransactionIDRIBSZVShieldedSpendInner.parse_obj({
            "anchor": obj.get("anchor"),
            "cv": obj.get("cv"),
            "nullifier": obj.get("nullifier"),
            "proof": obj.get("proof"),
            "rk": obj.get("rk"),
            "spend_auth_sig": obj.get("spendAuthSig")
        })
        return _obj

