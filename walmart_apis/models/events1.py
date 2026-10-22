from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .subscription_response_dtorecord import SubscriptionResponseDtorecord, SubscriptionResponseDtorecordDict


class Events1(SdkBaseModel):
    """List of event-specific subscription arrays."""

    event: Optional[list[SubscriptionResponseDtorecord]] = UNSET


class Events1Dict(TypedDict):
    event: NotRequired[list[SubscriptionResponseDtorecordDict]]
