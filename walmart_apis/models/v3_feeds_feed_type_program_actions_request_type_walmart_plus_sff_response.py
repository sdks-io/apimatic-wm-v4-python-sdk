from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .header1 import Header1, Header1Dict
from .payload20 import Payload20, Payload20Dict


class V3FeedsFeedTypeProgramActionsRequestTypeWalmartPlusSffResponse(SdkBaseModel):
    status: Optional[str] = UNSET
    """Overall status of the request."""

    header: Optional[Header1] = UNSET
    """Response header information."""

    errors: Optional[list[Any]] = UNSET
    """Contains a list of high-level errors encountered during the operation."""

    payload: Optional[Payload20] = UNSET
    """Response payload containing operation results."""


class V3FeedsFeedTypeProgramActionsRequestTypeWalmartPlusSffResponseDict(TypedDict):
    status: NotRequired[str]
    header: NotRequired[Header1Dict]
    errors: NotRequired[list[Any]]
    payload: NotRequired[Payload20Dict]
