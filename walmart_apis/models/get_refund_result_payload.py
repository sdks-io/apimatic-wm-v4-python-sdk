from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.cumulative_rate_trend6 import CumulativeRateTrend6OrStr
from .enums.gmv_loss_trend import GmvLossTrendOrStr
from .enums.orders_impacted_trend import OrdersImpactedTrendOrStr
from .enums.risk_level import RiskLevelOrStr
from .non_accountable_refunds_drivers import NonAccountableRefundsDrivers, NonAccountableRefundsDriversDict
from .performance_recommendation import PerformanceRecommendation, PerformanceRecommendationDict
from .seller_accountable_refunds_drivers import SellerAccountableRefundsDrivers, SellerAccountableRefundsDriversDict


class GetRefundResultPayload(SdkBaseModel):
    report_duration: Optional[int] = Field(default=UNSET, alias="reportDuration")
    """Past number of days the metrics calculated"""

    updated_timestamp: Optional[str] = Field(default=UNSET, alias="updatedTimestamp")
    """Timestamp when metrics are calculated in ISO format"""

    cumulative_rate: Optional[float] = Field(default=UNSET, alias="cumulativeRate")
    """Cumulative refunds rate"""

    cumulative_rate_trend: Optional[CumulativeRateTrend6OrStr] = Field(default=UNSET, alias="cumulativeRateTrend")
    """Cumulative refunds rate trend"""

    gmv_loss: Optional[float] = Field(default=UNSET, alias="gmvLoss")
    """gmvLoss incurred"""

    gmv_loss_trend: Optional[GmvLossTrendOrStr] = Field(default=UNSET, alias="gmvLossTrend")
    """gmv Loss trend"""

    orders_impacted: Optional[int] = Field(default=UNSET, alias="ordersImpacted")
    """Number of orders impacted"""

    orders_impacted_trend: Optional[OrdersImpactedTrendOrStr] = Field(default=UNSET, alias="ordersImpactedTrend")
    """Impacted orders trend"""

    standard: Optional[str] = UNSET
    """Maximum allowed cumulative refund rate as per Walmart standards"""

    risk_level: Optional[RiskLevelOrStr] = Field(default=UNSET, alias="riskLevel")
    """Risk level as per Walmart standards"""

    seller_accountable_drivers: Optional[SellerAccountableRefundsDrivers] = Field(
        default=UNSET, alias="sellerAccountableDrivers"
    )
    """Seller accountable drivers, which impacting the refunds rate"""

    non_accountable_drivers: Optional[NonAccountableRefundsDrivers] = Field(
        default=UNSET, alias="nonAccountableDrivers"
    )
    """Non Accountable drivers, which impacting the refunds rate"""

    recommendations: Optional[list[PerformanceRecommendation]] = UNSET
    """recommendations insights"""


class GetRefundResultPayloadDict(TypedDict):
    report_duration: NotRequired[int]
    updated_timestamp: NotRequired[str]
    cumulative_rate: NotRequired[float]
    cumulative_rate_trend: NotRequired[CumulativeRateTrend6OrStr]
    gmv_loss: NotRequired[float]
    gmv_loss_trend: NotRequired[GmvLossTrendOrStr]
    orders_impacted: NotRequired[int]
    orders_impacted_trend: NotRequired[OrdersImpactedTrendOrStr]
    standard: NotRequired[str]
    risk_level: NotRequired[RiskLevelOrStr]
    seller_accountable_drivers: NotRequired[SellerAccountableRefundsDriversDict]
    non_accountable_drivers: NotRequired[NonAccountableRefundsDriversDict]
    recommendations: NotRequired[list[PerformanceRecommendationDict]]
