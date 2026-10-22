from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .subscription_response_dtorecord import SubscriptionResponseDtorecord, SubscriptionResponseDtorecordDict


class SubscriptionResponseDto(SdkBaseModel):
    """List of subscription records."""

    event: Optional[list[SubscriptionResponseDtorecord]] = UNSET


class SubscriptionResponseDtoDict(TypedDict):
    event: NotRequired[list[SubscriptionResponseDtorecordDict]]
