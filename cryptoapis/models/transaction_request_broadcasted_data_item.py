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



from pydantic import BaseModel, Field, StrictInt, StrictStr

class TransactionRequestBroadcastedDataItem(BaseModel):
    """
    Defines an `item` as one result.
    """
    blockchain: StrictStr = Field(..., description="Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.")
    network: StrictStr = Field(..., description="Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"goerli\", \"mordor\" are test networks.")
    required_approvals: StrictInt = Field(..., alias="requiredApprovals", description="The required number of approvals needed to approve the transaction.")
    required_rejections: StrictInt = Field(..., alias="requiredRejections", description="The required number of rejections needed to reject the transaction.")
    current_approvals: StrictInt = Field(..., alias="currentApprovals", description="The current number of approvals given for the transaction.")
    current_rejections: StrictInt = Field(..., alias="currentRejections", description="The current number of rejections given for the transaction.")
    transaction_id: StrictStr = Field(..., alias="transactionId", description="Defines the unique ID of the specific transaction, i.e. its identification number.")
    __properties = ["blockchain", "network", "requiredApprovals", "requiredRejections", "currentApprovals", "currentRejections", "transactionId"]

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
    def from_json(cls, json_str: str) -> TransactionRequestBroadcastedDataItem:
        """Create an instance of TransactionRequestBroadcastedDataItem from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TransactionRequestBroadcastedDataItem:
        """Create an instance of TransactionRequestBroadcastedDataItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TransactionRequestBroadcastedDataItem.parse_obj(obj)

        _obj = TransactionRequestBroadcastedDataItem.parse_obj({
            "blockchain": obj.get("blockchain"),
            "network": obj.get("network"),
            "required_approvals": obj.get("requiredApprovals"),
            "required_rejections": obj.get("requiredRejections"),
            "current_approvals": obj.get("currentApprovals"),
            "current_rejections": obj.get("currentRejections"),
            "transaction_id": obj.get("transactionId")
        })
        return _obj

