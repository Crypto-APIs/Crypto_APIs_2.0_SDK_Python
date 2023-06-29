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



from pydantic import BaseModel, Field, StrictStr, validator

class TokensForwardingFailDataItem(BaseModel):
    """
    Defines an `item` as one result.
    """
    blockchain: StrictStr = Field(..., description="Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.")
    network: StrictStr = Field(..., description="Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\", \"rinkeby\" are test networks.")
    from_address: StrictStr = Field(..., alias="fromAddress", description="Represents the hash of the address that provides the tokens.")
    to_address: StrictStr = Field(..., alias="toAddress", description="Represents the hash of the address to forward the tokens to.")
    trigger_transaction_id: StrictStr = Field(..., alias="triggerTransactionId", description="Defines the unique Transaction ID that triggered the token forwarding.")
    error_code: StrictStr = Field(..., alias="errorCode", description="Represents the error code received for the failed token forwarding.")
    error_message: StrictStr = Field(..., alias="errorMessage", description="Represents the error message received for the failed token forwarding.")
    __properties = ["blockchain", "network", "fromAddress", "toAddress", "triggerTransactionId", "errorCode", "errorMessage"]

    @validator('error_code')
    def error_code_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('NOT_ENOUGH_CREDITS', 'FEE_ADDRESS_OUT_OF_FUNDS', 'WRONG_ADDRESS_CREDENTIALS'):
            raise ValueError("must be one of enum values ('NOT_ENOUGH_CREDITS', 'FEE_ADDRESS_OUT_OF_FUNDS', 'WRONG_ADDRESS_CREDENTIALS')")
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
    def from_json(cls, json_str: str) -> TokensForwardingFailDataItem:
        """Create an instance of TokensForwardingFailDataItem from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TokensForwardingFailDataItem:
        """Create an instance of TokensForwardingFailDataItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TokensForwardingFailDataItem.parse_obj(obj)

        _obj = TokensForwardingFailDataItem.parse_obj({
            "blockchain": obj.get("blockchain"),
            "network": obj.get("network"),
            "from_address": obj.get("fromAddress"),
            "to_address": obj.get("toAddress"),
            "trigger_transaction_id": obj.get("triggerTransactionId"),
            "error_code": obj.get("errorCode"),
            "error_message": obj.get("errorMessage")
        })
        return _obj

