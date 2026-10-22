from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .items_success_response import ItemsSuccessResponse, ItemsSuccessResponseDict


class SuccessModel(SdkBaseModel):
    """Items succeeded."""

    items: Optional[list[ItemsSuccessResponse]] = UNSET
    """Items."""


class SuccessModelDict(TypedDict):
    items: NotRequired[list[ItemsSuccessResponseDict]]
