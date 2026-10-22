from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.cumulative_accuracy_trend2 import CumulativeAccuracyTrend2OrStr


class GetCmaresultPayload(SdkBaseModel):
    report_duration: Optional[int] = Field(default=UNSET, alias="reportDuration")
    """Past number of days the metrics calculated"""

    updated_timestamp: Optional[str] = Field(default=UNSET, alias="updatedTimestamp")
    """Timestamp when metrics are calculated in ISO format"""

    cumulative_accuracy: Optional[float] = Field(default=UNSET, alias="cumulativeAccuracy")
    """Cumulative carrier method accuracy"""

    cumulative_accuracy_trend: Optional[CumulativeAccuracyTrend2OrStr] = Field(
        default=UNSET, alias="cumulativeAccuracyTrend"
    )
    """Cumulative carrier method accuracy trend"""

    impacted_order_count: Optional[int] = Field(default=UNSET, alias="impactedOrderCount")
    """Number of orders impacted"""

    recommended_accuracy: Optional[float] = Field(default=UNSET, alias="recommendedAccuracy")
    """Recommended Carrier method accuracy value"""

    infraction_drivers: Optional[dict[str, float]] = Field(default=UNSET, alias="infractionDrivers")
    """Individual carrier method accuracies"""


class GetCmaresultPayloadDict(TypedDict):
    report_duration: NotRequired[int]
    updated_timestamp: NotRequired[str]
    cumulative_accuracy: NotRequired[float]
    cumulative_accuracy_trend: NotRequired[CumulativeAccuracyTrend2OrStr]
    impacted_order_count: NotRequired[int]
    recommended_accuracy: NotRequired[float]
    infraction_drivers: NotRequired[dict[str, float]]
