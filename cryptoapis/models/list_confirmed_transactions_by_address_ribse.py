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


from typing import Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr
from cryptoapis.models.list_confirmed_transactions_by_address_ribse_gas_price import ListConfirmedTransactionsByAddressRIBSEGasPrice

class ListConfirmedTransactionsByAddressRIBSE(BaseModel):
    """
    Ethereum
    """
    contract: Optional[StrictStr] = Field(None, description="Represents the specific transaction contract.")
    gas_limit: StrictStr = Field(..., alias="gasLimit", description="Represents the amount of gas used by this specific transaction alone.")
    gas_price: ListConfirmedTransactionsByAddressRIBSEGasPrice = Field(..., alias="gasPrice")
    gas_used: StrictStr = Field(..., alias="gasUsed", description="Represents the exact unit of gas that was used for the transaction.")
    input_data: Optional[StrictStr] = Field(None, alias="inputData", description="Represents additional information that is required for the transaction.")
    internal_transactions_count: StrictInt = Field(..., alias="internalTransactionsCount", description="Represents the total internal transactions count.")
    nonce: StrictInt = Field(..., description="Represents the sequential running number for an address, starting from 0 for the first transaction. E.g., if the nonce of a transaction is 10, it would be the 11th transaction sent from the sender's address.")
    token_transfers_count: StrictInt = Field(..., alias="tokenTransfersCount", description="Represents the total token transfers count.")
    transaction_status: StrictStr = Field(..., alias="transactionStatus", description="String representation of the transaction status")
    __properties = ["contract", "gasLimit", "gasPrice", "gasUsed", "inputData", "internalTransactionsCount", "nonce", "tokenTransfersCount", "transactionStatus"]

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
    def from_json(cls, json_str: str) -> ListConfirmedTransactionsByAddressRIBSE:
        """Create an instance of ListConfirmedTransactionsByAddressRIBSE from a JSON string"""
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
    def from_dict(cls, obj: dict) -> ListConfirmedTransactionsByAddressRIBSE:
        """Create an instance of ListConfirmedTransactionsByAddressRIBSE from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ListConfirmedTransactionsByAddressRIBSE.parse_obj(obj)

        _obj = ListConfirmedTransactionsByAddressRIBSE.parse_obj({
            "contract": obj.get("contract"),
            "gas_limit": obj.get("gasLimit"),
            "gas_price": ListConfirmedTransactionsByAddressRIBSEGasPrice.from_dict(obj.get("gasPrice")) if obj.get("gasPrice") is not None else None,
            "gas_used": obj.get("gasUsed"),
            "input_data": obj.get("inputData"),
            "internal_transactions_count": obj.get("internalTransactionsCount"),
            "nonce": obj.get("nonce"),
            "token_transfers_count": obj.get("tokenTransfersCount"),
            "transaction_status": obj.get("transactionStatus")
        })
        return _obj

