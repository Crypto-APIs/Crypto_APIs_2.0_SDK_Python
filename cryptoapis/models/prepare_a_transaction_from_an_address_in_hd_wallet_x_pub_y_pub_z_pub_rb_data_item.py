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
from cryptoapis.models.prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_rb_data_item_fee import PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRBDataItemFee

class PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRBDataItem(BaseModel):
    """
    PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRBDataItem
    """
    additional_data: Optional[StrictStr] = Field(None, alias="additionalData", description="Representation of the additional data.")
    amount: StrictStr = Field(..., description="Representation of the amount of the transaction")
    recipient: StrictStr = Field(..., description="Represents a list of recipient addresses with the respective amounts. In account-based protocols like Ethereum there is only one address in this list.")
    sender: StrictStr = Field(..., description="Represents a  sender address with the respective amount. In account-based protocols like Ethereum there is only one address in this list.")
    xpub: StrictStr = Field(..., description="Defines the account extended publicly known key which is used to derive all child public keys.")
    fee: PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRBDataItemFee = Field(...)
    nonce: Optional[StrictStr] = Field(None, description="Representation of the nonce value")
    transaction_type: Optional[StrictStr] = Field('gas-fee-market-transaction', alias="transactionType", description="Representation of the transaction type. For Ethereum-Classic and Binance Smart Chain there is no need to provide \"transactionType\" in the request.")
    sequence: StrictStr = Field(..., description="String representation of the sequence")
    __properties = ["additionalData", "amount", "recipient", "sender", "xpub", "fee", "nonce", "transactionType", "sequence"]

    @validator('transaction_type')
    def transaction_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

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
    def from_json(cls, json_str: str) -> PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRBDataItem:
        """Create an instance of PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRBDataItem from a JSON string"""
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
    def from_dict(cls, obj: dict) -> PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRBDataItem:
        """Create an instance of PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRBDataItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRBDataItem.parse_obj(obj)

        _obj = PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRBDataItem.parse_obj({
            "additional_data": obj.get("additionalData"),
            "amount": obj.get("amount"),
            "recipient": obj.get("recipient"),
            "sender": obj.get("sender"),
            "xpub": obj.get("xpub"),
            "fee": PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRBDataItemFee.from_dict(obj.get("fee")) if obj.get("fee") is not None else None,
            "nonce": obj.get("nonce"),
            "transaction_type": obj.get("transactionType") if obj.get("transactionType") is not None else 'gas-fee-market-transaction',
            "sequence": obj.get("sequence")
        })
        return _obj

