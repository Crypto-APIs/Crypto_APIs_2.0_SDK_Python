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
from cryptoapis.models.get_block_details_by_block_hash_from_callback_ribsb import GetBlockDetailsByBlockHashFromCallbackRIBSB
from cryptoapis.models.get_block_details_by_block_hash_from_callback_ribsbc import GetBlockDetailsByBlockHashFromCallbackRIBSBC
from cryptoapis.models.get_block_details_by_block_hash_from_callback_ribsbsc import GetBlockDetailsByBlockHashFromCallbackRIBSBSC
from cryptoapis.models.get_block_details_by_block_hash_from_callback_ribsd import GetBlockDetailsByBlockHashFromCallbackRIBSD
from cryptoapis.models.get_block_details_by_block_hash_from_callback_ribsd2 import GetBlockDetailsByBlockHashFromCallbackRIBSD2
from cryptoapis.models.get_block_details_by_block_hash_from_callback_ribse import GetBlockDetailsByBlockHashFromCallbackRIBSE
from cryptoapis.models.get_block_details_by_block_hash_from_callback_ribsec import GetBlockDetailsByBlockHashFromCallbackRIBSEC
from cryptoapis.models.get_block_details_by_block_hash_from_callback_ribsl import GetBlockDetailsByBlockHashFromCallbackRIBSL
from cryptoapis.models.get_block_details_by_block_hash_from_callback_ribst import GetBlockDetailsByBlockHashFromCallbackRIBST
from cryptoapis.models.get_block_details_by_block_hash_from_callback_ribsx import GetBlockDetailsByBlockHashFromCallbackRIBSX
from cryptoapis.models.get_block_details_by_block_hash_from_callback_ribsz import GetBlockDetailsByBlockHashFromCallbackRIBSZ
from typing import Any, List
from pydantic import StrictStr, Field

GETBLOCKDETAILSBYBLOCKHASHFROMCALLBACKRIBS_ONE_OF_SCHEMAS = ["GetBlockDetailsByBlockHashFromCallbackRIBSB", "GetBlockDetailsByBlockHashFromCallbackRIBSBC", "GetBlockDetailsByBlockHashFromCallbackRIBSBSC", "GetBlockDetailsByBlockHashFromCallbackRIBSD", "GetBlockDetailsByBlockHashFromCallbackRIBSD2", "GetBlockDetailsByBlockHashFromCallbackRIBSE", "GetBlockDetailsByBlockHashFromCallbackRIBSEC", "GetBlockDetailsByBlockHashFromCallbackRIBSL", "GetBlockDetailsByBlockHashFromCallbackRIBST", "GetBlockDetailsByBlockHashFromCallbackRIBSX", "GetBlockDetailsByBlockHashFromCallbackRIBSZ"]

