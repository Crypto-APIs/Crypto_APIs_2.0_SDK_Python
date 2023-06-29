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
from pydantic import BaseModel, Field, StrictInt
from cryptoapis.models.get_address_details_from_callback_ri_confirmed_balance import GetAddressDetailsFromCallbackRIConfirmedBalance
from cryptoapis.models.get_address_details_from_callback_ri_total_received import GetAddressDetailsFromCallbackRITotalReceived
from cryptoapis.models.get_address_details_from_callback_ri_total_spent import GetAddressDetailsFromCallbackRITotalSpent

class GetAddressDetailsFromCallbackRI(BaseModel):
    """
    GetAddressDetailsFromCallbackRI
    """
    incoming_transactions_count: StrictInt = Field(..., alias="incomingTransactionsCount", description="Defines the received transaction count to the address.")
    outgoing_transactions_count: StrictInt = Field(..., alias="outgoingTransactionsCount", description="Defines the sent transaction count from the address.")
    transactions_count: StrictInt = Field(..., alias="transactionsCount", description="Represents the total number of confirmed coins transactions for this address, both incoming and outgoing. Applies for coins only and not tokens transfers e.g. for Ethereum. transactionsCount could result as less than incoming and outgoing transactions put together (e.g. in Bitcoin), due to the fact that one and the same address could be in senders and receivers addresses.")
    confirmed_balance: GetAddressDetailsFromCallbackRIConfirmedBalance = Field(..., alias="confirmedBalance")
    total_received: GetAddressDetailsFromCallbackRITotalReceived = Field(..., alias="totalReceived")
    total_spent: GetAddressDetailsFromCallbackRITotalSpent = Field(..., alias="totalSpent")
    sequence: Optional[StrictInt] = Field(None, description="Defines the transaction input's sequence as an integer, which is is used when transactions are replaced with newer versions before LockTime.")
    __properties = ["incomingTransactionsCount", "outgoingTransactionsCount", "transactionsCount", "confirmedBalance", "totalReceived", "totalSpent", "sequence"]

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
    def from_json(cls, json_str: str) -> GetAddressDetailsFromCallbackRI:
        """Create an instance of GetAddressDetailsFromCallbackRI from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of confirmed_balance
        if self.confirmed_balance:
            _dict['confirmedBalance'] = self.confirmed_balance.to_dict()
        # override the default output from pydantic by calling `to_dict()` of total_received
        if self.total_received:
            _dict['totalReceived'] = self.total_received.to_dict()
        # override the default output from pydantic by calling `to_dict()` of total_spent
        if self.total_spent:
            _dict['totalSpent'] = self.total_spent.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GetAddressDetailsFromCallbackRI:
        """Create an instance of GetAddressDetailsFromCallbackRI from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GetAddressDetailsFromCallbackRI.parse_obj(obj)

        _obj = GetAddressDetailsFromCallbackRI.parse_obj({
            "incoming_transactions_count": obj.get("incomingTransactionsCount"),
            "outgoing_transactions_count": obj.get("outgoingTransactionsCount"),
            "transactions_count": obj.get("transactionsCount"),
            "confirmed_balance": GetAddressDetailsFromCallbackRIConfirmedBalance.from_dict(obj.get("confirmedBalance")) if obj.get("confirmedBalance") is not None else None,
            "total_received": GetAddressDetailsFromCallbackRITotalReceived.from_dict(obj.get("totalReceived")) if obj.get("totalReceived") is not None else None,
            "total_spent": GetAddressDetailsFromCallbackRITotalSpent.from_dict(obj.get("totalSpent")) if obj.get("totalSpent") is not None else None,
            "sequence": obj.get("sequence")
        })
        return _obj

