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
from cryptoapis.models.get_fee_address_details_ri_balance import GetFeeAddressDetailsRIBalance

class GetFeeAddressDetailsRI(BaseModel):
    """
    GetFeeAddressDetailsRI
    """
    address: StrictStr = Field(..., description="Represents the specific fee address, which is always automatically generated. Users must fund it.")
    balance: GetFeeAddressDetailsRIBalance = Field(...)
    minimum_transfer_amount: StrictStr = Field(..., alias="minimumTransferAmount", description="Represents the minimum transfer amount of the currency in the `fromAddress` that can be allowed for an automatic forwarding.")
    __properties = ["address", "balance", "minimumTransferAmount"]

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
    def from_json(cls, json_str: str) -> GetFeeAddressDetailsRI:
        """Create an instance of GetFeeAddressDetailsRI from a JSON string"""
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
    def from_dict(cls, obj: dict) -> GetFeeAddressDetailsRI:
        """Create an instance of GetFeeAddressDetailsRI from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GetFeeAddressDetailsRI.parse_obj(obj)

        _obj = GetFeeAddressDetailsRI.parse_obj({
            "address": obj.get("address"),
            "balance": GetFeeAddressDetailsRIBalance.from_dict(obj.get("balance")) if obj.get("balance") is not None else None,
            "minimum_transfer_amount": obj.get("minimumTransferAmount")
        })
        return _obj
