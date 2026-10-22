from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .feed5 import Feed5, Feed5Dict


class Results4(SdkBaseModel):
    """Specifies the feed status results."""

    feed: Optional[list[Feed5]] = UNSET
    """Specifies the feed status results."""


class Results4Dict(TypedDict):
    feed: NotRequired[list[Feed5Dict]]
