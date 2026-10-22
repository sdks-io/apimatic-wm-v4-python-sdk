from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.cumulative_rate_trend2 import CumulativeRateTrend2OrStr
from .ots_infraction_drivers import OtsInfractionDrivers, OtsInfractionDriversDict


class GetOtsresultPayload(SdkBaseModel):
    report_duration: Optional[int] = Field(default=UNSET, alias="reportDuration")
    """Past number of days the metrics calculated"""

    updated_timestamp: Optional[str] = Field(default=UNSET, alias="updatedTimestamp")
    """Timestamp when metrics are calculated in ISO format"""

    cumulative_rate: Optional[float] = Field(default=UNSET, alias="cumulativeRate")
    """Cumulative on time shipment rate"""

    cumulative_rate_trend: Optional[CumulativeRateTrend2OrStr] = Field(default=UNSET, alias="cumulativeRateTrend")
    """Cumulative on time shipment rate trend"""

    impacted_order_count: Optional[int] = Field(default=UNSET, alias="impactedOrderCount")
    """Number of orders impacted"""

    recommended_rate: Optional[float] = Field(default=UNSET, alias="recommendedRate")
    """Recommended on time shipment rate value"""

    infraction_drivers: Optional[OtsInfractionDrivers] = Field(default=UNSET, alias="infractionDrivers")
    """Individual drivers of on time shipment rate"""


class GetOtsresultPayloadDict(TypedDict):
    report_duration: NotRequired[int]
    updated_timestamp: NotRequired[str]
    cumulative_rate: NotRequired[float]
    cumulative_rate_trend: NotRequired[CumulativeRateTrend2OrStr]
    impacted_order_count: NotRequired[int]
    recommended_rate: NotRequired[float]
    infraction_drivers: NotRequired[OtsInfractionDriversDict]
