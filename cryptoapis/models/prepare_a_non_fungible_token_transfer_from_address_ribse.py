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
from pydantic import BaseModel, Field, StrictStr, validator
from cryptoapis.models.prepare_a_non_fungible_token_transfer_from_address_ribse_fee import PrepareANonFungibleTokenTransferFromAddressRIBSEFee

class PrepareANonFungibleTokenTransferFromAddressRIBSE(BaseModel):
    """
    Ethereum
    """
    data_hex: Optional[StrictStr] = Field(None, alias="dataHex", description="0x0079006f00750072004100640064006900740069006f006e0061006c00440061007400610048006500720065")
    nonce: Optional[StrictStr] = Field(None, description="Represents the sequential running number for an address, starting from 0 for the first transaction. E.g., if the nonce of a transaction is 10, it would be the 11th transaction sent from the sender's address.")
    sig_hash: StrictStr = Field(..., alias="sigHash", description="Representation of the hash that should be signed")
    fee: PrepareANonFungibleTokenTransferFromAddressRIBSEFee = Field(...)
    transaction_type: StrictStr = Field(..., alias="transactionType", description="Representation of the transaction type")
    __properties = ["dataHex", "nonce", "sigHash", "fee", "transactionType"]

    @validator('transaction_type')
    def transaction_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('legacy-transaction', 'access-list-transaction', 'gas-fee-market-transaction'):
            raise ValueError("must be one of enum values ('legacy-transaction', 'access-list-transaction', 'gas-fee-market-transaction')")
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
    def from_json(cls, json_str: str) -> PrepareANonFungibleTokenTransferFromAddressRIBSE:
        """Create an instance of PrepareANonFungibleTokenTransferFromAddressRIBSE from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of fee
        if self.fee:
            _dict['fee'] = self.fee.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PrepareANonFungibleTokenTransferFromAddressRIBSE:
        """Create an instance of PrepareANonFungibleTokenTransferFromAddressRIBSE from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PrepareANonFungibleTokenTransferFromAddressRIBSE.parse_obj(obj)

        _obj = PrepareANonFungibleTokenTransferFromAddressRIBSE.parse_obj({
            "data_hex": obj.get("dataHex"),
            "nonce": obj.get("nonce"),
            "sig_hash": obj.get("sigHash"),
            "fee": PrepareANonFungibleTokenTransferFromAddressRIBSEFee.from_dict(obj.get("fee")) if obj.get("fee") is not None else None,
            "transaction_type": obj.get("transactionType")
        })
        return _obj

