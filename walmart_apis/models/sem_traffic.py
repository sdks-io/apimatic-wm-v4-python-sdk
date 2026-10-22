from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SemTraffic(SdkBaseModel):
    """Performance data of the campaign"""

    impressions: Optional[int] = UNSET
    """The number of times the advertisement was displayed."""

    clicks: Optional[int] = UNSET
    """The number of times the advertisement was clicked."""

    ctr: Optional[float] = UNSET
    """Click-Through Rate (CTR), calculated as clicks divided by impressions."""

    adspend: Optional[float] = UNSET
    """Total amount spent on ads."""

    cpc: Optional[float] = UNSET
    """Cost Per Click (CPC), calculated as ad spend divided by clicks."""

    gmv: Optional[float] = UNSET
    """Gross Merchandise Value (GMV), representing total sales generated."""

    roas: Optional[float] = UNSET
    """Return on Ad Spend (ROAS), calculated as GMV divided by ad spend."""


class SemTrafficDict(TypedDict):
    impressions: NotRequired[int]
    clicks: NotRequired[int]
    ctr: NotRequired[float]
    adspend: NotRequired[float]
    cpc: NotRequired[float]
    gmv: NotRequired[float]
    roas: NotRequired[float]
