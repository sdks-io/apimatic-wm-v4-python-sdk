from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SubscriptionDeleteResponseDto(SdkBaseModel):
    subscription_id: Optional[str] = Field(default=UNSET, alias="subscriptionId")
    """Unique identifier of the deleted subscription."""

    message: Optional[str] = UNSET
    """Confirmation message indicating the subscription was deleted."""


class SubscriptionDeleteResponseDtoDict(TypedDict):
    subscription_id: NotRequired[str]
    message: NotRequired[str]
