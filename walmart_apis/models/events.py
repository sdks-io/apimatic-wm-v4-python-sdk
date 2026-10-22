from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .events1 import Events1, Events1Dict


class Events(SdkBaseModel):
    events: Optional[list[Events1]] = UNSET
    """List of subscriptions grouped by event."""


class EventsDict(TypedDict):
    events: NotRequired[list[Events1Dict]]
