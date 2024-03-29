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
from cryptoapis.models.get_transaction_details_by_transaction_id_from_callback_ribst_bandwidth_used import GetTransactionDetailsByTransactionIDFromCallbackRIBSTBandwidthUsed
from cryptoapis.models.get_transaction_details_by_transaction_id_from_callback_ribst_energy_used import GetTransactionDetailsByTransactionIDFromCallbackRIBSTEnergyUsed

class GetTransactionDetailsByTransactionIDFromCallbackRIBST(BaseModel):
    """
    Tron
    """
    amount: StrictStr = Field(..., description="Defines the amount of the transaction.")
    bandwidth_used: GetTransactionDetailsByTransactionIDFromCallbackRIBSTBandwidthUsed = Field(..., alias="bandwidthUsed")
    contract: StrictStr = Field(..., description="Represents the specific transaction contract.")
    energy_used: GetTransactionDetailsByTransactionIDFromCallbackRIBSTEnergyUsed = Field(..., alias="energyUsed")
    has_internal_transactions: StrictBool = Field(..., alias="hasInternalTransactions", description="Defines if the transaction includes internal transactions (true) or not (false).")
    has_token_transfers: StrictStr = Field(..., alias="hasTokenTransfers", description="Defines if the transaction includes token transfers (true) or not (false).")
    input: StrictStr = Field(..., description="Represents the transaction's input value.")
    recipients: StrictStr = Field(..., description="Represents the recipient address.")
    senders: StrictStr = Field(..., description="Represents the sender address.")
    transaction_status: StrictStr = Field(..., alias="transactionStatus", description="Represents the status of this transaction.")
    __properties = ["amount", "bandwidthUsed", "contract", "energyUsed", "hasInternalTransactions", "hasTokenTransfers", "input", "recipients", "senders", "transactionStatus"]

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
    def from_json(cls, json_str: str) -> GetTransactionDetailsByTransactionIDFromCallbackRIBST:
        """Create an instance of GetTransactionDetailsByTransactionIDFromCallbackRIBST from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of bandwidth_used
        if self.bandwidth_used:
            _dict['bandwidthUsed'] = self.bandwidth_used.to_dict()
        # override the default output from pydantic by calling `to_dict()` of energy_used
        if self.energy_used:
            _dict['energyUsed'] = self.energy_used.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GetTransactionDetailsByTransactionIDFromCallbackRIBST:
        """Create an instance of GetTransactionDetailsByTransactionIDFromCallbackRIBST from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GetTransactionDetailsByTransactionIDFromCallbackRIBST.parse_obj(obj)

        _obj = GetTransactionDetailsByTransactionIDFromCallbackRIBST.parse_obj({
            "amount": obj.get("amount"),
            "bandwidth_used": GetTransactionDetailsByTransactionIDFromCallbackRIBSTBandwidthUsed.from_dict(obj.get("bandwidthUsed")) if obj.get("bandwidthUsed") is not None else None,
            "contract": obj.get("contract"),
            "energy_used": GetTransactionDetailsByTransactionIDFromCallbackRIBSTEnergyUsed.from_dict(obj.get("energyUsed")) if obj.get("energyUsed") is not None else None,
            "has_internal_transactions": obj.get("hasInternalTransactions"),
            "has_token_transfers": obj.get("hasTokenTransfers"),
            "input": obj.get("input"),
            "recipients": obj.get("recipients"),
            "senders": obj.get("senders"),
            "transaction_status": obj.get("transactionStatus")
        })
        return _obj

