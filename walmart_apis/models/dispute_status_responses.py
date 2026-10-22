from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .dispute_status_response import DisputeStatusResponse, DisputeStatusResponseDict


class DisputeStatusResponses(SdkBaseModel):
    item_response: list[DisputeStatusResponse] = Field(alias="itemResponse")
    """Items status included in the list."""


class DisputeStatusResponsesDict(TypedDict):
    item_response: list[DisputeStatusResponseDict]
