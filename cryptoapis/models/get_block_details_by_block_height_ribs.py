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
from cryptoapis.models.get_block_details_by_block_height_ribsb import GetBlockDetailsByBlockHeightRIBSB
from cryptoapis.models.get_block_details_by_block_height_ribsbc import GetBlockDetailsByBlockHeightRIBSBC
from cryptoapis.models.get_block_details_by_block_height_ribsbsc import GetBlockDetailsByBlockHeightRIBSBSC
from cryptoapis.models.get_block_details_by_block_height_ribsd import GetBlockDetailsByBlockHeightRIBSD
from cryptoapis.models.get_block_details_by_block_height_ribsd2 import GetBlockDetailsByBlockHeightRIBSD2
from cryptoapis.models.get_block_details_by_block_height_ribse import GetBlockDetailsByBlockHeightRIBSE
from cryptoapis.models.get_block_details_by_block_height_ribsec import GetBlockDetailsByBlockHeightRIBSEC
from cryptoapis.models.get_block_details_by_block_height_ribsl import GetBlockDetailsByBlockHeightRIBSL
from cryptoapis.models.get_block_details_by_block_height_ribsz import GetBlockDetailsByBlockHeightRIBSZ
from typing import Any, List
from pydantic import StrictStr, Field

GETBLOCKDETAILSBYBLOCKHEIGHTRIBS_ONE_OF_SCHEMAS = ["GetBlockDetailsByBlockHeightRIBSB", "GetBlockDetailsByBlockHeightRIBSBC", "GetBlockDetailsByBlockHeightRIBSBSC", "GetBlockDetailsByBlockHeightRIBSD", "GetBlockDetailsByBlockHeightRIBSD2", "GetBlockDetailsByBlockHeightRIBSE", "GetBlockDetailsByBlockHeightRIBSEC", "GetBlockDetailsByBlockHeightRIBSL", "GetBlockDetailsByBlockHeightRIBSZ"]

