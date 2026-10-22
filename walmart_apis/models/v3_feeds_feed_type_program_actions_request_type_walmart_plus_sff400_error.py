from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class V3FeedsFeedTypeProgramActionsRequestTypeWalmartPlusSff400Error(SdkBaseModel):
    errors: Optional[list[Any]] = UNSET
    """Contains a list of high-level errors encountered during the operation."""


class V3FeedsFeedTypeProgramActionsRequestTypeWalmartPlusSff400ErrorDict(TypedDict):
    errors: NotRequired[list[Any]]
