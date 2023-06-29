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
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401

from typing import Any, List, Optional
from pydantic import BaseModel, Field, StrictStr, ValidationError, validator
from cryptoapis.models.create_fungible_tokens_transaction_request_from_address_rise import CreateFungibleTokensTransactionRequestFromAddressRISE
from typing import Any, List
from pydantic import StrictStr, Field

CREATEFUNGIBLETOKENSTRANSACTIONREQUESTFROMADDRESSRIS_ONE_OF_SCHEMAS = ["CreateFungibleTokensTransactionRequestFromAddressRISE"]

class CreateFungibleTokensTransactionRequestFromAddressRIS(BaseModel):
    """
    Represents the specific token data which depends on its type - if it is a Coin or Token.
    """
    # data type: CreateFungibleTokensTransactionRequestFromAddressRISE
    oneof_schema_1_validator: Optional[CreateFungibleTokensTransactionRequestFromAddressRISE] = None
    actual_instance: Any
    one_of_schemas: List[str] = Field(CREATEFUNGIBLETOKENSTRANSACTIONREQUESTFROMADDRESSRIS_ONE_OF_SCHEMAS, const=True)

    class Config:
        validate_assignment = True

    def __init__(self, *args, **kwargs):
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = CreateFungibleTokensTransactionRequestFromAddressRIS.construct()
        error_messages = []
        match = 0
        # validate data type: CreateFungibleTokensTransactionRequestFromAddressRISE
        if not isinstance(v, CreateFungibleTokensTransactionRequestFromAddressRISE):
            error_messages.append(f"Error! Input type `{type(v)}` is not `CreateFungibleTokensTransactionRequestFromAddressRISE`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in CreateFungibleTokensTransactionRequestFromAddressRIS with oneOf schemas: CreateFungibleTokensTransactionRequestFromAddressRISE. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in CreateFungibleTokensTransactionRequestFromAddressRIS with oneOf schemas: CreateFungibleTokensTransactionRequestFromAddressRISE. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> CreateFungibleTokensTransactionRequestFromAddressRIS:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> CreateFungibleTokensTransactionRequestFromAddressRIS:
        """Returns the object represented by the json string"""
        instance = CreateFungibleTokensTransactionRequestFromAddressRIS.construct()
        error_messages = []
        match = 0

        # deserialize data into CreateFungibleTokensTransactionRequestFromAddressRISE
        try:
            instance.actual_instance = CreateFungibleTokensTransactionRequestFromAddressRISE.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into CreateFungibleTokensTransactionRequestFromAddressRIS with oneOf schemas: CreateFungibleTokensTransactionRequestFromAddressRISE. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into CreateFungibleTokensTransactionRequestFromAddressRIS with oneOf schemas: CreateFungibleTokensTransactionRequestFromAddressRISE. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        to_json = getattr(self.actual_instance, "to_json", None)
        if callable(to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> dict:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        to_dict = getattr(self.actual_instance, "to_dict", None)
        if callable(to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.dict())

