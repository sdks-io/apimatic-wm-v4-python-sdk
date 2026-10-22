from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .event4 import Event4, Event4Dict


class V3WebhooksSubscriptionsResponse3(SdkBaseModel):
    """List of updated subscription objects."""

    event: Optional[list[Event4]] = UNSET


class V3WebhooksSubscriptionsResponse3Dict(TypedDict):
    event: NotRequired[list[Event4Dict]]
