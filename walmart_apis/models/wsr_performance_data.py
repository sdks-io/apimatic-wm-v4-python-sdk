from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .wsr_metrics import WsrMetrics, WsrMetricsDict


class WsrPerformanceData(SdkBaseModel):
    """Performance data aggregated by the specified performance level.

    **Field Availability by ``performanceBy``**:

    | Field | CAMPAIGN | ADGROUP | CREATIVE |
    |:--|:--:|:--:|:--:|
    | ``campaignId`` | ✓ | ✓ | ✓ |
    | ``adGroupId`` | null | ✓ | ✓ |
    | ``creativeId`` | null | null | ✓ |"""

    campaign_id: OptionalNullable[str] = Field(default=UNSET, alias="campaignId")
    """External campaign identifier. Available for all performanceBy levels (CAMPAIGN, ADGROUP, CREATIVE)."""

    ad_group_id: OptionalNullable[str] = Field(default=UNSET, alias="adGroupId")
    """External ad group identifier.

    > **Note:** Only populated when ``performanceBy`` is ``ADGROUP`` or ``CREATIVE``. Returns ``null`` for
        campaign-level aggregation."""

    creative_id: OptionalNullable[str] = Field(default=UNSET, alias="creativeId")
    """External creative/link identifier.

    > **Note:** Only populated when ``performanceBy`` is ``CREATIVE``. Returns ``null`` for campaign and adgroup-level
        aggregation."""

    metrics: Optional[WsrMetrics] = UNSET
    """Performance metrics for the aggregated data.

    All metrics are based on last-touch attribution with a 14-day window."""


class WsrPerformanceDataDict(TypedDict):
    campaign_id: NotRequired[str | None]
    ad_group_id: NotRequired[str | None]
    creative_id: NotRequired[str | None]
    metrics: NotRequired[WsrMetricsDict]
