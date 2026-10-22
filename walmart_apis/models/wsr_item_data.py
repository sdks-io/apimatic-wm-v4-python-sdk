from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .wsr_metrics import WsrMetrics, WsrMetricsDict


class WsrItemData(SdkBaseModel):
    """Item-level performance data with product details.

    **Note**: Item details (``itemName``, ``productType``, ``category``) are enriched from the seller's catalogue and
    may be null if the item is not found."""

    campaign_id: OptionalNullable[str] = Field(default=UNSET, alias="campaignId")
    """External campaign identifier. Available for all performanceBy levels (``CAMPAIGN``, ``ADGROUP``,
    ``CREATIVE``)."""

    ad_group_id: OptionalNullable[str] = Field(default=UNSET, alias="adGroupId")
    """External ad group identifier.

    > **Note:** Only populated when ``performanceBy`` is ``ADGROUP`` or ``CREATIVE``. Returns ``null`` for
        campaign-level aggregation."""

    creative_id: OptionalNullable[str] = Field(default=UNSET, alias="creativeId")
    """External creative/link identifier.

    > **Note:** Only populated when ``performanceBy`` is ``CREATIVE``. Returns ``null`` for campaign and adgroup-level
        aggregation.."""

    item_id: Optional[str] = Field(default=UNSET, alias="itemId")
    """Walmart item identifier"""

    item_name: OptionalNullable[str] = Field(default=UNSET, alias="itemName")
    """Name of the item/product from catalogue. May be null if item not found in seller's catalogue."""

    product_type: OptionalNullable[str] = Field(default=UNSET, alias="productType")
    """Product type classification from catalogue. May be null if item not found in seller's catalogue."""

    category: OptionalNullable[str] = UNSET
    """Product category from catalogue. May be null if item not found in seller's catalogue."""

    metrics: Optional[WsrMetrics] = UNSET
    """Performance metrics for the aggregated data.

    All metrics are based on last-touch attribution with a 14-day window."""


class WsrItemDataDict(TypedDict):
    campaign_id: NotRequired[str | None]
    ad_group_id: NotRequired[str | None]
    creative_id: NotRequired[str | None]
    item_id: NotRequired[str]
    item_name: NotRequired[str | None]
    product_type: NotRequired[str | None]
    category: NotRequired[str | None]
    metrics: NotRequired[WsrMetricsDict]
