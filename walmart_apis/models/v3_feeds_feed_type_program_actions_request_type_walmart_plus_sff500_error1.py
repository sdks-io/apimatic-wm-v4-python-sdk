from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .header import Header, HeaderDict


class V3FeedsFeedTypeProgramActionsRequestTypeWalmartPlusSff500Error1(SdkBaseModel):
    status: Optional[str] = UNSET
    """Overall status of the request."""

    header: Optional[Header] = UNSET
    """Response header information."""

    errors: Optional[list[Any]] = UNSET
    """Contains a list of high-level errors encountered during the operation."""


class V3FeedsFeedTypeProgramActionsRequestTypeWalmartPlusSff500Error1Dict(TypedDict):
    status: NotRequired[str]
    header: NotRequired[HeaderDict]
    errors: NotRequired[list[Any]]
