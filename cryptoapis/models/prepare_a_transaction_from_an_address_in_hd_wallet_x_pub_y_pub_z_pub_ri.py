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
from cryptoapis.models.prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_ribs import PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRIBS

class PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRI(BaseModel):
    """
    PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRI
    """
    amount: StrictStr = Field(..., description="Representation of the amount of the transaction")
    recipient: StrictStr = Field(..., description="Represents a recipient addresses. In account-based protocols like Ethereum there is only one address in this list.")
    sender: StrictStr = Field(..., description="Represents a sender address with the respective amount. In account-based protocols like Ethereum there is only one address in this list.")
    sig_hash: StrictStr = Field(..., alias="sigHash", description="Representation of the hash that should be signed.")
    blockchain_specific: PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRIBS = Field(..., alias="blockchainSpecific")
    __properties = ["amount", "recipient", "sender", "sigHash", "blockchainSpecific"]

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
    def from_json(cls, json_str: str) -> PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRI:
        """Create an instance of PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRI from a JSON string"""
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
    def from_dict(cls, obj: dict) -> PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRI:
        """Create an instance of PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRI from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRI.parse_obj(obj)

        _obj = PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRI.parse_obj({
            "amount": obj.get("amount"),
            "recipient": obj.get("recipient"),
            "sender": obj.get("sender"),
            "sig_hash": obj.get("sigHash"),
            "blockchain_specific": PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRIBS.from_dict(obj.get("blockchainSpecific")) if obj.get("blockchainSpecific") is not None else None
        })
        return _obj

