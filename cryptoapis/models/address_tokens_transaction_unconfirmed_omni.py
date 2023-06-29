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

class AddressTokensTransactionUnconfirmedOmni(BaseModel):
    """
    OMNI
    """
    name: StrictStr = Field(..., description="Specifies the name of the token.")
    property_id: StrictStr = Field(..., alias="propertyId", description="Defines the ID of the property for Omni Layer.")
    transaction_type: StrictStr = Field(..., alias="transactionType", description="Defines the type of the transaction made.")
    created_by_transaction_id: StrictStr = Field(..., alias="createdByTransactionId", description="The transaction ID used to create the token.")
    amount: StrictStr = Field(..., description="Defines the amount of tokens sent with the transaction that is pending confirmation.")
    __properties = ["name", "propertyId", "transactionType", "createdByTransactionId", "amount"]

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
    def from_json(cls, json_str: str) -> AddressTokensTransactionUnconfirmedOmni:
        """Create an instance of AddressTokensTransactionUnconfirmedOmni from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AddressTokensTransactionUnconfirmedOmni:
        """Create an instance of AddressTokensTransactionUnconfirmedOmni from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AddressTokensTransactionUnconfirmedOmni.parse_obj(obj)

        _obj = AddressTokensTransactionUnconfirmedOmni.parse_obj({
            "name": obj.get("name"),
            "property_id": obj.get("propertyId"),
            "transaction_type": obj.get("transactionType"),
            "created_by_transaction_id": obj.get("createdByTransactionId"),
            "amount": obj.get("amount")
        })
        return _obj

