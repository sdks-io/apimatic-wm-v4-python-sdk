from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.cumulative_rate_trend8 import CumulativeRateTrend8OrStr
from .enums.risk_level import RiskLevelOrStr
from .non_accountable_cancellations_drivers import (
    NonAccountableCancellationsDrivers,
    NonAccountableCancellationsDriversDict,
)
from .performance_recommendation import PerformanceRecommendation, PerformanceRecommendationDict
from .seller_accountable_cancellations_drivers import (
    SellerAccountableCancellationsDrivers,
    SellerAccountableCancellationsDriversDict,
)


class GetCancelResultPayload(SdkBaseModel):
    report_duration: Optional[int] = Field(default=UNSET, alias="reportDuration")
    """Past number of days the metrics calculated"""

    updated_timestamp: Optional[str] = Field(default=UNSET, alias="updatedTimestamp")
    """Timestamp when metrics are calculated in ISO format"""

    cumulative_rate: Optional[float] = Field(default=UNSET, alias="cumulativeRate")
    """Cumulative rate of orders cancelled"""

    cumulative_rate_trend: Optional[CumulativeRateTrend8OrStr] = Field(default=UNSET, alias="cumulativeRateTrend")
    """Cumulative rate of orders cancelled trend"""

    gmv_loss: Optional[float] = Field(default=UNSET, alias="gmvLoss")
    """gmvLoss incurred"""

    orders_impacted: Optional[int] = Field(default=UNSET, alias="ordersImpacted")
    """Number of orders impacted"""

    standard: Optional[str] = UNSET
    """Maximum allowed cumulative cancellations rate as per Walmart standards"""

    risk_level: Optional[RiskLevelOrStr] = Field(default=UNSET, alias="riskLevel")
    """Risk level as per Walmart standards"""

    seller_accountable_drivers: Optional[SellerAccountableCancellationsDrivers] = Field(
        default=UNSET, alias="sellerAccountableDrivers"
    )
    """Seller accountable drivers, which impacting the cancellations rate"""

    non_accountable_drivers: Optional[NonAccountableCancellationsDrivers] = Field(
        default=UNSET, alias="nonAccountableDrivers"
    )
    """Non Accountable drivers, which impacting the cancellations rate"""

    recommendations: Optional[list[PerformanceRecommendation]] = UNSET
    """Recommendations to decrease the cancellation rate"""


class GetCancelResultPayloadDict(TypedDict):
    report_duration: NotRequired[int]
    updated_timestamp: NotRequired[str]
    cumulative_rate: NotRequired[float]
    cumulative_rate_trend: NotRequired[CumulativeRateTrend8OrStr]
    gmv_loss: NotRequired[float]
    orders_impacted: NotRequired[int]
    standard: NotRequired[str]
    risk_level: NotRequired[RiskLevelOrStr]
    seller_accountable_drivers: NotRequired[SellerAccountableCancellationsDriversDict]
    non_accountable_drivers: NotRequired[NonAccountableCancellationsDriversDict]
    recommendations: NotRequired[list[PerformanceRecommendationDict]]
