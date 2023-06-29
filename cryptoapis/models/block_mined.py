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
from cryptoapis.models.block_mined_data import BlockMinedData

class BlockMined(BaseModel):
    """
    BlockMined
    """
    api_version: StrictStr = Field(..., alias="apiVersion", description="Specifies the version of the API that incorporates this endpoint.")
    reference_id: StrictStr = Field(..., alias="referenceId", description="Represents a unique identifier that serves as reference to the specific request which prompts a callback, e.g. Blockchain Events Subscription, Blockchain Automation, etc.")
    idempotency_key: StrictStr = Field(..., alias="idempotencyKey", description="Specifies a unique ID generated by the system and attached to each callback. It is used by the server to recognize consecutive requests with the same data with the purpose not to perform the same operation twice.")
    data: BlockMinedData = Field(...)
    __properties = ["apiVersion", "referenceId", "idempotencyKey", "data"]

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
    def from_json(cls, json_str: str) -> BlockMined:
        """Create an instance of BlockMined from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of data
        if self.data:
            _dict['data'] = self.data.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> BlockMined:
        """Create an instance of BlockMined from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return BlockMined.parse_obj(obj)

        _obj = BlockMined.parse_obj({
            "api_version": obj.get("apiVersion"),
            "reference_id": obj.get("referenceId"),
            "idempotency_key": obj.get("idempotencyKey"),
            "data": BlockMinedData.from_dict(obj.get("data")) if obj.get("data") is not None else None
        })
        return _obj

