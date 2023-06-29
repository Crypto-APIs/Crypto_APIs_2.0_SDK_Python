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
from cryptoapis.models.get_transaction_details_by_transaction_id_from_callback_ribsb import GetTransactionDetailsByTransactionIDFromCallbackRIBSB
from cryptoapis.models.get_transaction_details_by_transaction_id_from_callback_ribsbc import GetTransactionDetailsByTransactionIDFromCallbackRIBSBC
from cryptoapis.models.get_transaction_details_by_transaction_id_from_callback_ribsbsc import GetTransactionDetailsByTransactionIDFromCallbackRIBSBSC
from cryptoapis.models.get_transaction_details_by_transaction_id_from_callback_ribsd import GetTransactionDetailsByTransactionIDFromCallbackRIBSD
from cryptoapis.models.get_transaction_details_by_transaction_id_from_callback_ribsd2 import GetTransactionDetailsByTransactionIDFromCallbackRIBSD2
from cryptoapis.models.get_transaction_details_by_transaction_id_from_callback_ribse import GetTransactionDetailsByTransactionIDFromCallbackRIBSE
from cryptoapis.models.get_transaction_details_by_transaction_id_from_callback_ribsec import GetTransactionDetailsByTransactionIDFromCallbackRIBSEC
from cryptoapis.models.get_transaction_details_by_transaction_id_from_callback_ribsl import GetTransactionDetailsByTransactionIDFromCallbackRIBSL
from cryptoapis.models.get_transaction_details_by_transaction_id_from_callback_ribsp import GetTransactionDetailsByTransactionIDFromCallbackRIBSP
from cryptoapis.models.get_transaction_details_by_transaction_id_from_callback_ribst import GetTransactionDetailsByTransactionIDFromCallbackRIBST
from cryptoapis.models.get_transaction_details_by_transaction_id_from_callback_ribsx import GetTransactionDetailsByTransactionIDFromCallbackRIBSX
from cryptoapis.models.get_transaction_details_by_transaction_id_from_callback_ribsz import GetTransactionDetailsByTransactionIDFromCallbackRIBSZ
from typing import Any, List
from pydantic import StrictStr, Field

GETTRANSACTIONDETAILSBYTRANSACTIONIDFROMCALLBACKRIBS_ONE_OF_SCHEMAS = ["GetTransactionDetailsByTransactionIDFromCallbackRIBSB", "GetTransactionDetailsByTransactionIDFromCallbackRIBSBC", "GetTransactionDetailsByTransactionIDFromCallbackRIBSBSC", "GetTransactionDetailsByTransactionIDFromCallbackRIBSD", "GetTransactionDetailsByTransactionIDFromCallbackRIBSD2", "GetTransactionDetailsByTransactionIDFromCallbackRIBSE", "GetTransactionDetailsByTransactionIDFromCallbackRIBSEC", "GetTransactionDetailsByTransactionIDFromCallbackRIBSL", "GetTransactionDetailsByTransactionIDFromCallbackRIBSP", "GetTransactionDetailsByTransactionIDFromCallbackRIBST", "GetTransactionDetailsByTransactionIDFromCallbackRIBSX", "GetTransactionDetailsByTransactionIDFromCallbackRIBSZ"]

