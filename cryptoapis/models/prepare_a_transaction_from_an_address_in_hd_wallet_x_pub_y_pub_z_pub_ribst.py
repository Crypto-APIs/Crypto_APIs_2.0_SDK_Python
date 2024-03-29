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
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr
from cryptoapis.models.prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_ribst_raw_data import PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRIBSTRawData

class PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRIBST(BaseModel):
    """
    Tron
    """
    data: StrictStr = Field(..., description="String representation of the data")
    derivation_index: StrictStr = Field(..., alias="derivationIndex", description="Representation of the derivation index of the xpub address")
    expiration: StrictInt = Field(..., description="Rrepresentation of the expiration value")
    raw_data: Optional[PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRIBSTRawData] = Field(None, alias="rawData")
    raw_data_hex: StrictStr = Field(..., alias="rawDataHex", description="Representation of the raw data in hex format")
    recipient: StrictStr = Field(..., description="Rrepresentation of the recipients' address")
    ref_block_bytes: StrictStr = Field(..., alias="refBlockBytes", description="Representation of the block bytes")
    ref_block_hash: StrictStr = Field(..., alias="refBlockHash", description="Representation of the block hash refference")
    sender: StrictStr = Field(..., description="Representation of the sender")
    timestamp: StrictInt = Field(..., description="Representation of the timestamp")
    transaction_id: StrictStr = Field(..., alias="transactionId", description="Represents the reference transaction identifier.")
    type: StrictStr = Field(..., description="Representation of the transfer type.")
    type_url: StrictStr = Field(..., alias="typeUrl", description="Representation of the URL")
    unit: StrictStr = Field(..., description="Represents the unit of the amount to be sent.")
    visible: StrictBool = Field(..., description="Representation of the address visibility")
    __properties = ["data", "derivationIndex", "expiration", "rawData", "rawDataHex", "recipient", "refBlockBytes", "refBlockHash", "sender", "timestamp", "transactionId", "type", "typeUrl", "unit", "visible"]

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
    def from_json(cls, json_str: str) -> PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRIBST:
        """Create an instance of PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRIBST from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of raw_data
        if self.raw_data:
            _dict['rawData'] = self.raw_data.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRIBST:
        """Create an instance of PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRIBST from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRIBST.parse_obj(obj)

        _obj = PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRIBST.parse_obj({
            "data": obj.get("data"),
            "derivation_index": obj.get("derivationIndex"),
            "expiration": obj.get("expiration"),
            "raw_data": PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRIBSTRawData.from_dict(obj.get("rawData")) if obj.get("rawData") is not None else None,
            "raw_data_hex": obj.get("rawDataHex"),
            "recipient": obj.get("recipient"),
            "ref_block_bytes": obj.get("refBlockBytes"),
            "ref_block_hash": obj.get("refBlockHash"),
            "sender": obj.get("sender"),
            "timestamp": obj.get("timestamp"),
            "transaction_id": obj.get("transactionId"),
            "type": obj.get("type"),
            "type_url": obj.get("typeUrl"),
            "unit": obj.get("unit"),
            "visible": obj.get("visible")
        })
        return _obj

