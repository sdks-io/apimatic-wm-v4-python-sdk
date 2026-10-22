from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class V3WebhooksSubscriptionsResponse2(SdkBaseModel):
    subscription_id: Optional[str] = Field(default=UNSET, alias="subscriptionId")
    """Unique identifier of the deleted subscription.<br><b style='color:green;'>Market availability: Global</b>"""

    message: Optional[str] = UNSET
    """Confirmation message indicating the subscription was deleted.<br><b style='color:green;'>Market availability:
    Global</b>"""


class V3WebhooksSubscriptionsResponse2Dict(TypedDict):
    subscription_id: NotRequired[str]
    message: NotRequired[str]
