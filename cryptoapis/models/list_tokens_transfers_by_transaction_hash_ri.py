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
from cryptoapis.models.list_tokens_transfers_by_transaction_hash_ri_transaction_fee import ListTokensTransfersByTransactionHashRITransactionFee

class ListTokensTransfersByTransactionHashRI(BaseModel):
    """
    ListTokensTransfersByTransactionHashRI
    """
    contract_address: StrictStr = Field(..., alias="contractAddress", description="Represents the contract address of the token, which controls its logic. It is not the address that holds the tokens.")
    mined_in_block_height: StrictInt = Field(..., alias="minedInBlockHeight", description="Defines the block height in which this transaction was confirmed/mined.")
    recipient_address: StrictStr = Field(..., alias="recipientAddress", description="Defines the address to which the recipient receives the transferred tokens.")
    sender_address: StrictStr = Field(..., alias="senderAddress", description="Defines the address from which the sender transfers tokens.")
    token_decimals: Optional[StrictInt] = Field(None, alias="tokenDecimals", description="Defines the decimals of the token, i.e. the number of digits that come after the decimal coma of the token.")
    token_name: Optional[StrictStr] = Field(None, alias="tokenName", description="Defines the token's name as a string.")
    token_symbol: Optional[StrictStr] = Field(None, alias="tokenSymbol", description="Defines the token symbol by which the token contract is known. It is usually 3-4 characters in length.")
    token_type: StrictStr = Field(..., alias="tokenType", description="Defines the specific token type.")
    tokens_amount: StrictStr = Field(..., alias="tokensAmount", description="Defines the token amount of the transfer.")
    transaction_hash: StrictStr = Field(..., alias="transactionHash", description="Represents the hash of the transaction, which is its unique identifier. It represents a cryptographic digital fingerprint made by hashing the block header twice through the SHA256 algorithm.")
    transaction_timestamp: StrictInt = Field(..., alias="transactionTimestamp", description="Defines the specific time/date when the transaction was created in Unix Timestamp.")
    transaction_fee: ListTokensTransfersByTransactionHashRITransactionFee = Field(..., alias="transactionFee")
    __properties = ["contractAddress", "minedInBlockHeight", "recipientAddress", "senderAddress", "tokenDecimals", "tokenName", "tokenSymbol", "tokenType", "tokensAmount", "transactionHash", "transactionTimestamp", "transactionFee"]

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
    def from_json(cls, json_str: str) -> ListTokensTransfersByTransactionHashRI:
        """Create an instance of ListTokensTransfersByTransactionHashRI from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of transaction_fee
        if self.transaction_fee:
            _dict['transactionFee'] = self.transaction_fee.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ListTokensTransfersByTransactionHashRI:
        """Create an instance of ListTokensTransfersByTransactionHashRI from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ListTokensTransfersByTransactionHashRI.parse_obj(obj)

        _obj = ListTokensTransfersByTransactionHashRI.parse_obj({
            "contract_address": obj.get("contractAddress"),
            "mined_in_block_height": obj.get("minedInBlockHeight"),
            "recipient_address": obj.get("recipientAddress"),
            "sender_address": obj.get("senderAddress"),
            "token_decimals": obj.get("tokenDecimals"),
            "token_name": obj.get("tokenName"),
            "token_symbol": obj.get("tokenSymbol"),
            "token_type": obj.get("tokenType"),
            "tokens_amount": obj.get("tokensAmount"),
            "transaction_hash": obj.get("transactionHash"),
            "transaction_timestamp": obj.get("transactionTimestamp"),
            "transaction_fee": ListTokensTransfersByTransactionHashRITransactionFee.from_dict(obj.get("transactionFee")) if obj.get("transactionFee") is not None else None
        })
        return _obj

