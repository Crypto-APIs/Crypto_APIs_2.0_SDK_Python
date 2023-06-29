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

class CreateCoinsTransactionRequestFromAddressRBDataItem(BaseModel):
    """
    CreateCoinsTransactionRequestFromAddressRBDataItem
    """
    amount: StrictStr = Field(..., description="Represents the specific amount of the transaction.")
    callback_secret_key: Optional[StrictStr] = Field(None, alias="callbackSecretKey", description="Represents the Secret Key value provided by the customer. This field is used for security purposes during the callback notification, in order to prove the sender of the callback as Crypto APIs. For more information please see our [Documentation](https://developers.cryptoapis.io/technical-documentation/general-information/callbacks#callback-security).")
    callback_url: Optional[StrictStr] = Field(None, alias="callbackUrl", description="Represents the URL that is set by the customer where the callback will be received at. The callback notification will be received only if and when the event occurs. `We support ONLY httpS type of protocol`.")
    fee_priority: StrictStr = Field(..., alias="feePriority", description="Represents the fee priority of the automation, whether it is \"slow\", \"standard\" or \"fast\".")
    note: Optional[StrictStr] = Field(None, description="Represents an optional note to add a free text in, explaining or providing additional detail on the transaction request.")
    recipient_address: StrictStr = Field(..., alias="recipientAddress", description="Defines the specific recipient address for the transaction. For XRP we also support the X-address format.")
    __properties = ["amount", "callbackSecretKey", "callbackUrl", "feePriority", "note", "recipientAddress"]

    @validator('fee_priority')
    def fee_priority_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('slow', 'standard', 'fast'):
            raise ValueError("must be one of enum values ('slow', 'standard', 'fast')")
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
    def from_json(cls, json_str: str) -> CreateCoinsTransactionRequestFromAddressRBDataItem:
        """Create an instance of CreateCoinsTransactionRequestFromAddressRBDataItem from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CreateCoinsTransactionRequestFromAddressRBDataItem:
        """Create an instance of CreateCoinsTransactionRequestFromAddressRBDataItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CreateCoinsTransactionRequestFromAddressRBDataItem.parse_obj(obj)

        _obj = CreateCoinsTransactionRequestFromAddressRBDataItem.parse_obj({
            "amount": obj.get("amount"),
            "callback_secret_key": obj.get("callbackSecretKey"),
            "callback_url": obj.get("callbackUrl"),
            "fee_priority": obj.get("feePriority"),
            "note": obj.get("note"),
            "recipient_address": obj.get("recipientAddress")
        })
        return _obj