class GetBlockDetailsByBlockHeightRIBS(BaseModel):
    """
    GetBlockDetailsByBlockHeightRIBS
    """
    # data type: GetBlockDetailsByBlockHeightRIBSB
    oneof_schema_1_validator: Optional[GetBlockDetailsByBlockHeightRIBSB] = None
    # data type: GetBlockDetailsByBlockHeightRIBSE
    oneof_schema_2_validator: Optional[GetBlockDetailsByBlockHeightRIBSE] = None
    # data type: GetBlockDetailsByBlockHeightRIBSEC
    oneof_schema_3_validator: Optional[GetBlockDetailsByBlockHeightRIBSEC] = None
    # data type: GetBlockDetailsByBlockHeightRIBSBC
    oneof_schema_4_validator: Optional[GetBlockDetailsByBlockHeightRIBSBC] = None
    # data type: GetBlockDetailsByBlockHeightRIBSL
    oneof_schema_5_validator: Optional[GetBlockDetailsByBlockHeightRIBSL] = None
    # data type: GetBlockDetailsByBlockHeightRIBSD
    oneof_schema_6_validator: Optional[GetBlockDetailsByBlockHeightRIBSD] = None
    # data type: GetBlockDetailsByBlockHeightRIBSD2
    oneof_schema_7_validator: Optional[GetBlockDetailsByBlockHeightRIBSD2] = None
    # data type: GetBlockDetailsByBlockHeightRIBSBSC
    oneof_schema_8_validator: Optional[GetBlockDetailsByBlockHeightRIBSBSC] = None
    # data type: GetBlockDetailsByBlockHeightRIBSZ
    oneof_schema_9_validator: Optional[GetBlockDetailsByBlockHeightRIBSZ] = None
    actual_instance: Any
    one_of_schemas: List[str] = Field(GETBLOCKDETAILSBYBLOCKHEIGHTRIBS_ONE_OF_SCHEMAS, const=True)

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
        instance = GetBlockDetailsByBlockHeightRIBS.construct()
        error_messages = []
        match = 0
        # validate data type: GetBlockDetailsByBlockHeightRIBSB
        if not isinstance(v, GetBlockDetailsByBlockHeightRIBSB):
            error_messages.append(f"Error! Input type `{type(v)}` is not `GetBlockDetailsByBlockHeightRIBSB`")
        else:
            match += 1
        # validate data type: GetBlockDetailsByBlockHeightRIBSE
        if not isinstance(v, GetBlockDetailsByBlockHeightRIBSE):
            error_messages.append(f"Error! Input type `{type(v)}` is not `GetBlockDetailsByBlockHeightRIBSE`")
        else:
            match += 1
        # validate data type: GetBlockDetailsByBlockHeightRIBSEC
        if not isinstance(v, GetBlockDetailsByBlockHeightRIBSEC):
            error_messages.append(f"Error! Input type `{type(v)}` is not `GetBlockDetailsByBlockHeightRIBSEC`")
        else:
            match += 1
        # validate data type: GetBlockDetailsByBlockHeightRIBSBC
        if not isinstance(v, GetBlockDetailsByBlockHeightRIBSBC):
            error_messages.append(f"Error! Input type `{type(v)}` is not `GetBlockDetailsByBlockHeightRIBSBC`")
        else:
            match += 1
        # validate data type: GetBlockDetailsByBlockHeightRIBSL
        if not isinstance(v, GetBlockDetailsByBlockHeightRIBSL):
            error_messages.append(f"Error! Input type `{type(v)}` is not `GetBlockDetailsByBlockHeightRIBSL`")
        else:
            match += 1
        # validate data type: GetBlockDetailsByBlockHeightRIBSD
        if not isinstance(v, GetBlockDetailsByBlockHeightRIBSD):
            error_messages.append(f"Error! Input type `{type(v)}` is not `GetBlockDetailsByBlockHeightRIBSD`")
        else:
            match += 1
        # validate data type: GetBlockDetailsByBlockHeightRIBSD2
        if not isinstance(v, GetBlockDetailsByBlockHeightRIBSD2):
            error_messages.append(f"Error! Input type `{type(v)}` is not `GetBlockDetailsByBlockHeightRIBSD2`")
        else:
            match += 1
        # validate data type: GetBlockDetailsByBlockHeightRIBSBSC
        if not isinstance(v, GetBlockDetailsByBlockHeightRIBSBSC):
            error_messages.append(f"Error! Input type `{type(v)}` is not `GetBlockDetailsByBlockHeightRIBSBSC`")
        else:
            match += 1
        # validate data type: GetBlockDetailsByBlockHeightRIBSZ
        if not isinstance(v, GetBlockDetailsByBlockHeightRIBSZ):
            error_messages.append(f"Error! Input type `{type(v)}` is not `GetBlockDetailsByBlockHeightRIBSZ`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in GetBlockDetailsByBlockHeightRIBS with oneOf schemas: GetBlockDetailsByBlockHeightRIBSB, GetBlockDetailsByBlockHeightRIBSBC, GetBlockDetailsByBlockHeightRIBSBSC, GetBlockDetailsByBlockHeightRIBSD, GetBlockDetailsByBlockHeightRIBSD2, GetBlockDetailsByBlockHeightRIBSE, GetBlockDetailsByBlockHeightRIBSEC, GetBlockDetailsByBlockHeightRIBSL, GetBlockDetailsByBlockHeightRIBSZ. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in GetBlockDetailsByBlockHeightRIBS with oneOf schemas: GetBlockDetailsByBlockHeightRIBSB, GetBlockDetailsByBlockHeightRIBSBC, GetBlockDetailsByBlockHeightRIBSBSC, GetBlockDetailsByBlockHeightRIBSD, GetBlockDetailsByBlockHeightRIBSD2, GetBlockDetailsByBlockHeightRIBSE, GetBlockDetailsByBlockHeightRIBSEC, GetBlockDetailsByBlockHeightRIBSL, GetBlockDetailsByBlockHeightRIBSZ. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> GetBlockDetailsByBlockHeightRIBS:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> GetBlockDetailsByBlockHeightRIBS:
        """Returns the object represented by the json string"""
        instance = GetBlockDetailsByBlockHeightRIBS.construct()
        error_messages = []
        match = 0

        # deserialize data into GetBlockDetailsByBlockHeightRIBSB
        try:
            instance.actual_instance = GetBlockDetailsByBlockHeightRIBSB.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into GetBlockDetailsByBlockHeightRIBSE
        try:
            instance.actual_instance = GetBlockDetailsByBlockHeightRIBSE.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into GetBlockDetailsByBlockHeightRIBSEC
        try:
            instance.actual_instance = GetBlockDetailsByBlockHeightRIBSEC.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into GetBlockDetailsByBlockHeightRIBSBC
        try:
            instance.actual_instance = GetBlockDetailsByBlockHeightRIBSBC.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into GetBlockDetailsByBlockHeightRIBSL
        try:
            instance.actual_instance = GetBlockDetailsByBlockHeightRIBSL.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into GetBlockDetailsByBlockHeightRIBSD
        try:
            instance.actual_instance = GetBlockDetailsByBlockHeightRIBSD.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into GetBlockDetailsByBlockHeightRIBSD2
        try:
            instance.actual_instance = GetBlockDetailsByBlockHeightRIBSD2.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into GetBlockDetailsByBlockHeightRIBSBSC
        try:
            instance.actual_instance = GetBlockDetailsByBlockHeightRIBSBSC.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into GetBlockDetailsByBlockHeightRIBSZ
        try:
            instance.actual_instance = GetBlockDetailsByBlockHeightRIBSZ.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into GetBlockDetailsByBlockHeightRIBS with oneOf schemas: GetBlockDetailsByBlockHeightRIBSB, GetBlockDetailsByBlockHeightRIBSBC, GetBlockDetailsByBlockHeightRIBSBSC, GetBlockDetailsByBlockHeightRIBSD, GetBlockDetailsByBlockHeightRIBSD2, GetBlockDetailsByBlockHeightRIBSE, GetBlockDetailsByBlockHeightRIBSEC, GetBlockDetailsByBlockHeightRIBSL, GetBlockDetailsByBlockHeightRIBSZ. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into GetBlockDetailsByBlockHeightRIBS with oneOf schemas: GetBlockDetailsByBlockHeightRIBSB, GetBlockDetailsByBlockHeightRIBSBC, GetBlockDetailsByBlockHeightRIBSBSC, GetBlockDetailsByBlockHeightRIBSD, GetBlockDetailsByBlockHeightRIBSD2, GetBlockDetailsByBlockHeightRIBSE, GetBlockDetailsByBlockHeightRIBSEC, GetBlockDetailsByBlockHeightRIBSL, GetBlockDetailsByBlockHeightRIBSZ. Details: " + ", ".join(error_messages))
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
