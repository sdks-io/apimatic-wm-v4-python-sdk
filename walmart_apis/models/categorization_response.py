from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .categorization_response_payload import CategorizationResponsePayload, CategorizationResponsePayloadDict


class CategorizationResponse(SdkBaseModel):
    payload: Optional[CategorizationResponsePayload] = UNSET
    """Payload in the response having the categorization details about the item recommendations."""


class CategorizationResponseDict(TypedDict):
    payload: NotRequired[CategorizationResponsePayloadDict]
