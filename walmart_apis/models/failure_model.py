from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .items_failure_response import ItemsFailureResponse, ItemsFailureResponseDict


class FailureModel(SdkBaseModel):
    """Items failed."""

    items: Optional[list[ItemsFailureResponse]] = UNSET
    """Items."""


class FailureModelDict(TypedDict):
    items: NotRequired[list[ItemsFailureResponseDict]]
