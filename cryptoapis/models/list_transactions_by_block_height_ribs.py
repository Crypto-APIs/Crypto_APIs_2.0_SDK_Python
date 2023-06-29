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
from cryptoapis.models.list_transactions_by_block_height_ribsb import ListTransactionsByBlockHeightRIBSB
from cryptoapis.models.list_transactions_by_block_height_ribsbc import ListTransactionsByBlockHeightRIBSBC
from cryptoapis.models.list_transactions_by_block_height_ribsbsc import ListTransactionsByBlockHeightRIBSBSC
from cryptoapis.models.list_transactions_by_block_height_ribsd import ListTransactionsByBlockHeightRIBSD
from cryptoapis.models.list_transactions_by_block_height_ribsd2 import ListTransactionsByBlockHeightRIBSD2
from cryptoapis.models.list_transactions_by_block_height_ribse import ListTransactionsByBlockHeightRIBSE
from cryptoapis.models.list_transactions_by_block_height_ribsec import ListTransactionsByBlockHeightRIBSEC
from cryptoapis.models.list_transactions_by_block_height_ribsl import ListTransactionsByBlockHeightRIBSL
from cryptoapis.models.list_transactions_by_block_height_ribsz import ListTransactionsByBlockHeightRIBSZ
from typing import Any, List
from pydantic import StrictStr, Field

LISTTRANSACTIONSBYBLOCKHEIGHTRIBS_ONE_OF_SCHEMAS = ["ListTransactionsByBlockHeightRIBSB", "ListTransactionsByBlockHeightRIBSBC", "ListTransactionsByBlockHeightRIBSBSC", "ListTransactionsByBlockHeightRIBSD", "ListTransactionsByBlockHeightRIBSD2", "ListTransactionsByBlockHeightRIBSE", "ListTransactionsByBlockHeightRIBSEC", "ListTransactionsByBlockHeightRIBSL", "ListTransactionsByBlockHeightRIBSZ"]

