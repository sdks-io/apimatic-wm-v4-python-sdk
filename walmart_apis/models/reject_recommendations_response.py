from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .reject_recommendations_response_payload import (
    RejectRecommendationsResponsePayload,
    RejectRecommendationsResponsePayloadDict,
)


class RejectRecommendationsResponse(SdkBaseModel):
    payload: Optional[RejectRecommendationsResponsePayload] = UNSET
    """Payload in the response for rejecting recommendations."""


class RejectRecommendationsResponseDict(TypedDict):
    payload: NotRequired[RejectRecommendationsResponsePayloadDict]
