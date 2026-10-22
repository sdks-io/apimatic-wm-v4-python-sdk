from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .status206_item_response import Status206ItemResponse, Status206ItemResponseDict


class Status206Response(SdkBaseModel):
    item_response: Optional[list[Status206ItemResponse]] = Field(default=UNSET, alias="itemResponse")
    """list of ItemResponses"""


class Status206ResponseDict(TypedDict):
    item_response: NotRequired[list[Status206ItemResponseDict]]
