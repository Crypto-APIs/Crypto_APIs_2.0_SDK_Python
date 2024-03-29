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
from pydantic import BaseModel, Field, StrictStr, conlist, validator
from cryptoapis.models.create_single_transaction_request_from_address_without_fee_priority_ri_recipient_inner import CreateSingleTransactionRequestFromAddressWithoutFeePriorityRIRecipientInner
from cryptoapis.models.create_single_transaction_request_from_address_without_fee_priority_ri_sender import CreateSingleTransactionRequestFromAddressWithoutFeePriorityRISender
from cryptoapis.models.create_single_transaction_request_from_address_without_fee_priority_ri_total_amount import CreateSingleTransactionRequestFromAddressWithoutFeePriorityRITotalAmount

class CreateSingleTransactionRequestFromAddressWithoutFeePriorityRI(BaseModel):
    """
    CreateSingleTransactionRequestFromAddressWithoutFeePriorityRI
    """
    callback_secret_key: Optional[StrictStr] = Field(None, alias="callbackSecretKey", description="Represents the Secret Key value provided by the customer. This field is used for security purposes during the callback notification, in order to prove the sender of the callback as Crypto APIs. For more information please see our [Documentation](https://developers.cryptoapis.io/technical-documentation/general-information/callbacks#callback-security).")
    callback_url: Optional[StrictStr] = Field(None, alias="callbackUrl", description="Represents the URL that is set by the customer where the callback will be received at. The callback notification will be received only if and when the event occurs. `We support ONLY httpS type of protocol`.")
    classic_address: Optional[StrictStr] = Field(None, alias="classicAddress", description="Represents the public address, which is a compressed and shortened form of a public key. The classic address is shown when the source address is an x-Address.")
    note: Optional[StrictStr] = Field(None, description="Represents an optional note to add a free text in, explaining or providing additional detail on the transaction request.")
    recipient: conlist(CreateSingleTransactionRequestFromAddressWithoutFeePriorityRIRecipientInner) = Field(..., description="Defines the destination for the transaction, i.e. the recipient(s).")
    sender: CreateSingleTransactionRequestFromAddressWithoutFeePriorityRISender = Field(...)
    transaction_request_id: StrictStr = Field(..., alias="transactionRequestId", description="Represents a unique identifier of the transaction request (the request sent to make a transaction), which helps in identifying which callback and which `referenceId` concern that specific transaction request.")
    transaction_request_status: StrictStr = Field(..., alias="transactionRequestStatus", description="Defines the status of the transaction, e.g. \"created, \"await_approval\", \"pending\", \"prepared\", \"signed\", \"broadcasted\", \"success\", \"failed\", \"rejected\", mined\".")
    total_amount: Optional[CreateSingleTransactionRequestFromAddressWithoutFeePriorityRITotalAmount] = Field(None, alias="totalAmount")
    __properties = ["callbackSecretKey", "callbackUrl", "classicAddress", "note", "recipient", "sender", "transactionRequestId", "transactionRequestStatus", "totalAmount"]

    @validator('transaction_request_status')
    def transaction_request_status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('created', 'await-approval', 'pending', 'prepared', 'signed', 'broadcasted', 'success', 'failed', 'rejected', 'mined', 'mined-with-errors'):
            raise ValueError("must be one of enum values ('created', 'await-approval', 'pending', 'prepared', 'signed', 'broadcasted', 'success', 'failed', 'rejected', 'mined', 'mined-with-errors')")
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
    def from_json(cls, json_str: str) -> CreateSingleTransactionRequestFromAddressWithoutFeePriorityRI:
        """Create an instance of CreateSingleTransactionRequestFromAddressWithoutFeePriorityRI from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in recipient (list)
        _items = []
        if self.recipient:
            for _item in self.recipient:
                if _item:
                    _items.append(_item.to_dict())
            _dict['recipient'] = _items
        # override the default output from pydantic by calling `to_dict()` of sender
        if self.sender:
            _dict['sender'] = self.sender.to_dict()
        # override the default output from pydantic by calling `to_dict()` of total_amount
        if self.total_amount:
            _dict['totalAmount'] = self.total_amount.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CreateSingleTransactionRequestFromAddressWithoutFeePriorityRI:
        """Create an instance of CreateSingleTransactionRequestFromAddressWithoutFeePriorityRI from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CreateSingleTransactionRequestFromAddressWithoutFeePriorityRI.parse_obj(obj)

        _obj = CreateSingleTransactionRequestFromAddressWithoutFeePriorityRI.parse_obj({
            "callback_secret_key": obj.get("callbackSecretKey"),
            "callback_url": obj.get("callbackUrl"),
            "classic_address": obj.get("classicAddress"),
            "note": obj.get("note"),
            "recipient": [CreateSingleTransactionRequestFromAddressWithoutFeePriorityRIRecipientInner.from_dict(_item) for _item in obj.get("recipient")] if obj.get("recipient") is not None else None,
            "sender": CreateSingleTransactionRequestFromAddressWithoutFeePriorityRISender.from_dict(obj.get("sender")) if obj.get("sender") is not None else None,
            "transaction_request_id": obj.get("transactionRequestId"),
            "transaction_request_status": obj.get("transactionRequestStatus"),
            "total_amount": CreateSingleTransactionRequestFromAddressWithoutFeePriorityRITotalAmount.from_dict(obj.get("totalAmount")) if obj.get("totalAmount") is not None else None
        })
        return _obj

