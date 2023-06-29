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

class ListHDWalletXPubYPubZPubUTXOsRI(BaseModel):
    """
    ListHDWalletXPubYPubZPubUTXOsRI
    """
    address: StrictStr = Field(..., description="Represents the public address, which is a compressed and shortened form of a public key.")
    address_path: StrictStr = Field(..., alias="addressPath", description="Defines a data which tells a Hierarchical Deterministic wallet how to derive a specific key within a tree of keys.")
    amount: StrictStr = Field(..., description="Represents the UTXO amount value.")
    derivation: StrictStr = Field(..., description="The way how the HD walled derives, for example when the type is ACCOUNT, it derives change and receive addresses while when the type is BIP32 it derives directly.")
    index: StrictInt = Field(..., description="Represents the output index. It refers to the UTXO sequence in the transaction outputs (vout).")
    is_available: StrictBool = Field(..., alias="isAvailable", description="Represents if the UTXO has been used from another unconfirmed transaction. If it is - the value will be \"false\".")
    is_confirmed: StrictBool = Field(..., alias="isConfirmed", description="Represents the state of the transaction whether it is confirmed or not confirmed.")
    reference_id: StrictStr = Field(..., alias="referenceId", description="Represents the reference id of the record. It may be used for the startingAfter pagination attribute.")
    transaction_id: StrictStr = Field(..., alias="transactionId", description="Represents the unique identifier of a transaction, i.e. it could be transactionId in UTXO-based protocols like Bitcoin, and transaction hash in Ethereum blockchain.")
    __properties = ["address", "addressPath", "amount", "derivation", "index", "isAvailable", "isConfirmed", "referenceId", "transactionId"]

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
    def from_json(cls, json_str: str) -> ListHDWalletXPubYPubZPubUTXOsRI:
        """Create an instance of ListHDWalletXPubYPubZPubUTXOsRI from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ListHDWalletXPubYPubZPubUTXOsRI:
        """Create an instance of ListHDWalletXPubYPubZPubUTXOsRI from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ListHDWalletXPubYPubZPubUTXOsRI.parse_obj(obj)

        _obj = ListHDWalletXPubYPubZPubUTXOsRI.parse_obj({
            "address": obj.get("address"),
            "address_path": obj.get("addressPath"),
            "amount": obj.get("amount"),
            "derivation": obj.get("derivation"),
            "index": obj.get("index"),
            "is_available": obj.get("isAvailable"),
            "is_confirmed": obj.get("isConfirmed"),
            "reference_id": obj.get("referenceId"),
            "transaction_id": obj.get("transactionId")
        })
        return _obj

