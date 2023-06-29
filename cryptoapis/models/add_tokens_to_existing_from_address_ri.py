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



from pydantic import BaseModel, Field, StrictInt, StrictStr, validator
from cryptoapis.models.add_tokens_to_existing_from_address_rits import AddTokensToExistingFromAddressRITS

class AddTokensToExistingFromAddressRI(BaseModel):
    """
    AddTokensToExistingFromAddressRI
    """
    callback_url: StrictStr = Field(..., alias="callbackUrl", description="Represents the URL that is set by the customer where the callback will be received at. The callback notification will be received only if and when the event occurs. `We support ONLY httpS type of protocol`.")
    confirmations_count: StrictInt = Field(..., alias="confirmationsCount", description="Represents the number of confirmations, i.e. the amount of blocks that have been built on top of this block.")
    created_timestamp: StrictInt = Field(..., alias="createdTimestamp", description="Defines the specific time/date when the automatic forwarding was created in Unix Timestamp.")
    fee_address: StrictStr = Field(..., alias="feeAddress", description="Represents the specific fee address, which is always automatically generated. Users must fund it.")
    fee_priority: StrictStr = Field(..., alias="feePriority", description="Represents the fee priority of the automation, whether it is \"SLOW\", \"STANDARD\" or \"FAST\".")
    from_address: StrictStr = Field(..., alias="fromAddress", description="Represents the hash of the address that forwards the tokens.")
    minimum_transfer_amount: StrictStr = Field(..., alias="minimumTransferAmount", description="Represents the minimum transfer amount of the tokens in the `fromAddress` that can be allowed for an automatic forwarding.")
    reference_id: StrictStr = Field(..., alias="referenceId", description="Represents a unique ID used to reference the specific callback subscription.")
    to_address: StrictStr = Field(..., alias="toAddress", description="Represents the hash of the address the tokens are forwarded to.")
    token_data: AddTokensToExistingFromAddressRITS = Field(..., alias="tokenData")
    __properties = ["callbackUrl", "confirmationsCount", "createdTimestamp", "feeAddress", "feePriority", "fromAddress", "minimumTransferAmount", "referenceId", "toAddress", "tokenData"]

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
    def from_json(cls, json_str: str) -> AddTokensToExistingFromAddressRI:
        """Create an instance of AddTokensToExistingFromAddressRI from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of token_data
        if self.token_data:
            _dict['tokenData'] = self.token_data.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AddTokensToExistingFromAddressRI:
        """Create an instance of AddTokensToExistingFromAddressRI from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AddTokensToExistingFromAddressRI.parse_obj(obj)

        _obj = AddTokensToExistingFromAddressRI.parse_obj({
            "callback_url": obj.get("callbackUrl"),
            "confirmations_count": obj.get("confirmationsCount"),
            "created_timestamp": obj.get("createdTimestamp"),
            "fee_address": obj.get("feeAddress"),
            "fee_priority": obj.get("feePriority"),
            "from_address": obj.get("fromAddress"),
            "minimum_transfer_amount": obj.get("minimumTransferAmount"),
            "reference_id": obj.get("referenceId"),
            "to_address": obj.get("toAddress"),
            "token_data": AddTokensToExistingFromAddressRITS.from_dict(obj.get("tokenData")) if obj.get("tokenData") is not None else None
        })
        return _obj

