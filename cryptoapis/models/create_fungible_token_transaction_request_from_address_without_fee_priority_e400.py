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
from cryptoapis.models.invalid_pagination import InvalidPagination
from cryptoapis.models.limit_greater_than_allowed import LimitGreaterThanAllowed
from cryptoapis.models.uri_not_found import UriNotFound
from typing import Any, List
from pydantic import StrictStr, Field

CREATEFUNGIBLETOKENTRANSACTIONREQUESTFROMADDRESSWITHOUTFEEPRIORITYE400_ONE_OF_SCHEMAS = ["InvalidPagination", "LimitGreaterThanAllowed", "UriNotFound"]

class CreateFungibleTokenTransactionRequestFromAddressWithoutFeePriorityE400(BaseModel):
    """
    CreateFungibleTokenTransactionRequestFromAddressWithoutFeePriorityE400
    """
    # data type: UriNotFound
    oneof_schema_1_validator: Optional[UriNotFound] = None
    # data type: LimitGreaterThanAllowed
    oneof_schema_2_validator: Optional[LimitGreaterThanAllowed] = None
    # data type: InvalidPagination
    oneof_schema_3_validator: Optional[InvalidPagination] = None
    actual_instance: Any
    one_of_schemas: List[str] = Field(CREATEFUNGIBLETOKENTRANSACTIONREQUESTFROMADDRESSWITHOUTFEEPRIORITYE400_ONE_OF_SCHEMAS, const=True)

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
        instance = CreateFungibleTokenTransactionRequestFromAddressWithoutFeePriorityE400.construct()
        error_messages = []
        match = 0
        # validate data type: UriNotFound
        if not isinstance(v, UriNotFound):
            error_messages.append(f"Error! Input type `{type(v)}` is not `UriNotFound`")
        else:
            match += 1
        # validate data type: LimitGreaterThanAllowed
        if not isinstance(v, LimitGreaterThanAllowed):
            error_messages.append(f"Error! Input type `{type(v)}` is not `LimitGreaterThanAllowed`")
        else:
            match += 1
        # validate data type: InvalidPagination
        if not isinstance(v, InvalidPagination):
            error_messages.append(f"Error! Input type `{type(v)}` is not `InvalidPagination`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in CreateFungibleTokenTransactionRequestFromAddressWithoutFeePriorityE400 with oneOf schemas: InvalidPagination, LimitGreaterThanAllowed, UriNotFound. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in CreateFungibleTokenTransactionRequestFromAddressWithoutFeePriorityE400 with oneOf schemas: InvalidPagination, LimitGreaterThanAllowed, UriNotFound. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> CreateFungibleTokenTransactionRequestFromAddressWithoutFeePriorityE400:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> CreateFungibleTokenTransactionRequestFromAddressWithoutFeePriorityE400:
        """Returns the object represented by the json string"""
        instance = CreateFungibleTokenTransactionRequestFromAddressWithoutFeePriorityE400.construct()
        error_messages = []
        match = 0

        # deserialize data into UriNotFound
        try:
            instance.actual_instance = UriNotFound.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into LimitGreaterThanAllowed
        try:
            instance.actual_instance = LimitGreaterThanAllowed.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into InvalidPagination
        try:
            instance.actual_instance = InvalidPagination.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into CreateFungibleTokenTransactionRequestFromAddressWithoutFeePriorityE400 with oneOf schemas: InvalidPagination, LimitGreaterThanAllowed, UriNotFound. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into CreateFungibleTokenTransactionRequestFromAddressWithoutFeePriorityE400 with oneOf schemas: InvalidPagination, LimitGreaterThanAllowed, UriNotFound. Details: " + ", ".join(error_messages))
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

