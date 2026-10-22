from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .item_response3 import ItemResponse3, ItemResponse3Dict


class V3ItemsDisputeDuplicatesStatusResponse(SdkBaseModel):
    item_response: list[ItemResponse3] = Field(alias="itemResponse")
    """Items status included in the list."""


class V3ItemsDisputeDuplicatesStatusResponseDict(TypedDict):
    item_response: list[ItemResponse3Dict]
