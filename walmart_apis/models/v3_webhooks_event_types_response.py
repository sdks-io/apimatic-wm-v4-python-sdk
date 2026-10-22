from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .event_types2 import EventTypes2, EventTypes2Dict


class V3WebhooksEventTypesResponse(SdkBaseModel):
    event_types: Optional[list[EventTypes2]] = Field(default=UNSET, alias="eventTypes")
    """List of event type definitions available for subscription.<br><b style='color:green;'>Market availability:
    Global</b>"""


class V3WebhooksEventTypesResponseDict(TypedDict):
    event_types: NotRequired[list[EventTypes2Dict]]
