from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.item_status5 import ItemStatus5OrStr


class GetCategoriesResponsePayload(SdkBaseModel):
    """Response payload."""

    item_status: Optional[ItemStatus5OrStr] = Field(default=UNSET, alias="itemStatus")
    """IRP status of the items."""

    categories: Optional[list[str]] = UNSET
    """The Category of the items in requested item status."""


class GetCategoriesResponsePayloadDict(TypedDict):
    item_status: NotRequired[ItemStatus5OrStr]
    categories: NotRequired[list[str]]