class GetBlockDetailsByBlockHashFromCallbackRIBS(BaseModel):
    """
    GetBlockDetailsByBlockHashFromCallbackRIBS
    """
    # data type: GetBlockDetailsByBlockHashFromCallbackRIBSB
    oneof_schema_1_validator: Optional[GetBlockDetailsByBlockHashFromCallbackRIBSB] = None
    # data type: GetBlockDetailsByBlockHashFromCallbackRIBSBC
    oneof_schema_2_validator: Optional[GetBlockDetailsByBlockHashFromCallbackRIBSBC] = None
    # data type: GetBlockDetailsByBlockHashFromCallbackRIBSL
    oneof_schema_3_validator: Optional[GetBlockDetailsByBlockHashFromCallbackRIBSL] = None
    # data type: GetBlockDetailsByBlockHashFromCallbackRIBSD
    oneof_schema_4_validator: Optional[GetBlockDetailsByBlockHashFromCallbackRIBSD] = None
    # data type: GetBlockDetailsByBlockHashFromCallbackRIBSD2
    oneof_schema_5_validator: Optional[GetBlockDetailsByBlockHashFromCallbackRIBSD2] = None
    # data type: GetBlockDetailsByBlockHashFromCallbackRIBSE
    oneof_schema_6_validator: Optional[GetBlockDetailsByBlockHashFromCallbackRIBSE] = None
    # data type: GetBlockDetailsByBlockHashFromCallbackRIBSBSC
    oneof_schema_7_validator: Optional[GetBlockDetailsByBlockHashFromCallbackRIBSBSC] = None
    # data type: GetBlockDetailsByBlockHashFromCallbackRIBSEC
    oneof_schema_8_validator: Optional[GetBlockDetailsByBlockHashFromCallbackRIBSEC] = None
    # data type: GetBlockDetailsByBlockHashFromCallbackRIBSX
    oneof_schema_9_validator: Optional[GetBlockDetailsByBlockHashFromCallbackRIBSX] = None
    # data type: GetBlockDetailsByBlockHashFromCallbackRIBSZ
    oneof_schema_10_validator: Optional[GetBlockDetailsByBlockHashFromCallbackRIBSZ] = None
    # data type: GetBlockDetailsByBlockHashFromCallbackRIBST
    oneof_schema_11_validator: Optional[GetBlockDetailsByBlockHashFromCallbackRIBST] = None
    actual_instance: Any
    one_of_schemas: List[str] = Field(GETBLOCKDETAILSBYBLOCKHASHFROMCALLBACKRIBS_ONE_OF_SCHEMAS, const=True)

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
        instance = GetBlockDetailsByBlockHashFromCallbackRIBS.construct()
        error_messages = []
        match = 0
        # validate data type: GetBlockDetailsByBlockHashFromCallbackRIBSB
        if not isinstance(v, GetBlockDetailsByBlockHashFromCallbackRIBSB):
            error_messages.append(f"Error! Input type `{type(v)}` is not `GetBlockDetailsByBlockHashFromCallbackRIBSB`")
        else:
            match += 1
        # validate data type: GetBlockDetailsByBlockHashFromCallbackRIBSBC
        if not isinstance(v, GetBlockDetailsByBlockHashFromCallbackRIBSBC):
            error_messages.append(f"Error! Input type `{type(v)}` is not `GetBlockDetailsByBlockHashFromCallbackRIBSBC`")
        else:
            match += 1
        # validate data type: GetBlockDetailsByBlockHashFromCallbackRIBSL
        if not isinstance(v, GetBlockDetailsByBlockHashFromCallbackRIBSL):
            error_messages.append(f"Error! Input type `{type(v)}` is not `GetBlockDetailsByBlockHashFromCallbackRIBSL`")
        else:
            match += 1
        # validate data type: GetBlockDetailsByBlockHashFromCallbackRIBSD
        if not isinstance(v, GetBlockDetailsByBlockHashFromCallbackRIBSD):
            error_messages.append(f"Error! Input type `{type(v)}` is not `GetBlockDetailsByBlockHashFromCallbackRIBSD`")
        else:
            match += 1
        # validate data type: GetBlockDetailsByBlockHashFromCallbackRIBSD2
        if not isinstance(v, GetBlockDetailsByBlockHashFromCallbackRIBSD2):
            error_messages.append(f"Error! Input type `{type(v)}` is not `GetBlockDetailsByBlockHashFromCallbackRIBSD2`")
        else:
            match += 1
        # validate data type: GetBlockDetailsByBlockHashFromCallbackRIBSE
        if not isinstance(v, GetBlockDetailsByBlockHashFromCallbackRIBSE):
            error_messages.append(f"Error! Input type `{type(v)}` is not `GetBlockDetailsByBlockHashFromCallbackRIBSE`")
        else:
            match += 1
        # validate data type: GetBlockDetailsByBlockHashFromCallbackRIBSBSC
        if not isinstance(v, GetBlockDetailsByBlockHashFromCallbackRIBSBSC):
            error_messages.append(f"Error! Input type `{type(v)}` is not `GetBlockDetailsByBlockHashFromCallbackRIBSBSC`")
        else:
            match += 1
        # validate data type: GetBlockDetailsByBlockHashFromCallbackRIBSEC
        if not isinstance(v, GetBlockDetailsByBlockHashFromCallbackRIBSEC):
            error_messages.append(f"Error! Input type `{type(v)}` is not `GetBlockDetailsByBlockHashFromCallbackRIBSEC`")
        else:
            match += 1
        # validate data type: GetBlockDetailsByBlockHashFromCallbackRIBSX
        if not isinstance(v, GetBlockDetailsByBlockHashFromCallbackRIBSX):
            error_messages.append(f"Error! Input type `{type(v)}` is not `GetBlockDetailsByBlockHashFromCallbackRIBSX`")
        else:
            match += 1
        # validate data type: GetBlockDetailsByBlockHashFromCallbackRIBSZ
        if not isinstance(v, GetBlockDetailsByBlockHashFromCallbackRIBSZ):
            error_messages.append(f"Error! Input type `{type(v)}` is not `GetBlockDetailsByBlockHashFromCallbackRIBSZ`")
        else:
            match += 1
        # validate data type: GetBlockDetailsByBlockHashFromCallbackRIBST
        if not isinstance(v, GetBlockDetailsByBlockHashFromCallbackRIBST):
            error_messages.append(f"Error! Input type `{type(v)}` is not `GetBlockDetailsByBlockHashFromCallbackRIBST`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in GetBlockDetailsByBlockHashFromCallbackRIBS with oneOf schemas: GetBlockDetailsByBlockHashFromCallbackRIBSB, GetBlockDetailsByBlockHashFromCallbackRIBSBC, GetBlockDetailsByBlockHashFromCallbackRIBSBSC, GetBlockDetailsByBlockHashFromCallbackRIBSD, GetBlockDetailsByBlockHashFromCallbackRIBSD2, GetBlockDetailsByBlockHashFromCallbackRIBSE, GetBlockDetailsByBlockHashFromCallbackRIBSEC, GetBlockDetailsByBlockHashFromCallbackRIBSL, GetBlockDetailsByBlockHashFromCallbackRIBST, GetBlockDetailsByBlockHashFromCallbackRIBSX, GetBlockDetailsByBlockHashFromCallbackRIBSZ. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in GetBlockDetailsByBlockHashFromCallbackRIBS with oneOf schemas: GetBlockDetailsByBlockHashFromCallbackRIBSB, GetBlockDetailsByBlockHashFromCallbackRIBSBC, GetBlockDetailsByBlockHashFromCallbackRIBSBSC, GetBlockDetailsByBlockHashFromCallbackRIBSD, GetBlockDetailsByBlockHashFromCallbackRIBSD2, GetBlockDetailsByBlockHashFromCallbackRIBSE, GetBlockDetailsByBlockHashFromCallbackRIBSEC, GetBlockDetailsByBlockHashFromCallbackRIBSL, GetBlockDetailsByBlockHashFromCallbackRIBST, GetBlockDetailsByBlockHashFromCallbackRIBSX, GetBlockDetailsByBlockHashFromCallbackRIBSZ. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> GetBlockDetailsByBlockHashFromCallbackRIBS:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> GetBlockDetailsByBlockHashFromCallbackRIBS:
        """Returns the object represented by the json string"""
        instance = GetBlockDetailsByBlockHashFromCallbackRIBS.construct()
        error_messages = []
        match = 0

        # deserialize data into GetBlockDetailsByBlockHashFromCallbackRIBSB
        try:
            instance.actual_instance = GetBlockDetailsByBlockHashFromCallbackRIBSB.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into GetBlockDetailsByBlockHashFromCallbackRIBSBC
        try:
            instance.actual_instance = GetBlockDetailsByBlockHashFromCallbackRIBSBC.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into GetBlockDetailsByBlockHashFromCallbackRIBSL
        try:
            instance.actual_instance = GetBlockDetailsByBlockHashFromCallbackRIBSL.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into GetBlockDetailsByBlockHashFromCallbackRIBSD
        try:
            instance.actual_instance = GetBlockDetailsByBlockHashFromCallbackRIBSD.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into GetBlockDetailsByBlockHashFromCallbackRIBSD2
        try:
            instance.actual_instance = GetBlockDetailsByBlockHashFromCallbackRIBSD2.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into GetBlockDetailsByBlockHashFromCallbackRIBSE
        try:
            instance.actual_instance = GetBlockDetailsByBlockHashFromCallbackRIBSE.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into GetBlockDetailsByBlockHashFromCallbackRIBSBSC
        try:
            instance.actual_instance = GetBlockDetailsByBlockHashFromCallbackRIBSBSC.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into GetBlockDetailsByBlockHashFromCallbackRIBSEC
        try:
            instance.actual_instance = GetBlockDetailsByBlockHashFromCallbackRIBSEC.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into GetBlockDetailsByBlockHashFromCallbackRIBSX
        try:
            instance.actual_instance = GetBlockDetailsByBlockHashFromCallbackRIBSX.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into GetBlockDetailsByBlockHashFromCallbackRIBSZ
        try:
            instance.actual_instance = GetBlockDetailsByBlockHashFromCallbackRIBSZ.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into GetBlockDetailsByBlockHashFromCallbackRIBST
        try:
            instance.actual_instance = GetBlockDetailsByBlockHashFromCallbackRIBST.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into GetBlockDetailsByBlockHashFromCallbackRIBS with oneOf schemas: GetBlockDetailsByBlockHashFromCallbackRIBSB, GetBlockDetailsByBlockHashFromCallbackRIBSBC, GetBlockDetailsByBlockHashFromCallbackRIBSBSC, GetBlockDetailsByBlockHashFromCallbackRIBSD, GetBlockDetailsByBlockHashFromCallbackRIBSD2, GetBlockDetailsByBlockHashFromCallbackRIBSE, GetBlockDetailsByBlockHashFromCallbackRIBSEC, GetBlockDetailsByBlockHashFromCallbackRIBSL, GetBlockDetailsByBlockHashFromCallbackRIBST, GetBlockDetailsByBlockHashFromCallbackRIBSX, GetBlockDetailsByBlockHashFromCallbackRIBSZ. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into GetBlockDetailsByBlockHashFromCallbackRIBS with oneOf schemas: GetBlockDetailsByBlockHashFromCallbackRIBSB, GetBlockDetailsByBlockHashFromCallbackRIBSBC, GetBlockDetailsByBlockHashFromCallbackRIBSBSC, GetBlockDetailsByBlockHashFromCallbackRIBSD, GetBlockDetailsByBlockHashFromCallbackRIBSD2, GetBlockDetailsByBlockHashFromCallbackRIBSE, GetBlockDetailsByBlockHashFromCallbackRIBSEC, GetBlockDetailsByBlockHashFromCallbackRIBSL, GetBlockDetailsByBlockHashFromCallbackRIBST, GetBlockDetailsByBlockHashFromCallbackRIBSX, GetBlockDetailsByBlockHashFromCallbackRIBSZ. Details: " + ", ".join(error_messages))
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

