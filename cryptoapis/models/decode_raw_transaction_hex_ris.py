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
from cryptoapis.models.decode_raw_transaction_hex_risb import DecodeRawTransactionHexRISB
from cryptoapis.models.decode_raw_transaction_hex_risb2 import DecodeRawTransactionHexRISB2
from cryptoapis.models.decode_raw_transaction_hex_risb22 import DecodeRawTransactionHexRISB22
from cryptoapis.models.decode_raw_transaction_hex_risd import DecodeRawTransactionHexRISD
from cryptoapis.models.decode_raw_transaction_hex_risd2 import DecodeRawTransactionHexRISD2
from cryptoapis.models.decode_raw_transaction_hex_rise import DecodeRawTransactionHexRISE
from cryptoapis.models.decode_raw_transaction_hex_rise2 import DecodeRawTransactionHexRISE2
from cryptoapis.models.decode_raw_transaction_hex_risl import DecodeRawTransactionHexRISL
from cryptoapis.models.decode_raw_transaction_hex_risz import DecodeRawTransactionHexRISZ
from typing import Any, List
from pydantic import StrictStr, Field

DECODERAWTRANSACTIONHEXRIS_ONE_OF_SCHEMAS = ["DecodeRawTransactionHexRISB", "DecodeRawTransactionHexRISB2", "DecodeRawTransactionHexRISB22", "DecodeRawTransactionHexRISD", "DecodeRawTransactionHexRISD2", "DecodeRawTransactionHexRISE", "DecodeRawTransactionHexRISE2", "DecodeRawTransactionHexRISL", "DecodeRawTransactionHexRISZ"]

