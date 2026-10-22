from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .filter2 import Filter2, Filter2Dict
from .query1 import Query1, Query1Dict


class V3InsightsItemsListingQualityItemsRequest(SdkBaseModel):
    query: Optional[Query1] = UNSET
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    filters: Optional[list[Filter2]] = UNSET
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""


class V3InsightsItemsListingQualityItemsRequestDict(TypedDict):
    query: NotRequired[Query1Dict]
    filters: NotRequired[list[Filter2Dict]]
