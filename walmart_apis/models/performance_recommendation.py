from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PerformanceRecommendation(SdkBaseModel):
    """Recommendations to decrease the cancellation rate"""

    recommendation: Optional[str] = UNSET
    """recommendation"""

    more_info_link: Optional[str] = Field(default=UNSET, alias="moreInfoLink")
    """More information link url"""


class PerformanceRecommendationDict(TypedDict):
    recommendation: NotRequired[str]
    more_info_link: NotRequired[str]
