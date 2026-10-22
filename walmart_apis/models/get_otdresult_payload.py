from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.overall_trend import OverallTrendOrStr
from .enums.risk_level import RiskLevelOrStr
from .enums.seller_accountable_trend import SellerAccountableTrendOrStr
from .enums.shipping_method import ShippingMethodOrStr
from .non_accountable_otd_drivers import NonAccountableOtdDrivers, NonAccountableOtdDriversDict
from .performance_recommendation import PerformanceRecommendation, PerformanceRecommendationDict
from .seller_accountable_otd_drivers import SellerAccountableOtdDrivers, SellerAccountableOtdDriversDict


class GetOtdresultPayload(SdkBaseModel):
    report_duration: Optional[int] = Field(default=UNSET, alias="reportDuration")
    """Past number of days the metrics calculated"""

    updated_timestamp: Optional[str] = Field(default=UNSET, alias="updatedTimestamp")
    """Timestamp when metrics are calculated in ISO format"""

    shipping_method: Optional[ShippingMethodOrStr] = Field(default=UNSET, alias="shippingMethod")
    """shipping methods used to calculate these metrics"""

    overall_rate: Optional[float] = Field(default=UNSET, alias="overallRate")
    """Overall ontime delivery rate"""

    overall_trend: Optional[OverallTrendOrStr] = Field(default=UNSET, alias="overallTrend")
    """Overall On Time Delivery trand"""

    seller_accountable_rate: Optional[float] = Field(default=UNSET, alias="sellerAccountableRate")
    """Seller accountable ontime delivery rate"""

    seller_accountable_trend: Optional[SellerAccountableTrendOrStr] = Field(
        default=UNSET, alias="sellerAccountableTrend"
    )
    """Seller accountable On Time Delivery rate trend"""

    impacted_customer_count: Optional[int] = Field(default=UNSET, alias="impactedCustomerCount")
    """Number of customers impacted"""

    standard: Optional[str] = UNSET
    """Minimum seller accountable on time delivery rate required as per Walmart standards"""

    risk_level: Optional[RiskLevelOrStr] = Field(default=UNSET, alias="riskLevel")
    """Risk level as per Walmart standards"""

    seller_accountable_drivers: Optional[SellerAccountableOtdDrivers] = Field(
        default=UNSET, alias="sellerAccountableDrivers"
    )
    """Seller accountable drivers, which impacting the on time delivery rate"""

    non_accountable_drivers: Optional[NonAccountableOtdDrivers] = Field(default=UNSET, alias="nonAccountableDrivers")
    """Non Accountable drivers, which impacting the on time delivery rate"""

    recommendations: Optional[list[PerformanceRecommendation]] = UNSET
    """Recommendations to improve the On Time Delivery rate"""


class GetOtdresultPayloadDict(TypedDict):
    report_duration: NotRequired[int]
    updated_timestamp: NotRequired[str]
    shipping_method: NotRequired[ShippingMethodOrStr]
    overall_rate: NotRequired[float]
    overall_trend: NotRequired[OverallTrendOrStr]
    seller_accountable_rate: NotRequired[float]
    seller_accountable_trend: NotRequired[SellerAccountableTrendOrStr]
    impacted_customer_count: NotRequired[int]
    standard: NotRequired[str]
    risk_level: NotRequired[RiskLevelOrStr]
    seller_accountable_drivers: NotRequired[SellerAccountableOtdDriversDict]
    non_accountable_drivers: NotRequired[NonAccountableOtdDriversDict]
    recommendations: NotRequired[list[PerformanceRecommendationDict]]
