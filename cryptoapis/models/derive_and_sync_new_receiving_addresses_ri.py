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



from pydantic import BaseModel, Field, StrictStr, validator

class DeriveAndSyncNewReceivingAddressesRI(BaseModel):
    """
    DeriveAndSyncNewReceivingAddressesRI
    """
    address: StrictStr = Field(..., description="Represents the public address, which is a compressed and shortened form of a public key.")
    address_format: StrictStr = Field(..., alias="addressFormat", description="Represents the format of the address.")
    address_type: StrictStr = Field(..., alias="addressType", description="Defines the address type.")
    derivation_type: StrictStr = Field(..., alias="derivationType", description="Represents the derivation type")
    index: StrictStr = Field(..., description="Represents the output index. It refers to the UTXO sequence in the transaction outputs (vout).")
    __properties = ["address", "addressFormat", "addressType", "derivationType", "index"]

    @validator('address_type')
    def address_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('change'):
            raise ValueError("must be one of enum values ('change')")
        return value

    @validator('derivation_type')
    def derivation_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('account', 'bip32'):
            raise ValueError("must be one of enum values ('account', 'bip32')")
        return value

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
    def from_json(cls, json_str: str) -> DeriveAndSyncNewReceivingAddressesRI:
        """Create an instance of DeriveAndSyncNewReceivingAddressesRI from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DeriveAndSyncNewReceivingAddressesRI:
        """Create an instance of DeriveAndSyncNewReceivingAddressesRI from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DeriveAndSyncNewReceivingAddressesRI.parse_obj(obj)

        _obj = DeriveAndSyncNewReceivingAddressesRI.parse_obj({
            "address": obj.get("address"),
            "address_format": obj.get("addressFormat"),
            "address_type": obj.get("addressType"),
            "derivation_type": obj.get("derivationType"),
            "index": obj.get("index")
        })
        return _obj

