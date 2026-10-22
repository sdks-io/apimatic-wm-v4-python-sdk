from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class EventTypes2(SdkBaseModel):
    """List of event types."""

    resource_name: Optional[str] = Field(default=UNSET, alias="resourceName")
    """Resource (functional category) that the event type is mapped to (for example, ITEM, PRICE, ORDER)."""

    event_type: Optional[str] = Field(default=UNSET, alias="eventType")
    """Event type available for subscription."""

    event_version: Optional[str] = Field(default=UNSET, alias="eventVersion")
    """Version identifier of the event type."""

    description: Optional[str] = UNSET
    """Description of the specific event type."""


class EventTypes2Dict(TypedDict):
    resource_name: NotRequired[str]
    event_type: NotRequired[str]
    event_version: NotRequired[str]
    description: NotRequired[str]
