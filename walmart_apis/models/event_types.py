from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .event_types1 import EventTypes1, EventTypes1Dict


class EventTypes(SdkBaseModel):
    event_types: Optional[list[EventTypes1]] = Field(default=UNSET, alias="eventTypes")
    """List of event types."""


class EventTypesDict(TypedDict):
    event_types: NotRequired[list[EventTypes1Dict]]