class DecodeRawTransactionHexRIS(BaseModel):
    """
    Represents the specific transaction data according to the blockchain
    """
    # data type: DecodeRawTransactionHexRISB
    oneof_schema_1_validator: Optional[DecodeRawTransactionHexRISB] = None
    # data type: DecodeRawTransactionHexRISB2
    oneof_schema_2_validator: Optional[DecodeRawTransactionHexRISB2] = None
    # data type: DecodeRawTransactionHexRISD
    oneof_schema_3_validator: Optional[DecodeRawTransactionHexRISD] = None
    # data type: DecodeRawTransactionHexRISD2
    oneof_schema_4_validator: Optional[DecodeRawTransactionHexRISD2] = None
    # data type: DecodeRawTransactionHexRISL
    oneof_schema_5_validator: Optional[DecodeRawTransactionHexRISL] = None
    # data type: DecodeRawTransactionHexRISE
    oneof_schema_6_validator: Optional[DecodeRawTransactionHexRISE] = None
    # data type: DecodeRawTransactionHexRISE2
    oneof_schema_7_validator: Optional[DecodeRawTransactionHexRISE2] = None
    # data type: DecodeRawTransactionHexRISB22
    oneof_schema_8_validator: Optional[DecodeRawTransactionHexRISB22] = None
    # data type: DecodeRawTransactionHexRISZ
    oneof_schema_9_validator: Optional[DecodeRawTransactionHexRISZ] = None
    actual_instance: Any
    one_of_schemas: List[str] = Field(DECODERAWTRANSACTIONHEXRIS_ONE_OF_SCHEMAS, const=True)

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
        instance = DecodeRawTransactionHexRIS.construct()
        error_messages = []
        match = 0
        # validate data type: DecodeRawTransactionHexRISB
        if not isinstance(v, DecodeRawTransactionHexRISB):
            error_messages.append(f"Error! Input type `{type(v)}` is not `DecodeRawTransactionHexRISB`")
        else:
            match += 1
        # validate data type: DecodeRawTransactionHexRISB2
        if not isinstance(v, DecodeRawTransactionHexRISB2):
            error_messages.append(f"Error! Input type `{type(v)}` is not `DecodeRawTransactionHexRISB2`")
        else:
            match += 1
        # validate data type: DecodeRawTransactionHexRISD
        if not isinstance(v, DecodeRawTransactionHexRISD):
            error_messages.append(f"Error! Input type `{type(v)}` is not `DecodeRawTransactionHexRISD`")
        else:
            match += 1
        # validate data type: DecodeRawTransactionHexRISD2
        if not isinstance(v, DecodeRawTransactionHexRISD2):
            error_messages.append(f"Error! Input type `{type(v)}` is not `DecodeRawTransactionHexRISD2`")
        else:
            match += 1
        # validate data type: DecodeRawTransactionHexRISL
        if not isinstance(v, DecodeRawTransactionHexRISL):
            error_messages.append(f"Error! Input type `{type(v)}` is not `DecodeRawTransactionHexRISL`")
        else:
            match += 1
        # validate data type: DecodeRawTransactionHexRISE
        if not isinstance(v, DecodeRawTransactionHexRISE):
            error_messages.append(f"Error! Input type `{type(v)}` is not `DecodeRawTransactionHexRISE`")
        else:
            match += 1
        # validate data type: DecodeRawTransactionHexRISE2
        if not isinstance(v, DecodeRawTransactionHexRISE2):
            error_messages.append(f"Error! Input type `{type(v)}` is not `DecodeRawTransactionHexRISE2`")
        else:
            match += 1
        # validate data type: DecodeRawTransactionHexRISB22
        if not isinstance(v, DecodeRawTransactionHexRISB22):
            error_messages.append(f"Error! Input type `{type(v)}` is not `DecodeRawTransactionHexRISB22`")
        else:
            match += 1
        # validate data type: DecodeRawTransactionHexRISZ
        if not isinstance(v, DecodeRawTransactionHexRISZ):
            error_messages.append(f"Error! Input type `{type(v)}` is not `DecodeRawTransactionHexRISZ`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in DecodeRawTransactionHexRIS with oneOf schemas: DecodeRawTransactionHexRISB, DecodeRawTransactionHexRISB2, DecodeRawTransactionHexRISB22, DecodeRawTransactionHexRISD, DecodeRawTransactionHexRISD2, DecodeRawTransactionHexRISE, DecodeRawTransactionHexRISE2, DecodeRawTransactionHexRISL, DecodeRawTransactionHexRISZ. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in DecodeRawTransactionHexRIS with oneOf schemas: DecodeRawTransactionHexRISB, DecodeRawTransactionHexRISB2, DecodeRawTransactionHexRISB22, DecodeRawTransactionHexRISD, DecodeRawTransactionHexRISD2, DecodeRawTransactionHexRISE, DecodeRawTransactionHexRISE2, DecodeRawTransactionHexRISL, DecodeRawTransactionHexRISZ. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> DecodeRawTransactionHexRIS:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> DecodeRawTransactionHexRIS:
        """Returns the object represented by the json string"""
        instance = DecodeRawTransactionHexRIS.construct()
        error_messages = []
        match = 0

        # deserialize data into DecodeRawTransactionHexRISB
        try:
            instance.actual_instance = DecodeRawTransactionHexRISB.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into DecodeRawTransactionHexRISB2
        try:
            instance.actual_instance = DecodeRawTransactionHexRISB2.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into DecodeRawTransactionHexRISD
        try:
            instance.actual_instance = DecodeRawTransactionHexRISD.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into DecodeRawTransactionHexRISD2
        try:
            instance.actual_instance = DecodeRawTransactionHexRISD2.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into DecodeRawTransactionHexRISL
        try:
            instance.actual_instance = DecodeRawTransactionHexRISL.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into DecodeRawTransactionHexRISE
        try:
            instance.actual_instance = DecodeRawTransactionHexRISE.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into DecodeRawTransactionHexRISE2
        try:
            instance.actual_instance = DecodeRawTransactionHexRISE2.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into DecodeRawTransactionHexRISB22
        try:
            instance.actual_instance = DecodeRawTransactionHexRISB22.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into DecodeRawTransactionHexRISZ
        try:
            instance.actual_instance = DecodeRawTransactionHexRISZ.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into DecodeRawTransactionHexRIS with oneOf schemas: DecodeRawTransactionHexRISB, DecodeRawTransactionHexRISB2, DecodeRawTransactionHexRISB22, DecodeRawTransactionHexRISD, DecodeRawTransactionHexRISD2, DecodeRawTransactionHexRISE, DecodeRawTransactionHexRISE2, DecodeRawTransactionHexRISL, DecodeRawTransactionHexRISZ. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into DecodeRawTransactionHexRIS with oneOf schemas: DecodeRawTransactionHexRISB, DecodeRawTransactionHexRISB2, DecodeRawTransactionHexRISB22, DecodeRawTransactionHexRISD, DecodeRawTransactionHexRISD2, DecodeRawTransactionHexRISE, DecodeRawTransactionHexRISE2, DecodeRawTransactionHexRISL, DecodeRawTransactionHexRISZ. Details: " + ", ".join(error_messages))
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
