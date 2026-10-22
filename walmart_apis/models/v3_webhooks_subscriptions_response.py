from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .events2 import Events2, Events2Dict


class V3WebhooksSubscriptionsResponse(SdkBaseModel):
    events: Optional[list[Events2]] = UNSET
    """List of subscriptions that match the request filters.<br><b style='color:green;'>Market availability:
    Global</b>"""


class V3WebhooksSubscriptionsResponseDict(TypedDict):
    events: NotRequired[list[Events2Dict]]
