from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .filter_criteria3 import FilterCriteria3, FilterCriteria3Dict
from .meta6 import Meta6, Meta6Dict


class V3GrowthAssortmentRecommendationsRequest(SdkBaseModel):
    recommendation_type: Literal["ITEM"] = Field(default="ITEM", alias="recommendationType")
    """| Attribute | Description | Data Type |
    | --- | ----------- | ------- |
    | ITEM | To get list of recommended items | string |

    <br><b style='color:green;'>Market availability: US | CA | MX</span></b>"""

    meta: Optional[Meta6] = UNSET
    """Meta information for the request."""

    filter_criteria: Optional[FilterCriteria3] = Field(default=UNSET, alias="filterCriteria")
    """Different type of filters can be passed in this object."""


class V3GrowthAssortmentRecommendationsRequestDict(TypedDict):
    recommendation_type: Literal["ITEM"]
    meta: NotRequired[Meta6Dict]
    filter_criteria: NotRequired[FilterCriteria3Dict]
