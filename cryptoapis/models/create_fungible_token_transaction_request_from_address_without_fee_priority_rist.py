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

class CreateFungibleTokenTransactionRequestFromAddressWithoutFeePriorityRIST(BaseModel):
    """
    Tron Trc20 Token
    """
    contract_address: StrictStr = Field(..., alias="contractAddress", description="Defines the contract address in the blockchain for an ERC20 token.")
    fee_limit: StrictStr = Field(..., alias="feeLimit", description="Defines the fee limit value.")
    symbol: StrictStr = Field(..., description="Defines the Token symbol.")
    __properties = ["contractAddress", "feeLimit", "symbol"]

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
    def from_json(cls, json_str: str) -> CreateFungibleTokenTransactionRequestFromAddressWithoutFeePriorityRIST:
        """Create an instance of CreateFungibleTokenTransactionRequestFromAddressWithoutFeePriorityRIST from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CreateFungibleTokenTransactionRequestFromAddressWithoutFeePriorityRIST:
        """Create an instance of CreateFungibleTokenTransactionRequestFromAddressWithoutFeePriorityRIST from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CreateFungibleTokenTransactionRequestFromAddressWithoutFeePriorityRIST.parse_obj(obj)

        _obj = CreateFungibleTokenTransactionRequestFromAddressWithoutFeePriorityRIST.parse_obj({
            "contract_address": obj.get("contractAddress"),
            "fee_limit": obj.get("feeLimit"),
            "symbol": obj.get("symbol")
        })
        return _obj

