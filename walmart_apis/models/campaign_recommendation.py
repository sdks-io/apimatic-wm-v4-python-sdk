from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.type import TypeOrStr
from .recommended_value_impact import RecommendedValueImpact, RecommendedValueImpactDict


class CampaignRecommendation(SdkBaseModel):
    """An actionable recommendation for a campaign. Includes the recommendation type, suggested value, and projected
    performance impact at three levels (recommended, minimum, maximum)."""

    type_: Optional[TypeOrStr] = Field(default=UNSET, alias="type")
    """Recommendation category.

    - **BUDGET**: Recommended budget adjustment (daily or total)
    - **BIDDING_STRATEGY**: Recommended change to bidding strategy"""

    sub_type: Optional[str] = Field(default=UNSET, alias="subType")
    """Specific recommendation subtype indicating the optimization action being suggested. Example values include
    ``INCREASE_DAILY_BUDGET`` and bidding strategy adjustment actions."""

    recommended_value: Optional[str] = Field(default=UNSET, alias="recommendedValue")
    """The primary recommended value as a string representation. For budget recommendations, this is the suggested new
    budget amount."""

    recommended_value_impact: Optional[RecommendedValueImpact] = Field(default=UNSET, alias="recommendedValueImpact")
    """Projected performance impact of the recommendation at three levels.

    - **recommended**: The optimal suggested value (marked ``isRecommended: true``)
    - **minRecommendation**: A conservative lower-bound option. May be ``null`` if not applicable.
    - **maxRecommendation**: An aggressive upper-bound option. May be ``null`` if not applicable."""


class CampaignRecommendationDict(TypedDict):
    type_: NotRequired[TypeOrStr]
    sub_type: NotRequired[str]
    recommended_value: NotRequired[str]
    recommended_value_impact: NotRequired[RecommendedValueImpactDict]
