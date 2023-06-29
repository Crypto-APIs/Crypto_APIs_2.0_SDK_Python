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
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist, validator
from cryptoapis.models.create_coins_transaction_request_from_address_ri_recipients_inner import CreateCoinsTransactionRequestFromAddressRIRecipientsInner
from cryptoapis.models.create_coins_transaction_request_from_address_ri_senders import CreateCoinsTransactionRequestFromAddressRISenders

class CreateCoinsTransactionRequestFromAddressRI(BaseModel):
    """
    CreateCoinsTransactionRequestFromAddressRI
    """
    address_tag: Optional[StrictInt] = Field(None, alias="addressTag", description="Defines a specific Tag that is an additional XRP address feature. It helps identify a transaction recipient beyond a wallet address. The tag that was encoded into the x-Address along with the Source Classic Address.")
    callback_secret_key: Optional[StrictStr] = Field(None, alias="callbackSecretKey", description="Represents the Secret Key value provided by the customer. This field is used for security purposes during the callback notification, in order to prove the sender of the callback as Crypto APIs. For more information please see our [Documentation](https://developers.cryptoapis.io/technical-documentation/general-information/callbacks#callback-security).")
    callback_url: Optional[StrictStr] = Field(None, alias="callbackUrl", description="Represents the URL that is set by the customer where the callback will be received at. The callback notification will be received only if and when the event occurs. `We support ONLY httpS type of protocol`.")
    classic_address: Optional[StrictStr] = Field(None, alias="classicAddress", description="Represents the public address, which is a compressed and shortened form of a public key. The classic address is shown when the source address is an x-Address.")
    fee_priority: StrictStr = Field(..., alias="feePriority", description="Represents the fee priority of the automation, whether it is \"slow\", \"standard\" or \"fast\".")
    note: Optional[StrictStr] = Field(None, description="Represents an optional note to add a free text in, explaining or providing additional detail on the transaction request.")
    recipients: conlist(CreateCoinsTransactionRequestFromAddressRIRecipientsInner) = Field(..., description="Defines the destination for the transaction, i.e. the recipient(s).")
    senders: CreateCoinsTransactionRequestFromAddressRISenders = Field(...)
    transaction_request_id: StrictStr = Field(..., alias="transactionRequestId", description="Represents a unique identifier of the transaction request (the request sent to make a transaction), which helps in identifying which callback and which `referenceId` concern that specific transaction request.")
    transaction_request_status: StrictStr = Field(..., alias="transactionRequestStatus", description="Defines the status of the transaction request, e.g. \"created, \"await_approval\", \"pending\", \"prepared\", \"signed\", \"broadcasted\", \"success\", \"failed\", \"rejected\", mined\".")
    __properties = ["addressTag", "callbackSecretKey", "callbackUrl", "classicAddress", "feePriority", "note", "recipients", "senders", "transactionRequestId", "transactionRequestStatus"]

    @validator('fee_priority')
    def fee_priority_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('slow', 'standard', 'fast'):
            raise ValueError("must be one of enum values ('slow', 'standard', 'fast')")
        return value

    @validator('transaction_request_status')
    def transaction_request_status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('created', 'await-approval', 'pending', 'prepared', 'signed', 'broadcasted', 'success', 'failed', 'rejected', 'mined'):
            raise ValueError("must be one of enum values ('created', 'await-approval', 'pending', 'prepared', 'signed', 'broadcasted', 'success', 'failed', 'rejected', 'mined')")
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
    def from_json(cls, json_str: str) -> CreateCoinsTransactionRequestFromAddressRI:
        """Create an instance of CreateCoinsTransactionRequestFromAddressRI from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in recipients (list)
        _items = []
        if self.recipients:
            for _item in self.recipients:
                if _item:
                    _items.append(_item.to_dict())
            _dict['recipients'] = _items
        # override the default output from pydantic by calling `to_dict()` of senders
        if self.senders:
            _dict['senders'] = self.senders.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CreateCoinsTransactionRequestFromAddressRI:
        """Create an instance of CreateCoinsTransactionRequestFromAddressRI from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CreateCoinsTransactionRequestFromAddressRI.parse_obj(obj)

        _obj = CreateCoinsTransactionRequestFromAddressRI.parse_obj({
            "address_tag": obj.get("addressTag"),
            "callback_secret_key": obj.get("callbackSecretKey"),
            "callback_url": obj.get("callbackUrl"),
            "classic_address": obj.get("classicAddress"),
            "fee_priority": obj.get("feePriority"),
            "note": obj.get("note"),
            "recipients": [CreateCoinsTransactionRequestFromAddressRIRecipientsInner.from_dict(_item) for _item in obj.get("recipients")] if obj.get("recipients") is not None else None,
            "senders": CreateCoinsTransactionRequestFromAddressRISenders.from_dict(obj.get("senders")) if obj.get("senders") is not None else None,
            "transaction_request_id": obj.get("transactionRequestId"),
            "transaction_request_status": obj.get("transactionRequestStatus")
        })
        return _obj
