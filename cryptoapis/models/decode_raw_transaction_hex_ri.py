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
from cryptoapis.models.decode_raw_transaction_hex_ris import DecodeRawTransactionHexRIS

class DecodeRawTransactionHexRI(BaseModel):
    """
    DecodeRawTransactionHexRI
    """
    blockchain_speficic_data: DecodeRawTransactionHexRIS = Field(..., alias="blockchainSpeficicData")
    size: StrictInt = Field(..., description="Represents the total size of this transaction.")
    transaction_id: StrictStr = Field(..., alias="transactionId", description="Represents the decoded transaction hex.")
    __properties = ["blockchainSpeficicData", "size", "transactionId"]

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
    def from_json(cls, json_str: str) -> DecodeRawTransactionHexRI:
        """Create an instance of DecodeRawTransactionHexRI from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of blockchain_speficic_data
        if self.blockchain_speficic_data:
            _dict['blockchainSpeficicData'] = self.blockchain_speficic_data.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DecodeRawTransactionHexRI:
        """Create an instance of DecodeRawTransactionHexRI from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DecodeRawTransactionHexRI.parse_obj(obj)

        _obj = DecodeRawTransactionHexRI.parse_obj({
            "blockchain_speficic_data": DecodeRawTransactionHexRIS.from_dict(obj.get("blockchainSpeficicData")) if obj.get("blockchainSpeficicData") is not None else None,
            "size": obj.get("size"),
            "transaction_id": obj.get("transactionId")
        })
        return _obj
