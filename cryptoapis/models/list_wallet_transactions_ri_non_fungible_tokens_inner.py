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

class ListWalletTransactionsRINonFungibleTokensInner(BaseModel):
    """
    ListWalletTransactionsRINonFungibleTokensInner
    """
    converted_amount: StrictStr = Field(..., alias="convertedAmount", description="Defines the tokens' converted amount value.")
    exchange_rate_unit: StrictStr = Field(..., alias="exchangeRateUnit", description="Represents token's exchange rate unit.")
    name: StrictStr = Field(..., description="Defines the token's name as a string.")
    recipient: StrictStr = Field(..., description="Defines the address to which the recipient receives the transferred tokens.")
    sender: StrictStr = Field(..., description="Defines the address from which the sender transfers tokens.")
    symbol: StrictStr = Field(..., description="Defines the symbol of the non-fungible tokens.")
    token_id: StrictStr = Field(..., alias="tokenId", description="Represents tokens' unique identifier.")
    type: StrictStr = Field(..., description="Defines the specific token type.")
    __properties = ["convertedAmount", "exchangeRateUnit", "name", "recipient", "sender", "symbol", "tokenId", "type"]

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
    def from_json(cls, json_str: str) -> ListWalletTransactionsRINonFungibleTokensInner:
        """Create an instance of ListWalletTransactionsRINonFungibleTokensInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ListWalletTransactionsRINonFungibleTokensInner:
        """Create an instance of ListWalletTransactionsRINonFungibleTokensInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ListWalletTransactionsRINonFungibleTokensInner.parse_obj(obj)

        _obj = ListWalletTransactionsRINonFungibleTokensInner.parse_obj({
            "converted_amount": obj.get("convertedAmount"),
            "exchange_rate_unit": obj.get("exchangeRateUnit"),
            "name": obj.get("name"),
            "recipient": obj.get("recipient"),
            "sender": obj.get("sender"),
            "symbol": obj.get("symbol"),
            "token_id": obj.get("tokenId"),
            "type": obj.get("type")
        })
        return _obj

