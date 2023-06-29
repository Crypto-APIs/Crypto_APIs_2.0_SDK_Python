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

class GetBlockDetailsByBlockHeightRIBSBSC(BaseModel):
    """
    Binance Smart Chain
    """
    difficulty: StrictStr = Field(..., description="Represents a mathematical value of how hard it is to find a valid hash for this block.")
    extra_data: StrictStr = Field(..., alias="extraData", description="Represents any data that can be included by the miner in the block.")
    gas_limit: StrictStr = Field(..., alias="gasLimit", description="Defines the total gas limit of all transactions in the block.")
    gas_used: StrictStr = Field(..., alias="gasUsed", description="Represents the total amount of gas used by all transactions in this block.")
    mined_in_seconds: StrictInt = Field(..., alias="minedInSeconds", description="Specifies the amount of time required for the block to be mined in seconds.")
    nonce: StrictStr = Field(..., description="Represents a random value that can be adjusted to satisfy the Proof of Work.")
    sha3_uncles: StrictStr = Field(..., alias="sha3Uncles", description="Defines the combined hash of all uncles for a given parent.")
    size: StrictInt = Field(..., description="Represents the total size of the block in Bytes.")
    total_difficulty: StrictStr = Field(..., alias="totalDifficulty", description="Defines the total difficulty of the chain until this block, i.e. how difficult it is for a specific miner to mine a new block.")
    __properties = ["difficulty", "extraData", "gasLimit", "gasUsed", "minedInSeconds", "nonce", "sha3Uncles", "size", "totalDifficulty"]

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
    def from_json(cls, json_str: str) -> GetBlockDetailsByBlockHeightRIBSBSC:
        """Create an instance of GetBlockDetailsByBlockHeightRIBSBSC from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GetBlockDetailsByBlockHeightRIBSBSC:
        """Create an instance of GetBlockDetailsByBlockHeightRIBSBSC from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GetBlockDetailsByBlockHeightRIBSBSC.parse_obj(obj)

        _obj = GetBlockDetailsByBlockHeightRIBSBSC.parse_obj({
            "difficulty": obj.get("difficulty"),
            "extra_data": obj.get("extraData"),
            "gas_limit": obj.get("gasLimit"),
            "gas_used": obj.get("gasUsed"),
            "mined_in_seconds": obj.get("minedInSeconds"),
            "nonce": obj.get("nonce"),
            "sha3_uncles": obj.get("sha3Uncles"),
            "size": obj.get("size"),
            "total_difficulty": obj.get("totalDifficulty")
        })
        return _obj

