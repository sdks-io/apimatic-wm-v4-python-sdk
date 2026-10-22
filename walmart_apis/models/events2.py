from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .event3 import Event3, Event3Dict


class Events2(SdkBaseModel):
    """List of events."""

    event: Optional[list[Event3]] = UNSET
    """Array of subscription objects returned by the service."""


class Events2Dict(TypedDict):
    event: NotRequired[list[Event3Dict]]
