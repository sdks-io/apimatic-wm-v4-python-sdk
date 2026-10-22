from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .payload18 import Payload18, Payload18Dict
from .total_gmv_amount1 import TotalGmvAmount1, TotalGmvAmount1Dict


class V3InsightsItemsUnpublishedItemsResponse(SdkBaseModel):
    payload: Optional[list[Payload18]] = UNSET
    total_count: Optional[int] = Field(default=UNSET, alias="totalCount")
    """total number of unpublished items<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    total_gmv_amount: Optional[TotalGmvAmount1] = Field(default=UNSET, alias="totalGmvAmount")
    """Gross Merchandise Value of the total result set<br><b style='color:green;'>Market availability: US | CA |
    MX</b>"""


class V3InsightsItemsUnpublishedItemsResponseDict(TypedDict):
    payload: NotRequired[list[Payload18Dict]]
    total_count: NotRequired[int]
    total_gmv_amount: NotRequired[TotalGmvAmount1Dict]
