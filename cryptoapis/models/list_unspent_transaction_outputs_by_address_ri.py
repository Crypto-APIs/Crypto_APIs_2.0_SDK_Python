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



from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr

class ListUnspentTransactionOutputsByAddressRI(BaseModel):
    """
    ListUnspentTransactionOutputsByAddressRI
    """
    address: StrictStr = Field(..., description="Represents the address that has unspend funds per which the result is returned.")
    amount: StrictStr = Field(..., description="Represents the sent/received amount.")
    index: StrictInt = Field(..., description="Represents the index position of the transaction in the block.")
    is_available: StrictBool = Field(..., alias="isAvailable", description="Represents if the UTXO has been used from another unconfirmed transaction. If it is - the value will be \"false\".")
    is_confirmed: StrictBool = Field(..., alias="isConfirmed", description="Represents the state of the transaction whether it is confirmed or not confirmed.")
    timestamp: StrictInt = Field(..., description="Defines the exact date/time in Unix Timestamp when this transaction was mined, confirmed or first seen in Mempool, if it is unconfirmed.")
    transaction_id: StrictStr = Field(..., alias="transactionId", description="Represents the unique identifier of a transaction, i.e. it could be `transactionId` in UTXO-based protocols like Bitcoin, and transaction `hash` in Ethereum blockchain.")
    __properties = ["address", "amount", "index", "isAvailable", "isConfirmed", "timestamp", "transactionId"]

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
    def from_json(cls, json_str: str) -> ListUnspentTransactionOutputsByAddressRI:
        """Create an instance of ListUnspentTransactionOutputsByAddressRI from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ListUnspentTransactionOutputsByAddressRI:
        """Create an instance of ListUnspentTransactionOutputsByAddressRI from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ListUnspentTransactionOutputsByAddressRI.parse_obj(obj)

        _obj = ListUnspentTransactionOutputsByAddressRI.parse_obj({
            "address": obj.get("address"),
            "amount": obj.get("amount"),
            "index": obj.get("index"),
            "is_available": obj.get("isAvailable"),
            "is_confirmed": obj.get("isConfirmed"),
            "timestamp": obj.get("timestamp"),
            "transaction_id": obj.get("transactionId")
        })
        return _obj
