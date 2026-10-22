from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class RejectRecommendationsResponsePayload(SdkBaseModel):
    """Payload in the response for rejecting recommendations."""

    message: Optional[str] = UNSET
    """Message confirming the rejection of the recommendations."""


class RejectRecommendationsResponsePayloadDict(TypedDict):
    message: NotRequired[str]
