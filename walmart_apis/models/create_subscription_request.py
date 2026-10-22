from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .create_subscription_request_record import CreateSubscriptionRequestRecord, CreateSubscriptionRequestRecordDict


class CreateSubscriptionRequest(SdkBaseModel):
    events: Optional[list[CreateSubscriptionRequestRecord]] = UNSET


class CreateSubscriptionRequestDict(TypedDict):
    events: NotRequired[list[CreateSubscriptionRequestRecordDict]]