class GetTransactionDetailsByTransactionIDFromCallbackRIBS(BaseModel):
    """
    GetTransactionDetailsByTransactionIDFromCallbackRIBS
    """
    # data type: GetTransactionDetailsByTransactionIDFromCallbackRIBSB
    oneof_schema_1_validator: Optional[GetTransactionDetailsByTransactionIDFromCallbackRIBSB] = None
    # data type: GetTransactionDetailsByTransactionIDFromCallbackRIBSE
    oneof_schema_2_validator: Optional[GetTransactionDetailsByTransactionIDFromCallbackRIBSE] = None
    # data type: GetTransactionDetailsByTransactionIDFromCallbackRIBSBC
    oneof_schema_3_validator: Optional[GetTransactionDetailsByTransactionIDFromCallbackRIBSBC] = None
    # data type: GetTransactionDetailsByTransactionIDFromCallbackRIBSL
    oneof_schema_4_validator: Optional[GetTransactionDetailsByTransactionIDFromCallbackRIBSL] = None
    # data type: GetTransactionDetailsByTransactionIDFromCallbackRIBSD
    oneof_schema_5_validator: Optional[GetTransactionDetailsByTransactionIDFromCallbackRIBSD] = None
    # data type: GetTransactionDetailsByTransactionIDFromCallbackRIBSD2
    oneof_schema_6_validator: Optional[GetTransactionDetailsByTransactionIDFromCallbackRIBSD2] = None
    # data type: GetTransactionDetailsByTransactionIDFromCallbackRIBSZ
    oneof_schema_7_validator: Optional[GetTransactionDetailsByTransactionIDFromCallbackRIBSZ] = None
    # data type: GetTransactionDetailsByTransactionIDFromCallbackRIBSEC
    oneof_schema_8_validator: Optional[GetTransactionDetailsByTransactionIDFromCallbackRIBSEC] = None
    # data type: GetTransactionDetailsByTransactionIDFromCallbackRIBSBSC
    oneof_schema_9_validator: Optional[GetTransactionDetailsByTransactionIDFromCallbackRIBSBSC] = None
    # data type: GetTransactionDetailsByTransactionIDFromCallbackRIBSX
    oneof_schema_10_validator: Optional[GetTransactionDetailsByTransactionIDFromCallbackRIBSX] = None
    # data type: GetTransactionDetailsByTransactionIDFromCallbackRIBST
    oneof_schema_11_validator: Optional[GetTransactionDetailsByTransactionIDFromCallbackRIBST] = None
    # data type: GetTransactionDetailsByTransactionIDFromCallbackRIBSP
    oneof_schema_12_validator: Optional[GetTransactionDetailsByTransactionIDFromCallbackRIBSP] = None
    actual_instance: Any
    one_of_schemas: List[str] = Field(GETTRANSACTIONDETAILSBYTRANSACTIONIDFROMCALLBACKRIBS_ONE_OF_SCHEMAS, const=True)

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
        instance = GetTransactionDetailsByTransactionIDFromCallbackRIBS.construct()
        error_messages = []
        match = 0
        # validate data type: GetTransactionDetailsByTransactionIDFromCallbackRIBSB
        if not isinstance(v, GetTransactionDetailsByTransactionIDFromCallbackRIBSB):
            error_messages.append(f"Error! Input type `{type(v)}` is not `GetTransactionDetailsByTransactionIDFromCallbackRIBSB`")
        else:
            match += 1
        # validate data type: GetTransactionDetailsByTransactionIDFromCallbackRIBSE
        if not isinstance(v, GetTransactionDetailsByTransactionIDFromCallbackRIBSE):
            error_messages.append(f"Error! Input type `{type(v)}` is not `GetTransactionDetailsByTransactionIDFromCallbackRIBSE`")
        else:
            match += 1
        # validate data type: GetTransactionDetailsByTransactionIDFromCallbackRIBSBC
        if not isinstance(v, GetTransactionDetailsByTransactionIDFromCallbackRIBSBC):
            error_messages.append(f"Error! Input type `{type(v)}` is not `GetTransactionDetailsByTransactionIDFromCallbackRIBSBC`")
        else:
            match += 1
        # validate data type: GetTransactionDetailsByTransactionIDFromCallbackRIBSL
        if not isinstance(v, GetTransactionDetailsByTransactionIDFromCallbackRIBSL):
            error_messages.append(f"Error! Input type `{type(v)}` is not `GetTransactionDetailsByTransactionIDFromCallbackRIBSL`")
        else:
            match += 1
        # validate data type: GetTransactionDetailsByTransactionIDFromCallbackRIBSD
        if not isinstance(v, GetTransactionDetailsByTransactionIDFromCallbackRIBSD):
            error_messages.append(f"Error! Input type `{type(v)}` is not `GetTransactionDetailsByTransactionIDFromCallbackRIBSD`")
        else:
            match += 1
        # validate data type: GetTransactionDetailsByTransactionIDFromCallbackRIBSD2
        if not isinstance(v, GetTransactionDetailsByTransactionIDFromCallbackRIBSD2):
            error_messages.append(f"Error! Input type `{type(v)}` is not `GetTransactionDetailsByTransactionIDFromCallbackRIBSD2`")
        else:
            match += 1
        # validate data type: GetTransactionDetailsByTransactionIDFromCallbackRIBSZ
        if not isinstance(v, GetTransactionDetailsByTransactionIDFromCallbackRIBSZ):
            error_messages.append(f"Error! Input type `{type(v)}` is not `GetTransactionDetailsByTransactionIDFromCallbackRIBSZ`")
        else:
            match += 1
        # validate data type: GetTransactionDetailsByTransactionIDFromCallbackRIBSEC
        if not isinstance(v, GetTransactionDetailsByTransactionIDFromCallbackRIBSEC):
            error_messages.append(f"Error! Input type `{type(v)}` is not `GetTransactionDetailsByTransactionIDFromCallbackRIBSEC`")
        else:
            match += 1
        # validate data type: GetTransactionDetailsByTransactionIDFromCallbackRIBSBSC
        if not isinstance(v, GetTransactionDetailsByTransactionIDFromCallbackRIBSBSC):
            error_messages.append(f"Error! Input type `{type(v)}` is not `GetTransactionDetailsByTransactionIDFromCallbackRIBSBSC`")
        else:
            match += 1
        # validate data type: GetTransactionDetailsByTransactionIDFromCallbackRIBSX
        if not isinstance(v, GetTransactionDetailsByTransactionIDFromCallbackRIBSX):
            error_messages.append(f"Error! Input type `{type(v)}` is not `GetTransactionDetailsByTransactionIDFromCallbackRIBSX`")
        else:
            match += 1
        # validate data type: GetTransactionDetailsByTransactionIDFromCallbackRIBST
        if not isinstance(v, GetTransactionDetailsByTransactionIDFromCallbackRIBST):
            error_messages.append(f"Error! Input type `{type(v)}` is not `GetTransactionDetailsByTransactionIDFromCallbackRIBST`")
        else:
            match += 1
        # validate data type: GetTransactionDetailsByTransactionIDFromCallbackRIBSP
        if not isinstance(v, GetTransactionDetailsByTransactionIDFromCallbackRIBSP):
            error_messages.append(f"Error! Input type `{type(v)}` is not `GetTransactionDetailsByTransactionIDFromCallbackRIBSP`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in GetTransactionDetailsByTransactionIDFromCallbackRIBS with oneOf schemas: GetTransactionDetailsByTransactionIDFromCallbackRIBSB, GetTransactionDetailsByTransactionIDFromCallbackRIBSBC, GetTransactionDetailsByTransactionIDFromCallbackRIBSBSC, GetTransactionDetailsByTransactionIDFromCallbackRIBSD, GetTransactionDetailsByTransactionIDFromCallbackRIBSD2, GetTransactionDetailsByTransactionIDFromCallbackRIBSE, GetTransactionDetailsByTransactionIDFromCallbackRIBSEC, GetTransactionDetailsByTransactionIDFromCallbackRIBSL, GetTransactionDetailsByTransactionIDFromCallbackRIBSP, GetTransactionDetailsByTransactionIDFromCallbackRIBST, GetTransactionDetailsByTransactionIDFromCallbackRIBSX, GetTransactionDetailsByTransactionIDFromCallbackRIBSZ. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in GetTransactionDetailsByTransactionIDFromCallbackRIBS with oneOf schemas: GetTransactionDetailsByTransactionIDFromCallbackRIBSB, GetTransactionDetailsByTransactionIDFromCallbackRIBSBC, GetTransactionDetailsByTransactionIDFromCallbackRIBSBSC, GetTransactionDetailsByTransactionIDFromCallbackRIBSD, GetTransactionDetailsByTransactionIDFromCallbackRIBSD2, GetTransactionDetailsByTransactionIDFromCallbackRIBSE, GetTransactionDetailsByTransactionIDFromCallbackRIBSEC, GetTransactionDetailsByTransactionIDFromCallbackRIBSL, GetTransactionDetailsByTransactionIDFromCallbackRIBSP, GetTransactionDetailsByTransactionIDFromCallbackRIBST, GetTransactionDetailsByTransactionIDFromCallbackRIBSX, GetTransactionDetailsByTransactionIDFromCallbackRIBSZ. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> GetTransactionDetailsByTransactionIDFromCallbackRIBS:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> GetTransactionDetailsByTransactionIDFromCallbackRIBS:
        """Returns the object represented by the json string"""
        instance = GetTransactionDetailsByTransactionIDFromCallbackRIBS.construct()
        error_messages = []
        match = 0

        # deserialize data into GetTransactionDetailsByTransactionIDFromCallbackRIBSB
        try:
            instance.actual_instance = GetTransactionDetailsByTransactionIDFromCallbackRIBSB.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into GetTransactionDetailsByTransactionIDFromCallbackRIBSE
        try:
            instance.actual_instance = GetTransactionDetailsByTransactionIDFromCallbackRIBSE.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into GetTransactionDetailsByTransactionIDFromCallbackRIBSBC
        try:
            instance.actual_instance = GetTransactionDetailsByTransactionIDFromCallbackRIBSBC.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into GetTransactionDetailsByTransactionIDFromCallbackRIBSL
        try:
            instance.actual_instance = GetTransactionDetailsByTransactionIDFromCallbackRIBSL.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into GetTransactionDetailsByTransactionIDFromCallbackRIBSD
        try:
            instance.actual_instance = GetTransactionDetailsByTransactionIDFromCallbackRIBSD.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into GetTransactionDetailsByTransactionIDFromCallbackRIBSD2
        try:
            instance.actual_instance = GetTransactionDetailsByTransactionIDFromCallbackRIBSD2.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into GetTransactionDetailsByTransactionIDFromCallbackRIBSZ
        try:
            instance.actual_instance = GetTransactionDetailsByTransactionIDFromCallbackRIBSZ.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into GetTransactionDetailsByTransactionIDFromCallbackRIBSEC
        try:
            instance.actual_instance = GetTransactionDetailsByTransactionIDFromCallbackRIBSEC.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into GetTransactionDetailsByTransactionIDFromCallbackRIBSBSC
        try:
            instance.actual_instance = GetTransactionDetailsByTransactionIDFromCallbackRIBSBSC.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into GetTransactionDetailsByTransactionIDFromCallbackRIBSX
        try:
            instance.actual_instance = GetTransactionDetailsByTransactionIDFromCallbackRIBSX.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into GetTransactionDetailsByTransactionIDFromCallbackRIBST
        try:
            instance.actual_instance = GetTransactionDetailsByTransactionIDFromCallbackRIBST.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into GetTransactionDetailsByTransactionIDFromCallbackRIBSP
        try:
            instance.actual_instance = GetTransactionDetailsByTransactionIDFromCallbackRIBSP.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into GetTransactionDetailsByTransactionIDFromCallbackRIBS with oneOf schemas: GetTransactionDetailsByTransactionIDFromCallbackRIBSB, GetTransactionDetailsByTransactionIDFromCallbackRIBSBC, GetTransactionDetailsByTransactionIDFromCallbackRIBSBSC, GetTransactionDetailsByTransactionIDFromCallbackRIBSD, GetTransactionDetailsByTransactionIDFromCallbackRIBSD2, GetTransactionDetailsByTransactionIDFromCallbackRIBSE, GetTransactionDetailsByTransactionIDFromCallbackRIBSEC, GetTransactionDetailsByTransactionIDFromCallbackRIBSL, GetTransactionDetailsByTransactionIDFromCallbackRIBSP, GetTransactionDetailsByTransactionIDFromCallbackRIBST, GetTransactionDetailsByTransactionIDFromCallbackRIBSX, GetTransactionDetailsByTransactionIDFromCallbackRIBSZ. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into GetTransactionDetailsByTransactionIDFromCallbackRIBS with oneOf schemas: GetTransactionDetailsByTransactionIDFromCallbackRIBSB, GetTransactionDetailsByTransactionIDFromCallbackRIBSBC, GetTransactionDetailsByTransactionIDFromCallbackRIBSBSC, GetTransactionDetailsByTransactionIDFromCallbackRIBSD, GetTransactionDetailsByTransactionIDFromCallbackRIBSD2, GetTransactionDetailsByTransactionIDFromCallbackRIBSE, GetTransactionDetailsByTransactionIDFromCallbackRIBSEC, GetTransactionDetailsByTransactionIDFromCallbackRIBSL, GetTransactionDetailsByTransactionIDFromCallbackRIBSP, GetTransactionDetailsByTransactionIDFromCallbackRIBST, GetTransactionDetailsByTransactionIDFromCallbackRIBSX, GetTransactionDetailsByTransactionIDFromCallbackRIBSZ. Details: " + ", ".join(error_messages))
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

