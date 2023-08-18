# coding: utf-8

"""
    

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations

import json
import pprint
import re  # noqa: F401

from inspect import getfullargspec
from typing import Any, Dict, Optional

from pydantic import BaseModel, StrictStr


class CreateConnectionRequest(BaseModel):
    """
    CreateConnectionRequest
    """

    project_id: StrictStr = ...
    name: Optional[StrictStr] = None
    type: StrictStr = ...
    credentials: Dict[str, Any] = ...
    __properties = ["project_id", "name", "type", "credentials"]

    class Config:
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> CreateConnectionRequest:
        """Create an instance of CreateConnectionRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CreateConnectionRequest:
        """Create an instance of CreateConnectionRequest from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return CreateConnectionRequest.parse_obj(obj)

        _obj = CreateConnectionRequest.parse_obj(
            {
                "project_id": obj.get("project_id"),
                "name": obj.get("name"),
                "type": obj.get("type"),
                "credentials": obj.get("credentials"),
            }
        )
        return _obj