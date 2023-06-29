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


from typing import Optional
from pydantic import BaseModel, Field, StrictStr
from cryptoapis.models.list_zilliqa_transactions_by_block_hash_e403 import ListZilliqaTransactionsByBlockHashE403

class ListZilliqaTransactionsByBlockHash403Response(BaseModel):
    """
    ListZilliqaTransactionsByBlockHash403Response
    """
    api_version: StrictStr = Field(..., alias="apiVersion", description="Specifies the version of the API that incorporates this endpoint.")
    request_id: StrictStr = Field(..., alias="requestId", description="Defines the ID of the request. The `requestId` is generated by Crypto APIs and it's unique for every request.")
    context: Optional[StrictStr] = Field(None, description="In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user.")
    error: ListZilliqaTransactionsByBlockHashE403 = Field(...)
    __properties = ["apiVersion", "requestId", "context", "error"]

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
    def from_json(cls, json_str: str) -> ListZilliqaTransactionsByBlockHash403Response:
        """Create an instance of ListZilliqaTransactionsByBlockHash403Response from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of error
        if self.error:
            _dict['error'] = self.error.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ListZilliqaTransactionsByBlockHash403Response:
        """Create an instance of ListZilliqaTransactionsByBlockHash403Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ListZilliqaTransactionsByBlockHash403Response.parse_obj(obj)

        _obj = ListZilliqaTransactionsByBlockHash403Response.parse_obj({
            "api_version": obj.get("apiVersion"),
            "request_id": obj.get("requestId"),
            "context": obj.get("context"),
            "error": ListZilliqaTransactionsByBlockHashE403.from_dict(obj.get("error")) if obj.get("error") is not None else None
        })
        return _obj

