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



from pydantic import BaseModel, Field, StrictInt
from cryptoapis.models.get_zilliqa_address_details_ri_balance import GetZilliqaAddressDetailsRIBalance

class GetZilliqaAddressDetailsRI(BaseModel):
    """
    GetZilliqaAddressDetailsRI
    """
    balance: GetZilliqaAddressDetailsRIBalance = Field(...)
    incoming_transactions_count: StrictInt = Field(..., alias="incomingTransactionsCount", description="Defines the received transaction count to the address.")
    outgoing_transactions_count: StrictInt = Field(..., alias="outgoingTransactionsCount", description="Defines the sent transaction count from the address.")
    transactions_count: StrictInt = Field(..., alias="transactionsCount", description="Defines the entire count of the transactions.")
    __properties = ["balance", "incomingTransactionsCount", "outgoingTransactionsCount", "transactionsCount"]

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
    def from_json(cls, json_str: str) -> GetZilliqaAddressDetailsRI:
        """Create an instance of GetZilliqaAddressDetailsRI from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of balance
        if self.balance:
            _dict['balance'] = self.balance.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GetZilliqaAddressDetailsRI:
        """Create an instance of GetZilliqaAddressDetailsRI from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GetZilliqaAddressDetailsRI.parse_obj(obj)

        _obj = GetZilliqaAddressDetailsRI.parse_obj({
            "balance": GetZilliqaAddressDetailsRIBalance.from_dict(obj.get("balance")) if obj.get("balance") is not None else None,
            "incoming_transactions_count": obj.get("incomingTransactionsCount"),
            "outgoing_transactions_count": obj.get("outgoingTransactionsCount"),
            "transactions_count": obj.get("transactionsCount")
        })
        return _obj
