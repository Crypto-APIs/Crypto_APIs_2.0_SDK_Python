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
from cryptoapis.models.prepare_a_fungible_token_transfer_from_address_ribs import PrepareAFungibleTokenTransferFromAddressRIBS

class PrepareAFungibleTokenTransferFromAddressRI(BaseModel):
    """
    PrepareAFungibleTokenTransferFromAddressRI
    """
    amount: StrictStr = Field(..., description="Representation of the amount to be transferred")
    nonce: Optional[StrictStr] = Field(None, description="Represents the sequential running number for an address, starting from 0 for the first transaction. E.g., if the nonce of a transaction is 10, it would be the 11th transaction sent from the sender's address.")
    recipient: StrictStr = Field(..., description="The address which receives this transaction. In UTXO-based protocols like Bitcoin there could be several senders while in account-based protocols like Ethereum there is always only one recipient.")
    sender: StrictStr = Field(..., description="Represents the address which sends this transaction. In UTXO-based protocols like Bitcoin there could be several senders while in account-based protocols like Ethereum there is always only one sender.")
    blockchain_specific: PrepareAFungibleTokenTransferFromAddressRIBS = Field(..., alias="blockchainSpecific")
    __properties = ["amount", "nonce", "recipient", "sender", "blockchainSpecific"]

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
    def from_json(cls, json_str: str) -> PrepareAFungibleTokenTransferFromAddressRI:
        """Create an instance of PrepareAFungibleTokenTransferFromAddressRI from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of blockchain_specific
        if self.blockchain_specific:
            _dict['blockchainSpecific'] = self.blockchain_specific.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PrepareAFungibleTokenTransferFromAddressRI:
        """Create an instance of PrepareAFungibleTokenTransferFromAddressRI from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PrepareAFungibleTokenTransferFromAddressRI.parse_obj(obj)

        _obj = PrepareAFungibleTokenTransferFromAddressRI.parse_obj({
            "amount": obj.get("amount"),
            "nonce": obj.get("nonce"),
            "recipient": obj.get("recipient"),
            "sender": obj.get("sender"),
            "blockchain_specific": PrepareAFungibleTokenTransferFromAddressRIBS.from_dict(obj.get("blockchainSpecific")) if obj.get("blockchainSpecific") is not None else None
        })
        return _obj
