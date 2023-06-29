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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conlist
from cryptoapis.models.list_blockchain_events_subscriptions_ri_deactivation_reasons_inner import ListBlockchainEventsSubscriptionsRIDeactivationReasonsInner

class ListBlockchainEventsSubscriptionsRI(BaseModel):
    """
    ListBlockchainEventsSubscriptionsRI
    """
    address: StrictStr = Field(..., description="Represents the address of the transaction.")
    callback_secret_key: Optional[StrictStr] = Field(None, alias="callbackSecretKey", description="Represents the Secret Key value provided by the customer. This field is used for security purposes during the callback notification, in order to prove the sender of the callback as Crypto APIs. For more information please see our [Documentation](https://developers.cryptoapis.io/technical-documentation/general-information/callbacks#callback-security).")
    callback_url: StrictStr = Field(..., alias="callbackUrl", description="Represents the URL that is set by the customer where the callback will be received at. The callback notification will be received only if and when the event occurs. `We support ONLY httpS type of protocol`.")
    confirmations_count: StrictInt = Field(..., alias="confirmationsCount", description="Represents the number of confirmations, i.e. the amount of blocks that have been built on top of this block.")
    created_timestamp: StrictInt = Field(..., alias="createdTimestamp", description="Defines the specific time/date when the subscription was created in Unix Timestamp.")
    deactivation_reasons: Optional[conlist(ListBlockchainEventsSubscriptionsRIDeactivationReasonsInner)] = Field(None, alias="deactivationReasons", description="Represents the deactivation reason details, available when a blockchain event subscription has status isActive - false.")
    event_type: StrictStr = Field(..., alias="eventType", description="Defines the type of the specific event available for the customer to subscribe to for callback notification.")
    is_active: StrictBool = Field(..., alias="isActive", description="Defines whether the subscription is active or not. Set as boolean.")
    reference_id: StrictStr = Field(..., alias="referenceId", description="Represents a unique ID used to reference the specific callback subscription.")
    transaction_id: Optional[StrictStr] = Field(None, alias="transactionId", description="Represents the unique identification string that defines the transaction.")
    __properties = ["address", "callbackSecretKey", "callbackUrl", "confirmationsCount", "createdTimestamp", "deactivationReasons", "eventType", "isActive", "referenceId", "transactionId"]

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
    def from_json(cls, json_str: str) -> ListBlockchainEventsSubscriptionsRI:
        """Create an instance of ListBlockchainEventsSubscriptionsRI from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in deactivation_reasons (list)
        _items = []
        if self.deactivation_reasons:
            for _item in self.deactivation_reasons:
                if _item:
                    _items.append(_item.to_dict())
            _dict['deactivationReasons'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ListBlockchainEventsSubscriptionsRI:
        """Create an instance of ListBlockchainEventsSubscriptionsRI from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ListBlockchainEventsSubscriptionsRI.parse_obj(obj)

        _obj = ListBlockchainEventsSubscriptionsRI.parse_obj({
            "address": obj.get("address"),
            "callback_secret_key": obj.get("callbackSecretKey"),
            "callback_url": obj.get("callbackUrl"),
            "confirmations_count": obj.get("confirmationsCount"),
            "created_timestamp": obj.get("createdTimestamp"),
            "deactivation_reasons": [ListBlockchainEventsSubscriptionsRIDeactivationReasonsInner.from_dict(_item) for _item in obj.get("deactivationReasons")] if obj.get("deactivationReasons") is not None else None,
            "event_type": obj.get("eventType"),
            "is_active": obj.get("isActive"),
            "reference_id": obj.get("referenceId"),
            "transaction_id": obj.get("transactionId")
        })
        return _obj

