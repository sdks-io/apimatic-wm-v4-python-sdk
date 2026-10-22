from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .events3 import Events3, Events3Dict


class V3WebhooksSubscriptionsRequest(SdkBaseModel):
    events: Optional[list[Events3]] = UNSET
    """Array of subscription definitions to create."""


class V3WebhooksSubscriptionsRequestDict(TypedDict):
    events: NotRequired[list[Events3Dict]]