class ListTransactionsByBlockHeightRIBS(BaseModel):
    """
    ListTransactionsByBlockHeightRIBS
    """
    # data type: ListTransactionsByBlockHeightRIBSB
    oneof_schema_1_validator: Optional[ListTransactionsByBlockHeightRIBSB] = None
    # data type: ListTransactionsByBlockHeightRIBSE
    oneof_schema_2_validator: Optional[ListTransactionsByBlockHeightRIBSE] = None
    # data type: ListTransactionsByBlockHeightRIBSD
    oneof_schema_3_validator: Optional[ListTransactionsByBlockHeightRIBSD] = None
    # data type: ListTransactionsByBlockHeightRIBSD2
    oneof_schema_4_validator: Optional[ListTransactionsByBlockHeightRIBSD2] = None
    # data type: ListTransactionsByBlockHeightRIBSL
    oneof_schema_5_validator: Optional[ListTransactionsByBlockHeightRIBSL] = None
    # data type: ListTransactionsByBlockHeightRIBSBC
    oneof_schema_6_validator: Optional[ListTransactionsByBlockHeightRIBSBC] = None
    # data type: ListTransactionsByBlockHeightRIBSEC
    oneof_schema_7_validator: Optional[ListTransactionsByBlockHeightRIBSEC] = None
    # data type: ListTransactionsByBlockHeightRIBSBSC
    oneof_schema_8_validator: Optional[ListTransactionsByBlockHeightRIBSBSC] = None
    # data type: ListTransactionsByBlockHeightRIBSZ
    oneof_schema_9_validator: Optional[ListTransactionsByBlockHeightRIBSZ] = None
    actual_instance: Any
    one_of_schemas: List[str] = Field(LISTTRANSACTIONSBYBLOCKHEIGHTRIBS_ONE_OF_SCHEMAS, const=True)

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
        instance = ListTransactionsByBlockHeightRIBS.construct()
        error_messages = []
        match = 0
        # validate data type: ListTransactionsByBlockHeightRIBSB
        if not isinstance(v, ListTransactionsByBlockHeightRIBSB):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ListTransactionsByBlockHeightRIBSB`")
        else:
            match += 1
        # validate data type: ListTransactionsByBlockHeightRIBSE
        if not isinstance(v, ListTransactionsByBlockHeightRIBSE):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ListTransactionsByBlockHeightRIBSE`")
        else:
            match += 1
        # validate data type: ListTransactionsByBlockHeightRIBSD
        if not isinstance(v, ListTransactionsByBlockHeightRIBSD):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ListTransactionsByBlockHeightRIBSD`")
        else:
            match += 1
        # validate data type: ListTransactionsByBlockHeightRIBSD2
        if not isinstance(v, ListTransactionsByBlockHeightRIBSD2):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ListTransactionsByBlockHeightRIBSD2`")
        else:
            match += 1
        # validate data type: ListTransactionsByBlockHeightRIBSL
        if not isinstance(v, ListTransactionsByBlockHeightRIBSL):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ListTransactionsByBlockHeightRIBSL`")
        else:
            match += 1
        # validate data type: ListTransactionsByBlockHeightRIBSBC
        if not isinstance(v, ListTransactionsByBlockHeightRIBSBC):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ListTransactionsByBlockHeightRIBSBC`")
        else:
            match += 1
        # validate data type: ListTransactionsByBlockHeightRIBSEC
        if not isinstance(v, ListTransactionsByBlockHeightRIBSEC):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ListTransactionsByBlockHeightRIBSEC`")
        else:
            match += 1
        # validate data type: ListTransactionsByBlockHeightRIBSBSC
        if not isinstance(v, ListTransactionsByBlockHeightRIBSBSC):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ListTransactionsByBlockHeightRIBSBSC`")
        else:
            match += 1
        # validate data type: ListTransactionsByBlockHeightRIBSZ
        if not isinstance(v, ListTransactionsByBlockHeightRIBSZ):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ListTransactionsByBlockHeightRIBSZ`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in ListTransactionsByBlockHeightRIBS with oneOf schemas: ListTransactionsByBlockHeightRIBSB, ListTransactionsByBlockHeightRIBSBC, ListTransactionsByBlockHeightRIBSBSC, ListTransactionsByBlockHeightRIBSD, ListTransactionsByBlockHeightRIBSD2, ListTransactionsByBlockHeightRIBSE, ListTransactionsByBlockHeightRIBSEC, ListTransactionsByBlockHeightRIBSL, ListTransactionsByBlockHeightRIBSZ. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in ListTransactionsByBlockHeightRIBS with oneOf schemas: ListTransactionsByBlockHeightRIBSB, ListTransactionsByBlockHeightRIBSBC, ListTransactionsByBlockHeightRIBSBSC, ListTransactionsByBlockHeightRIBSD, ListTransactionsByBlockHeightRIBSD2, ListTransactionsByBlockHeightRIBSE, ListTransactionsByBlockHeightRIBSEC, ListTransactionsByBlockHeightRIBSL, ListTransactionsByBlockHeightRIBSZ. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> ListTransactionsByBlockHeightRIBS:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> ListTransactionsByBlockHeightRIBS:
        """Returns the object represented by the json string"""
        instance = ListTransactionsByBlockHeightRIBS.construct()
        error_messages = []
        match = 0

        # deserialize data into ListTransactionsByBlockHeightRIBSB
        try:
            instance.actual_instance = ListTransactionsByBlockHeightRIBSB.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ListTransactionsByBlockHeightRIBSE
        try:
            instance.actual_instance = ListTransactionsByBlockHeightRIBSE.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ListTransactionsByBlockHeightRIBSD
        try:
            instance.actual_instance = ListTransactionsByBlockHeightRIBSD.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ListTransactionsByBlockHeightRIBSD2
        try:
            instance.actual_instance = ListTransactionsByBlockHeightRIBSD2.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ListTransactionsByBlockHeightRIBSL
        try:
            instance.actual_instance = ListTransactionsByBlockHeightRIBSL.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ListTransactionsByBlockHeightRIBSBC
        try:
            instance.actual_instance = ListTransactionsByBlockHeightRIBSBC.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ListTransactionsByBlockHeightRIBSEC
        try:
            instance.actual_instance = ListTransactionsByBlockHeightRIBSEC.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ListTransactionsByBlockHeightRIBSBSC
        try:
            instance.actual_instance = ListTransactionsByBlockHeightRIBSBSC.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ListTransactionsByBlockHeightRIBSZ
        try:
            instance.actual_instance = ListTransactionsByBlockHeightRIBSZ.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into ListTransactionsByBlockHeightRIBS with oneOf schemas: ListTransactionsByBlockHeightRIBSB, ListTransactionsByBlockHeightRIBSBC, ListTransactionsByBlockHeightRIBSBSC, ListTransactionsByBlockHeightRIBSD, ListTransactionsByBlockHeightRIBSD2, ListTransactionsByBlockHeightRIBSE, ListTransactionsByBlockHeightRIBSEC, ListTransactionsByBlockHeightRIBSL, ListTransactionsByBlockHeightRIBSZ. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into ListTransactionsByBlockHeightRIBS with oneOf schemas: ListTransactionsByBlockHeightRIBSB, ListTransactionsByBlockHeightRIBSBC, ListTransactionsByBlockHeightRIBSBSC, ListTransactionsByBlockHeightRIBSD, ListTransactionsByBlockHeightRIBSD2, ListTransactionsByBlockHeightRIBSE, ListTransactionsByBlockHeightRIBSEC, ListTransactionsByBlockHeightRIBSL, ListTransactionsByBlockHeightRIBSZ. Details: " + ", ".join(error_messages))
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

