from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .dispute_contest_response import DisputeContestResponse, DisputeContestResponseDict


class DisputeContestResponses(SdkBaseModel):
    item_response: list[DisputeContestResponse] = Field(alias="itemResponse")
    """Items status included in the response list."""


class DisputeContestResponsesDict(TypedDict):
    item_response: list[DisputeContestResponseDict]
