from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .trend import Trend, TrendDict


class Payload5(SdkBaseModel):
    """Payload in the response having the trend details for the recommended item."""

    recommendation_unique_id: str = Field(alias="recommendationUniqueId")
    """Unique ID that is returned in the response of the get recommendations API or in the on-request bulk CSV
    file.<br><b style='color:green;'>Market availability: US only</span></b>"""

    trends: Optional[list[Trend]] = UNSET
    """Trend data for the recommended item. This will include Price trends and Demand trends.<br><b
    style='color:green;'>Market availability: US only</span></b>"""


class Payload5Dict(TypedDict):
    recommendation_unique_id: str
    trends: NotRequired[list[TrendDict]]
