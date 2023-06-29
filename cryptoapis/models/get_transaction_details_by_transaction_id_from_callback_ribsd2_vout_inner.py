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



from pydantic import BaseModel, Field, StrictBool, StrictStr
from cryptoapis.models.get_transaction_details_by_transaction_id_from_callback_ribsd2_vout_inner_script_pub_key import GetTransactionDetailsByTransactionIDFromCallbackRIBSD2VoutInnerScriptPubKey

class GetTransactionDetailsByTransactionIDFromCallbackRIBSD2VoutInner(BaseModel):
    """
    GetTransactionDetailsByTransactionIDFromCallbackRIBSD2VoutInner
    """
    is_spent: StrictBool = Field(..., alias="isSpent", description="Defines whether the output is spent or not.")
    script_pub_key: GetTransactionDetailsByTransactionIDFromCallbackRIBSD2VoutInnerScriptPubKey = Field(..., alias="scriptPubKey")
    value: StrictStr = Field(..., description="String representation of the amount")
    __properties = ["isSpent", "scriptPubKey", "value"]

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
    def from_json(cls, json_str: str) -> GetTransactionDetailsByTransactionIDFromCallbackRIBSD2VoutInner:
        """Create an instance of GetTransactionDetailsByTransactionIDFromCallbackRIBSD2VoutInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of script_pub_key
        if self.script_pub_key:
            _dict['scriptPubKey'] = self.script_pub_key.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GetTransactionDetailsByTransactionIDFromCallbackRIBSD2VoutInner:
        """Create an instance of GetTransactionDetailsByTransactionIDFromCallbackRIBSD2VoutInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GetTransactionDetailsByTransactionIDFromCallbackRIBSD2VoutInner.parse_obj(obj)

        _obj = GetTransactionDetailsByTransactionIDFromCallbackRIBSD2VoutInner.parse_obj({
            "is_spent": obj.get("isSpent"),
            "script_pub_key": GetTransactionDetailsByTransactionIDFromCallbackRIBSD2VoutInnerScriptPubKey.from_dict(obj.get("scriptPubKey")) if obj.get("scriptPubKey") is not None else None,
            "value": obj.get("value")
        })
        return _obj

