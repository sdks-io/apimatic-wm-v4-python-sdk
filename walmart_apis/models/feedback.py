from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Feedback(SdkBaseModel):
    """Required only when decision is REJECTED"""

    feedback: Optional[str] = UNSET
    """Optional feedback provided explaining the decision."""


class FeedbackDict(TypedDict):
    feedback: NotRequired[str]
