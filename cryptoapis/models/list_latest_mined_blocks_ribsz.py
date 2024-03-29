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



from pydantic import BaseModel, Field, StrictInt, StrictStr

class ListLatestMinedBlocksRIBSZ(BaseModel):
    """
    Zcash
    """
    bits: StrictStr = Field(..., description="Represents a specific sub-unit of Zcash. Bits have two-decimal precision")
    chainwork: StrictStr = Field(..., description="Represents a hexadecimal number of all the hashes necessary to produce the current chain. E.g., when converting 0000000000000000000000000000000000000000000086859f7a841475b236fd to a decimal you get 635262017308958427068157 hashes, or 635262 exahashes.")
    difficulty: StrictStr = Field(..., description="Represents a mathematical value of how hard it is to find a valid hash for this block.")
    merkle_root: StrictStr = Field(..., alias="merkleRoot", description="Defines the single and final (root) node of a Merkle tree. It is the combined hash of all transactions' hashes that are part of a blockchain block.")
    nonce: StrictStr = Field(..., description="Represents a random value that can be adjusted to satisfy the proof of work")
    size: StrictInt = Field(..., description="Represents the total size of the block in Bytes.")
    version: StrictInt = Field(..., description="Represents the transaction version number.")
    __properties = ["bits", "chainwork", "difficulty", "merkleRoot", "nonce", "size", "version"]

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
    def from_json(cls, json_str: str) -> ListLatestMinedBlocksRIBSZ:
        """Create an instance of ListLatestMinedBlocksRIBSZ from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ListLatestMinedBlocksRIBSZ:
        """Create an instance of ListLatestMinedBlocksRIBSZ from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ListLatestMinedBlocksRIBSZ.parse_obj(obj)

        _obj = ListLatestMinedBlocksRIBSZ.parse_obj({
            "bits": obj.get("bits"),
            "chainwork": obj.get("chainwork"),
            "difficulty": obj.get("difficulty"),
            "merkle_root": obj.get("merkleRoot"),
            "nonce": obj.get("nonce"),
            "size": obj.get("size"),
            "version": obj.get("version")
        })
        return _obj

