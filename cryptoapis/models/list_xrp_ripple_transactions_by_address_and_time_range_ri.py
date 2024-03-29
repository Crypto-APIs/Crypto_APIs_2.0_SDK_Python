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
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist
from cryptoapis.models.get_xrp_ripple_transaction_details_by_transaction_idri_recipients_inner import GetXRPRippleTransactionDetailsByTransactionIDRIRecipientsInner
from cryptoapis.models.get_xrp_ripple_transaction_details_by_transaction_idri_senders_inner import GetXRPRippleTransactionDetailsByTransactionIDRISendersInner
from cryptoapis.models.list_xrp_ripple_transactions_by_address_ri_fee import ListXRPRippleTransactionsByAddressRIFee
from cryptoapis.models.list_xrp_ripple_transactions_by_address_ri_offer import ListXRPRippleTransactionsByAddressRIOffer
from cryptoapis.models.list_xrp_ripple_transactions_by_address_ri_receive import ListXRPRippleTransactionsByAddressRIReceive
from cryptoapis.models.list_xrp_ripple_transactions_by_address_ri_value import ListXRPRippleTransactionsByAddressRIValue

class ListXRPRippleTransactionsByAddressAndTimeRangeRI(BaseModel):
    """
    ListXRPRippleTransactionsByAddressAndTimeRangeRI
    """
    destination_tag: Optional[StrictInt] = Field(None, alias="destinationTag", description="A destination tag is a value used to discern the holder of the Ripple (XRP) being deposited or withdrawn.")
    index: StrictInt = Field(..., description="Represents the index position of the transaction in the block.")
    mined_in_block_hash: StrictStr = Field(..., alias="minedInBlockHash", description="Represents the hash of the block where this transaction was mined/confirmed for first time. The hash is defined as a cryptographic digital fingerprint made by hashing the block header twice through the SHA256 algorithm.")
    mined_in_block_height: StrictInt = Field(..., alias="minedInBlockHeight", description="Represents the hight of the block where this transaction was mined/confirmed for first time. The height is defined as the number of blocks in the blockchain preceding this specific block.")
    recipients: conlist(GetXRPRippleTransactionDetailsByTransactionIDRIRecipientsInner) = Field(..., description="Represents an object of addresses that receive the transactions.")
    senders: conlist(GetXRPRippleTransactionDetailsByTransactionIDRISendersInner) = Field(..., description="Represents an object of addresses that provide the funds.")
    sequence: StrictInt = Field(..., description="Defines the transaction input's sequence as an integer, which is is used when transactions are replaced with newer versions before LockTime.")
    status: StrictStr = Field(..., description="Defines the status of the transaction.")
    timestamp: StrictInt = Field(..., description="Defines the exact date/time in Unix Timestamp when this transaction was mined, confirmed or first seen in Mempool, if it is unconfirmed.")
    transaction_hash: StrictStr = Field(..., alias="transactionHash", description="Represents the hash of the XRP transaction.")
    type: StrictStr = Field(..., description="Specifies the type of the transaction.")
    fee: ListXRPRippleTransactionsByAddressRIFee = Field(...)
    offer: ListXRPRippleTransactionsByAddressRIOffer = Field(...)
    receive: ListXRPRippleTransactionsByAddressRIReceive = Field(...)
    value: ListXRPRippleTransactionsByAddressRIValue = Field(...)
    __properties = ["destinationTag", "index", "minedInBlockHash", "minedInBlockHeight", "recipients", "senders", "sequence", "status", "timestamp", "transactionHash", "type", "fee", "offer", "receive", "value"]

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
    def from_json(cls, json_str: str) -> ListXRPRippleTransactionsByAddressAndTimeRangeRI:
        """Create an instance of ListXRPRippleTransactionsByAddressAndTimeRangeRI from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in senders (list)
        _items = []
        if self.senders:
            for _item in self.senders:
                if _item:
                    _items.append(_item.to_dict())
            _dict['senders'] = _items
        # override the default output from pydantic by calling `to_dict()` of fee
        if self.fee:
            _dict['fee'] = self.fee.to_dict()
        # override the default output from pydantic by calling `to_dict()` of offer
        if self.offer:
            _dict['offer'] = self.offer.to_dict()
        # override the default output from pydantic by calling `to_dict()` of receive
        if self.receive:
            _dict['receive'] = self.receive.to_dict()
        # override the default output from pydantic by calling `to_dict()` of value
        if self.value:
            _dict['value'] = self.value.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ListXRPRippleTransactionsByAddressAndTimeRangeRI:
        """Create an instance of ListXRPRippleTransactionsByAddressAndTimeRangeRI from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ListXRPRippleTransactionsByAddressAndTimeRangeRI.parse_obj(obj)

        _obj = ListXRPRippleTransactionsByAddressAndTimeRangeRI.parse_obj({
            "destination_tag": obj.get("destinationTag"),
            "index": obj.get("index"),
            "mined_in_block_hash": obj.get("minedInBlockHash"),
            "mined_in_block_height": obj.get("minedInBlockHeight"),
            "recipients": [GetXRPRippleTransactionDetailsByTransactionIDRIRecipientsInner.from_dict(_item) for _item in obj.get("recipients")] if obj.get("recipients") is not None else None,
            "senders": [GetXRPRippleTransactionDetailsByTransactionIDRISendersInner.from_dict(_item) for _item in obj.get("senders")] if obj.get("senders") is not None else None,
            "sequence": obj.get("sequence"),
            "status": obj.get("status"),
            "timestamp": obj.get("timestamp"),
            "transaction_hash": obj.get("transactionHash"),
            "type": obj.get("type"),
            "fee": ListXRPRippleTransactionsByAddressRIFee.from_dict(obj.get("fee")) if obj.get("fee") is not None else None,
            "offer": ListXRPRippleTransactionsByAddressRIOffer.from_dict(obj.get("offer")) if obj.get("offer") is not None else None,
            "receive": ListXRPRippleTransactionsByAddressRIReceive.from_dict(obj.get("receive")) if obj.get("receive") is not None else None,
            "value": ListXRPRippleTransactionsByAddressRIValue.from_dict(obj.get("value")) if obj.get("value") is not None else None
        })
        return _obj

