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
from pydantic import BaseModel, Field, StrictBool, StrictStr

class NewUnconfirmedCoinsTransactionsRBDataItem(BaseModel):
    """
    NewUnconfirmedCoinsTransactionsRBDataItem
    """
    address: StrictStr = Field(..., description="Represents the address of the transaction, per which the result is returned.")
    allow_duplicates: Optional[StrictBool] = Field(False, alias="allowDuplicates", description="Specifies a flag that permits or denies the creation of duplicate addresses.")
    callback_secret_key: Optional[StrictStr] = Field(None, alias="callbackSecretKey", description="Represents the Secret Key value provided by the customer. This field is used for security purposes during the callback notification, in order to prove the sender of the callback as Crypto APIs 2.0. For more information please see our [Documentation](https://developers.cryptoapis.io/technical-documentation/general-information/callbacks#callback-security).")
    callback_url: StrictStr = Field(..., alias="callbackUrl", description="Represents the URL that is set by the customer where the callback will be received at. The callback notification will be received only if and when the event occurs. `We support ONLY httpS type of protocol`.")
    __properties = ["address", "allowDuplicates", "callbackSecretKey", "callbackUrl"]

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
    def from_json(cls, json_str: str) -> NewUnconfirmedCoinsTransactionsRBDataItem:
        """Create an instance of NewUnconfirmedCoinsTransactionsRBDataItem from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> NewUnconfirmedCoinsTransactionsRBDataItem:
        """Create an instance of NewUnconfirmedCoinsTransactionsRBDataItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return NewUnconfirmedCoinsTransactionsRBDataItem.parse_obj(obj)

        _obj = NewUnconfirmedCoinsTransactionsRBDataItem.parse_obj({
            "address": obj.get("address"),
            "allow_duplicates": obj.get("allowDuplicates") if obj.get("allowDuplicates") is not None else False,
            "callback_secret_key": obj.get("callbackSecretKey"),
            "callback_url": obj.get("callbackUrl")
        })
        return _obj

