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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conlist, validator
from cryptoapis.models.prepare_autxo_based_transaction_from_hd_wallet_x_pub_y_pub_z_pub_rb_data_item_fee import PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRBDataItemFee
from cryptoapis.models.prepare_autxo_based_transaction_from_hd_wallet_x_pub_y_pub_z_pub_rb_data_item_recipients_inner import PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRBDataItemRecipientsInner

class PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRBDataItem(BaseModel):
    """
    PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRBDataItem
    """
    additional_data: Optional[StrictStr] = Field(None, alias="additionalData", description="Representation of the additional data.")
    locktime: Optional[StrictInt] = Field(None, description="Represents the time at which a particular transaction can be added to the blockchain.")
    xpub: StrictStr = Field(..., description="Defines the account extended publicly known key which is used to derive all child public keys.")
    fee: PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRBDataItemFee = Field(...)
    prepare_strategy: Optional[StrictStr] = Field(None, alias="prepareStrategy", description="Representation of the transaction's strategy type")
    recipients: conlist(PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRBDataItemRecipientsInner) = Field(..., description="Object Array representation of transaction receivers")
    replaceable: Optional[StrictBool] = Field(None, description="Representation of whether the transaction is replaceable. This is an Optional attribute that is not supported for Dogecoin, Dash and Bitcoin-Cash.")
    __properties = ["additionalData", "locktime", "xpub", "fee", "prepareStrategy", "recipients", "replaceable"]

    @validator('prepare_strategy')
    def prepare_strategy_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('none', 'minimize-dust', 'optimize-size'):
            raise ValueError("must be one of enum values ('none', 'minimize-dust', 'optimize-size')")
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
    def from_json(cls, json_str: str) -> PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRBDataItem:
        """Create an instance of PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRBDataItem from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in recipients (list)
        _items = []
        if self.recipients:
            for _item in self.recipients:
                if _item:
                    _items.append(_item.to_dict())
            _dict['recipients'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRBDataItem:
        """Create an instance of PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRBDataItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRBDataItem.parse_obj(obj)

        _obj = PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRBDataItem.parse_obj({
            "additional_data": obj.get("additionalData"),
            "locktime": obj.get("locktime"),
            "xpub": obj.get("xpub"),
            "fee": PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRBDataItemFee.from_dict(obj.get("fee")) if obj.get("fee") is not None else None,
            "prepare_strategy": obj.get("prepareStrategy"),
            "recipients": [PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRBDataItemRecipientsInner.from_dict(_item) for _item in obj.get("recipients")] if obj.get("recipients") is not None else None,
            "replaceable": obj.get("replaceable")
        })
        return _obj

