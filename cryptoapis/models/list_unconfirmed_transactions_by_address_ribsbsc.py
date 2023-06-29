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
from cryptoapis.models.list_confirmed_transactions_by_address_ribsbsc_gas_price import ListConfirmedTransactionsByAddressRIBSBSCGasPrice

class ListUnconfirmedTransactionsByAddressRIBSBSC(BaseModel):
    """
    Binance Smart Chain
    """
    gas_limit: StrictStr = Field(..., alias="gasLimit", description="Represents the amount of gas used by this specific transaction alone.")
    gas_price: ListConfirmedTransactionsByAddressRIBSBSCGasPrice = Field(..., alias="gasPrice")
    input_data: StrictStr = Field(..., alias="inputData", description="Represents additional information that is required for the transaction.")
    nonce: StrictInt = Field(..., description="Represents the sequential running number for an address, starting from 0 for the first transaction. E.g., if the nonce of a transaction is 10, it would be the 11th transaction sent from the sender's address.")
    transaction_status: StrictStr = Field(..., alias="transactionStatus", description="String representation of the transaction status")
    __properties = ["gasLimit", "gasPrice", "inputData", "nonce", "transactionStatus"]

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
    def from_json(cls, json_str: str) -> ListUnconfirmedTransactionsByAddressRIBSBSC:
        """Create an instance of ListUnconfirmedTransactionsByAddressRIBSBSC from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of gas_price
        if self.gas_price:
            _dict['gasPrice'] = self.gas_price.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ListUnconfirmedTransactionsByAddressRIBSBSC:
        """Create an instance of ListUnconfirmedTransactionsByAddressRIBSBSC from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ListUnconfirmedTransactionsByAddressRIBSBSC.parse_obj(obj)

        _obj = ListUnconfirmedTransactionsByAddressRIBSBSC.parse_obj({
            "gas_limit": obj.get("gasLimit"),
            "gas_price": ListConfirmedTransactionsByAddressRIBSBSCGasPrice.from_dict(obj.get("gasPrice")) if obj.get("gasPrice") is not None else None,
            "input_data": obj.get("inputData"),
            "nonce": obj.get("nonce"),
            "transaction_status": obj.get("transactionStatus")
        })
        return _obj

