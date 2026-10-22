from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .approved import Approved, ApprovedDict
from .feedback import Feedback, FeedbackDict


class V3SeoRecommendationUpdateItemsRequest(SdkBaseModel):
    approved: Optional[Approved] = UNSET
    """Required only when decision is APPROVED"""

    feedback: Optional[Feedback] = UNSET
    """Required only when decision is REJECTED"""


class V3SeoRecommendationUpdateItemsRequestDict(TypedDict):
    approved: NotRequired[ApprovedDict]
    feedback: NotRequired[FeedbackDict]
