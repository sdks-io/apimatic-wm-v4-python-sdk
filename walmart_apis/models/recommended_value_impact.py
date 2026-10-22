from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .impact_option import ImpactOption, ImpactOptionDict


class RecommendedValueImpact(SdkBaseModel):
    """Projected performance impact of the recommendation at three levels.

    - **recommended**: The optimal suggested value (marked ``isRecommended: true``)
    - **minRecommendation**: A conservative lower-bound option. May be ``null`` if not applicable.
    - **maxRecommendation**: An aggressive upper-bound option. May be ``null`` if not applicable."""

    recommended: Optional[ImpactOption] = UNSET
    """A single recommendation option with its projected performance impact."""

    min_recommendation: OptionalNullable[ImpactOption] = Field(default=UNSET, alias="minRecommendation")
    """Conservative lower-bound recommendation option. May be ``null`` when a minimum option is not applicable."""

    max_recommendation: OptionalNullable[ImpactOption] = Field(default=UNSET, alias="maxRecommendation")
    """Aggressive upper-bound recommendation option. May be ``null`` when a maximum option is not applicable."""


class RecommendedValueImpactDict(TypedDict):
    recommended: NotRequired[ImpactOptionDict]
    min_recommendation: NotRequired[ImpactOptionDict | None]
    max_recommendation: NotRequired[ImpactOptionDict | None]
