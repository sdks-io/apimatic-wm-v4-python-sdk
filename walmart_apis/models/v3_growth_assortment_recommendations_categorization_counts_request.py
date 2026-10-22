from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.categorization_type3 import CategorizationType3OrStr
from .filter_criteria4 import FilterCriteria4, FilterCriteria4Dict
from .meta10 import Meta10, Meta10Dict


class V3GrowthAssortmentRecommendationsCategorizationCountsRequest(SdkBaseModel):
    categorization_type: CategorizationType3OrStr = Field(alias="categorizationType")
    """| Attribute | Description | Data Type |
    | --- | ----------- | ------- |
    | BRAND | To get list of brands which are associated with the assortment recommendations | string |
    | CATEGORY | To get list of categories which are associated with the assortment recommendations | string |

    <br><b style='color:green;'>Market availability: US | CA | MX</span></b>"""

    meta: Optional[Meta10] = UNSET
    """Meta information for the request. <br><b style='color:green;'>Market availability: US only</span></b>"""

    filter_criteria: Optional[FilterCriteria4] = Field(default=UNSET, alias="filterCriteria")
    """Different type of filters can be passed in this object.<br><b style='color:green;'>Market availability: US | CA |
    MX</span></b>"""


class V3GrowthAssortmentRecommendationsCategorizationCountsRequestDict(TypedDict):
    categorization_type: CategorizationType3OrStr
    meta: NotRequired[Meta10Dict]
    filter_criteria: NotRequired[FilterCriteria4Dict]
