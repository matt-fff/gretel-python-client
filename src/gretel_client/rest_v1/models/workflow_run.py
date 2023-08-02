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

from datetime import datetime
from inspect import getfullargspec
from typing import Any, Dict, Optional

from pydantic import BaseModel, StrictStr, validator

from gretel_client.rest_v1.models.user_profile import UserProfile
from gretel_client.rest_v1.models.workflow_run_cancellation_request import (
    WorkflowRunCancellationRequest,
)


class WorkflowRun(BaseModel):
    """
    WorkflowRun
    """

    id: StrictStr = ...
    workflow_id: StrictStr = ...
    config: Optional[Dict[str, Any]] = None
    status: StrictStr = ...
    created_by: StrictStr = ...
    created_at: datetime = ...
    updated_at: Optional[datetime] = None
    pending_at: Optional[datetime] = None
    active_at: Optional[datetime] = None
    error_at: Optional[datetime] = None
    lost_at: Optional[datetime] = None
    cancelled_at: Optional[datetime] = None
    cancellation_request: Optional[WorkflowRunCancellationRequest] = None
    created_by_profile: Optional[UserProfile] = None
    __properties = [
        "id",
        "workflow_id",
        "config",
        "status",
        "created_by",
        "created_at",
        "updated_at",
        "pending_at",
        "active_at",
        "error_at",
        "lost_at",
        "cancelled_at",
        "cancellation_request",
        "created_by_profile",
    ]

    @validator("status")
    def status_validate_enum(cls, v):
        if v not in (
            "RUN_STATUS_UNKNOWN",
            "RUN_STATUS_CREATED",
            "RUN_STATUS_PENDING",
            "RUN_STATUS_ACTIVE",
            "RUN_STATUS_ERROR",
            "RUN_STATUS_LOST",
            "RUN_STATUS_COMPLETED",
            "RUN_STATUS_CANCELLING",
            "RUN_STATUS_CANCELLED",
        ):
            raise ValueError(
                "must be one of enum values ('RUN_STATUS_UNKNOWN', 'RUN_STATUS_CREATED', 'RUN_STATUS_PENDING', 'RUN_STATUS_ACTIVE', 'RUN_STATUS_ERROR', 'RUN_STATUS_LOST', 'RUN_STATUS_COMPLETED', 'RUN_STATUS_CANCELLING', 'RUN_STATUS_CANCELLED')"
            )
        return v

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
    def from_json(cls, json_str: str) -> WorkflowRun:
        """Create an instance of WorkflowRun from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of cancellation_request
        if self.cancellation_request:
            _dict["cancellation_request"] = self.cancellation_request.to_dict()
        # override the default output from pydantic by calling `to_dict()` of created_by_profile
        if self.created_by_profile:
            _dict["created_by_profile"] = self.created_by_profile.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> WorkflowRun:
        """Create an instance of WorkflowRun from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return WorkflowRun.parse_obj(obj)

        _obj = WorkflowRun.parse_obj(
            {
                "id": obj.get("id"),
                "workflow_id": obj.get("workflow_id"),
                "config": obj.get("config"),
                "status": obj.get("status"),
                "created_by": obj.get("created_by"),
                "created_at": obj.get("created_at"),
                "updated_at": obj.get("updated_at"),
                "pending_at": obj.get("pending_at"),
                "active_at": obj.get("active_at"),
                "error_at": obj.get("error_at"),
                "lost_at": obj.get("lost_at"),
                "cancelled_at": obj.get("cancelled_at"),
                "cancellation_request": WorkflowRunCancellationRequest.from_dict(
                    obj.get("cancellation_request")
                )
                if obj.get("cancellation_request") is not None
                else None,
                "created_by_profile": UserProfile.from_dict(
                    obj.get("created_by_profile")
                )
                if obj.get("created_by_profile") is not None
                else None,
            }
        )
        return _obj
